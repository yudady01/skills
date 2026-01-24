# Mentoring the Machine — Eric Hou, Augment Code

**Video URL:** https://www.youtube.com/watch?v=Zniw5c9_jx8

---

## Full Transcript

### [00:00 - 01:00]

**[00:16]** My name is Eric, member of technical

**[00:16]** My name is Eric, member of technical staff at Augment Code and today's talk

**[00:18]** staff at Augment Code and today's talk

**[00:18]** staff at Augment Code and today's talk is about mentoring the machine. Uh now

**[00:20]** is about mentoring the machine. Uh now

**[00:20]** is about mentoring the machine. Uh now the talk today is a personal story uh a

**[00:22]** the talk today is a personal story uh a

**[00:22]** the talk today is a personal story uh a glimpse into how we at augment use AI to

**[00:25]** glimpse into how we at augment use AI to

**[00:25]** glimpse into how we at augment use AI to build production grade software and how

**[00:27]** build production grade software and how

**[00:27]** build production grade software and how that's changed how we operate both as a

**[00:29]** that's changed how we operate both as a

**[00:29]** that's changed how we operate both as a team and as a business.

**[00:33]** team and as a business.

**[00:33]** team and as a business. So at Augment we build for real software

**[00:35]** So at Augment we build for real software

**[00:35]** So at Augment we build for real software engineering at scale in production.

**[00:37]** engineering at scale in production.

**[00:37]** engineering at scale in production. Before Augment, I spent six years

**[00:39]** Before Augment, I spent six years

**[00:39]** Before Augment, I spent six years building products and standards for the

**[00:40]** building products and standards for the

**[00:40]** building products and standards for the automotive industry. And my peers and I

**[00:42]** automotive industry. And my peers and I

**[00:42]** automotive industry. And my peers and I have created and maintained systems that

**[00:44]** have created and maintained systems that

**[00:44]** have created and maintained systems that tens of thousands of engineer engineers

**[00:46]** tens of thousands of engineer engineers

**[00:46]** tens of thousands of engineer engineers have touched where not one person fully

**[00:48]** have touched where not one person fully

**[00:48]** have touched where not one person fully understands even how 5% of the system

**[00:50]** understands even how 5% of the system

**[00:50]** understands even how 5% of the system works. So we kind of understand the get

**[00:52]** works. So we kind of understand the get

**[00:52]** works. So we kind of understand the get your hands dirty kind of work we as

**[00:53]** your hands dirty kind of work we as

**[00:53]** your hands dirty kind of work we as engineers have to do sometimes.

**[00:56]** engineers have to do sometimes.

**[00:56]** engineers have to do sometimes. Now that's why we have all the line

**[00:57]** Now that's why we have all the line

**[00:58]** Now that's why we have all the line items that you would expect but are kind

**[00:59]** items that you would expect but are kind

**[00:59]** items that you would expect but are kind of shockingly rare in today's vibecoded


### [01:00 - 02:00]

**[01:01]** of shockingly rare in today's vibecoded

**[01:01]** of shockingly rare in today's vibecoded world. Uh if you wanted to learn more uh

**[01:04]** world. Uh if you wanted to learn more uh

**[01:04]** world. Uh if you wanted to learn more uh please come visit our booth or visit us

**[01:06]** please come visit our booth or visit us

**[01:06]** please come visit our booth or visit us at augmentcode.com.

**[01:09]** at augmentcode.com.

**[01:09]** at augmentcode.com. Now let me walk you through our journey

**[01:10]** Now let me walk you through our journey

**[01:10]** Now let me walk you through our journey which is broken into four sections. The

**[01:13]** which is broken into four sections. The

**[01:13]** which is broken into four sections. The first two go through my personal journey

**[01:14]** first two go through my personal journey

**[01:14]** first two go through my personal journey as an engineer at augment and how I as

**[01:16]** as an engineer at augment and how I as

**[01:16]** as an engineer at augment and how I as well as other engineers learn to use

**[01:18]** well as other engineers learn to use

**[01:18]** well as other engineers learn to use agents most effectively. And the second

**[01:21]** agents most effectively. And the second

**[01:21]** agents most effectively. And the second two discuss the gaps that most

**[01:22]** two discuss the gaps that most

**[01:22]** two discuss the gaps that most organizations and even our own face when

**[01:25]** organizations and even our own face when

**[01:25]** organizations and even our own face when trying to adopt Agentic AI and how we

**[01:28]** trying to adopt Agentic AI and how we

**[01:28]** trying to adopt Agentic AI and how we can address those gaps to solve both our

**[01:29]** can address those gaps to solve both our

**[01:29]** can address those gaps to solve both our current problems and unlock new

**[01:31]** current problems and unlock new

**[01:31]** current problems and unlock new opportunities in our businesses.

**[01:34]** opportunities in our businesses.

**[01:34]** opportunities in our businesses. So without further ado, let's dive into

**[01:36]** So without further ado, let's dive into

**[01:36]** So without further ado, let's dive into my own journey to realization which

**[01:38]** my own journey to realization which

**[01:38]** my own journey to realization which actually happened a few months ago as we

**[01:39]** actually happened a few months ago as we

**[01:39]** actually happened a few months ago as we were first rolling out the augment

**[01:41]** were first rolling out the augment

**[01:41]** were first rolling out the augment agent.

**[01:42]** agent.

**[01:42]** agent. So picture this. It's Tuesday morning.

**[01:45]** So picture this. It's Tuesday morning.

**[01:45]** So picture this. It's Tuesday morning. Uh for me it's about to be one of those

**[01:47]** Uh for me it's about to be one of those

**[01:48]** Uh for me it's about to be one of those days. You're all probably going to

**[01:49]** days. You're all probably going to

**[01:49]** days. You're all probably going to recognize this day. In fact, most of you

**[01:51]** recognize this day. In fact, most of you

**[01:51]** recognize this day. In fact, most of you have probably lived it many times. But

**[01:54]** have probably lived it many times. But

**[01:54]** have probably lived it many times. But at the moment, for me, just another

**[01:56]** at the moment, for me, just another

**[01:56]** at the moment, for me, just another Tuesday. Now, it's 9:00 a.m. I'm behind

**[01:59]** Tuesday. Now, it's 9:00 a.m. I'm behind

**[01:59]** Tuesday. Now, it's 9:00 a.m. I'm behind on a critical design system component


### [02:00 - 03:00]

**[02:01]** on a critical design system component

**[02:01]** on a critical design system component that was supposed to merge last Friday.

**[02:02]** that was supposed to merge last Friday.

**[02:02]** that was supposed to merge last Friday. The design team's waiting. Downstream

**[02:04]** The design team's waiting. Downstream

**[02:04]** The design team's waiting. Downstream teams are waiting. I'm feeling the

**[02:06]** teams are waiting. I'm feeling the

**[02:06]** teams are waiting. I'm feeling the pressure, but I'm determined to knock it

**[02:08]** pressure, but I'm determined to knock it

**[02:08]** pressure, but I'm determined to knock it out. So, clear calendar, cup of coffee

**[02:10]** out. So, clear calendar, cup of coffee

**[02:10]** out. So, clear calendar, cup of coffee in hand, and my fingers are just hitting

**[02:12]** in hand, and my fingers are just hitting

**[02:12]** in hand, and my fingers are just hitting the keyboard. 9:30 a.m. My phone buzzes.

**[02:15]** the keyboard. 9:30 a.m. My phone buzzes.

**[02:15]** the keyboard. 9:30 a.m. My phone buzzes. Staging emergency. Uh the main API

**[02:18]** Staging emergency. Uh the main API

**[02:18]** Staging emergency. Uh the main API endpoint is completely broken. There's a

**[02:19]** endpoint is completely broken. There's a

**[02:19]** endpoint is completely broken. There's a request format mismatch between our

**[02:22]** request format mismatch between our

**[02:22]** request format mismatch between our client and server. Uh blocking all QA

**[02:25]** client and server. Uh blocking all QA

**[02:25]** client and server. Uh blocking all QA testing and blocking deployments. So the

**[02:27]** testing and blocking deployments. So the

**[02:27]** testing and blocking deployments. So the primary is on vacation at this point.

**[02:29]** primary is on vacation at this point.

**[02:29]** primary is on vacation at this point. I'm the service secondary and I'm

**[02:30]** I'm the service secondary and I'm

**[02:30]** I'm the service secondary and I'm responsible for the on call process and

**[02:32]** responsible for the on call process and

**[02:32]** responsible for the on call process and seeing that through. So my carefully

**[02:35]** seeing that through. So my carefully

**[02:35]** seeing that through. So my carefully planned day just evaporated like that.

**[02:39]** planned day just evaporated like that.

**[02:39]** planned day just evaporated like that. 10:15 I'm starting to wrap up some

**[02:41]** 10:15 I'm starting to wrap up some

**[02:41]** 10:15 I'm starting to wrap up some service log exploration and the new hire

**[02:44]** service log exploration and the new hire

**[02:44]** service log exploration and the new hire engineer that I'm mentoring slacks me.

**[02:46]** engineer that I'm mentoring slacks me.

**[02:46]** engineer that I'm mentoring slacks me. Hey, when you have a minute, can you

**[02:47]** Hey, when you have a minute, can you

**[02:47]** Hey, when you have a minute, can you help me understand how our extension

**[02:49]** help me understand how our extension

**[02:49]** help me understand how our extension system works? I'm stuck.

**[02:52]** system works? I'm stuck.

**[02:52]** system works? I'm stuck. Now, if you've been an engineer before,

**[02:54]** Now, if you've been an engineer before,

**[02:54]** Now, if you've been an engineer before, we you know, you've been here. That

**[02:56]** we you know, you've been here. That

**[02:56]** we you know, you've been here. That sinking feeling when your day derails.

**[02:58]** sinking feeling when your day derails.

**[02:58]** sinking feeling when your day derails. You're pulled in three different

**[02:59]** You're pulled in three different

**[02:59]** You're pulled in three different directions. You go home feeling like


### [03:00 - 04:00]

**[03:01]** directions. You go home feeling like

**[03:01]** directions. You go home feeling like you've accomplished nothing even though

**[03:03]** you've accomplished nothing even though

**[03:03]** you've accomplished nothing even though you've worked for 12 hours. And you know

**[03:04]** you've worked for 12 hours. And you know

**[03:04]** you've worked for 12 hours. And you know that when you wake up the next morning,

**[03:06]** that when you wake up the next morning,

**[03:06]** that when you wake up the next morning, the on call remediation is going to put

**[03:08]** the on call remediation is going to put

**[03:08]** the on call remediation is going to put another week or two of work on your

**[03:11]** another week or two of work on your

**[03:11]** another week or two of work on your plate. And if that scenario felt

**[03:13]** plate. And if that scenario felt

**[03:13]** plate. And if that scenario felt familiar, you're not alone. This is not

**[03:15]** familiar, you're not alone. This is not

**[03:15]** familiar, you're not alone. This is not just your team, not just your company or

**[03:18]** just your team, not just your company or

**[03:18]** just your team, not just your company or bad luck. Every single interruption

**[03:20]** bad luck. Every single interruption

**[03:20]** bad luck. Every single interruption costs us 23 minutes of recovery time.

**[03:23]** costs us 23 minutes of recovery time.

**[03:23]** costs us 23 minutes of recovery time. And as an industry, we're spending 23 of

**[03:25]** And as an industry, we're spending 23 of

**[03:26]** And as an industry, we're spending 23 of our time maintaining code instead of

**[03:28]** our time maintaining code instead of

**[03:28]** our time maintaining code instead of building new features. That translates

**[03:30]** building new features. That translates

**[03:30]** building new features. That translates to $300 billion annually spent on

**[03:33]** to $300 billion annually spent on

**[03:34]** to $300 billion annually spent on context switching and firefighting. So,

**[03:36]** context switching and firefighting. So,

**[03:36]** context switching and firefighting. So, we've normalized this chaos and we've

**[03:38]** we've normalized this chaos and we've

**[03:38]** we've normalized this chaos and we've accepted that days like this are just

**[03:40]** accepted that days like this are just

**[03:40]** accepted that days like this are just part of being an engineer. Of course,

**[03:44]** part of being an engineer. Of course,

**[03:44]** part of being an engineer. Of course, this is an AI, you know, conference. So,

**[03:45]** this is an AI, you know, conference. So,

**[03:45]** this is an AI, you know, conference. So, what if I told you it didn't need to be

**[03:48]** what if I told you it didn't need to be

**[03:48]** what if I told you it didn't need to be that way? In fact, what if I told you it

**[03:50]** that way? In fact, what if I told you it

**[03:50]** that way? In fact, what if I told you it already isn't? I'm going to show you

**[03:53]** already isn't? I'm going to show you

**[03:53]** already isn't? I'm going to show you exactly how.

**[03:56]** exactly how.

**[03:56]** exactly how. So, let's see if I can bring this over.


### [04:00 - 05:00]

**[04:01]** So, let's see if I can bring this over.

**[04:01]** So, let's see if I can bring this over. Uh, this is our product, the Augment

**[04:03]** Uh, this is our product, the Augment

**[04:03]** Uh, this is our product, the Augment Extension. It's got everything you like

**[04:04]** Extension. It's got everything you like

**[04:04]** Extension. It's got everything you like in your favorite AI coding assistants

**[04:06]** in your favorite AI coding assistants

**[04:06]** in your favorite AI coding assistants and more. But today we're Oh, today

**[04:11]** and more. But today we're Oh, today

**[04:11]** and more. But today we're Oh, today we're focusing on the agent. Uh now,

**[04:19]** uh here what we have is uh I want the

**[04:19]** uh here what we have is uh I want the agent to take on a personality. I want

**[04:21]** agent to take on a personality. I want

**[04:21]** agent to take on a personality. I want it to go ahead and talk to me about uh

**[04:25]** it to go ahead and talk to me about uh

**[04:25]** it to go ahead and talk to me about uh you know the AI World Fair, the energy

**[04:27]** you know the AI World Fair, the energy

**[04:27]** you know the AI World Fair, the energy and excitement uh of San Francisco. And

**[04:30]** and excitement uh of San Francisco. And

**[04:30]** and excitement uh of San Francisco. And I'm going to go ahead give it this

**[04:32]** I'm going to go ahead give it this

**[04:32]** I'm going to go ahead give it this prompt. And here are some guidelines

**[04:34]** prompt. And here are some guidelines

**[04:34]** prompt. And here are some guidelines that I'm going to give it. Uh, if you

**[04:36]** that I'm going to give it. Uh, if you

**[04:36]** that I'm going to give it. Uh, if you notice what these guidelines are,

**[04:37]** notice what these guidelines are,

**[04:37]** notice what these guidelines are, they're not telling it exactly what to

**[04:38]** they're not telling it exactly what to

**[04:38]** they're not telling it exactly what to implement. They're really drawing the

**[04:41]** implement. They're really drawing the

**[04:41]** implement. They're really drawing the boundaries for the agent itself. So, I'm

**[04:44]** boundaries for the agent itself. So, I'm

**[04:44]** boundaries for the agent itself. So, I'm going to go ahead press run and let it

**[04:46]** going to go ahead press run and let it

**[04:46]** going to go ahead press run and let it run in the background. And we're going

**[04:48]** run in the background. And we're going

**[04:48]** run in the background. And we're going to in the meantime go back to the talk.

**[04:59]** So, this seemingly simple example of

**[04:59]** So, this seemingly simple example of working with the agent has kind of


### [05:00 - 06:00]

**[05:00]** working with the agent has kind of

**[05:00]** working with the agent has kind of fundamentally transformed how we work.

**[05:02]** fundamentally transformed how we work.

**[05:02]** fundamentally transformed how we work. Uh, and a few months ago, it transformed

**[05:04]** Uh, and a few months ago, it transformed

**[05:04]** Uh, and a few months ago, it transformed what should have been a terrible day for

**[05:06]** what should have been a terrible day for

**[05:06]** what should have been a terrible day for me.

**[05:11]** So, to see this in action, let's take a

**[05:11]** So, to see this in action, let's take a look at my Tuesday a little bit more in

**[05:12]** look at my Tuesday a little bit more in

**[05:12]** look at my Tuesday a little bit more in depth. What actually happened and how

**[05:14]** depth. What actually happened and how

**[05:14]** depth. What actually happened and how this approach exemplifies the changes

**[05:16]** this approach exemplifies the changes

**[05:16]** this approach exemplifies the changes we've taken at Augment to integrate the

**[05:17]** we've taken at Augment to integrate the

**[05:18]** we've taken at Augment to integrate the growing capabilities of agents into our

**[05:20]** growing capabilities of agents into our

**[05:20]** growing capabilities of agents into our team. So, it's Tuesday morning, 9:00

**[05:22]** team. So, it's Tuesday morning, 9:00

**[05:22]** team. So, it's Tuesday morning, 9:00 a.m. Before I grab my coffee, I start

**[05:24]** a.m. Before I grab my coffee, I start

**[05:24]** a.m. Before I grab my coffee, I start scoping out the design system component

**[05:26]** scoping out the design system component

**[05:26]** scoping out the design system component with an agent. And instead of

**[05:28]** with an agent. And instead of

**[05:28]** with an agent. And instead of micromanaging, what I'm doing is I'm

**[05:29]** micromanaging, what I'm doing is I'm

**[05:29]** micromanaging, what I'm doing is I'm scaffolding and providing context. I'm

**[05:32]** scaffolding and providing context. I'm

**[05:32]** scaffolding and providing context. I'm giving AI the outcomes, the context,

**[05:35]** giving AI the outcomes, the context,

**[05:35]** giving AI the outcomes, the context, constraints, and I'd have it perform the

**[05:37]** constraints, and I'd have it perform the

**[05:37]** constraints, and I'd have it perform the same tasks I'd expect of any other

**[05:39]** same tasks I'd expect of any other

**[05:39]** same tasks I'd expect of any other engineer. And so, while AI goes and

**[05:41]** engineer. And so, while AI goes and

**[05:41]** engineer. And so, while AI goes and explores the codebase and builds the

**[05:43]** explores the codebase and builds the

**[05:43]** explores the codebase and builds the RFC, I'm taking my morning coffee break.

**[05:45]** RFC, I'm taking my morning coffee break.

**[05:45]** RFC, I'm taking my morning coffee break. And when I return, it has a mostly

**[05:47]** And when I return, it has a mostly

**[05:47]** And when I return, it has a mostly completed RFC that follows our

**[05:49]** completed RFC that follows our

**[05:49]** completed RFC that follows our architectural patterns. At 9:30 a.m., my

**[05:52]** architectural patterns. At 9:30 a.m., my

**[05:52]** architectural patterns. At 9:30 a.m., my phone buzzes. The staging emergency is

**[05:55]** phone buzzes. The staging emergency is

**[05:55]** phone buzzes. The staging emergency is on my plate and instead of dropping

**[05:57]** on my plate and instead of dropping

**[05:57]** on my plate and instead of dropping everything for six to eight hours of

**[05:58]** everything for six to eight hours of

**[05:58]** everything for six to eight hours of firefighting, I parallelize my


### [06:00 - 07:00]

**[06:00]** firefighting, I parallelize my

**[06:00]** firefighting, I parallelize my parallelize my work to parse through the

**[06:02]** parallelize my work to parse through the

**[06:02]** parallelize my work to parse through the noise. And so I take the component, hand

**[06:05]** noise. And so I take the component, hand

**[06:06]** noise. And so I take the component, hand it off to an agent, and it's working in

**[06:07]** it off to an agent, and it's working in

**[06:07]** it off to an agent, and it's working in the background for me. Two AI agents are

**[06:10]** the background for me. Two AI agents are

**[06:10]** the background for me. Two AI agents are working with me to help me parse through

**[06:13]** working with me to help me parse through

**[06:13]** working with me to help me parse through logs and performing a git bisect. And

**[06:15]** logs and performing a git bisect. And

**[06:15]** logs and performing a git bisect. And the augment slackbot helps me manage

**[06:18]** the augment slackbot helps me manage

**[06:18]** the augment slackbot helps me manage communications with the teams that are,

**[06:20]** communications with the teams that are,

**[06:20]** communications with the teams that are, you know, annoyed that they can't

**[06:21]** you know, annoyed that they can't

**[06:21]** you know, annoyed that they can't deploy. So in this world, I'm not

**[06:24]** deploy. So in this world, I'm not

**[06:24]** deploy. So in this world, I'm not fighting fires anymore. What I'm doing

**[06:26]** fighting fires anymore. What I'm doing

**[06:26]** fighting fires anymore. What I'm doing is I'm orchestrating parallel AI work

**[06:28]** is I'm orchestrating parallel AI work

**[06:28]** is I'm orchestrating parallel AI work streams while I get to focus on the

**[06:31]** streams while I get to focus on the

**[06:31]** streams while I get to focus on the critical path of solving the on call

**[06:32]** critical path of solving the on call

**[06:32]** critical path of solving the on call issue.

**[06:34]** issue.

**[06:34]** issue. At 10:15, the new hire interrupts my on

**[06:37]** At 10:15, the new hire interrupts my on

**[06:37]** At 10:15, the new hire interrupts my on call flow. And here, our knowledge

**[06:39]** call flow. And here, our knowledge

**[06:39]** call flow. And here, our knowledge infrastructure really starts to kick in.

**[06:41]** infrastructure really starts to kick in.

**[06:41]** infrastructure really starts to kick in. I direct the new hire to the augment

**[06:43]** I direct the new hire to the augment

**[06:43]** I direct the new hire to the augment Slackbot, which has access to our

**[06:45]** Slackbot, which has access to our

**[06:45]** Slackbot, which has access to our context engine, our codebase, all of our

**[06:47]** context engine, our codebase, all of our

**[06:47]** context engine, our codebase, all of our documentation, linear, etc. Now the new

**[06:50]** documentation, linear, etc. Now the new

**[06:50]** documentation, linear, etc. Now the new hire can have personalized realtime help

**[06:52]** hire can have personalized realtime help

**[06:52]** hire can have personalized realtime help while I can stay focused on on call

**[06:54]** while I can stay focused on on call

**[06:54]** while I can stay focused on on call response.

**[06:56]** response.

**[06:56]** response. By 11, I'm evaluating agents work and

**[06:59]** By 11, I'm evaluating agents work and

**[06:59]** By 11, I'm evaluating agents work and coordinating the next steps. The design


### [07:00 - 08:00]

**[07:01]** coordinating the next steps. The design

**[07:01]** coordinating the next steps. The design system component is complete. There's a

**[07:03]** system component is complete. There's a

**[07:03]** system component is complete. There's a storybook link and my agents have found

**[07:05]** storybook link and my agents have found

**[07:05]** storybook link and my agents have found the bad commit and already reverted it.

**[07:07]** the bad commit and already reverted it.

**[07:07]** the bad commit and already reverted it. They've started writing up a postmortem

**[07:09]** They've started writing up a postmortem

**[07:09]** They've started writing up a postmortem doc and already started exploring

**[07:11]** doc and already started exploring

**[07:11]** doc and already started exploring remediation.

**[07:12]** remediation.

**[07:12]** remediation. In this world, my role has shifted from

**[07:15]** In this world, my role has shifted from

**[07:15]** In this world, my role has shifted from implementation to evaluation.

**[07:19]** implementation to evaluation.

**[07:19]** implementation to evaluation. So now I get ready to manage the

**[07:21]** So now I get ready to manage the

**[07:21]** So now I get ready to manage the deployment of the fix and the agents are

**[07:24]** deployment of the fix and the agents are

**[07:24]** deployment of the fix and the agents are setting up off to tie up some loose

**[07:26]** setting up off to tie up some loose

**[07:26]** setting up off to tie up some loose ends.

**[07:28]** ends.

**[07:28]** ends. Now it's 12. Lunch food. Uh I go eat

**[07:31]** Now it's 12. Lunch food. Uh I go eat

**[07:31]** Now it's 12. Lunch food. Uh I go eat while the agents are doing work for me.

**[07:34]** while the agents are doing work for me.

**[07:34]** while the agents are doing work for me. After lunch, I complete what should have

**[07:36]** After lunch, I complete what should have

**[07:36]** After lunch, I complete what should have been impossible. The augment agents have

**[07:38]** been impossible. The augment agents have

**[07:38]** been impossible. The augment agents have executed the entire remediation process.

**[07:40]** executed the entire remediation process.

**[07:40]** executed the entire remediation process. The problem was with a gRPC library

**[07:42]** The problem was with a gRPC library

**[07:42]** The problem was with a gRPC library upgrade and it touched 12 services,

**[07:45]** upgrade and it touched 12 services,

**[07:46]** upgrade and it touched 12 services, 20,000 lines of code. It has tests. It

**[07:48]** 20,000 lines of code. It has tests. It

**[07:48]** 20,000 lines of code. It has tests. It has a writeup. And actually one of my uh

**[07:51]** has a writeup. And actually one of my uh

**[07:51]** has a writeup. And actually one of my uh engineering peers told me that uh it was

**[07:54]** engineering peers told me that uh it was

**[07:54]** engineering peers told me that uh it was quite surprising and and really thanked

**[07:56]** quite surprising and and really thanked

**[07:56]** quite surprising and and really thanked me for pushing this across the line uh

**[07:59]** me for pushing this across the line uh

**[07:59]** me for pushing this across the line uh when really it was all the agents doing


### [08:00 - 09:00]

**[08:01]** when really it was all the agents doing

**[08:01]** when really it was all the agents doing the work. So here what a normal

**[08:03]** the work. So here what a normal

**[08:03]** the work. So here what a normal organization might estimate as maybe

**[08:05]** organization might estimate as maybe

**[08:05]** organization might estimate as maybe three weeks of engineering work to

**[08:07]** three weeks of engineering work to

**[08:07]** three weeks of engineering work to upgrade the gRPC services is complete,

**[08:10]** upgrade the gRPC services is complete,

**[08:10]** upgrade the gRPC services is complete, tested and you know almost ready for

**[08:12]** tested and you know almost ready for

**[08:12]** tested and you know almost ready for deployment. But of course, it needs one

**[08:16]** deployment. But of course, it needs one

**[08:16]** deployment. But of course, it needs one final round of human polish.

**[08:19]** final round of human polish.

**[08:19]** final round of human polish. So the real transformation here is not

**[08:23]** So the real transformation here is not

**[08:23]** So the real transformation here is not just that I've completed this work in

**[08:25]** just that I've completed this work in

**[08:25]** just that I've completed this work in parallel. The real transformation is

**[08:27]** parallel. The real transformation is

**[08:27]** parallel. The real transformation is that I've unlocked time that I

**[08:29]** that I've unlocked time that I

**[08:29]** that I've unlocked time that I previously did not have.

**[08:32]** previously did not have.

**[08:32]** previously did not have. Now that's not a dream. That's not a

**[08:33]** Now that's not a dream. That's not a

**[08:33]** Now that's not a dream. That's not a pitch. This scenario that I just

**[08:35]** pitch. This scenario that I just

**[08:35]** pitch. This scenario that I just described, all three of these challenges

**[08:36]** described, all three of these challenges

**[08:36]** described, all three of these challenges was something that I personally had to

**[08:38]** was something that I personally had to

**[08:38]** was something that I personally had to face and solved in around half a day of

**[08:41]** face and solved in around half a day of

**[08:41]** face and solved in around half a day of active keyboard time. Same problems,

**[08:45]** active keyboard time. Same problems,

**[08:45]** active keyboard time. Same problems, same complexity, same time pressure, but

**[08:47]** same complexity, same time pressure, but

**[08:47]** same complexity, same time pressure, but instead of it being one of those days,

**[08:48]** instead of it being one of those days,

**[08:48]** instead of it being one of those days, it became a normal Tuesday.

**[08:52]** it became a normal Tuesday.

**[08:52]** it became a normal Tuesday. Now, what I just show kind of the crux

**[08:54]** Now, what I just show kind of the crux

**[08:54]** Now, what I just show kind of the crux of how we at Augment work with agents

**[08:56]** of how we at Augment work with agents

**[08:56]** of how we at Augment work with agents today by leveraging its unique strengths

**[08:58]** today by leveraging its unique strengths

**[08:58]** today by leveraging its unique strengths while compensating for its weaknesses.


### [09:00 - 10:00]

**[09:00]** while compensating for its weaknesses.

**[09:00]** while compensating for its weaknesses. And that can be summed up in one core

**[09:02]** And that can be summed up in one core

**[09:02]** And that can be summed up in one core realization.

**[09:03]** realization.

**[09:03]** realization. To make the most use out of AI, we need

**[09:06]** To make the most use out of AI, we need

**[09:06]** To make the most use out of AI, we need to work with it as we would work with

**[09:08]** to work with it as we would work with

**[09:08]** to work with it as we would work with junior engineers. Not assigning tickets,

**[09:11]** junior engineers. Not assigning tickets,

**[09:11]** junior engineers. Not assigning tickets, but mentoring.

**[09:13]** but mentoring.

**[09:13]** but mentoring. Now, I know we we've all heard this.

**[09:15]** Now, I know we we've all heard this.

**[09:16]** Now, I know we we've all heard this. We're all rolling our eyes a little bit.

**[09:17]** We're all rolling our eyes a little bit.

**[09:17]** We're all rolling our eyes a little bit. You know, AI has the intelligence of a

**[09:19]** You know, AI has the intelligence of a

**[09:19]** You know, AI has the intelligence of a junior engineer. Let's actually break

**[09:21]** junior engineer. Let's actually break

**[09:21]** junior engineer. Let's actually break down uh how this analogy applies and

**[09:24]** down uh how this analogy applies and

**[09:24]** down uh how this analogy applies and more importantly where it doesn't. Both

**[09:27]** more importantly where it doesn't. Both

**[09:27]** more importantly where it doesn't. Both AI and new engineers start with no

**[09:29]** AI and new engineers start with no

**[09:29]** AI and new engineers start with no context of your systems. They lack your

**[09:31]** context of your systems. They lack your

**[09:31]** context of your systems. They lack your organizational context and most

**[09:33]** organizational context and most

**[09:33]** organizational context and most importantly they lack years of

**[09:35]** importantly they lack years of

**[09:35]** importantly they lack years of experience working with systems and your

**[09:37]** experience working with systems and your

**[09:38]** experience working with systems and your systems. So they're able to implement in

**[09:40]** systems. So they're able to implement in

**[09:40]** systems. So they're able to implement in isolation but they kind of need a

**[09:42]** isolation but they kind of need a

**[09:42]** isolation but they kind of need a structured environment to work in to

**[09:43]** structured environment to work in to

**[09:43]** structured environment to work in to perform best. These three pieces make up

**[09:47]** perform best. These three pieces make up

**[09:47]** perform best. These three pieces make up what we call the context or knowledge

**[09:49]** what we call the context or knowledge

**[09:50]** what we call the context or knowledge gap.

**[09:51]** gap.

**[09:51]** gap. Now in learning and speed is kind of

**[09:53]** Now in learning and speed is kind of

**[09:53]** Now in learning and speed is kind of where they differ really drastically. A

**[09:55]** where they differ really drastically. A

**[09:55]** where they differ really drastically. A junior engineer learns and executes

**[09:56]** junior engineer learns and executes

**[09:56]** junior engineer learns and executes fairly slowly, but they can retain and

**[09:58]** fairly slowly, but they can retain and

**[09:58]** fairly slowly, but they can retain and synthesize knowledge while if given the


### [10:00 - 11:00]

**[10:01]** synthesize knowledge while if given the

**[10:01]** synthesize knowledge while if given the same information, AI can process it and

**[10:03]** same information, AI can process it and

**[10:03]** same information, AI can process it and implement what you want in minutes or

**[10:05]** implement what you want in minutes or

**[10:05]** implement what you want in minutes or even seconds, but forgets things between

**[10:08]** even seconds, but forgets things between

**[10:08]** even seconds, but forgets things between conversations.

**[10:10]** conversations.

**[10:10]** conversations. So for us, that means that AI is

**[10:13]** So for us, that means that AI is

**[10:13]** So for us, that means that AI is effectively a perpetually junior

**[10:14]** effectively a perpetually junior

**[10:14]** effectively a perpetually junior engineer, but one that can work on

**[10:16]** engineer, but one that can work on

**[10:16]** engineer, but one that can work on multiple tasks simultaneously and

**[10:18]** multiple tasks simultaneously and

**[10:18]** multiple tasks simultaneously and incredibly quickly. So to make the most

**[10:20]** incredibly quickly. So to make the most

**[10:20]** incredibly quickly. So to make the most use out of AI, we must become perpetual

**[10:23]** use out of AI, we must become perpetual

**[10:23]** use out of AI, we must become perpetual tech leads. We need to become mentors to

**[10:25]** tech leads. We need to become mentors to

**[10:25]** tech leads. We need to become mentors to our AI apprentices just as we would

**[10:27]** our AI apprentices just as we would

**[10:27]** our AI apprentices just as we would become mentors to our juniors.

**[10:30]** become mentors to our juniors.

**[10:30]** become mentors to our juniors. Now you might be thinking this sounds

**[10:32]** Now you might be thinking this sounds

**[10:32]** Now you might be thinking this sounds great for individual engineers. What

**[10:34]** great for individual engineers. What

**[10:34]** great for individual engineers. What does this mean for teams my

**[10:36]** does this mean for teams my

**[10:36]** does this mean for teams my organization? Uh and that's the right

**[10:38]** organization? Uh and that's the right

**[10:38]** organization? Uh and that's the right question to ask and where a lot of

**[10:39]** question to ask and where a lot of

**[10:39]** question to ask and where a lot of organizations struggle including

**[10:41]** organizations struggle including

**[10:41]** organizations struggle including augment.

**[10:42]** augment.

**[10:42]** augment. So we've seen this pattern repeatedly.

**[10:44]** So we've seen this pattern repeatedly.

**[10:44]** So we've seen this pattern repeatedly. Individual engineers can achieve

**[10:45]** Individual engineers can achieve

**[10:46]** Individual engineers can achieve remarkable productivity gains with AI

**[10:48]** remarkable productivity gains with AI

**[10:48]** remarkable productivity gains with AI but when the teams try to scale progress

**[10:51]** but when the teams try to scale progress

**[10:51]** but when the teams try to scale progress stalls.

**[10:53]** stalls.

**[10:53]** stalls. Even when we first started working on

**[10:54]** Even when we first started working on

**[10:54]** Even when we first started working on the Augment agent, actually I remember

**[10:55]** the Augment agent, actually I remember

**[10:55]** the Augment agent, actually I remember people were saying, "Your agent is so

**[10:58]** people were saying, "Your agent is so

**[10:58]** people were saying, "Your agent is so good. How can I get what Eric has. Now


### [11:00 - 12:00]

**[11:01]** good. How can I get what Eric has. Now

**[11:01]** good. How can I get what Eric has. Now this is kind of indicative of two bigger

**[11:04]** this is kind of indicative of two bigger

**[11:04]** this is kind of indicative of two bigger problems.

**[11:06]** problems.

**[11:06]** problems. How do we replicate individual success

**[11:07]** How do we replicate individual success

**[11:08]** How do we replicate individual success with AI across teams? And how do we turn

**[11:10]** with AI across teams? And how do we turn

**[11:10]** with AI across teams? And how do we turn team productivity into sustainable

**[11:12]** team productivity into sustainable

**[11:12]** team productivity into sustainable business advantage? What's actually

**[11:15]** business advantage? What's actually

**[11:15]** business advantage? What's actually blocking real organizations from using

**[11:18]** blocking real organizations from using

**[11:18]** blocking real organizations from using AI effectively?"

**[11:21]** AI effectively?"

**[11:21]** AI effectively?" This answer turns out to be fairly

**[11:23]** This answer turns out to be fairly

**[11:23]** This answer turns out to be fairly simple. Remember the context of

**[11:25]** simple. Remember the context of

**[11:25]** simple. Remember the context of knowledge gap we were just talking

**[11:26]** knowledge gap we were just talking

**[11:26]** knowledge gap we were just talking about. This is not a new blocker. It's

**[11:29]** about. This is not a new blocker. It's

**[11:29]** about. This is not a new blocker. It's the same problem that makes new hires

**[11:32]** the same problem that makes new hires

**[11:32]** the same problem that makes new hires take 6 months to ramp up in your

**[11:34]** take 6 months to ramp up in your

**[11:34]** take 6 months to ramp up in your standard or why four out of every five

**[11:37]** standard or why four out of every five

**[11:37]** standard or why four out of every five engineers across our industry site

**[11:39]** engineers across our industry site

**[11:39]** engineers across our industry site context deficit as the biggest blocker.

**[11:42]** context deficit as the biggest blocker.

**[11:42]** context deficit as the biggest blocker. So the the core problem here is context.

**[11:45]** So the the core problem here is context.

**[11:45]** So the the core problem here is context. And we've had this problem for decades

**[11:46]** And we've had this problem for decades

**[11:46]** And we've had this problem for decades even without AI in the mix.

**[11:50]** even without AI in the mix.

**[11:50]** even without AI in the mix. And so a paradox kind of arises in our

**[11:52]** And so a paradox kind of arises in our

**[11:52]** And so a paradox kind of arises in our industry. How can we hope to solve the

**[11:54]** industry. How can we hope to solve the

**[11:54]** industry. How can we hope to solve the knowledge infrastructure problem when

**[11:56]** knowledge infrastructure problem when

**[11:56]** knowledge infrastructure problem when it's still this bad for human teams? And

**[11:58]** it's still this bad for human teams? And

**[11:58]** it's still this bad for human teams? And how can we scale AI beyond an individual


### [12:00 - 13:00]

**[12:00]** how can we scale AI beyond an individual

**[12:00]** how can we scale AI beyond an individual when we don't have the requisite

**[12:02]** when we don't have the requisite

**[12:02]** when we don't have the requisite knowledge infrastructure to do so?

**[12:09]** This doesn't mean writing more docs.

**[12:09]** This doesn't mean writing more docs. This doesn't mean doing knowledge

**[12:10]** This doesn't mean doing knowledge

**[12:10]** This doesn't mean doing knowledge reorgs. This doesn't mean you know

**[12:12]** reorgs. This doesn't mean you know

**[12:12]** reorgs. This doesn't mean you know completely rebuilding your organization

**[12:14]** completely rebuilding your organization

**[12:14]** completely rebuilding your organization for AI. In that world, humans are

**[12:16]** for AI. In that world, humans are

**[12:16]** for AI. In that world, humans are serving AI, not the other way around.

**[12:20]** serving AI, not the other way around.

**[12:20]** serving AI, not the other way around. It means kind of choosing the right

**[12:22]** It means kind of choosing the right

**[12:22]** It means kind of choosing the right tools and systems that can

**[12:23]** tools and systems that can

**[12:23]** tools and systems that can institutionalize knowledge

**[12:25]** institutionalize knowledge

**[12:25]** institutionalize knowledge infrastructure for you.

**[12:28]** infrastructure for you.

**[12:28]** infrastructure for you. So, here's how to get started. Companies

**[12:31]** So, here's how to get started. Companies

**[12:31]** So, here's how to get started. Companies that you successfully use augment and

**[12:32]** that you successfully use augment and

**[12:32]** that you successfully use augment and other AI tools tend to follow a fairly

**[12:35]** other AI tools tend to follow a fairly

**[12:35]** other AI tools tend to follow a fairly similar pattern to get started, which

**[12:37]** similar pattern to get started, which

**[12:37]** similar pattern to get started, which we've distilled into three steps. The

**[12:40]** we've distilled into three steps. The

**[12:40]** we've distilled into three steps. The first step is knowledge gathering. Start

**[12:42]** first step is knowledge gathering. Start

**[12:42]** first step is knowledge gathering. Start by exploring your existing knowledge

**[12:43]** by exploring your existing knowledge

**[12:44]** by exploring your existing knowledge bases. What do you have documented? Map

**[12:47]** bases. What do you have documented? Map

**[12:47]** bases. What do you have documented? Map out your key knowledge sources, Notion,

**[12:49]** out your key knowledge sources, Notion,

**[12:49]** out your key knowledge sources, Notion, Google Docs, GitHub, etc. Fill in the

**[12:53]** Google Docs, GitHub, etc. Fill in the

**[12:53]** Google Docs, GitHub, etc. Fill in the critical knowledge gaps specifically

**[12:54]** critical knowledge gaps specifically

**[12:54]** critical knowledge gaps specifically around meetings and decisions with

**[12:57]** around meetings and decisions with

**[12:57]** around meetings and decisions with meeting intelligence tools to capture

**[12:59]** meeting intelligence tools to capture

**[12:59]** meeting intelligence tools to capture that knowledge that would otherwise be


### [13:00 - 14:00]

**[13:01]** that knowledge that would otherwise be

**[13:01]** that knowledge that would otherwise be lost.

**[13:03]** lost.

**[13:03]** lost. In fact, actually most of the uh

**[13:04]** In fact, actually most of the uh

**[13:04]** In fact, actually most of the uh meetings that I personally uh attend

**[13:06]** meetings that I personally uh attend

**[13:06]** meetings that I personally uh attend outside of engineering nowadays start

**[13:08]** outside of engineering nowadays start

**[13:08]** outside of engineering nowadays start and end with a granola AI recording and

**[13:10]** and end with a granola AI recording and

**[13:10]** and end with a granola AI recording and uh comes with basically a list of tasks

**[13:13]** uh comes with basically a list of tasks

**[13:13]** uh comes with basically a list of tasks that we can directly put into our task

**[13:14]** that we can directly put into our task

**[13:14]** that we can directly put into our task tracker at the end of it.

**[13:17]** tracker at the end of it.

**[13:17]** tracker at the end of it. Uh and finally, begin integrating data

**[13:18]** Uh and finally, begin integrating data

**[13:18]** Uh and finally, begin integrating data sources using things like MCP and

**[13:20]** sources using things like MCP and

**[13:20]** sources using things like MCP and augment native integrations to create

**[13:22]** augment native integrations to create

**[13:22]** augment native integrations to create the beginnings of your knowledge

**[13:24]** the beginnings of your knowledge

**[13:24]** the beginnings of your knowledge infrastructure.

**[13:29]** Step two is starting to gain familiarity

**[13:29]** Step two is starting to gain familiarity with your tools. This refers to both you

**[13:31]** with your tools. This refers to both you

**[13:31]** with your tools. This refers to both you gaining familiarity with the tools, but

**[13:33]** gaining familiarity with the tools, but

**[13:33]** gaining familiarity with the tools, but also letting the tools gain familiarity

**[13:35]** also letting the tools gain familiarity

**[13:35]** also letting the tools gain familiarity with you and your organization.

**[13:37]** with you and your organization.

**[13:38]** with you and your organization. More broadly, introduce these tools

**[13:39]** More broadly, introduce these tools

**[13:39]** More broadly, introduce these tools across your teams and enable them to

**[13:41]** across your teams and enable them to

**[13:42]** across your teams and enable them to explore the strengths and weaknesses of

**[13:44]** explore the strengths and weaknesses of

**[13:44]** explore the strengths and weaknesses of AI in your specific contexts.

**[13:47]** AI in your specific contexts.

**[13:47]** AI in your specific contexts. This is where you build up the muscle of

**[13:49]** This is where you build up the muscle of

**[13:49]** This is where you build up the muscle of working with AI and start teaching your

**[13:51]** working with AI and start teaching your

**[13:51]** working with AI and start teaching your platform of choice about things like

**[13:53]** platform of choice about things like

**[13:53]** platform of choice about things like coding patterns, architectural

**[13:54]** coding patterns, architectural

**[13:54]** coding patterns, architectural decisions, business logic, etc.

**[13:59]** decisions, business logic, etc.

**[13:59]** decisions, business logic, etc. Step three is leaning in. Expand the


### [14:00 - 15:00]

**[14:01]** Step three is leaning in. Expand the

**[14:01]** Step three is leaning in. Expand the successful patterns you've discovered.

**[14:03]** successful patterns you've discovered.

**[14:03]** successful patterns you've discovered. And you can at this point start to

**[14:04]** And you can at this point start to

**[14:04]** And you can at this point start to entrust more complex tasks as you've

**[14:07]** entrust more complex tasks as you've

**[14:07]** entrust more complex tasks as you've built up trust and as your confidence in

**[14:09]** built up trust and as your confidence in

**[14:09]** built up trust and as your confidence in these systems grow. Share your

**[14:11]** these systems grow. Share your

**[14:12]** these systems grow. Share your successful memories and task lists

**[14:13]** successful memories and task lists

**[14:13]** successful memories and task lists across teams. This is where compound

**[14:15]** across teams. This is where compound

**[14:15]** across teams. This is where compound learning starts to really take off. When

**[14:17]** learning starts to really take off. When

**[14:17]** learning starts to really take off. When people were asking me about the, you

**[14:19]** people were asking me about the, you

**[14:19]** people were asking me about the, you know, how can I get Eric's agent? We

**[14:21]** know, how can I get Eric's agent? We

**[14:21]** know, how can I get Eric's agent? We have a a feature called memories and I

**[14:23]** have a a feature called memories and I

**[14:23]** have a a feature called memories and I basically just shared that file with

**[14:24]** basically just shared that file with

**[14:24]** basically just shared that file with them.

**[14:27]** them.

**[14:27]** them. This is where again compound learning

**[14:29]** This is where again compound learning

**[14:29]** This is where again compound learning can take off and knowledge uh and

**[14:31]** can take off and knowledge uh and

**[14:31]** can take off and knowledge uh and individual successes can start to

**[14:33]** individual successes can start to

**[14:33]** individual successes can start to multiply and spread across your

**[14:34]** multiply and spread across your

**[14:34]** multiply and spread across your organization.

**[14:36]** organization.

**[14:36]** organization. So while us as engineers are working

**[14:39]** So while us as engineers are working

**[14:39]** So while us as engineers are working with AI systems by providing missing

**[14:41]** with AI systems by providing missing

**[14:41]** with AI systems by providing missing structure and guidance, successful

**[14:43]** structure and guidance, successful

**[14:43]** structure and guidance, successful organizations as a whole are enabling AI

**[14:46]** organizations as a whole are enabling AI

**[14:46]** organizations as a whole are enabling AI systems by institutionalizing their

**[14:47]** systems by institutionalizing their

**[14:47]** systems by institutionalizing their knowledge infrastructure.

**[14:55]** So now if these things are possible now,

**[14:56]** So now if these things are possible now, how is that actually changed the way we

**[14:57]** how is that actually changed the way we

**[14:57]** how is that actually changed the way we operate at augment? What future is


### [15:00 - 16:00]

**[15:00]** operate at augment? What future is

**[15:00]** operate at augment? What future is actually available to us? Let me bring

**[15:02]** actually available to us? Let me bring

**[15:02]** actually available to us? Let me bring you back to the agent here and show you.

**[15:06]** you back to the agent here and show you.

**[15:06]** you back to the agent here and show you. So I have a development environment up

**[15:09]** So I have a development environment up

**[15:10]** So I have a development environment up here. So this is uh uh on the real

**[15:12]** here. So this is uh uh on the real

**[15:12]** here. So this is uh uh on the real augment codebase. This is our a dev

**[15:14]** augment codebase. This is our a dev

**[15:14]** augment codebase. This is our a dev version of our build. You can see in the

**[15:16]** version of our build. You can see in the

**[15:16]** version of our build. You can see in the top that's the extension development

**[15:17]** top that's the extension development

**[15:18]** top that's the extension development environment. And hopefully when I type

**[15:20]** environment. And hopefully when I type

**[15:20]** environment. And hopefully when I type at I can okay personalities AI engineer

**[15:25]** at I can okay personalities AI engineer

**[15:25]** at I can okay personalities AI engineer world fair Auggie. Awesome.

**[15:28]** world fair Auggie. Awesome.

**[15:28]** world fair Auggie. Awesome. You can see it even created a little

**[15:30]** You can see it even created a little

**[15:30]** You can see it even created a little icon. It's uh it's a little rough but

**[15:32]** icon. It's uh it's a little rough but

**[15:32]** icon. It's uh it's a little rough but there it is. Uh what is your favorite

**[15:36]** there it is. Uh what is your favorite

**[15:36]** there it is. Uh what is your favorite city?

**[15:43]** Let's see what it says.

**[15:43]** Let's see what it says. Awesome. There we go. Uh easy question.

**[15:47]** Awesome. There we go. Uh easy question.

**[15:48]** Awesome. There we go. Uh easy question. It's absolutely hands down San

**[15:49]** It's absolutely hands down San

**[15:49]** It's absolutely hands down San Francisco. I mean, are you kidding me?

**[15:51]** Francisco. I mean, are you kidding me?

**[15:51]** Francisco. I mean, are you kidding me? The city is the epicenter of the AI

**[15:52]** The city is the epicenter of the AI

**[15:52]** The city is the epicenter of the AI revolution. So, that's awesome. Uh, you

**[15:56]** revolution. So, that's awesome. Uh, you

**[15:56]** revolution. So, that's awesome. Uh, you can see that, you know, as I was giving

**[15:58]** can see that, you know, as I was giving

**[15:58]** can see that, you know, as I was giving this talk with just a simple prompt, we


### [16:00 - 17:00]

**[16:00]** this talk with just a simple prompt, we

**[16:00]** this talk with just a simple prompt, we were able to create a new personality.

**[16:02]** were able to create a new personality.

**[16:02]** were able to create a new personality. This kind of exemplifies, uh, some of

**[16:04]** This kind of exemplifies, uh, some of

**[16:04]** This kind of exemplifies, uh, some of the agent personality stuff, uh, that

**[16:06]** the agent personality stuff, uh, that

**[16:06]** the agent personality stuff, uh, that was talked about earlier. Um but this

**[16:09]** was talked about earlier. Um but this

**[16:09]** was talked about earlier. Um but this you know really starts to change when

**[16:12]** you know really starts to change when

**[16:12]** you know really starts to change when you know if I can give a talk and also

**[16:15]** you know if I can give a talk and also

**[16:15]** you know if I can give a talk and also implement a feature it really starts to

**[16:17]** implement a feature it really starts to

**[16:17]** implement a feature it really starts to change how we think about the economics

**[16:19]** change how we think about the economics

**[16:19]** change how we think about the economics of developing software.

**[16:26]** See once we solve the knowledge

**[16:26]** See once we solve the knowledge infrastructure problem everything starts

**[16:28]** infrastructure problem everything starts

**[16:28]** infrastructure problem everything starts to change. When information transfer

**[16:31]** to change. When information transfer

**[16:31]** to change. When information transfer becomes instant and scalable, we unlock

**[16:34]** becomes instant and scalable, we unlock

**[16:34]** becomes instant and scalable, we unlock AI's true economic potential. Parallel

**[16:37]** AI's true economic potential. Parallel

**[16:37]** AI's true economic potential. Parallel exploration of your business. The

**[16:39]** exploration of your business. The

**[16:39]** exploration of your business. The traditional approach to building

**[16:40]** traditional approach to building

**[16:40]** traditional approach to building software starts with designing then

**[16:42]** software starts with designing then

**[16:42]** software starts with designing then building than testing. And each

**[16:44]** building than testing. And each

**[16:44]** building than testing. And each iteration locks us out of potential

**[16:45]** iteration locks us out of potential

**[16:45]** iteration locks us out of potential decisions at every single step. But when

**[16:48]** decisions at every single step. But when

**[16:48]** decisions at every single step. But when knowledge infrastructure exists,

**[16:50]** knowledge infrastructure exists,

**[16:50]** knowledge infrastructure exists, prototyping is cheap and building takes

**[16:52]** prototyping is cheap and building takes

**[16:52]** prototyping is cheap and building takes fewer resources. We can do something

**[16:53]** fewer resources. We can do something

**[16:53]** fewer resources. We can do something drastically different. Instead of

**[16:55]** drastically different. Instead of

**[16:55]** drastically different. Instead of guessing at what might be the best

**[16:57]** guessing at what might be the best

**[16:57]** guessing at what might be the best approach, we can rapidly prototype,

**[16:59]** approach, we can rapidly prototype,

**[16:59]** approach, we can rapidly prototype, iterate, test, and then converge on a


### [17:00 - 18:00]

**[17:02]** iterate, test, and then converge on a

**[17:02]** iterate, test, and then converge on a real decision based on real metrics and

**[17:04]** real decision based on real metrics and

**[17:04]** real decision based on real metrics and by putting our products in front of

**[17:05]** by putting our products in front of

**[17:06]** by putting our products in front of people.

**[17:07]** people.

**[17:07]** people. At Augment today, we have constantly

**[17:09]** At Augment today, we have constantly

**[17:09]** At Augment today, we have constantly have prototypes floating around. We have

**[17:11]** have prototypes floating around. We have

**[17:11]** have prototypes floating around. We have a prototype of a VS code fork in case we

**[17:13]** a prototype of a VS code fork in case we

**[17:13]** a prototype of a VS code fork in case we need it. Uh, Augment itself became uh uh

**[17:16]** need it. Uh, Augment itself became uh uh

**[17:16]** need it. Uh, Augment itself became uh uh or sorry, agents itself began as a

**[17:18]** or sorry, agents itself began as a

**[17:18]** or sorry, agents itself began as a prototype as well. And many of the

**[17:20]** prototype as well. And many of the

**[17:20]** prototype as well. And many of the features in our product that our users

**[17:22]** features in our product that our users

**[17:22]** features in our product that our users love uh began as a prototype when an

**[17:25]** love uh began as a prototype when an

**[17:25]** love uh began as a prototype when an engineer at augment just decided hey I'm

**[17:27]** engineer at augment just decided hey I'm

**[17:27]** engineer at augment just decided hey I'm going to try this and with an agent and

**[17:30]** going to try this and with an agent and

**[17:30]** going to try this and with an agent and by trying multiple approaches

**[17:32]** by trying multiple approaches

**[17:32]** by trying multiple approaches simultaneously again we can quickly

**[17:33]** simultaneously again we can quickly

**[17:34]** simultaneously again we can quickly converge with real data on the best

**[17:36]** converge with real data on the best

**[17:36]** converge with real data on the best approaches that we should actually

**[17:38]** approaches that we should actually

**[17:38]** approaches that we should actually invest in productionizing without

**[17:40]** invest in productionizing without

**[17:40]** invest in productionizing without arguing you know in a room talking to

**[17:42]** arguing you know in a room talking to

**[17:42]** arguing you know in a room talking to each other about what might be best.

**[17:46]** each other about what might be best.

**[17:46]** each other about what might be best. As an engineer, we've all had to justify

**[17:48]** As an engineer, we've all had to justify

**[17:48]** As an engineer, we've all had to justify a designi decision to leadership,

**[17:50]** a designi decision to leadership,

**[17:50]** a designi decision to leadership, complained about tech debt, or cursed

**[17:52]** complained about tech debt, or cursed

**[17:52]** complained about tech debt, or cursed our past selves for doing something in a

**[17:54]** our past selves for doing something in a

**[17:54]** our past selves for doing something in a particular way. And as leadership, we

**[17:56]** particular way. And as leadership, we

**[17:56]** particular way. And as leadership, we all wish we could go back and redo some

**[17:57]** all wish we could go back and redo some

**[17:57]** all wish we could go back and redo some critical decisions or enable our teams

**[17:59]** critical decisions or enable our teams

**[17:59]** critical decisions or enable our teams to do more strategic work instead of


### [18:00 - 19:00]

**[18:01]** to do more strategic work instead of

**[18:01]** to do more strategic work instead of constantly throwing fires at them to put

**[18:03]** constantly throwing fires at them to put

**[18:03]** constantly throwing fires at them to put out. But with parallel exploration, we

**[18:05]** out. But with parallel exploration, we

**[18:05]** out. But with parallel exploration, we can turn these wishes from retroactive

**[18:07]** can turn these wishes from retroactive

**[18:07]** can turn these wishes from retroactive to proactive. By measuring and testing

**[18:10]** to proactive. By measuring and testing

**[18:10]** to proactive. By measuring and testing divergent approaches from the start, we

**[18:12]** divergent approaches from the start, we

**[18:12]** divergent approaches from the start, we can start making decisions better

**[18:14]** can start making decisions better

**[18:14]** can start making decisions better informed by data. And when we can

**[18:16]** informed by data. And when we can

**[18:16]** informed by data. And when we can measure hypotheses of designs,

**[18:18]** measure hypotheses of designs,

**[18:18]** measure hypotheses of designs, prototypes, and architectures early on

**[18:20]** prototypes, and architectures early on

**[18:20]** prototypes, and architectures early on and validate them, we reach a

**[18:22]** and validate them, we reach a

**[18:22]** and validate them, we reach a fascinating conclusion.

**[18:25]** fascinating conclusion.

**[18:25]** fascinating conclusion. If we use AI effectively to augment our

**[18:28]** If we use AI effectively to augment our

**[18:28]** If we use AI effectively to augment our organizations, we can make the creation

**[18:30]** organizations, we can make the creation

**[18:30]** organizations, we can make the creation of software more of a science, not less.

**[18:34]** of software more of a science, not less.

**[18:34]** of software more of a science, not less. And that begins with all of our

**[18:36]** And that begins with all of our

**[18:36]** And that begins with all of our engineers, organizations, teams choosing

**[18:38]** engineers, organizations, teams choosing

**[18:38]** engineers, organizations, teams choosing the best tools for our jobs that most

**[18:41]** the best tools for our jobs that most

**[18:41]** the best tools for our jobs that most effectively allow us to mentor our

**[18:44]** effectively allow us to mentor our

**[18:44]** effectively allow us to mentor our machines.

**[18:46]** machines.

**[18:46]** machines. Thank you all so much for your time. If

**[18:48]** Thank you all so much for your time. If

**[18:48]** Thank you all so much for your time. If what we talked about today resonates

**[18:49]** what we talked about today resonates

**[18:49]** what we talked about today resonates with you, please visit the augment booth

**[18:51]** with you, please visit the augment booth

**[18:51]** with you, please visit the augment booth on the explo uh expo floor. Go to

**[18:53]** on the explo uh expo floor. Go to

**[18:53]** on the explo uh expo floor. Go to augment.com, try us out for free. And

**[18:55]** augment.com, try us out for free. And

**[18:56]** augment.com, try us out for free. And remote agents is out this week. Let it

**[18:57]** remote agents is out this week. Let it

**[18:57]** remote agents is out this week. Let it parallelize your work for you. Thank you

**[18:59]** parallelize your work for you. Thank you

**[18:59]** parallelize your work for you. Thank you so much.


