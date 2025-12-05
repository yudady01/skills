# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Claude Code marketplace containing three specialized skills/plugins for different development domains:

- **yudady-skills**: A marketplace containing translation tools, SQL script generators, and payment channel integration development skills
- **Location**: `/Users/tommy/Documents/work.nosync/skills/`
- **Structure**: Marketplace format with `.claude-plugin/marketplace.json` and individual plugins in `plugins/` directory

## Plugin Architecture

### Marketplace Structure
```
.claude-plugin/marketplace.json    # Main marketplace configuration
plugins/
├── en-to-zh-translator/          # Technical translation skill
├── repeatable-sql/               # Database migration script generator
└── thirdparty-pay-channel/       # Payment integration development skill
```

Each plugin follows the standard structure:
- `.claude-plugin/marketplace.json` - Plugin metadata
- `skills/SKILL.md` - Main skill definition with YAML frontmatter
- `README.md` - Plugin documentation
- `skills/scripts/` - Python utility scripts
- `skills/assets/` - Templates and reference materials
- `skills/references/` - Documentation and best practices

## Common Development Commands

### Plugin Testing and Validation
```bash
# Validate plugin structure (run from project root)
find plugins/ -name "SKILL.md" -exec grep -l "^---" {} \;

# Check for marketplace.json consistency
python -c "import json; print(json.load(open('.claude-plugin/marketplace.json'))['plugins'])"

# Test Python scripts in plugins
python3 plugins/thirdparty-pay-channel/skills/scripts/generate_payment_handler.py --help
python3 plugins/repeatable-sql/skills/scripts/index_manager.py --help
```

### Python Script Execution
All Python scripts are located in `plugins/*/skills/scripts/` and use the shebang `#!/usr/bin/env python3`. They can be run directly:

```bash
# Payment channel development
python3 plugins/thirdparty-pay-channel/skills/scripts/generate_payment_handler.py --channel-name NewPay --channel-code 1270 --support-recharge --support-withdraw --auth-type sign
python3 plugins/thirdparty-pay-channel/skills/scripts/validate_payment_handler.py --file Pay1270.java

# SQL script generation
python3 plugins/repeatable-sql/skills/scripts/index_manager.py --database mysql
python3 plugins/repeatable-sql/skills/scripts/flyway_validator.py --directory migrations/

# Translation validation
python3 plugins/en-to-zh-translator/skills/scripts/validate_translation.py --file translation.md
```

## Plugin-Specific Guidelines

### Payment Channel Plugin (thirdparty-pay-channel)
- **Purpose**: Generate payment handler classes and validate payment integration code
- **Key Files**: `generate_payment_handler.py`, `validate_payment_handler.py`
- **Templates**: Java payment handler templates in `skills/assets/templates/`
- **References**: Security guidelines, API documentation, error codes in `skills/references/`

### SQL Plugin (repeatable-sql)
- **Purpose**: Generate idempotent database migration scripts for MySQL and PostgreSQL
- **Key Files**: `index_manager.py`, `table_migrator.py`, `flyway_validator.py`
- **Templates**: Migration scripts for both databases in `skills/assets/templates/`
- **Pattern**: Uses Dynamic_Create_Index stored procedure pattern for MySQL

### Translation Plugin (en-to-zh-translator)
- **Purpose**: Technical English to Chinese translation preserving code blocks and formatting
- **Key Files**: `validate_translation.py`
- **References**: Technical term mappings, quality guidelines, translation examples

## File Structure Conventions

### Skill Definition Format
Each `SKILL.md` must have YAML frontmatter:
```yaml
---
name: plugin-name
description: Brief description of the skill
license: Apache 2.0  # optional
---
```

### Plugin Metadata Format
Each plugin's `.claude-plugin/marketplace.json` must match the skill name:
```json
{
  "name": "plugin-name",
  "description": "Description",
  "version": "1.0.0",
  "author": {"name": "yudady", "email": "yudady@gmail.com"}
}
```

## Key Integration Points

### Environment Variables
Scripts use `${CLAUDE_PLUGIN_ROOT}` for portable paths when deployed

### Inter-plugin Dependencies
- Payment channel plugin uses translation plugin for API documentation localization
- SQL plugin templates are referenced by payment channel plugin for database schema changes

### External Tool Integrations
- Flyway for database migrations (repeatable-sql)
- Jackson for JSON processing (payment channel)
- Standard Python libraries for file processing and validation

## Development Workflow

1. **Plugin Development**: Edit `skills/SKILL.md` and associated scripts
2. **Local Testing**: Use Python scripts directly with `--help` to understand parameters
3. **Validation**: Ensure marketplace.json references match plugin directory names
4. **Documentation**: Update README.md files when adding new functionality
5. **Consistency**: Maintain naming conventions between directories, skill files, and metadata