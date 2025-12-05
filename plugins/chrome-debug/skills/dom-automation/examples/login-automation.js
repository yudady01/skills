/**
 * Chrome Debug Login Automation Example
 * Complete automated login workflow for http://localhost:8193/x_mgr/start/index.html#/user/login
 */

const mcp = require('chrome-devtools-mcp');

class LoginAutomation {
  constructor(config = {}) {
    this.config = {
      target_url: config.target_url || "http://localhost:8193/x_mgr/start/index.html#/user/login",
      username: config.username || "superadmin",
      password: config.password || "abc123456",
      timeout: config.timeout || 30000,
      headless: config.headless || false,
      ...config
    };

    this.selectors = {
      // Username field selectors in order of preference
      username: [
        '#username',
        '[name="username"]',
        'input[type="text"]',
        'input[placeholder*="username"]',
        'input[placeholder*="用户名"]'
      ],

      // Password field selectors
      password: [
        '#password',
        '[name="password"]',
        'input[type="password"]',
        'input[placeholder*="password"]',
        'input[placeholder*="密码"]'
      ],

      // Login button selectors
      loginButton: [
        '#login-button',
        '#submit',
        '#login',
        '.btn-primary',
        '.btn-login',
        'button[type="submit"]',
        'input[type="submit"]',
        '.login-btn'
      ],

      // Success indicators
      successIndicators: [
        '.dashboard',
        '.main-content',
        '[data-testid="dashboard"]',
        '.user-info',
        '.welcome-message',
        '[data-role="main"]'
      ],

      // Error indicators
      errorIndicators: [
        '.error-message',
        '.alert-danger',
        '.login-error',
        '[data-testid="error"]',
        '.notification.error'
      ]
    };
  }

  /**
   * Initialize browser connection
   */
  async initialize() {
    console.log('🚀 Initializing browser...');

    try {
      // Connect to Chrome DevTools MCP
      this.client = await mcp.connect({
        chromePath: this.config.chrome_path,
        headless: this.config.headless,
        timeout: this.config.timeout
      });

      console.log('✅ Browser initialized successfully');
      return true;
    } catch (error) {
      console.error('❌ Failed to initialize browser:', error.message);
      return false;
    }
  }

  /**
   * Navigate to login page
   */
  async navigateToLogin() {
    console.log(`🔍 Navigating to: ${this.config.target_url}`);

    try {
      await this.client.call('navigate', {
        url: this.config.target_url
      });

      // Wait for page to load
      await this.client.call('wait_for_load');

      console.log('✅ Page loaded successfully');
      return true;
    } catch (error) {
      console.error('❌ Failed to navigate to login page:', error.message);
      return false;
    }
  }

  /**
   * Find element using multiple selector strategies
   */
  async findElement(selectorList, timeout = 5000) {
    for (const selector of selectorList) {
      try {
        const exists = await this.client.call('element_exists', {
          selector
        });

        if (exists) {
          const visible = await this.client.call('is_element_visible', {
            selector
          });

          if (visible) {
            console.log(`🎯 Found element with selector: ${selector}`);
            return selector;
          }
        }
      } catch (error) {
        // Continue to next selector
        continue;
      }
    }

    throw new Error(`No visible element found with any selector: ${selectorList.join(', ')}`);
  }

  /**
   * Fill username field
   */
  async fillUsername() {
    console.log('📝 Filling username field...');

    try {
      const usernameSelector = await this.findElement(this.selectors.username);

      await this.client.call('clear_field', { selector: usernameSelector });
      await this.client.call('type', {
        selector: usernameSelector,
        text: this.config.username
      });

      console.log(`✅ Username filled: ${this.config.username}`);
      return true;
    } catch (error) {
      console.error('❌ Failed to fill username:', error.message);
      return false;
    }
  }

  /**
   * Fill password field
   */
  async fillPassword() {
    console.log('🔒 Filling password field...');

    try {
      const passwordSelector = await this.findElement(this.selectors.password);

      await this.client.call('clear_field', { selector: passwordSelector });
      await this.client.call('type', {
        selector: passwordSelector,
        text: this.config.password
      });

      console.log('✅ Password filled');
      return true;
    } catch (error) {
      console.error('❌ Failed to fill password:', error.message);
      return false;
    }
  }

  /**
   * Submit login form
   */
  async submitLogin() {
    console.log('🚀 Submitting login form...');

    try {
      const buttonSelector = await this.findElement(this.selectors.loginButton);

      // Wait for button to be clickable
      await this.client.call('wait_for_clickable', {
        selector: buttonSelector,
        timeout: 5000
      });

      // Click login button
      await this.client.call('click', { selector: buttonSelector });

      console.log('✅ Login form submitted');
      return true;
    } catch (error) {
      console.error('❌ Failed to submit login form:', error.message);
      return false;
    }
  }

  /**
   * Check for login success
   */
  async checkLoginSuccess() {
    console.log('🔍 Checking login status...');

    try {
      // First check for errors
      for (const errorSelector of this.selectors.errorIndicators) {
        const hasError = await this.client.call('element_exists', {
          selector: errorSelector
        });

        if (hasError) {
          const errorText = await this.client.call('get_element_text', {
            selector: errorSelector
          });

          console.log(`❌ Login failed with error: ${errorText}`);
          return { success: false, error: errorText };
        }
      }

      // Check for success indicators
      for (const successSelector of this.selectors.successIndicators) {
        try {
          await this.client.call('wait_for_selector', {
            selector: successSelector,
            timeout: 5000
          });

          console.log('✅ Login successful!');
          return { success: true };
        } catch (error) {
          // Try next selector
          continue;
        }
      }

      // If no explicit success indicators found, check URL change
      const currentUrl = await this.client.call('get_current_url');
      if (currentUrl !== this.config.target_url) {
        console.log('✅ Login successful (URL changed)');
        return { success: true };
      }

      console.log('⚠️  Login status unclear');
      return { success: false, error: 'Unable to verify login success' };

    } catch (error) {
      console.error('❌ Error checking login status:', error.message);
      return { success: false, error: error.message };
    }
  }

  /**
   * Take screenshot for debugging
   */
  async takeScreenshot(filename = 'login-debug.png') {
    try {
      const screenshot = await this.client.call('take_screenshot', {
        full_page: true,
        filename
      });

      console.log(`📸 Screenshot saved: ${filename}`);
      return screenshot;
    } catch (error) {
      console.warn('⚠️  Failed to take screenshot:', error.message);
      return null;
    }
  }

  /**
   * Execute complete login workflow
   */
  async execute() {
    console.log('🎯 Starting login automation workflow');
    console.log('=' .repeat(50));

    const workflowSteps = [
      { name: 'Initialize', action: () => this.initialize() },
      { name: 'Navigate', action: () => this.navigateToLogin() },
      { name: 'Fill Username', action: () => this.fillUsername() },
      { name: 'Fill Password', action: () => this.fillPassword() },
      { name: 'Submit Login', action: () => this.submitLogin() }
    ];

    // Execute workflow steps
    for (const step of workflowSteps) {
      console.log(`\n📍 ${step.name}...`);

      const success = await step.action();
      if (!success) {
        await this.takeScreenshot(`${step.name.toLowerCase()}-failed.png`);
        throw new Error(`Failed at step: ${step.name}`);
      }
    }

    // Wait for navigation
    console.log('\n⏳ Waiting for login completion...');
    await this.client.call('wait_for_navigation_or_timeout', {
      timeout: 10000
    });

    // Check login result
    const result = await this.checkLoginSuccess();

    if (result.success) {
      await this.takeScreenshot('login-success.png');
      console.log('\n🎉 Login automation completed successfully!');
    } else {
      await this.takeScreenshot('login-failed.png');
      console.log('\n💥 Login automation failed:', result.error);
    }

    return result;
  }

  /**
   * Close browser session
   */
  async cleanup() {
    try {
      if (this.client) {
        await this.client.close();
        console.log('🧹 Browser session closed');
      }
    } catch (error) {
      console.warn('⚠️  Error during cleanup:', error.message);
    }
  }
}

// Example usage
async function main() {
  const config = {
    target_url: "http://localhost:8193/x_mgr/start/index.html#/user/login",
    username: "superadmin",
    password: "abc123456",
    timeout: 30000,
    headless: false
  };

  const automation = new LoginAutomation(config);

  try {
    const result = await automation.execute();

    if (result.success) {
      console.log('\n✅ Workflow completed successfully');
      process.exit(0);
    } else {
      console.log('\n❌ Workflow failed:', result.error);
      process.exit(1);
    }
  } catch (error) {
    console.error('\n💥 Workflow error:', error.message);
    process.exit(1);
  } finally {
    await automation.cleanup();
  }
}

// Export for use as module
module.exports = { LoginAutomation };

// Run if called directly
if (require.main === module) {
  main();
}