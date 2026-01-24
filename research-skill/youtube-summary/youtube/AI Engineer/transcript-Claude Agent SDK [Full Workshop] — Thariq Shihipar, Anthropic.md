# Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic

**Video URL:** https://youtu.be/TqC1qOfiVcQ?si=Fz9YUae0Ux7QirHZ

---

## Full Transcript

### [00:00 - 01:00]

**[00:23]** Okay. Yeah, thanks for joining me. I uh

**[00:23]** Okay. Yeah, thanks for joining me. I uh I'm still on the West Coast time, so it

**[00:24]** I'm still on the West Coast time, so it

**[00:24]** I'm still on the West Coast time, so it feels like I'm doing this at like 7:00

**[00:27]** feels like I'm doing this at like 7:00

**[00:27]** feels like I'm doing this at like 7:00 a.m.

**[00:28]** a.m.

**[00:28]** a.m. Uh so yeah, but um glad to talk to you

**[00:33]** Uh so yeah, but um glad to talk to you

**[00:33]** Uh so yeah, but um glad to talk to you about the Claude agent SDK. So um yeah,

**[00:38]** about the Claude agent SDK. So um yeah,

**[00:38]** about the Claude agent SDK. So um yeah, I think like this is going to be like a

**[00:40]** I think like this is going to be like a

**[00:40]** I think like this is going to be like a rough agenda, but we're going to talk

**[00:41]** rough agenda, but we're going to talk

**[00:41]** rough agenda, but we're going to talk about we're going to talk about like

**[00:43]** about we're going to talk about like

**[00:43]** about we're going to talk about like what is the claud agent SDK? Why use it?

**[00:46]** what is the claud agent SDK? Why use it?

**[00:46]** what is the claud agent SDK? Why use it? There's so many other agent frameworks.

**[00:48]** There's so many other agent frameworks.

**[00:48]** There's so many other agent frameworks. What is an agent? What is an agent

**[00:49]** What is an agent? What is an agent

**[00:49]** What is an agent? What is an agent framework?

**[00:51]** framework?

**[00:51]** framework? um how do you design an agent uh using

**[00:54]** um how do you design an agent uh using

**[00:54]** um how do you design an agent uh using the agent SDK or or just in general? Um

**[00:57]** the agent SDK or or just in general? Um

**[00:57]** the agent SDK or or just in general? Um and then I'm going to do some like live


### [01:00 - 02:00]

**[01:00]** and then I'm going to do some like live

**[01:00]** and then I'm going to do some like live coding or Claude is going to do some

**[01:01]** coding or Claude is going to do some

**[01:01]** coding or Claude is going to do some live coding on prototyping an agent. Um

**[01:04]** live coding on prototyping an agent. Um

**[01:04]** live coding on prototyping an agent. Um and uh I've got some starter code. But

**[01:07]** and uh I've got some starter code. But

**[01:07]** and uh I've got some starter code. But uh yeah, I I the whole goal of this is

**[01:11]** uh yeah, I I the whole goal of this is

**[01:11]** uh yeah, I I the whole goal of this is like know we got two hours. We're going

**[01:12]** like know we got two hours. We're going

**[01:12]** like know we got two hours. We're going to be super collaborative, ask

**[01:14]** to be super collaborative, ask

**[01:14]** to be super collaborative, ask questions. Um, this is also going to be

**[01:17]** questions. Um, this is also going to be

**[01:17]** questions. Um, this is also going to be not like a super canned demo in the

**[01:20]** not like a super canned demo in the

**[01:20]** not like a super canned demo in the sense that like we're going to be like

**[01:22]** sense that like we're going to be like

**[01:22]** sense that like we're going to be like thinking through things live. You know,

**[01:24]** thinking through things live. You know,

**[01:24]** thinking through things live. You know, I'm not going to have all the answers

**[01:25]** I'm not going to have all the answers

**[01:25]** I'm not going to have all the answers right away. Um, and I think that'll be a

**[01:28]** right away. Um, and I think that'll be a

**[01:28]** right away. Um, and I think that'll be a good way of like building an agent loop

**[01:31]** good way of like building an agent loop

**[01:31]** good way of like building an agent loop I think is like really very much like

**[01:33]** I think is like really very much like

**[01:33]** I think is like really very much like kind of an art or intuition. So, um, but

**[01:37]** kind of an art or intuition. So, um, but

**[01:37]** kind of an art or intuition. So, um, but yeah, before we get started, just

**[01:39]** yeah, before we get started, just

**[01:39]** yeah, before we get started, just curious, a show of hands, like how many

**[01:41]** curious, a show of hands, like how many

**[01:41]** curious, a show of hands, like how many people have heard of the cloud agent SDK

**[01:43]** people have heard of the cloud agent SDK

**[01:43]** people have heard of the cloud agent SDK or Okay, great. Cool. How many have like

**[01:47]** or Okay, great. Cool. How many have like

**[01:47]** or Okay, great. Cool. How many have like used it or tried it out? Okay, awesome.

**[01:50]** used it or tried it out? Okay, awesome.

**[01:50]** used it or tried it out? Okay, awesome. Okay, so pretty good show of hands. Um,

**[01:53]** Okay, so pretty good show of hands. Um,

**[01:53]** Okay, so pretty good show of hands. Um, yeah, so I'll I'll just get started on

**[01:55]** yeah, so I'll I'll just get started on

**[01:55]** yeah, so I'll I'll just get started on like the like, you know, overview on

**[01:58]** like the like, you know, overview on

**[01:58]** like the like, you know, overview on agents. I I think that like this is I I


### [02:00 - 03:00]

**[02:02]** agents. I I think that like this is I I

**[02:02]** agents. I I think that like this is I I I think something that people

**[02:04]** I think something that people

**[02:04]** I think something that people [clears throat] have seen before, but I

**[02:06]** [clears throat] have seen before, but I

**[02:06]** [clears throat] have seen before, but I think it still is taking some time to

**[02:08]** think it still is taking some time to

**[02:08]** think it still is taking some time to like really sink in. Uh how AI features

**[02:12]** like really sink in. Uh how AI features

**[02:12]** like really sink in. Uh how AI features are evolving, you know? So I think like

**[02:15]** are evolving, you know? So I think like

**[02:15]** are evolving, you know? So I think like when GPT, you know, 3 came out, it was

**[02:18]** when GPT, you know, 3 came out, it was

**[02:18]** when GPT, you know, 3 came out, it was really about like single LLM features,

**[02:20]** really about like single LLM features,

**[02:20]** really about like single LLM features, right? You're like, oh, like, hey, can

**[02:21]** right? You're like, oh, like, hey, can

**[02:21]** right? You're like, oh, like, hey, can you categorize this like return a

**[02:23]** you categorize this like return a

**[02:23]** you categorize this like return a response in one of these categories? Um,

**[02:26]** response in one of these categories? Um,

**[02:26]** response in one of these categories? Um, and then we've got more like workflow

**[02:28]** and then we've got more like workflow

**[02:28]** and then we've got more like workflow like things, right? Hey, like can you

**[02:30]** like things, right? Hey, like can you

**[02:30]** like things, right? Hey, like can you like take this email and label it or

**[02:33]** like take this email and label it or

**[02:33]** like take this email and label it or like, hey, here's my codebase like index

**[02:36]** like, hey, here's my codebase like index

**[02:36]** like, hey, here's my codebase like index via rag. Can you give me like the next

**[02:38]** via rag. Can you give me like the next

**[02:38]** via rag. Can you give me like the next completion or the next um the next file

**[02:42]** completion or the next um the next file

**[02:42]** completion or the next um the next file to edit, right? And so that's what we'd

**[02:44]** to edit, right? And so that's what we'd

**[02:44]** to edit, right? And so that's what we'd call like a workflow where you're very

**[02:46]** call like a workflow where you're very

**[02:46]** call like a workflow where you're very like structured. You're like, hey, like

**[02:49]** like structured. You're like, hey, like

**[02:49]** like structured. You're like, hey, like given this code, give me code back out,

**[02:51]** given this code, give me code back out,

**[02:51]** given this code, give me code back out, right? And now we're getting to agents,

**[02:54]** right? And now we're getting to agents,

**[02:54]** right? And now we're getting to agents, right? And uh like the canonical agent

**[02:58]** right? And uh like the canonical agent

**[02:58]** right? And uh like the canonical agent to use is cloud code, right? Cloud code


### [03:00 - 04:00]

**[03:01]** to use is cloud code, right? Cloud code

**[03:01]** to use is cloud code, right? Cloud code is a tool where you don't really tell

**[03:04]** is a tool where you don't really tell

**[03:04]** is a tool where you don't really tell it. We don't restrict what it can do

**[03:07]** it. We don't restrict what it can do

**[03:07]** it. We don't restrict what it can do really, right? You're just talking to it

**[03:08]** really, right? You're just talking to it

**[03:08]** really, right? You're just talking to it in text and it will take a really wide

**[03:11]** in text and it will take a really wide

**[03:11]** in text and it will take a really wide variety of actions, right? And so agents

**[03:14]** variety of actions, right? And so agents

**[03:14]** variety of actions, right? And so agents uh build their own context, like decide

**[03:17]** uh build their own context, like decide

**[03:17]** uh build their own context, like decide their own trajectories, are working very

**[03:18]** their own trajectories, are working very

**[03:18]** their own trajectories, are working very very autonomously, right? And so, uh,

**[03:22]** very autonomously, right? And so, uh,

**[03:22]** very autonomously, right? And so, uh, yeah, and I think like as the future

**[03:25]** yeah, and I think like as the future

**[03:25]** yeah, and I think like as the future goes on, like agents will get more and

**[03:27]** goes on, like agents will get more and

**[03:27]** goes on, like agents will get more and more autonomous. Um, and we,

**[03:31]** more autonomous. Um, and we,

**[03:31]** more autonomous. Um, and we, uh, yeah, I think it's like we're kind

**[03:32]** uh, yeah, I think it's like we're kind

**[03:32]** uh, yeah, I think it's like we're kind of at a break point where we can start

**[03:34]** of at a break point where we can start

**[03:34]** of at a break point where we can start to build these agents. Um, they're not

**[03:36]** to build these agents. Um, they're not

**[03:36]** to build these agents. Um, they're not perfect, you know, but it's definitely

**[03:39]** perfect, you know, but it's definitely

**[03:39]** perfect, you know, but it's definitely like the right time to get started. So,

**[03:41]** like the right time to get started. So,

**[03:42]** like the right time to get started. So, um, yeah, Cloud Code, I'm sure many of

**[03:43]** um, yeah, Cloud Code, I'm sure many of

**[03:44]** um, yeah, Cloud Code, I'm sure many of you have have tried or used. Um it is

**[03:47]** you have have tried or used. Um it is

**[03:47]** you have have tried or used. Um it is yeah I think the first true agent right

**[03:50]** yeah I think the first true agent right

**[03:50]** yeah I think the first true agent right like the first uh time where I saw an AI

**[03:53]** like the first uh time where I saw an AI

**[03:53]** like the first uh time where I saw an AI working for like 10 20 30 minutes right

**[03:56]** working for like 10 20 30 minutes right

**[03:56]** working for like 10 20 30 minutes right so um yeah it's a coding agent and uh


### [04:00 - 05:00]

**[04:01]** so um yeah it's a coding agent and uh

**[04:01]** so um yeah it's a coding agent and uh the cloud agent SDK is actually built on

**[04:03]** the cloud agent SDK is actually built on

**[04:03]** the cloud agent SDK is actually built on top of cloud code and uh the reason we

**[04:07]** top of cloud code and uh the reason we

**[04:07]** top of cloud code and uh the reason we did that is because

**[04:09]** did that is because

**[04:09]** did that is because um basically we found that when we were

**[04:13]** um basically we found that when we were

**[04:13]** um basically we found that when we were building agents at anthropic we kept

**[04:15]** building agents at anthropic we kept

**[04:15]** building agents at anthropic we kept rebuilding

**[04:16]** rebuilding

**[04:16]** rebuilding the same parts over and over again. And

**[04:18]** the same parts over and over again. And

**[04:18]** the same parts over and over again. And so to to give you a sense of like what

**[04:20]** so to to give you a sense of like what

**[04:20]** so to to give you a sense of like what that looks like, of course, they're the

**[04:22]** that looks like, of course, they're the

**[04:22]** that looks like, of course, they're the models to start, right? Um, and then in

**[04:26]** models to start, right? Um, and then in

**[04:26]** models to start, right? Um, and then in the harness, you've got tools, right?

**[04:28]** the harness, you've got tools, right?

**[04:28]** the harness, you've got tools, right? And that's like sort of the first

**[04:29]** And that's like sort of the first

**[04:29]** And that's like sort of the first obvious step, like let's add some tools

**[04:31]** obvious step, like let's add some tools

**[04:31]** obvious step, like let's add some tools to this harness. And later on, we'll

**[04:34]** to this harness. And later on, we'll

**[04:34]** to this harness. And later on, we'll give an example of sort of like trying

**[04:37]** give an example of sort of like trying

**[04:37]** give an example of sort of like trying to build your own harness from scratch,

**[04:38]** to build your own harness from scratch,

**[04:38]** to build your own harness from scratch, too, and and what that looks like and

**[04:40]** too, and and what that looks like and

**[04:40]** too, and and what that looks like and and how challenging it can be. But tools

**[04:43]** and how challenging it can be. But tools

**[04:43]** and how challenging it can be. But tools are not just like your own custom tools.

**[04:44]** are not just like your own custom tools.

**[04:44]** are not just like your own custom tools. might be tools to interact with your

**[04:46]** might be tools to interact with your

**[04:46]** might be tools to interact with your file system like with cloud code. Um did

**[04:49]** file system like with cloud code. Um did

**[04:49]** file system like with cloud code. Um did the volume just go up or were they not

**[04:51]** the volume just go up or were they not

**[04:51]** the volume just go up or were they not holding it close enough? [laughter]

**[04:53]** holding it close enough? [laughter]

**[04:53]** holding it close enough? [laughter] Okay. Now anyways um got tools tools you

**[04:58]** Okay. Now anyways um got tools tools you

**[04:58]** Okay. Now anyways um got tools tools you run in a loop and then you have the

**[04:59]** run in a loop and then you have the

**[04:59]** run in a loop and then you have the prompts right like the core agent


### [05:00 - 06:00]

**[05:00]** prompts right like the core agent

**[05:00]** prompts right like the core agent prompts the um the prompts for the

**[05:04]** prompts the um the prompts for the

**[05:04]** prompts the um the prompts for the things like that. Uh and then finally

**[05:08]** things like that. Uh and then finally

**[05:08]** things like that. Uh and then finally you have the file system right and or

**[05:11]** you have the file system right and or

**[05:11]** you have the file system right and or not finally but you have the file

**[05:12]** not finally but you have the file

**[05:12]** not finally but you have the file system. The file system is a way of

**[05:16]** system. The file system is a way of

**[05:16]** system. The file system is a way of context engineering that we'll talk more

**[05:18]** context engineering that we'll talk more

**[05:18]** context engineering that we'll talk more about later, right? And I think like I

**[05:21]** about later, right? And I think like I

**[05:21]** about later, right? And I think like I one of the key insights we had through

**[05:22]** one of the key insights we had through

**[05:22]** one of the key insights we had through cloud code was thinking a lot more

**[05:24]** cloud code was thinking a lot more

**[05:24]** cloud code was thinking a lot more through the like context not just a

**[05:27]** through the like context not just a

**[05:27]** through the like context not just a prompt, it's also the tools, the files

**[05:29]** prompt, it's also the tools, the files

**[05:29]** prompt, it's also the tools, the files and scripts that it can use. Um, and

**[05:32]** and scripts that it can use. Um, and

**[05:32]** and scripts that it can use. Um, and then there are skills which we've like

**[05:33]** then there are skills which we've like

**[05:33]** then there are skills which we've like rolled out recently and uh we can talk

**[05:35]** rolled out recently and uh we can talk

**[05:35]** rolled out recently and uh we can talk more about skills uh um if that's

**[05:37]** more about skills uh um if that's

**[05:37]** more about skills uh um if that's interesting to you guys as well. Um and

**[05:40]** interesting to you guys as well. Um and

**[05:40]** interesting to you guys as well. Um and then yeah things like uh sub aents uh

**[05:43]** then yeah things like uh sub aents uh

**[05:43]** then yeah things like uh sub aents uh web search you know like um like

**[05:46]** web search you know like um like

**[05:46]** web search you know like um like research compacting hooks memory there

**[05:49]** research compacting hooks memory there

**[05:49]** research compacting hooks memory there all these like other things around the

**[05:51]** all these like other things around the

**[05:51]** all these like other things around the harness as well um and uh it ends up

**[05:54]** harness as well um and uh it ends up

**[05:54]** harness as well um and uh it ends up being quite a lot. So the cloud agent

**[05:56]** being quite a lot. So the cloud agent

**[05:56]** being quite a lot. So the cloud agent SDK is all of these things packaged up

**[05:59]** SDK is all of these things packaged up

**[05:59]** SDK is all of these things packaged up for you to use right [clears throat]


### [06:00 - 07:00]

**[06:02]** for you to use right [clears throat]

**[06:02]** for you to use right [clears throat] um and yeah you have your application.

**[06:04]** um and yeah you have your application.

**[06:04]** um and yeah you have your application. So I I think like

**[06:07]** So I I think like

**[06:07]** So I I think like uh to give you a sense of uh yeah to

**[06:11]** uh to give you a sense of uh yeah to

**[06:11]** uh to give you a sense of uh yeah to give you a sense of like

**[06:14]** give you a sense of like

**[06:14]** give you a sense of like maybe why the cloud agent SDK is um

**[06:21]** maybe why the cloud agent SDK is um

**[06:21]** maybe why the cloud agent SDK is um yeah like like so yeah people are

**[06:22]** yeah like like so yeah people are

**[06:22]** yeah like like so yeah people are already building agents on the SDK a lot

**[06:25]** already building agents on the SDK a lot

**[06:25]** already building agents on the SDK a lot of software agents uh you know software

**[06:28]** of software agents uh you know software

**[06:28]** of software agents uh you know software reliability security triaging bug

**[06:31]** reliability security triaging bug

**[06:31]** reliability security triaging bug finding um site and dashboard builders

**[06:34]** finding um site and dashboard builders

**[06:34]** finding um site and dashboard builders if

**[06:34]** if

**[06:34]** if These are extremely popular. If you're

**[06:36]** These are extremely popular. If you're

**[06:36]** These are extremely popular. If you're using it, you should absolutely use the

**[06:37]** using it, you should absolutely use the

**[06:38]** using it, you should absolutely use the SDK. Um, I guess office agents, if

**[06:41]** SDK. Um, I guess office agents, if

**[06:41]** SDK. Um, I guess office agents, if you're doing any sort of office work,

**[06:43]** you're doing any sort of office work,

**[06:43]** you're doing any sort of office work, tons of examples there. Um, got some

**[06:46]** tons of examples there. Um, got some

**[06:46]** tons of examples there. Um, got some like, you know, legal, finance,

**[06:47]** like, you know, legal, finance,

**[06:47]** like, you know, legal, finance, healthcare ones. Um, so yeah, there are

**[06:50]** healthcare ones. Um, so yeah, there are

**[06:50]** healthcare ones. Um, so yeah, there are tons of people building on top of it.

**[06:52]** tons of people building on top of it.

**[06:52]** tons of people building on top of it. Um, I want to Oh, yeah. Okay. So, why

**[06:57]** Um, I want to Oh, yeah. Okay. So, why

**[06:57]** Um, I want to Oh, yeah. Okay. So, why the cloud agent SDK, right? Like why did

**[06:59]** the cloud agent SDK, right? Like why did

**[06:59]** the cloud agent SDK, right? Like why did we do it this way? It's why did we build


### [07:00 - 08:00]

**[07:01]** we do it this way? It's why did we build

**[07:01]** we do it this way? It's why did we build it on top of cloud code? And we realized

**[07:04]** it on top of cloud code? And we realized

**[07:04]** it on top of cloud code? And we realized basically that as soon as we put cloud

**[07:06]** basically that as soon as we put cloud

**[07:06]** basically that as soon as we put cloud code out, yeah, the engineers started

**[07:08]** code out, yeah, the engineers started

**[07:08]** code out, yeah, the engineers started using it, but then the finance people

**[07:10]** using it, but then the finance people

**[07:10]** using it, but then the finance people started using it and the data science

**[07:11]** started using it and the data science

**[07:11]** started using it and the data science people started using it and the

**[07:13]** people started using it and the

**[07:13]** people started using it and the marketing people started using it and

**[07:15]** marketing people started using it and

**[07:15]** marketing people started using it and yeah, I think it just like it we just

**[07:18]** yeah, I think it just like it we just

**[07:18]** yeah, I think it just like it we just realized that people were using cloud

**[07:19]** realized that people were using cloud

**[07:20]** realized that people were using cloud code for non-coding tasks and we felt

**[07:24]** code for non-coding tasks and we felt

**[07:24]** code for non-coding tasks and we felt and and as we were building, you know,

**[07:25]** and and as we were building, you know,

**[07:25]** and and as we were building, you know, non-coding agents, we kept coming back

**[07:27]** non-coding agents, we kept coming back

**[07:27]** non-coding agents, we kept coming back to it, right? And so, um, it's a like,

**[07:32]** to it, right? And so, um, it's a like,

**[07:32]** to it, right? And so, um, it's a like, and we'll go more into why that just

**[07:35]** and we'll go more into why that just

**[07:35]** and we'll go more into why that just works, why we you could use cloud code

**[07:37]** works, why we you could use cloud code

**[07:37]** works, why we you could use cloud code for non-coding task. Uh, spoiler alert,

**[07:39]** for non-coding task. Uh, spoiler alert,

**[07:39]** for non-coding task. Uh, spoiler alert, it's like the bash tool. Um, but yeah,

**[07:43]** it's like the bash tool. Um, but yeah,

**[07:43]** it's like the bash tool. Um, but yeah, it's uh it it was something that we saw

**[07:45]** it's uh it it was something that we saw

**[07:45]** it's uh it it was something that we saw as an emergent pattern that we want to

**[07:47]** as an emergent pattern that we want to

**[07:47]** as an emergent pattern that we want to use and we've built our agents on top of

**[07:49]** use and we've built our agents on top of

**[07:49]** use and we've built our agents on top of it, right? And uh these are lessons that

**[07:52]** it, right? And uh these are lessons that

**[07:52]** it, right? And uh these are lessons that we've learned from deploying cloud code

**[07:54]** we've learned from deploying cloud code

**[07:54]** we've learned from deploying cloud code that we've sort of baked in. So, uh,

**[07:56]** that we've sort of baked in. So, uh,

**[07:56]** that we've sort of baked in. So, uh, tool use errors or compacting or things

**[07:59]** tool use errors or compacting or things

**[07:59]** tool use errors or compacting or things like that, stuff that is like very can


### [08:00 - 09:00]

**[08:01]** like that, stuff that is like very can

**[08:02]** like that, stuff that is like very can take a lot of scale to find, you know,

**[08:04]** take a lot of scale to find, you know,

**[08:04]** take a lot of scale to find, you know, like what are the best practices we've

**[08:05]** like what are the best practices we've

**[08:05]** like what are the best practices we've sort of baked into the cloud agent SDK.

**[08:08]** sort of baked into the cloud agent SDK.

**[08:08]** sort of baked into the cloud agent SDK. Um, as a result, we have a lot of strong

**[08:09]** Um, as a result, we have a lot of strong

**[08:10]** Um, as a result, we have a lot of strong opinions on the best way to build

**[08:11]** opinions on the best way to build

**[08:11]** opinions on the best way to build agents. Uh, like I think the cloud agent

**[08:14]** agents. Uh, like I think the cloud agent

**[08:14]** agents. Uh, like I think the cloud agent SDK is quite opinionated. I'll talk over

**[08:16]** SDK is quite opinionated. I'll talk over

**[08:16]** SDK is quite opinionated. I'll talk over some of these opinions and and why like

**[08:19]** some of these opinions and and why like

**[08:19]** some of these opinions and and why like uh why we chose them, right? Um but

**[08:22]** uh why we chose them, right? Um but

**[08:22]** uh why we chose them, right? Um but yeah, one of the big opinions of the

**[08:23]** yeah, one of the big opinions of the

**[08:23]** yeah, one of the big opinions of the bash tool is the most powerful agent

**[08:25]** bash tool is the most powerful agent

**[08:25]** bash tool is the most powerful agent tool. So okay, um what what are like

**[08:29]** tool. So okay, um what what are like

**[08:29]** tool. So okay, um what what are like what I would describe as the anthropic

**[08:31]** what I would describe as the anthropic

**[08:31]** what I would describe as the anthropic way to build agents, right? And I'm not

**[08:32]** way to build agents, right? And I'm not

**[08:32]** way to build agents, right? And I'm not I'm not saying that you can only build

**[08:34]** I'm not saying that you can only build

**[08:34]** I'm not saying that you can only build agents using the API this way, right?

**[08:36]** agents using the API this way, right?

**[08:36]** agents using the API this way, right? But this is like um if you're using our

**[08:38]** But this is like um if you're using our

**[08:38]** But this is like um if you're using our opinionated stack on the agent SDK, what

**[08:41]** opinionated stack on the agent SDK, what

**[08:41]** opinionated stack on the agent SDK, what is it? Right? So roughly Unix primitives

**[08:44]** is it? Right? So roughly Unix primitives

**[08:44]** is it? Right? So roughly Unix primitives like the bash and file system and you

**[08:47]** like the bash and file system and you

**[08:47]** like the bash and file system and you know we're going to go over like

**[08:49]** know we're going to go over like

**[08:49]** know we're going to go over like prototyping an agent using cloud code

**[08:51]** prototyping an agent using cloud code

**[08:51]** prototyping an agent using cloud code and my goal is really to sort of show

**[08:53]** and my goal is really to sort of show

**[08:53]** and my goal is really to sort of show you what that looks like in real time

**[08:56]** you what that looks like in real time

**[08:56]** you what that looks like in real time right like why is batch useful why is

**[08:58]** right like why is batch useful why is

**[08:58]** right like why is batch useful why is the file system useful why not just use


### [09:00 - 10:00]

**[09:01]** the file system useful why not just use

**[09:01]** the file system useful why not just use tools um yeah agents uh I mean you can

**[09:05]** tools um yeah agents uh I mean you can

**[09:05]** tools um yeah agents uh I mean you can also make workflows and we'll talk about

**[09:06]** also make workflows and we'll talk about

**[09:06]** also make workflows and we'll talk about that a bit later but agents build their

**[09:08]** that a bit later but agents build their

**[09:08]** that a bit later but agents build their own context um thinking about code

**[09:10]** own context um thinking about code

**[09:10]** own context um thinking about code generation for non-coding

**[09:12]** generation for non-coding

**[09:12]** generation for non-coding um like we use codegen to generate docs,

**[09:15]** um like we use codegen to generate docs,

**[09:15]** um like we use codegen to generate docs, query the web, like do data analysis,

**[09:18]** query the web, like do data analysis,

**[09:18]** query the web, like do data analysis, take uh unstructured action. So um

**[09:21]** take uh unstructured action. So um

**[09:22]** take uh unstructured action. So um there's a lot of like uh this can be

**[09:24]** there's a lot of like uh this can be

**[09:24]** there's a lot of like uh this can be pretty counterintuitive to some people

**[09:26]** pretty counterintuitive to some people

**[09:26]** pretty counterintuitive to some people and again in the like prototyping

**[09:28]** and again in the like prototyping

**[09:28]** and again in the like prototyping session, we'll we'll go over how to use

**[09:30]** session, we'll we'll go over how to use

**[09:30]** session, we'll we'll go over how to use code generation for non-coding agents.

**[09:32]** code generation for non-coding agents.

**[09:32]** code generation for non-coding agents. Um and yeah, every agent has a container

**[09:35]** Um and yeah, every agent has a container

**[09:35]** Um and yeah, every agent has a container or is hosted locally because this is

**[09:37]** or is hosted locally because this is

**[09:37]** or is hosted locally because this is cloud code. uh it needs a file system,

**[09:40]** cloud code. uh it needs a file system,

**[09:40]** cloud code. uh it needs a file system, it needs bash, it needs to be able to

**[09:41]** it needs bash, it needs to be able to

**[09:41]** it needs bash, it needs to be able to operate on it. And so it's a very very

**[09:43]** operate on it. And so it's a very very

**[09:43]** operate on it. And so it's a very very different architecture. I'm not planning

**[09:45]** different architecture. I'm not planning

**[09:46]** different architecture. I'm not planning to talk too much about the architecture

**[09:47]** to talk too much about the architecture

**[09:47]** to talk too much about the architecture today, but we can at the end if that's

**[09:49]** today, but we can at the end if that's

**[09:49]** today, but we can at the end if that's what people are interested in in or

**[09:51]** what people are interested in in or

**[09:51]** what people are interested in in or sorry by architecture I mean hosting

**[09:53]** sorry by architecture I mean hosting

**[09:53]** sorry by architecture I mean hosting architecture like how do you host an

**[09:55]** architecture like how do you host an

**[09:55]** architecture like how do you host an agent and like uh what are best

**[09:57]** agent and like uh what are best

**[09:57]** agent and like uh what are best practices there? Have you talked about

**[09:58]** practices there? Have you talked about

**[09:58]** practices there? Have you talked about that at the end? Um [clears throat] yeah


### [10:00 - 11:00]

**[10:01]** that at the end? Um [clears throat] yeah

**[10:01]** that at the end? Um [clears throat] yeah so

**[10:03]** so

**[10:03]** so well let me pause there because I feel

**[10:05]** well let me pause there because I feel

**[10:05]** well let me pause there because I feel like I covered a lot already. any

**[10:07]** like I covered a lot already. any

**[10:07]** like I covered a lot already. any questions so far on the agent SDK agents

**[10:11]** questions so far on the agent SDK agents

**[10:11]** questions so far on the agent SDK agents um yeah like what you get from it

**[10:15]** um yeah like what you get from it

**[10:15]** um yeah like what you get from it >> can you can you explain what code

**[10:16]** >> can you can you explain what code

**[10:16]** >> can you can you explain what code generation for non-coding means exactly

**[10:19]** generation for non-coding means exactly

**[10:19]** generation for non-coding means exactly >> yeah um this is um like basically when

**[10:25]** >> yeah um this is um like basically when

**[10:25]** >> yeah um this is um like basically when you ask cloud code to do a task right

**[10:27]** you ask cloud code to do a task right

**[10:27]** you ask cloud code to do a task right like let's say that you ask it to uh

**[10:30]** like let's say that you ask it to uh

**[10:30]** like let's say that you ask it to uh find the weather in San Francisco and

**[10:33]** find the weather in San Francisco and

**[10:33]** find the weather in San Francisco and like you know tell me what I should wear

**[10:36]** like you know tell me what I should wear

**[10:36]** like you know tell me what I should wear or something right? Like uh what it

**[10:39]** or something right? Like uh what it

**[10:39]** or something right? Like uh what it might do is it might start writing a

**[10:41]** might do is it might start writing a

**[10:41]** might do is it might start writing a script uh to fetch a weather API, right?

**[10:46]** script uh to fetch a weather API, right?

**[10:46]** script uh to fetch a weather API, right? And then start like maybe it wants it to

**[10:49]** And then start like maybe it wants it to

**[10:49]** And then start like maybe it wants it to be reusable. Like maybe you want to do

**[10:50]** be reusable. Like maybe you want to do

**[10:50]** be reusable. Like maybe you want to do this pretty often, right? So it might

**[10:53]** this pretty often, right? So it might

**[10:53]** this pretty often, right? So it might fetch the weather API and then get the

**[10:57]** fetch the weather API and then get the

**[10:57]** fetch the weather API and then get the like maybe even get your location

**[10:58]** like maybe even get your location

**[10:58]** like maybe even get your location dynamically right based on your IP

**[10:59]** dynamically right based on your IP


### [11:00 - 12:00]

**[11:00]** dynamically right based on your IP address and then it will like um you

**[11:04]** address and then it will like um you

**[11:04]** address and then it will like um you know check the weather and then maybe

**[11:06]** know check the weather and then maybe

**[11:06]** know check the weather and then maybe like call out to like a sub agent to

**[11:08]** like call out to like a sub agent to

**[11:08]** like call out to like a sub agent to give you recommendations. Maybe there's

**[11:10]** give you recommendations. Maybe there's

**[11:10]** give you recommendations. Maybe there's an API for your closet or wardrobe,

**[11:13]** an API for your closet or wardrobe,

**[11:13]** an API for your closet or wardrobe, right? It's like so that's an example. I

**[11:16]** right? It's like so that's an example. I

**[11:16]** right? It's like so that's an example. I I think that like it's kind of um for

**[11:19]** I think that like it's kind of um for

**[11:19]** I think that like it's kind of um for any single example we can talk over how

**[11:21]** any single example we can talk over how

**[11:21]** any single example we can talk over how you might use code codegen. Uh a lot of

**[11:23]** you might use code codegen. Uh a lot of

**[11:23]** you might use code codegen. Uh a lot of it is like composing APIs is like the

**[11:25]** it is like composing APIs is like the

**[11:25]** it is like composing APIs is like the high level way to think about it. Yeah.

**[11:28]** high level way to think about it. Yeah.

**[11:28]** high level way to think about it. Yeah. >> Uh yeah. And [clears throat]

**[11:29]** >> Uh yeah. And [clears throat]

**[11:30]** >> Uh yeah. And [clears throat] >> yeah uh workflow versus agent uh like

**[11:32]** >> yeah uh workflow versus agent uh like

**[11:32]** >> yeah uh workflow versus agent uh like for repetitive task or you know like a

**[11:35]** for repetitive task or you know like a

**[11:35]** for repetitive task or you know like a process a business process that is

**[11:36]** process a business process that is

**[11:36]** process a business process that is always the same. Do you will still

**[11:38]** always the same. Do you will still

**[11:38]** always the same. Do you will still prefer to build an agent versus a fully

**[11:41]** prefer to build an agent versus a fully

**[11:41]** prefer to build an agent versus a fully deterministic workflow?

**[11:43]** deterministic workflow?

**[11:43]** deterministic workflow? >> Yeah. So, we do have

**[11:47]** >> Yeah. So, we do have

**[11:47]** >> Yeah. So, we do have >> Oh, sure. Yeah. Yeah. Um, so the

**[11:48]** >> Oh, sure. Yeah. Yeah. Um, so the

**[11:48]** >> Oh, sure. Yeah. Yeah. Um, so the question the question was about

**[11:50]** question the question was about

**[11:50]** question the question was about workflows versus agents and would you

**[11:52]** workflows versus agents and would you

**[11:52]** workflows versus agents and would you still use the cloud agent SDK for

**[11:55]** still use the cloud agent SDK for

**[11:55]** still use the cloud agent SDK for workflows? Is that right? Um, yes. And

**[11:58]** workflows? Is that right? Um, yes. And

**[11:58]** workflows? Is that right? Um, yes. And and so uh I mean we I just we just sort


### [12:00 - 13:00]

**[12:02]** and so uh I mean we I just we just sort

**[12:02]** and so uh I mean we I just we just sort of tell you what we do internally

**[12:04]** of tell you what we do internally

**[12:04]** of tell you what we do internally basically and what we do internally is

**[12:06]** basically and what we do internally is

**[12:06]** basically and what we do internally is we've done a lot of like GitHub

**[12:07]** we've done a lot of like GitHub

**[12:07]** we've done a lot of like GitHub automations and Slack automations built

**[12:09]** automations and Slack automations built

**[12:10]** automations and Slack automations built on the cloud agent SDK. So, uh, you

**[12:12]** on the cloud agent SDK. So, uh, you

**[12:12]** on the cloud agent SDK. So, uh, you know, we have a bot that triages issues

**[12:13]** know, we have a bot that triages issues

**[12:13]** know, we have a bot that triages issues when it comes in. That's a pretty

**[12:15]** when it comes in. That's a pretty

**[12:15]** when it comes in. That's a pretty workflow like thing, but we've still

**[12:17]** workflow like thing, but we've still

**[12:17]** workflow like thing, but we've still found that, you know, in order to triage

**[12:19]** found that, you know, in order to triage

**[12:19]** found that, you know, in order to triage issues, we want it to be able to clone

**[12:21]** issues, we want it to be able to clone

**[12:21]** issues, we want it to be able to clone the codebase and sometimes spin up a

**[12:22]** the codebase and sometimes spin up a

**[12:22]** the codebase and sometimes spin up a Docker container and test it and things

**[12:24]** Docker container and test it and things

**[12:24]** Docker container and test it and things like that. And so, it's still ends up

**[12:26]** like that. And so, it's still ends up

**[12:26]** like that. And so, it's still ends up being like a very like there's a lot of

**[12:29]** being like a very like there's a lot of

**[12:29]** being like a very like there's a lot of steps in the middle that need to be

**[12:31]** steps in the middle that need to be

**[12:31]** steps in the middle that need to be quite free flowing. Um, and then you

**[12:33]** quite free flowing. Um, and then you

**[12:33]** quite free flowing. Um, and then you like give structured output at the end.

**[12:35]** like give structured output at the end.

**[12:35]** like give structured output at the end. So, um, yes. All right, we'll take one

**[12:38]** So, um, yes. All right, we'll take one

**[12:38]** So, um, yes. All right, we'll take one more question and then we'll keep going.

**[12:39]** more question and then we'll keep going.

**[12:40]** more question and then we'll keep going. So, yeah, in the blue. Yeah. Uh so could

**[12:41]** So, yeah, in the blue. Yeah. Uh so could

**[12:41]** So, yeah, in the blue. Yeah. Uh so could you talk about security and guardians

**[12:43]** you talk about security and guardians

**[12:43]** you talk about security and guardians like if if you know you're using cloud

**[12:45]** like if if you know you're using cloud

**[12:45]** like if if you know you're using cloud agent SDK and you know you lean towards

**[12:47]** agent SDK and you know you lean towards

**[12:47]** agent SDK and you know you lean towards using bash as the you know all powerful

**[12:50]** using bash as the you know all powerful

**[12:50]** using bash as the you know all powerful generic tool and is the onus on uh

**[12:54]** generic tool and is the onus on uh

**[12:54]** generic tool and is the onus on uh building the agent builder to make sure

**[12:56]** building the agent builder to make sure

**[12:56]** building the agent builder to make sure that you know you're preventing against

**[12:58]** that you know you're preventing against

**[12:58]** that you know you're preventing against like common attack vectors or is that


### [13:00 - 14:00]

**[13:00]** like common attack vectors or is that

**[13:00]** like common attack vectors or is that something that the model is is is doing

**[13:02]** something that the model is is is doing

**[13:02]** something that the model is is is doing itself?

**[13:03]** itself?

**[13:03]** itself? >> Yeah. So I I think this is sort of like

**[13:05]** >> Yeah. So I I think this is sort of like

**[13:05]** >> Yeah. So I I think this is sort of like the Swiss chief. Oh yeah. Okay. So the

**[13:07]** the Swiss chief. Oh yeah. Okay. So the

**[13:07]** the Swiss chief. Oh yeah. Okay. So the question was uh permissions on the bash

**[13:10]** question was uh permissions on the bash

**[13:10]** question was uh permissions on the bash tool, right? Or like how do you think

**[13:12]** tool, right? Or like how do you think

**[13:12]** tool, right? Or like how do you think about permissions and guardrails the

**[13:14]** about permissions and guardrails the

**[13:14]** about permissions and guardrails the like in like when you're giving the

**[13:16]** like in like when you're giving the

**[13:16]** like in like when you're giving the agent this much power over you know your

**[13:19]** agent this much power over you know your

**[13:19]** agent this much power over you know your its environment and the computer, how do

**[13:20]** its environment and the computer, how do

**[13:20]** its environment and the computer, how do you make sure it's aligned, right? And

**[13:22]** you make sure it's aligned, right? And

**[13:22]** you make sure it's aligned, right? And so the way we think about this is uh

**[13:24]** so the way we think about this is uh

**[13:24]** so the way we think about this is uh what we call like the Swiss cheese

**[13:25]** what we call like the Swiss cheese

**[13:25]** what we call like the Swiss cheese defense, right? So like there is um like

**[13:29]** defense, right? So like there is um like

**[13:29]** defense, right? So like there is um like on every layer some defenses and

**[13:31]** on every layer some defenses and

**[13:31]** on every layer some defenses and together we hope that it like blocks

**[13:34]** together we hope that it like blocks

**[13:34]** together we hope that it like blocks everything, right? So obviously on the

**[13:35]** everything, right? So obviously on the

**[13:35]** everything, right? So obviously on the model layer uh we do a lot of um

**[13:39]** model layer uh we do a lot of um

**[13:39]** model layer uh we do a lot of um alignment there. We actually just put

**[13:41]** alignment there. We actually just put

**[13:41]** alignment there. We actually just put out a really good paper on reward

**[13:42]** out a really good paper on reward

**[13:42]** out a really good paper on reward hacking. Super recommend you check that

**[13:45]** hacking. Super recommend you check that

**[13:45]** hacking. Super recommend you check that out. Um so like definitely I think cloud

**[13:48]** out. Um so like definitely I think cloud

**[13:48]** out. Um so like definitely I think cloud models like we try and make them very

**[13:50]** models like we try and make them very

**[13:50]** models like we try and make them very very aligned, right? And uh so yeah

**[13:53]** very aligned, right? And uh so yeah

**[13:53]** very aligned, right? And uh so yeah there's the model alignment behavior

**[13:55]** there's the model alignment behavior

**[13:55]** there's the model alignment behavior then there is like the harness itself,

**[13:57]** then there is like the harness itself,

**[13:57]** then there is like the harness itself, right? And so we have a lot of like

**[13:59]** right? And so we have a lot of like

**[13:59]** right? And so we have a lot of like permissioning and prompting um and uh


### [14:00 - 15:00]

**[14:03]** permissioning and prompting um and uh

**[14:03]** permissioning and prompting um and uh like we do a pass par parser on the bash

**[14:06]** like we do a pass par parser on the bash

**[14:06]** like we do a pass par parser on the bash tool for example so we know um fairly

**[14:09]** tool for example so we know um fairly

**[14:09]** tool for example so we know um fairly reliably like what the bash tool is

**[14:11]** reliably like what the bash tool is

**[14:11]** reliably like what the bash tool is actually doing and definitely not

**[14:13]** actually doing and definitely not

**[14:13]** actually doing and definitely not something you want to build yourself. Um

**[14:15]** something you want to build yourself. Um

**[14:15]** something you want to build yourself. Um and then finally

**[14:17]** and then finally

**[14:17]** and then finally the last layer is sandboxing right so

**[14:19]** the last layer is sandboxing right so

**[14:19]** the last layer is sandboxing right so like let's say that an someone has

**[14:21]** like let's say that an someone has

**[14:21]** like let's say that an someone has maliciously taken over your agent what

**[14:23]** maliciously taken over your agent what

**[14:23]** maliciously taken over your agent what can it actually do uh we've included a

**[14:27]** can it actually do uh we've included a

**[14:27]** can it actually do uh we've included a sandbox and like where you can sandbox

**[14:29]** sandbox and like where you can sandbox

**[14:29]** sandbox and like where you can sandbox network request um and sandbox uh file

**[14:32]** network request um and sandbox uh file

**[14:32]** network request um and sandbox uh file system operations outside of the file

**[14:34]** system operations outside of the file

**[14:34]** system operations outside of the file system. And so, uh, yeah, ultimately

**[14:37]** system. And so, uh, yeah, ultimately

**[14:37]** system. And so, uh, yeah, ultimately that's what they call like the lethal

**[14:39]** that's what they call like the lethal

**[14:39]** that's what they call like the lethal triacto, right? Is like, um, like the

**[14:42]** triacto, right? Is like, um, like the

**[14:42]** triacto, right? Is like, um, like the ability to like execute code in an

**[14:44]** ability to like execute code in an

**[14:44]** ability to like execute code in an environment, change a file system, um,

**[14:46]** environment, change a file system, um,

**[14:46]** environment, change a file system, um, excfiltrate the code, right? I think I'm

**[14:48]** excfiltrate the code, right? I think I'm

**[14:48]** excfiltrate the code, right? I think I'm getting the lethal trifecta a little bit

**[14:49]** getting the lethal trifecta a little bit

**[14:50]** getting the lethal trifecta a little bit wrong there, but like the idea is

**[14:51]** wrong there, but like the idea is

**[14:51]** wrong there, but like the idea is basically like if they can excfiltrate

**[14:53]** basically like if they can excfiltrate

**[14:53]** basically like if they can excfiltrate your like information back out, right?

**[14:55]** your like information back out, right?

**[14:56]** your like information back out, right? Um, that's like they still need to be

**[14:58]** Um, that's like they still need to be

**[14:58]** Um, that's like they still need to be able to extract information. And so if


### [15:00 - 16:00]

**[15:00]** able to extract information. And so if

**[15:00]** able to extract information. And so if you sandbox the network, that's a good

**[15:01]** you sandbox the network, that's a good

**[15:01]** you sandbox the network, that's a good way of doing it. Um if you're hosting on

**[15:04]** way of doing it. Um if you're hosting on

**[15:04]** way of doing it. Um if you're hosting on a sandbox container like Cloudflare uh

**[15:07]** a sandbox container like Cloudflare uh

**[15:07]** a sandbox container like Cloudflare uh modal or you know E2B Daytona like all

**[15:09]** modal or you know E2B Daytona like all

**[15:09]** modal or you know E2B Daytona like all of these like sound sandbox providers

**[15:12]** of these like sound sandbox providers

**[15:12]** of these like sound sandbox providers they've also done like some level level

**[15:13]** they've also done like some level level

**[15:13]** they've also done like some level level of security there right it's like you're

**[15:15]** of security there right it's like you're

**[15:15]** of security there right it's like you're not hosting it on your personal computer

**[15:17]** not hosting it on your personal computer

**[15:17]** not hosting it on your personal computer um or on a computer with like your prod

**[15:19]** um or on a computer with like your prod

**[15:19]** um or on a computer with like your prod secrets or something so uh yeah lots of

**[15:21]** secrets or something so uh yeah lots of

**[15:21]** secrets or something so uh yeah lots of different layers there and and yeah we

**[15:23]** different layers there and and yeah we

**[15:23]** different layers there and and yeah we can talk more about hosting in depth um

**[15:25]** can talk more about hosting in depth um

**[15:25]** can talk more about hosting in depth um so okay so I'm going to uh talk a little

**[15:29]** so okay so I'm going to uh talk a little

**[15:29]** so okay so I'm going to uh talk a little bit about bash is all you need you

**[15:32]** bit about bash is all you need you

**[15:32]** bit about bash is all you need you Um, I think this is something that Oh,

**[15:35]** Um, I think this is something that Oh,

**[15:35]** Um, I think this is something that Oh, yeah. Um, this is like my stickick, you

**[15:38]** yeah. Um, this is like my stickick, you

**[15:38]** yeah. Um, this is like my stickick, you know? I'm just going to like keep

**[15:40]** know? I'm just going to like keep

**[15:40]** know? I'm just going to like keep talking about this until everyone like

**[15:42]** talking about this until everyone like

**[15:42]** talking about this until everyone like uh agrees with me. Um, or like I think

**[15:45]** uh agrees with me. Um, or like I think

**[15:45]** uh agrees with me. Um, or like I think this is something that we found

**[15:46]** this is something that we found

**[15:46]** this is something that we found atanthropic. I think it is sort of

**[15:48]** atanthropic. I think it is sort of

**[15:48]** atanthropic. I think it is sort of something I discovered once I got here.

**[15:51]** something I discovered once I got here.

**[15:51]** something I discovered once I got here. Um, bash is what makes code so good,

**[15:53]** Um, bash is what makes code so good,

**[15:53]** Um, bash is what makes code so good, right? So, I think like you guys have

**[15:55]** right? So, I think like you guys have

**[15:55]** right? So, I think like you guys have probably seen like code mode or

**[15:59]** probably seen like code mode or

**[15:59]** probably seen like code mode or programmatic tool use, right? like the


### [16:00 - 17:00]

**[16:01]** programmatic tool use, right? like the

**[16:01]** programmatic tool use, right? like the uh different ways of like composing MLPS

**[16:04]** uh different ways of like composing MLPS

**[16:04]** uh different ways of like composing MLPS uh cloudfl put out some blog post on

**[16:06]** uh cloudfl put out some blog post on

**[16:06]** uh cloudfl put out some blog post on that we put out some blog posts uh the

**[16:08]** that we put out some blog posts uh the

**[16:08]** that we put out some blog posts uh the way I think about code mode is like or

**[16:11]** way I think about code mode is like or

**[16:11]** way I think about code mode is like or bash is that it was like the first code

**[16:13]** bash is that it was like the first code

**[16:13]** bash is that it was like the first code mode right so the bash tool allows you

**[16:16]** mode right so the bash tool allows you

**[16:16]** mode right so the bash tool allows you to you know like store the results of

**[16:17]** to you know like store the results of

**[16:17]** to you know like store the results of your tool calls to files uh store memory

**[16:20]** your tool calls to files uh store memory

**[16:20]** your tool calls to files uh store memory dynamically generate scripts and call

**[16:22]** dynamically generate scripts and call

**[16:22]** dynamically generate scripts and call them compose functionality like tail

**[16:24]** them compose functionality like tail

**[16:24]** them compose functionality like tail graph uh it lets you use existing

**[16:27]** graph uh it lets you use existing

**[16:27]** graph uh it lets you use existing software like fmp or libra office right

**[16:29]** software like fmp or libra office right

**[16:29]** software like fmp or libra office right so there's a lot of like interesting

**[16:31]** so there's a lot of like interesting

**[16:31]** so there's a lot of like interesting things and powerful things that the

**[16:33]** things and powerful things that the

**[16:33]** things and powerful things that the batch tool can do. And like think about

**[16:36]** batch tool can do. And like think about

**[16:36]** batch tool can do. And like think about like again what made cloud code so good.

**[16:38]** like again what made cloud code so good.

**[16:38]** like again what made cloud code so good. If you were designing an agent harness,

**[16:40]** If you were designing an agent harness,

**[16:40]** If you were designing an agent harness, maybe what you would do is you'd have a

**[16:42]** maybe what you would do is you'd have a

**[16:42]** maybe what you would do is you'd have a search tool and a lint tool and an

**[16:44]** search tool and a lint tool and an

**[16:44]** search tool and a lint tool and an execute tool, right? And like you have

**[16:47]** execute tool, right? And like you have

**[16:47]** execute tool, right? And like you have end tools, right? Like every time you

**[16:48]** end tools, right? Like every time you

**[16:48]** end tools, right? Like every time you thought of like a new use case, you're

**[16:49]** thought of like a new use case, you're

**[16:49]** thought of like a new use case, you're like, I need to have another tool now,

**[16:51]** like, I need to have another tool now,

**[16:51]** like, I need to have another tool now, right? Um instead now cloud just uses

**[16:55]** right? Um instead now cloud just uses

**[16:55]** right? Um instead now cloud just uses grap, right? And nodes your package

**[16:57]** grap, right? And nodes your package

**[16:57]** grap, right? And nodes your package manager. So it runs like npm run like


### [17:00 - 18:00]

**[17:00]** manager. So it runs like npm run like

**[17:00]** manager. So it runs like npm run like test.ts or index.ts s or whatever,

**[17:03]** test.ts or index.ts s or whatever,

**[17:03]** test.ts or index.ts s or whatever, right? Like it can lint, right? And it

**[17:05]** right? Like it can lint, right? And it

**[17:05]** right? Like it can lint, right? And it can find out how you lint, right? And

**[17:07]** can find out how you lint, right? And

**[17:07]** can find out how you lint, right? And can run npm run lint if if you don't

**[17:08]** can run npm run lint if if you don't

**[17:08]** can run npm run lint if if you don't have a llinter. It can be like what if I

**[17:10]** have a llinter. It can be like what if I

**[17:10]** have a llinter. It can be like what if I install eslint for you, right? So, um

**[17:13]** install eslint for you, right? So, um

**[17:14]** install eslint for you, right? So, um this is like you know like I said the

**[17:15]** this is like you know like I said the

**[17:15]** this is like you know like I said the first programmatic tool calling first

**[17:18]** first programmatic tool calling first

**[17:18]** first programmatic tool calling first code mode, right? Like you can do a lot

**[17:21]** code mode, right? Like you can do a lot

**[17:21]** code mode, right? Like you can do a lot of different actions very very

**[17:23]** of different actions very very

**[17:23]** of different actions very very generically, right? Um and so to talk

**[17:27]** generically, right? Um and so to talk

**[17:27]** generically, right? Um and so to talk about this a little bit in the context

**[17:29]** about this a little bit in the context

**[17:29]** about this a little bit in the context of non-coding agents, right? So let's

**[17:31]** of non-coding agents, right? So let's

**[17:32]** of non-coding agents, right? So let's say that we have an email agent and the

**[17:35]** say that we have an email agent and the

**[17:35]** say that we have an email agent and the user is like okay how much did I spend

**[17:38]** user is like okay how much did I spend

**[17:38]** user is like okay how much did I spend on ride sharing this week um a you know

**[17:42]** on ride sharing this week um a you know

**[17:42]** on ride sharing this week um a you know like it's got one tool call or generally

**[17:44]** like it's got one tool call or generally

**[17:44]** like it's got one tool call or generally it's got the ability to search your

**[17:45]** it's got the ability to search your

**[17:45]** it's got the ability to search your inbox right and so it can run a query

**[17:48]** inbox right and so it can run a query

**[17:48]** inbox right and so it can run a query like hey search Uber oryft right and

**[17:54]** like hey search Uber oryft right and

**[17:54]** like hey search Uber oryft right and without bash it it searches Uber oryft

**[17:57]** without bash it it searches Uber oryft

**[17:57]** without bash it it searches Uber oryft it gets like a hundred emails or

**[17:59]** it gets like a hundred emails or

**[17:59]** it gets like a hundred emails or something and now it's just got to


### [18:00 - 19:00]

**[18:01]** something and now it's just got to

**[18:01]** something and now it's just got to think about it. You know what I mean?

**[18:03]** think about it. You know what I mean?

**[18:03]** think about it. You know what I mean? And I I think like a good like analogy

**[18:06]** And I I think like a good like analogy

**[18:06]** And I I think like a good like analogy is sort of like imagine if someone came

**[18:07]** is sort of like imagine if someone came

**[18:07]** is sort of like imagine if someone came to you with like like a stack of papers

**[18:10]** to you with like like a stack of papers

**[18:10]** to you with like like a stack of papers and like hey, how much did I spend on

**[18:11]** and like hey, how much did I spend on

**[18:11]** and like hey, how much did I spend on ride sharing this week? Can you like

**[18:13]** ride sharing this week? Can you like

**[18:13]** ride sharing this week? Can you like read through my emails? You know, I mean

**[18:14]** read through my emails? You know, I mean

**[18:14]** read through my emails? You know, I mean like that that would be really hard,

**[18:16]** like that that would be really hard,

**[18:16]** like that that would be really hard, right? Like uh you need very very good

**[18:18]** right? Like uh you need very very good

**[18:18]** right? Like uh you need very very good precision and recall to do it. Um or

**[18:21]** precision and recall to do it. Um or

**[18:21]** precision and recall to do it. Um or with bash, right? Like let's say there's

**[18:24]** with bash, right? Like let's say there's

**[18:24]** with bash, right? Like let's say there's a Gmail search script, right? It takes

**[18:26]** a Gmail search script, right? It takes

**[18:26]** a Gmail search script, right? It takes in a query function. Um, and then you

**[18:29]** in a query function. Um, and then you

**[18:29]** in a query function. Um, and then you can start to save that query function to

**[18:32]** can start to save that query function to

**[18:32]** can start to save that query function to a file or pipe it. You can GP for

**[18:35]** a file or pipe it. You can GP for

**[18:35]** a file or pipe it. You can GP for prices. You know, you can uh then add

**[18:37]** prices. You know, you can uh then add

**[18:37]** prices. You know, you can uh then add them together. You can check your work

**[18:39]** them together. You can check your work

**[18:40]** them together. You can check your work too, right? Like you can say, okay, let

**[18:41]** too, right? Like you can say, okay, let

**[18:41]** too, right? Like you can say, okay, let me grab all my prices, store those as

**[18:44]** me grab all my prices, store those as

**[18:44]** me grab all my prices, store those as like in a file with line numbers and

**[18:46]** like in a file with line numbers and

**[18:46]** like in a file with line numbers and then let me then be able to check

**[18:48]** then let me then be able to check

**[18:48]** then let me then be able to check afterwards like uh was this actually a

**[18:51]** afterwards like uh was this actually a

**[18:51]** afterwards like uh was this actually a price? Like what does each one correlate

**[18:53]** price? Like what does each one correlate

**[18:53]** price? Like what does each one correlate to? Right? So there's a lot more like

**[18:55]** to? Right? So there's a lot more like

**[18:55]** to? Right? So there's a lot more like dynamic information you can do to check

**[18:57]** dynamic information you can do to check

**[18:57]** dynamic information you can do to check your work with the bash tool. So this is


### [19:00 - 20:00]

**[19:00]** your work with the bash tool. So this is

**[19:00]** your work with the bash tool. So this is like

**[19:01]** like

**[19:02]** like um just a simple example but like

**[19:05]** um just a simple example but like

**[19:05]** um just a simple example but like hopefully showing you sort of the power

**[19:06]** hopefully showing you sort of the power

**[19:06]** hopefully showing you sort of the power of like the composability of bash right

**[19:08]** of like the composability of bash right

**[19:08]** of like the composability of bash right so I'll pause there any questions on

**[19:11]** so I'll pause there any questions on

**[19:11]** so I'll pause there any questions on bash is all you need the bash tool any

**[19:13]** bash is all you need the bash tool any

**[19:13]** bash is all you need the bash tool any any thing I can make a little bit

**[19:15]** any thing I can make a little bit

**[19:15]** any thing I can make a little bit clearer

**[19:16]** clearer

**[19:16]** clearer >> do you have stats on how many people use

**[19:17]** >> do you have stats on how many people use

**[19:17]** >> do you have stats on how many people use yolo mode

**[19:21]** yolo mode

**[19:21]** yolo mode >> uh stats on yolo mode we probably do

**[19:25]** >> uh stats on yolo mode we probably do

**[19:25]** >> uh stats on yolo mode we probably do um I mean internally we we don't uh but

**[19:27]** um I mean internally we we don't uh but

**[19:27]** um I mean internally we we don't uh but that's just I think we just have a

**[19:28]** that's just I think we just have a

**[19:28]** that's just I think we just have a higher security posture. Um,

**[19:31]** higher security posture. Um,

**[19:31]** higher security posture. Um, [clears throat]

**[19:32]** [clears throat]

**[19:32]** [clears throat] yeah, I'm not sure. Uh, I can probably

**[19:34]** yeah, I'm not sure. Uh, I can probably

**[19:34]** yeah, I'm not sure. Uh, I can probably pull that. Any other questions on bash?

**[19:38]** pull that. Any other questions on bash?

**[19:38]** pull that. Any other questions on bash? Okay, cool. Um, yeah, just to give you

**[19:42]** Okay, cool. Um, yeah, just to give you

**[19:42]** Okay, cool. Um, yeah, just to give you like some more examples like let's say

**[19:44]** like some more examples like let's say

**[19:44]** like some more examples like let's say that you had an email API and you wanted

**[19:47]** that you had an email API and you wanted

**[19:47]** that you had an email API and you wanted to uh, you know, like go through like

**[19:51]** to uh, you know, like go through like

**[19:51]** to uh, you know, like go through like fetch my like tell me who emailed me

**[19:53]** fetch my like tell me who emailed me

**[19:53]** fetch my like tell me who emailed me this week, right? So, you've got two

**[19:54]** this week, right? So, you've got two

**[19:54]** this week, right? So, you've got two APIs. You've got an inbox API and a

**[19:56]** APIs. You've got an inbox API and a

**[19:56]** APIs. You've got an inbox API and a contact API. Um this is like a way you

**[19:59]** contact API. Um this is like a way you

**[19:59]** contact API. Um this is like a way you can do it via bash. You can also do it


### [20:00 - 21:00]

**[20:00]** can do it via bash. You can also do it

**[20:00]** can do it via bash. You can also do it via codegen. This is kind of like enough

**[20:02]** via codegen. This is kind of like enough

**[20:02]** via codegen. This is kind of like enough bash that it is codegen, right? Like um

**[20:05]** bash that it is codegen, right? Like um

**[20:05]** bash that it is codegen, right? Like um bash is a ostensibly codegen tool. Um

**[20:09]** bash is a ostensibly codegen tool. Um

**[20:09]** bash is a ostensibly codegen tool. Um and then yeah like let's say that you

**[20:11]** and then yeah like let's say that you

**[20:11]** and then yeah like let's say that you wanted to you had a video meeting agent,

**[20:14]** wanted to you had a video meeting agent,

**[20:14]** wanted to you had a video meeting agent, right? You wanted to say like find all

**[20:15]** right? You wanted to say like find all

**[20:15]** right? You wanted to say like find all the moments where the speaker says

**[20:17]** the moments where the speaker says

**[20:17]** the moments where the speaker says quarterly results in this earnings call,

**[20:19]** quarterly results in this earnings call,

**[20:19]** quarterly results in this earnings call, right? You can use ffmpeg to like slice

**[20:21]** right? You can use ffmpeg to like slice

**[20:21]** right? You can use ffmpeg to like slice up this video, right? um you can use jq

**[20:25]** up this video, right? um you can use jq

**[20:25]** up this video, right? um you can use jq to like uh start analyzing the

**[20:27]** to like uh start analyzing the

**[20:27]** to like uh start analyzing the information afterward. So um yeah, lots

**[20:29]** information afterward. So um yeah, lots

**[20:29]** information afterward. So um yeah, lots of like def like powerful ways to use uh

**[20:33]** of like def like powerful ways to use uh

**[20:33]** of like def like powerful ways to use uh to use bash. So

**[20:36]** to use bash. So

**[20:36]** to use bash. So I'm going to talk a little bit about

**[20:37]** I'm going to talk a little bit about

**[20:37]** I'm going to talk a little bit about workflows and agents. Yeah, you can do

**[20:39]** workflows and agents. Yeah, you can do

**[20:39]** workflows and agents. Yeah, you can do both. You could use uh build workflows

**[20:41]** both. You could use uh build workflows

**[20:41]** both. You could use uh build workflows and agents on the agent SDK. Um yeah,

**[20:44]** and agents on the agent SDK. Um yeah,

**[20:44]** and agents on the agent SDK. Um yeah, agents are like cloud code. If if you

**[20:46]** agents are like cloud code. If if you

**[20:46]** agents are like cloud code. If if you are like building something where you

**[20:48]** are like building something where you

**[20:48]** are like building something where you want to talk to it in natural language

**[20:50]** want to talk to it in natural language

**[20:50]** want to talk to it in natural language and take action flexibly, right? Then

**[20:53]** and take action flexibly, right? Then

**[20:53]** and take action flexibly, right? Then that's why you're building an agent,

**[20:55]** that's why you're building an agent,

**[20:55]** that's why you're building an agent, right? Like you want you have an agent

**[20:57]** right? Like you want you have an agent

**[20:57]** right? Like you want you have an agent that talks to your like business data

**[20:58]** that talks to your like business data

**[20:58]** that talks to your like business data and you want to get insights or


### [21:00 - 22:00]

**[21:00]** and you want to get insights or

**[21:00]** and you want to get insights or dashboards or answer questions or uh

**[21:03]** dashboards or answer questions or uh

**[21:03]** dashboards or answer questions or uh write code or something like that's an

**[21:04]** write code or something like that's an

**[21:04]** write code or something like that's an agent, right? And then a workflow is

**[21:07]** agent, right? And then a workflow is

**[21:07]** agent, right? And then a workflow is kind of like, you know, we do a lot of

**[21:08]** kind of like, you know, we do a lot of

**[21:08]** kind of like, you know, we do a lot of GitHub actions for example, right? So

**[21:10]** GitHub actions for example, right? So

**[21:10]** GitHub actions for example, right? So you define the inputs and outputs very

**[21:12]** you define the inputs and outputs very

**[21:12]** you define the inputs and outputs very closely, right? So you're like, "Okay,

**[21:13]** closely, right? So you're like, "Okay,

**[21:13]** closely, right? So you're like, "Okay, take it a PR and give me a code review."

**[21:16]** take it a PR and give me a code review."

**[21:16]** take it a PR and give me a code review." Um, and yeah, both of these you can use

**[21:18]** Um, and yeah, both of these you can use

**[21:18]** Um, and yeah, both of these you can use agent SDK for. Um, when building

**[21:21]** agent SDK for. Um, when building

**[21:21]** agent SDK for. Um, when building workflows, you can use structured

**[21:22]** workflows, you can use structured

**[21:22]** workflows, you can use structured outputs. We just released this. Um, you

**[21:25]** outputs. We just released this. Um, you

**[21:25]** outputs. We just released this. Um, you can, yeah, Google agent SDK structured

**[21:27]** can, yeah, Google agent SDK structured

**[21:27]** can, yeah, Google agent SDK structured outputs. Um, but yeah, so you can do

**[21:31]** outputs. Um, but yeah, so you can do

**[21:31]** outputs. Um, but yeah, so you can do both. I'm going to primarily be talking

**[21:33]** both. I'm going to primarily be talking

**[21:33]** both. I'm going to primarily be talking about agents right now. A lot of the

**[21:35]** about agents right now. A lot of the

**[21:35]** about agents right now. A lot of the things that you can like learn from this

**[21:38]** things that you can like learn from this

**[21:38]** things that you can like learn from this are applicable to workflows as well. So,

**[21:42]** are applicable to workflows as well. So,

**[21:42]** are applicable to workflows as well. So, um, yeah, we'll we'll talk about this.

**[21:45]** um, yeah, we'll we'll talk about this.

**[21:45]** um, yeah, we'll we'll talk about this. Uh, wait, show of hands. How many people

**[21:47]** Uh, wait, show of hands. How many people

**[21:47]** Uh, wait, show of hands. How many people have like designed an agent loop before?

**[21:50]** have like designed an agent loop before?

**[21:50]** have like designed an agent loop before? Okay, cool. Okay, great. Great. Um, so

**[21:54]** Okay, cool. Okay, great. Great. Um, so

**[21:54]** Okay, cool. Okay, great. Great. Um, so yeah, I mean, I think the number one

**[21:56]** yeah, I mean, I think the number one

**[21:56]** yeah, I mean, I think the number one thing the the metalarning for designing

**[21:59]** thing the the metalarning for designing

**[21:59]** thing the the metalarning for designing an agent loop to me is just to read the


### [22:00 - 23:00]

**[22:01]** an agent loop to me is just to read the

**[22:01]** an agent loop to me is just to read the transcripts over and over again. Like

**[22:03]** transcripts over and over again. Like

**[22:03]** transcripts over and over again. Like every time you see see the agent

**[22:05]** every time you see see the agent

**[22:05]** every time you see see the agent running, just read it and figure out

**[22:06]** running, just read it and figure out

**[22:06]** running, just read it and figure out like, hey, what is it doing? Why is it

**[22:08]** like, hey, what is it doing? Why is it

**[22:08]** like, hey, what is it doing? Why is it doing this? can I uh help it out

**[22:10]** doing this? can I uh help it out

**[22:10]** doing this? can I uh help it out somehow? Right? Um and uh we'll do some

**[22:15]** somehow? Right? Um and uh we'll do some

**[22:15]** somehow? Right? Um and uh we'll do some of that later, right? So we'll uh we'll

**[22:17]** of that later, right? So we'll uh we'll

**[22:17]** of that later, right? So we'll uh we'll build an agent loop. Um but here is the

**[22:22]** build an agent loop. Um but here is the

**[22:22]** build an agent loop. Um but here is the uh the three parts to an agent loop,

**[22:25]** uh the three parts to an agent loop,

**[22:25]** uh the three parts to an agent loop, right? So uh first it's gather context,

**[22:28]** right? So uh first it's gather context,

**[22:28]** right? So uh first it's gather context, right? Second is taking action and the

**[22:32]** right? Second is taking action and the

**[22:32]** right? Second is taking action and the third is verifying the work, right? And

**[22:36]** third is verifying the work, right? And

**[22:36]** third is verifying the work, right? And uh this is like not the only way to

**[22:39]** uh this is like not the only way to

**[22:39]** uh this is like not the only way to build an agent, but I think a pretty

**[22:41]** build an agent, but I think a pretty

**[22:41]** build an agent, but I think a pretty good way to think about it. Um gathering

**[22:43]** good way to think about it. Um gathering

**[22:43]** good way to think about it. Um gathering context is uh like you know for cloud

**[22:46]** context is uh like you know for cloud

**[22:46]** context is uh like you know for cloud code it's grepping and finding the files

**[22:49]** code it's grepping and finding the files

**[22:49]** code it's grepping and finding the files needed, right? Um you know for an email

**[22:52]** needed, right? Um you know for an email

**[22:52]** needed, right? Um you know for an email agent it's like finding the relevant

**[22:53]** agent it's like finding the relevant

**[22:53]** agent it's like finding the relevant emails, right? Um, and so these are all

**[22:57]** emails, right? Um, and so these are all

**[22:57]** emails, right? Um, and so these are all like pretty um, yeah, like I I think


### [23:00 - 24:00]

**[23:00]** like pretty um, yeah, like I I think

**[23:00]** like pretty um, yeah, like I I think thinking about how it finds this context

**[23:02]** thinking about how it finds this context

**[23:02]** thinking about how it finds this context is very important and I think a lot of

**[23:04]** is very important and I think a lot of

**[23:04]** is very important and I think a lot of people sort of uh, skip the step or like

**[23:08]** people sort of uh, skip the step or like

**[23:08]** people sort of uh, skip the step or like underthink it. This can be like very

**[23:10]** underthink it. This can be like very

**[23:10]** underthink it. This can be like very very important. Uh, and then taking

**[23:11]** very important. Uh, and then taking

**[23:12]** very important. Uh, and then taking action um, how does it like do its work?

**[23:15]** action um, how does it like do its work?

**[23:15]** action um, how does it like do its work? Uh, does it have the right tools to do

**[23:17]** Uh, does it have the right tools to do

**[23:17]** Uh, does it have the right tools to do it like code generation, uh, bash these

**[23:19]** it like code generation, uh, bash these

**[23:19]** it like code generation, uh, bash these are more flexible ways of taking action,

**[23:21]** are more flexible ways of taking action,

**[23:21]** are more flexible ways of taking action, right? And then verification is another

**[23:24]** right? And then verification is another

**[23:24]** right? And then verification is another really important step. And so the

**[23:27]** really important step. And so the

**[23:27]** really important step. And so the basically what I'd say right now is like

**[23:28]** basically what I'd say right now is like

**[23:28]** basically what I'd say right now is like if you're thinking of building an agent,

**[23:31]** if you're thinking of building an agent,

**[23:31]** if you're thinking of building an agent, think about like can you verify its

**[23:34]** think about like can you verify its

**[23:34]** think about like can you verify its work, right? And if you can verify its

**[23:36]** work, right? And if you can verify its

**[23:36]** work, right? And if you can verify its work, it's like a great like candidate

**[23:38]** work, it's like a great like candidate

**[23:38]** work, it's like a great like candidate for an agent. If you can't verify its

**[23:40]** for an agent. If you can't verify its

**[23:40]** for an agent. If you can't verify its work, like it's like you know coding you

**[23:42]** work, like it's like you know coding you

**[23:42]** work, like it's like you know coding you can verify by lending, right? And you

**[23:44]** can verify by lending, right? And you

**[23:44]** can verify by lending, right? And you can at least make sure it compiles. So

**[23:46]** can at least make sure it compiles. So

**[23:46]** can at least make sure it compiles. So that's great. uh if you're doing let's

**[23:48]** that's great. uh if you're doing let's

**[23:48]** that's great. uh if you're doing let's say deep research for example it's

**[23:49]** say deep research for example it's

**[23:49]** say deep research for example it's actually a lot harder to verify your

**[23:51]** actually a lot harder to verify your

**[23:51]** actually a lot harder to verify your work one way you can do it is by citing

**[23:53]** work one way you can do it is by citing

**[23:53]** work one way you can do it is by citing sources right so that's like a step in

**[23:55]** sources right so that's like a step in

**[23:56]** sources right so that's like a step in verification but obviously research is

**[23:58]** verification but obviously research is

**[23:58]** verification but obviously research is less verifiable than code in some ways


### [24:00 - 25:00]

**[24:00]** less verifiable than code in some ways

**[24:00]** less verifiable than code in some ways right because like code has a compile

**[24:01]** right because like code has a compile

**[24:01]** right because like code has a compile step right you can also like execute it

**[24:04]** step right you can also like execute it

**[24:04]** step right you can also like execute it then see what it does right so um I

**[24:06]** then see what it does right so um I

**[24:06]** then see what it does right so um I think like thinking on you know like as

**[24:09]** think like thinking on you know like as

**[24:09]** think like thinking on you know like as we build agents the ones that are

**[24:11]** we build agents the ones that are

**[24:11]** we build agents the ones that are closest to being very general are the

**[24:12]** closest to being very general are the

**[24:12]** closest to being very general are the ones with the verification step that is

**[24:15]** ones with the verification step that is

**[24:15]** ones with the verification step that is very strong right So I I think there was

**[24:17]** very strong right So I I think there was

**[24:17]** very strong right So I I think there was a question here. Yeah.

**[24:18]** a question here. Yeah.

**[24:18]** a question here. Yeah. >> So when where do you generate a plan of

**[24:22]** >> So when where do you generate a plan of

**[24:22]** >> So when where do you generate a plan of the work?

**[24:28]** >> Yeah. I mean you you might

**[24:28]** >> Yeah. I mean you you might >> question

**[24:29]** >> question

**[24:29]** >> question >> Oh yeah sorry the the question was when

**[24:31]** >> Oh yeah sorry the the question was when

**[24:31]** >> Oh yeah sorry the the question was when do you generate a plan um before you run

**[24:34]** do you generate a plan um before you run

**[24:34]** do you generate a plan um before you run through it. So um like in cloud code you

**[24:38]** through it. So um like in cloud code you

**[24:38]** through it. So um like in cloud code you don't always generate a plan. Uh but if

**[24:41]** don't always generate a plan. Uh but if

**[24:41]** don't always generate a plan. Uh but if you want to you'd insert it between the

**[24:42]** you want to you'd insert it between the

**[24:42]** you want to you'd insert it between the gathering context and taking action

**[24:44]** gathering context and taking action

**[24:44]** gathering context and taking action step, right? And so um plans sort of

**[24:48]** step, right? And so um plans sort of

**[24:48]** step, right? And so um plans sort of help the agent think through step by

**[24:49]** help the agent think through step by

**[24:49]** help the agent think through step by step, but they add some latency, right?

**[24:52]** step, but they add some latency, right?

**[24:52]** step, but they add some latency, right? And so there is like some trade-off

**[24:53]** And so there is like some trade-off

**[24:53]** And so there is like some trade-off there. Um but yeah, the agent SDK helps

**[24:56]** there. Um but yeah, the agent SDK helps

**[24:56]** there. Um but yeah, the agent SDK helps you like do some planning as well. So

**[24:57]** you like do some planning as well. So

**[24:58]** you like do some planning as well. So yeah.

**[24:59]** yeah.

**[24:59]** yeah. >> Yeah. Can you like make the agent create


### [25:00 - 26:00]

**[25:03]** >> Yeah. Can you like make the agent create

**[25:03]** >> Yeah. Can you like make the agent create that to-do list for like 100%

**[25:08]** that to-do list for like 100%

**[25:08]** that to-do list for like 100% sure that it will create that to-do list

**[25:11]** sure that it will create that to-do list

**[25:11]** sure that it will create that to-do list and run by it?

**[25:12]** and run by it?

**[25:12]** and run by it? >> Uh yeah. So the question was will the

**[25:14]** >> Uh yeah. So the question was will the

**[25:14]** >> Uh yeah. So the question was will the agent create the to-do list? Uh yes. Um

**[25:18]** agent create the to-do list? Uh yes. Um

**[25:18]** agent create the to-do list? Uh yes. Um if you're using the agent SDK, we have

**[25:20]** if you're using the agent SDK, we have

**[25:20]** if you're using the agent SDK, we have like some to-do tools that come with it

**[25:21]** like some to-do tools that come with it

**[25:21]** like some to-do tools that come with it and so it will like maintain and check

**[25:23]** and so it will like maintain and check

**[25:23]** and so it will like maintain and check off to-dos and you can display that as

**[25:25]** off to-dos and you can display that as

**[25:25]** off to-dos and you can display that as you go. So yep.

**[25:28]** you go. So yep.

**[25:28]** you go. So yep. Um,

**[25:30]** Um,

**[25:30]** Um, any other questions about this right

**[25:32]** any other questions about this right

**[25:32]** any other questions about this right now? Okay, cool. Okay, so I'm going to

**[25:36]** now? Okay, cool. Okay, so I'm going to

**[25:36]** now? Okay, cool. Okay, so I'm going to quickly talk about like like how do you

**[25:37]** quickly talk about like like how do you

**[25:38]** quickly talk about like like how do you do this stuff? You like what are your

**[25:40]** do this stuff? You like what are your

**[25:40]** do this stuff? You like what are your tools for doing it, right? And uh there

**[25:43]** tools for doing it, right? And uh there

**[25:43]** tools for doing it, right? And uh there are three things you can do that you

**[25:45]** are three things you can do that you

**[25:45]** are three things you can do that you have tools, bash and code generation,

**[25:47]** have tools, bash and code generation,

**[25:47]** have tools, bash and code generation, right? And I I think traditionally I

**[25:49]** right? And I I think traditionally I

**[25:49]** right? And I I think traditionally I think a lot of people are only thinking

**[25:51]** think a lot of people are only thinking

**[25:51]** think a lot of people are only thinking about tools and uh yeah, basically one

**[25:53]** about tools and uh yeah, basically one

**[25:53]** about tools and uh yeah, basically one of the call to actions is just figuring

**[25:54]** of the call to actions is just figuring

**[25:54]** of the call to actions is just figuring out like thinking about it more broadly,

**[25:57]** out like thinking about it more broadly,

**[25:57]** out like thinking about it more broadly, right? So tools are extremely structured

**[25:59]** right? So tools are extremely structured

**[25:59]** right? So tools are extremely structured and very very reliable, right? Like if


### [26:00 - 27:00]

**[26:01]** and very very reliable, right? Like if

**[26:01]** and very very reliable, right? Like if you want to sort of have as fast an

**[26:03]** you want to sort of have as fast an

**[26:03]** you want to sort of have as fast an output as possible with minimal errors,

**[26:06]** output as possible with minimal errors,

**[26:06]** output as possible with minimal errors, uh minimal retries, uh tools are great.

**[26:10]** uh minimal retries, uh tools are great.

**[26:10]** uh minimal retries, uh tools are great. Uh cons, they're high context usage. If

**[26:12]** Uh cons, they're high context usage. If

**[26:12]** Uh cons, they're high context usage. If anyone's built an agent with like 50 or

**[26:15]** anyone's built an agent with like 50 or

**[26:15]** anyone's built an agent with like 50 or 100 tools, right? Like they take up a

**[26:17]** 100 tools, right? Like they take up a

**[26:17]** 100 tools, right? Like they take up a lot of context and the model it kind of

**[26:19]** lot of context and the model it kind of

**[26:19]** lot of context and the model it kind of gets a little bit confused, right? Um

**[26:21]** gets a little bit confused, right? Um

**[26:21]** gets a little bit confused, right? Um there's no like sort of discoverability

**[26:23]** there's no like sort of discoverability

**[26:23]** there's no like sort of discoverability of the tools. Um and they're not

**[26:25]** of the tools. Um and they're not

**[26:25]** of the tools. Um and they're not composable, right? and and I say tools

**[26:28]** composable, right? and and I say tools

**[26:28]** composable, right? and and I say tools in the sense of like if you're using you

**[26:30]** in the sense of like if you're using you

**[26:30]** in the sense of like if you're using you know messages or completion API right

**[26:32]** know messages or completion API right

**[26:32]** know messages or completion API right now um that's how the tools work of

**[26:36]** now um that's how the tools work of

**[26:36]** now um that's how the tools work of course like you know there's like code

**[26:37]** course like you know there's like code

**[26:37]** course like you know there's like code mode and programmatic tool calling so

**[26:38]** mode and programmatic tool calling so

**[26:38]** mode and programmatic tool calling so you can sort of blend some of these um

**[26:41]** you can sort of blend some of these um

**[26:41]** you can sort of blend some of these um but [clears throat] there's bash so bash

**[26:43]** but [clears throat] there's bash so bash

**[26:43]** but [clears throat] there's bash so bash is very composable right like uh static

**[26:46]** is very composable right like uh static

**[26:46]** is very composable right like uh static scripts low context usage uh it can take

**[26:49]** scripts low context usage uh it can take

**[26:49]** scripts low context usage uh it can take a little bit more discovery time because

**[26:51]** a little bit more discovery time because

**[26:51]** a little bit more discovery time because like let's say that you have whatever

**[26:53]** like let's say that you have whatever

**[26:53]** like let's say that you have whatever you have like the playright MCP or

**[26:55]** you have like the playright MCP or

**[26:55]** you have like the playright MCP or something like that um or sorry the

**[26:57]** something like that um or sorry the

**[26:57]** something like that um or sorry the playright CLI the playright like bash


### [27:00 - 28:00]

**[27:00]** playright CLI the playright like bash

**[27:00]** playright CLI the playright like bash tool um you can do playright-help to

**[27:03]** tool um you can do playright-help to

**[27:03]** tool um you can do playright-help to figure out all the things you can do but

**[27:04]** figure out all the things you can do but

**[27:04]** figure out all the things you can do but the agent needs to do that every time

**[27:06]** the agent needs to do that every time

**[27:06]** the agent needs to do that every time right so it needs to like discover what

**[27:07]** right so it needs to like discover what

**[27:07]** right so it needs to like discover what it can do um which is kind of powerful

**[27:10]** it can do um which is kind of powerful

**[27:10]** it can do um which is kind of powerful that it helps take away some of the high

**[27:12]** that it helps take away some of the high

**[27:12]** that it helps take away some of the high context usage but add some latency um

**[27:15]** context usage but add some latency um

**[27:15]** context usage but add some latency um there might be slightly lower call rates

**[27:17]** there might be slightly lower call rates

**[27:17]** there might be slightly lower call rates you know just because like it has a

**[27:19]** you know just because like it has a

**[27:19]** you know just because like it has a little bit more time to um it needs to

**[27:23]** little bit more time to um it needs to

**[27:23]** little bit more time to um it needs to like find the tools and what it can do.

**[27:25]** like find the tools and what it can do.

**[27:25]** like find the tools and what it can do. Um but this will definitely like improve

**[27:27]** Um but this will definitely like improve

**[27:27]** Um but this will definitely like improve as it goes. And then finally, codegen

**[27:30]** as it goes. And then finally, codegen

**[27:30]** as it goes. And then finally, codegen highly composable dynamic scripts. Um

**[27:34]** highly composable dynamic scripts. Um

**[27:34]** highly composable dynamic scripts. Um they take the longest to execute, right?

**[27:36]** they take the longest to execute, right?

**[27:36]** they take the longest to execute, right? So they need linking possibly

**[27:38]** So they need linking possibly

**[27:38]** So they need linking possibly compilation. API design becomes like a

**[27:41]** compilation. API design becomes like a

**[27:41]** compilation. API design becomes like a very very interesting step here, right?

**[27:44]** very very interesting step here, right?

**[27:44]** very very interesting step here, right? And I and I'll talk more about like uh

**[27:46]** And I and I'll talk more about like uh

**[27:46]** And I and I'll talk more about like uh best like how to think about API design

**[27:48]** best like how to think about API design

**[27:48]** best like how to think about API design in an agent. Um but yeah I think this is

**[27:51]** in an agent. Um but yeah I think this is

**[27:52]** in an agent. Um but yeah I think this is like how we like the the three tools you

**[27:54]** like how we like the the three tools you

**[27:54]** like how we like the the three tools you have and so yeah using tools think you

**[27:57]** have and so yeah using tools think you

**[27:57]** have and so yeah using tools think you still want some tools but you want to

**[27:59]** still want some tools but you want to

**[27:59]** still want some tools but you want to think about them as atomic actions your


### [28:00 - 29:00]

**[28:01]** think about them as atomic actions your

**[28:01]** think about them as atomic actions your agent usually needs to execute in

**[28:03]** agent usually needs to execute in

**[28:03]** agent usually needs to execute in sequence and you need a lot of control

**[28:05]** sequence and you need a lot of control

**[28:05]** sequence and you need a lot of control over right so for example in cloud code

**[28:07]** over right so for example in cloud code

**[28:07]** over right so for example in cloud code we don't use bash to write a file we

**[28:09]** we don't use bash to write a file we

**[28:09]** we don't use bash to write a file we have a write file tool right because we

**[28:11]** have a write file tool right because we

**[28:11]** have a write file tool right because we want the user to be able to sort of see

**[28:13]** want the user to be able to sort of see

**[28:13]** want the user to be able to sort of see the output and approve it and um we're

**[28:17]** the output and approve it and um we're

**[28:17]** the output and approve it and um we're not really composing write file with

**[28:18]** not really composing write file with

**[28:18]** not really composing write file with other things, right? It's like very

**[28:20]** other things, right? It's like very

**[28:20]** other things, right? It's like very atomic action. Um, sending an email is

**[28:23]** atomic action. Um, sending an email is

**[28:23]** atomic action. Um, sending an email is another example. Like any sort of like

**[28:24]** another example. Like any sort of like

**[28:24]** another example. Like any sort of like non-destruct like destructible or sort

**[28:27]** non-destruct like destructible or sort

**[28:27]** non-destruct like destructible or sort of like you know uh unreversible change

**[28:30]** of like you know uh unreversible change

**[28:30]** of like you know uh unreversible change is definitely like a a tool is a good

**[28:32]** is definitely like a a tool is a good

**[28:32]** is definitely like a a tool is a good place for that. Um then [clears throat]

**[28:35]** place for that. Um then [clears throat]

**[28:35]** place for that. Um then [clears throat] we've got bash. Uh so for example there

**[28:37]** we've got bash. Uh so for example there

**[28:37]** we've got bash. Uh so for example there are like uh composable actions like

**[28:40]** are like uh composable actions like

**[28:40]** are like uh composable actions like searching a folder using GitHub linting

**[28:42]** searching a folder using GitHub linting

**[28:42]** searching a folder using GitHub linting code and checking for errors or memory.

**[28:45]** code and checking for errors or memory.

**[28:45]** code and checking for errors or memory. Um and so yeah you can write files to

**[28:48]** Um and so yeah you can write files to

**[28:48]** Um and so yeah you can write files to memory and that can be your bash like

**[28:50]** memory and that can be your bash like

**[28:50]** memory and that can be your bash like bash can be your memory system for

**[28:51]** bash can be your memory system for

**[28:52]** bash can be your memory system for example right so um and then finally

**[28:54]** example right so um and then finally

**[28:54]** example right so um and then finally you've got code generation right so if

**[28:56]** you've got code generation right so if

**[28:56]** you've got code generation right so if you're trying to do this like highly

**[28:57]** you're trying to do this like highly

**[28:57]** you're trying to do this like highly dynamic very flexible logic composing

**[28:59]** dynamic very flexible logic composing


### [29:00 - 30:00]

**[29:00]** dynamic very flexible logic composing APIs uh like you're doing data analysis

**[29:02]** APIs uh like you're doing data analysis

**[29:02]** APIs uh like you're doing data analysis or deep research or like reusing

**[29:05]** or deep research or like reusing

**[29:05]** or deep research or like reusing patterns and so um yeah we'll talk more

**[29:07]** patterns and so um yeah we'll talk more

**[29:07]** patterns and so um yeah we'll talk more about uh code generation in a bit

**[29:11]** about uh code generation in a bit

**[29:11]** about uh code generation in a bit um any questions so far about like the

**[29:14]** um any questions so far about like the

**[29:14]** um any questions so far about like the SDK loop loop or tools versus bash

**[29:16]** SDK loop loop or tools versus bash

**[29:16]** SDK loop loop or tools versus bash versus codegen. Yeah.

**[29:18]** versus codegen. Yeah.

**[29:18]** versus codegen. Yeah. >> Yeah. Uh I was going to ask

**[29:19]** >> Yeah. Uh I was going to ask

**[29:20]** >> Yeah. Uh I was going to ask [clears throat] you are you going to

**[29:21]** [clears throat] you are you going to

**[29:21]** [clears throat] you are you going to have any readymade tools for like

**[29:24]** have any readymade tools for like

**[29:24]** have any readymade tools for like offloading results [snorts]

**[29:27]** offloading results [snorts]

**[29:27]** offloading results [snorts] >> offloading tool called results like into

**[29:28]** >> offloading tool called results like into

**[29:28]** >> offloading tool called results like into the file system or

**[29:29]** the file system or

**[29:29]** the file system or >> like let's say goes to bash and then

**[29:31]** >> like let's say goes to bash and then

**[29:31]** >> like let's say goes to bash and then context explodes.

**[29:33]** context explodes.

**[29:33]** context explodes. >> Does it like [clears throat] typed a

**[29:34]** >> Does it like [clears throat] typed a

**[29:34]** >> Does it like [clears throat] typed a command that like do everything up?

**[29:36]** command that like do everything up?

**[29:36]** command that like do everything up? >> Okay.

**[29:37]** >> Okay.

**[29:37]** >> Okay. >> Or or otherwise just like long outputs

**[29:39]** >> Or or otherwise just like long outputs

**[29:39]** >> Or or otherwise just like long outputs polluting your history.

**[29:40]** polluting your history.

**[29:40]** polluting your history. >> Sure. Yeah. Yeah. Yeah. I imagine like

**[29:42]** >> Sure. Yeah. Yeah. Yeah. I imagine like

**[29:42]** >> Sure. Yeah. Yeah. Yeah. I imagine like all the time just uploading them to

**[29:44]** all the time just uploading them to

**[29:44]** all the time just uploading them to files.

**[29:45]** files.

**[29:45]** files. >> Yeah. Yeah. I I think that's a good

**[29:47]** >> Yeah. Yeah. I I think that's a good

**[29:47]** >> Yeah. Yeah. I I think that's a good common practice. I think um we

**[29:52]** common practice. I think um we

**[29:52]** common practice. I think um we I I remember seeing some PRs about this

**[29:54]** I I remember seeing some PRs about this

**[29:54]** I I remember seeing some PRs about this very recently on on cloud code about

**[29:57]** very recently on on cloud code about

**[29:57]** very recently on on cloud code about handling very long outputs and I I I


### [30:00 - 31:00]

**[30:02]** handling very long outputs and I I I

**[30:02]** handling very long outputs and I I I don't know exactly like I I think I

**[30:06]** don't know exactly like I I think I

**[30:06]** don't know exactly like I I think I think we are moving towards a place

**[30:08]** think we are moving towards a place

**[30:08]** think we are moving towards a place where more and more things are being

**[30:09]** where more and more things are being

**[30:09]** where more and more things are being like just stored in the file system and

**[30:11]** like just stored in the file system and

**[30:11]** like just stored in the file system and this is like a good example. Yeah, like

**[30:12]** this is like a good example. Yeah, like

**[30:12]** this is like a good example. Yeah, like it's storing like long outputs uh over

**[30:15]** it's storing like long outputs uh over

**[30:15]** it's storing like long outputs uh over time. Um, I think like generally

**[30:18]** time. Um, I think like generally

**[30:18]** time. Um, I think like generally prompting the agent to do this is a good

**[30:20]** prompting the agent to do this is a good

**[30:20]** prompting the agent to do this is a good uh way to think about it. Or even if you

**[30:22]** uh way to think about it. Or even if you

**[30:22]** uh way to think about it. Or even if you have I think like something I just do

**[30:24]** have I think like something I just do

**[30:24]** have I think like something I just do always now is like whenever I have a

**[30:26]** always now is like whenever I have a

**[30:26]** always now is like whenever I have a tool call I um I save it like the

**[30:30]** tool call I um I save it like the

**[30:30]** tool call I um I save it like the results of the tool call to the file

**[30:31]** results of the tool call to the file

**[30:31]** results of the tool call to the file system so that you can like search

**[30:33]** system so that you can like search

**[30:33]** system so that you can like search across it and then have the tool call

**[30:34]** across it and then have the tool call

**[30:34]** across it and then have the tool call return the path of the result. Um just

**[30:38]** return the path of the result. Um just

**[30:38]** return the path of the result. Um just because like that helps it like sort of

**[30:40]** because like that helps it like sort of

**[30:40]** because like that helps it like sort of recheck its work. So um yes. Um, do you

**[30:45]** recheck its work. So um yes. Um, do you

**[30:45]** recheck its work. So um yes. Um, do you find that you need to [clears throat]

**[30:47]** find that you need to [clears throat]

**[30:48]** find that you need to [clears throat] use like the skills um kind of structure

**[30:51]** use like the skills um kind of structure

**[30:51]** use like the skills um kind of structure to help claude along to use the bash

**[30:54]** to help claude along to use the bash

**[30:54]** to help claude along to use the bash better or out of the box? You know,

**[30:57]** better or out of the box? You know,

**[30:57]** better or out of the box? You know, that's not necessary.

**[30:58]** that's not necessary.

**[30:58]** that's not necessary. >> Yeah. So, the question was about skills


### [31:00 - 32:00]

**[31:00]** >> Yeah. So, the question was about skills

**[31:00]** >> Yeah. So, the question was about skills and like do we need skills to use bash

**[31:03]** and like do we need skills to use bash

**[31:03]** and like do we need skills to use bash better? Um, yeah, for context skills

**[31:06]** better? Um, yeah, for context skills

**[31:06]** better? Um, yeah, for context skills maybe I can

**[31:08]** maybe I can

**[31:08]** maybe I can Okay, skills. Okay. Yeah, skills are

**[31:13]** Okay, skills. Okay. Yeah, skills are

**[31:13]** Okay, skills. Okay. Yeah, skills are basically a way of like uh you know

**[31:15]** basically a way of like uh you know

**[31:16]** basically a way of like uh you know allowing our agent to take longer

**[31:18]** allowing our agent to take longer

**[31:18]** allowing our agent to take longer complex tasks and like sort of load in

**[31:21]** complex tasks and like sort of load in

**[31:21]** complex tasks and like sort of load in things via context, right? So some like

**[31:23]** things via context, right? So some like

**[31:23]** things via context, right? So some like for example we have uh a bunch of DOCX

**[31:26]** for example we have uh a bunch of DOCX

**[31:26]** for example we have uh a bunch of DOCX skills and these DOCX skills tell it how

**[31:28]** skills and these DOCX skills tell it how

**[31:28]** skills and these DOCX skills tell it how to do code generation to generate these

**[31:30]** to do code generation to generate these

**[31:30]** to do code generation to generate these files, right? And so um yeah, I think

**[31:34]** files, right? And so um yeah, I think

**[31:34]** files, right? And so um yeah, I think overall skills are yeah, basically just

**[31:36]** overall skills are yeah, basically just

**[31:36]** overall skills are yeah, basically just a collection of files. They're also sort

**[31:38]** a collection of files. They're also sort

**[31:38]** a collection of files. They're also sort of like an example of being very like

**[31:40]** of like an example of being very like

**[31:40]** of like an example of being very like file system or bash tool pilled, right?

**[31:43]** file system or bash tool pilled, right?

**[31:43]** file system or bash tool pilled, right? Um because they're really just folders

**[31:46]** Um because they're really just folders

**[31:46]** Um because they're really just folders that your agent can like CD into and

**[31:49]** that your agent can like CD into and

**[31:49]** that your agent can like CD into and like read, right? Um and so yeah, they

**[31:53]** like read, right? Um and so yeah, they

**[31:53]** like read, right? Um and so yeah, they give like what we found the skills are

**[31:56]** give like what we found the skills are

**[31:56]** give like what we found the skills are really good for is pretty like

**[31:58]** really good for is pretty like

**[31:58]** really good for is pretty like repeatable instructions that need a lot


### [32:00 - 33:00]

**[32:00]** repeatable instructions that need a lot

**[32:00]** repeatable instructions that need a lot of expertise in them. Uh like for

**[32:03]** of expertise in them. Uh like for

**[32:03]** of expertise in them. Uh like for example, we released a front-end design

**[32:05]** example, we released a front-end design

**[32:05]** example, we released a front-end design skill recently that I really really like

**[32:07]** skill recently that I really really like

**[32:07]** skill recently that I really really like and um it's really just sort of a very

**[32:10]** and um it's really just sort of a very

**[32:10]** and um it's really just sort of a very detailed and good prompt on how to do

**[32:12]** detailed and good prompt on how to do

**[32:12]** detailed and good prompt on how to do front-end design. Uh but it comes from

**[32:14]** front-end design. Uh but it comes from

**[32:14]** front-end design. Uh but it comes from like our best, you know, like uh AI

**[32:18]** like our best, you know, like uh AI

**[32:18]** like our best, you know, like uh AI front-end engineer, you know what I

**[32:19]** front-end engineer, you know what I

**[32:19]** front-end engineer, you know what I mean? And he like really put a lot of

**[32:21]** mean? And he like really put a lot of

**[32:21]** mean? And he like really put a lot of top thought and iteration to it. So

**[32:22]** top thought and iteration to it. So

**[32:22]** top thought and iteration to it. So that's one way of using skills. Um

**[32:26]** that's one way of using skills. Um

**[32:26]** that's one way of using skills. Um >> yeah,

**[32:27]** >> yeah,

**[32:27]** >> yeah, >> quick question. Why use that front

**[32:29]** >> quick question. Why use that front

**[32:29]** >> quick question. Why use that front skill?

**[32:30]** skill?

**[32:30]** skill? >> Sure. It's pretty good. Thanks for

**[32:33]** >> Sure. It's pretty good. Thanks for

**[32:33]** >> Sure. It's pretty good. Thanks for publishing it. Uh I want to understand

**[32:35]** publishing it. Uh I want to understand

**[32:35]** publishing it. Uh I want to understand uh there are multiple MP files like MP

**[32:38]** uh there are multiple MP files like MP

**[32:38]** uh there are multiple MP files like MP is also there and it is also at the user

**[32:40]** is also there and it is also at the user

**[32:40]** is also there and it is also at the user level

**[32:42]** level

**[32:42]** level and then there are skill files like is

**[32:45]** and then there are skill files like is

**[32:45]** and then there are skill files like is there like a priority order should some

**[32:47]** there like a priority order should some

**[32:48]** there like a priority order should some stuff be relegated to claw.md and some

**[32:51]** stuff be relegated to claw.md and some

**[32:51]** stuff be relegated to claw.md and some other stuff should only come to

**[32:53]** other stuff should only come to

**[32:53]** other stuff should only come to skill.md? H so the question was about

**[32:55]** skill.md? H so the question was about

**[32:55]** skill.md? H so the question was about skill.md versus claw.md and how to think

**[32:58]** skill.md versus claw.md and how to think

**[32:58]** skill.md versus claw.md and how to think about uh that right and uh I think like


### [33:00 - 34:00]

**[33:03]** about uh that right and uh I think like

**[33:03]** about uh that right and uh I think like I I will say all of these concepts are

**[33:05]** I I will say all of these concepts are

**[33:05]** I I will say all of these concepts are so new you know I mean like even cloud

**[33:06]** so new you know I mean like even cloud

**[33:06]** so new you know I mean like even cloud code is like released it like eight or

**[33:08]** code is like released it like eight or

**[33:08]** code is like released it like eight or nine months ago right like um and so

**[33:11]** nine months ago right like um and so

**[33:11]** nine months ago right like um and so skills were released like two weeks ago

**[33:13]** skills were released like two weeks ago

**[33:13]** skills were released like two weeks ago like I like I won't pretend to know all

**[33:15]** like I like I won't pretend to know all

**[33:15]** like I like I won't pretend to know all of the best practices for for everything

**[33:17]** of the best practices for for everything

**[33:17]** of the best practices for for everything right um I think generally

**[33:21]** right um I think generally

**[33:21]** right um I think generally skills are a form of progressive context

**[33:23]** skills are a form of progressive context

**[33:23]** skills are a form of progressive context disclosure closure and that's sort of a

**[33:24]** disclosure closure and that's sort of a

**[33:24]** disclosure closure and that's sort of a pattern that we've talked about a bunch

**[33:26]** pattern that we've talked about a bunch

**[33:26]** pattern that we've talked about a bunch right like with like uh bash and you

**[33:29]** right like with like uh bash and you

**[33:29]** right like with like uh bash and you know like preferring that over like you

**[33:31]** know like preferring that over like you

**[33:31]** know like preferring that over like you know purely like normal tool calls is

**[33:34]** know purely like normal tool calls is

**[33:34]** know purely like normal tool calls is like it's a way of like the agent being

**[33:36]** like it's a way of like the agent being

**[33:36]** like it's a way of like the agent being like okay I need to do this let me find

**[33:39]** like okay I need to do this let me find

**[33:39]** like okay I need to do this let me find out how to do this and then let me read

**[33:41]** out how to do this and then let me read

**[33:41]** out how to do this and then let me read in this skill empty right so you ask it

**[33:43]** in this skill empty right so you ask it

**[33:43]** in this skill empty right so you ask it to make a docx file and then it like cds

**[33:46]** to make a docx file and then it like cds

**[33:46]** to make a docx file and then it like cds into the directory reads how to do it

**[33:48]** into the directory reads how to do it

**[33:48]** into the directory reads how to do it writes some scripts and keeps going so

**[33:51]** writes some scripts and keeps going so

**[33:51]** writes some scripts and keeps going so um yeah I think like there's still some

**[33:54]** um yeah I think like there's still some

**[33:54]** um yeah I think like there's still some intuition to build around like what what

**[33:56]** intuition to build around like what what

**[33:56]** intuition to build around like what what exactly you like define as a skill and

**[33:58]** exactly you like define as a skill and

**[33:58]** exactly you like define as a skill and how you split it out. Um but uh yeah, I


### [34:00 - 35:00]

**[34:01]** how you split it out. Um but uh yeah, I

**[34:01]** how you split it out. Um but uh yeah, I think uh yeah, lots of best practices to

**[34:04]** think uh yeah, lots of best practices to

**[34:04]** think uh yeah, lots of best practices to learn there still. Um

**[34:07]** learn there still. Um

**[34:07]** learn there still. Um >> yeah,

**[34:08]** >> yeah,

**[34:08]** >> yeah, >> so yesterday

**[34:10]** >> so yesterday

**[34:10]** >> so yesterday we [clears throat] talked about the

**[34:11]** we [clears throat] talked about the

**[34:12]** we [clears throat] talked about the future of skills over time.

**[34:15]** future of skills over time.

**[34:15]** future of skills over time. >> Do you see these as ultimately becoming

**[34:17]** >> Do you see these as ultimately becoming

**[34:17]** >> Do you see these as ultimately becoming part of the model and some of the skills

**[34:20]** part of the model and some of the skills

**[34:20]** part of the model and some of the skills this is just a way to bridge the gap for

**[34:21]** this is just a way to bridge the gap for

**[34:22]** this is just a way to bridge the gap for now?

**[34:22]** now?

**[34:22]** now? >> Yeah. Yeah. So the question was are

**[34:24]** >> Yeah. Yeah. So the question was are

**[34:24]** >> Yeah. Yeah. So the question was are skills ultimately part of the model? Um

**[34:27]** skills ultimately part of the model? Um

**[34:27]** skills ultimately part of the model? Um are they a way to bridge the gap? I

**[34:29]** are they a way to bridge the gap? I

**[34:29]** are they a way to bridge the gap? I missed Barry's talk at Barry and M's

**[34:31]** missed Barry's talk at Barry and M's

**[34:31]** missed Barry's talk at Barry and M's talk yesterday, but uh yeah, I think

**[34:33]** talk yesterday, but uh yeah, I think

**[34:33]** talk yesterday, but uh yeah, I think roughly the idea is that the model will

**[34:35]** roughly the idea is that the model will

**[34:35]** roughly the idea is that the model will get better and better at doing a wide

**[34:37]** get better and better at doing a wide

**[34:37]** get better and better at doing a wide variety of tasks and skills are the best

**[34:39]** variety of tasks and skills are the best

**[34:39]** variety of tasks and skills are the best way to give it out of distribution

**[34:40]** way to give it out of distribution

**[34:40]** way to give it out of distribution tasks, right? Um, [clears throat] but I

**[34:43]** tasks, right? Um, [clears throat] but I

**[34:43]** tasks, right? Um, [clears throat] but I I would broadly say that like it's

**[34:47]** I would broadly say that like it's

**[34:47]** I would broadly say that like it's really really hard especially like you

**[34:49]** really really hard especially like you

**[34:49]** really really hard especially like you know if you're like uh not at a lab to

**[34:53]** know if you're like uh not at a lab to

**[34:53]** know if you're like uh not at a lab to like tell where the models are going

**[34:55]** like tell where the models are going

**[34:55]** like tell where the models are going exactly. Um my general rule of thumb is

**[34:58]** exactly. Um my general rule of thumb is

**[34:58]** exactly. Um my general rule of thumb is like I try and like rethink or rewrite


### [35:00 - 36:00]

**[35:00]** like I try and like rethink or rewrite

**[35:00]** like I try and like rethink or rewrite my like agent code like every 6 months.

**[35:03]** my like agent code like every 6 months.

**[35:03]** my like agent code like every 6 months. Uh just cuz I'm like uh things have

**[35:04]** Uh just cuz I'm like uh things have

**[35:04]** Uh just cuz I'm like uh things have probably changed enough that I've like

**[35:06]** probably changed enough that I've like

**[35:06]** probably changed enough that I've like baked in some assumptions here. And so

**[35:09]** baked in some assumptions here. And so

**[35:09]** baked in some assumptions here. And so like I think that like our agent SDK is

**[35:12]** like I think that like our agent SDK is

**[35:12]** like I think that like our agent SDK is built to as much as possible sort of

**[35:14]** built to as much as possible sort of

**[35:14]** built to as much as possible sort of advance with capabilities, right? Like

**[35:16]** advance with capabilities, right? Like

**[35:16]** advance with capabilities, right? Like the bash tool will get better and

**[35:17]** the bash tool will get better and

**[35:18]** the bash tool will get better and better. Uh we're building it on top of

**[35:19]** better. Uh we're building it on top of

**[35:19]** better. Uh we're building it on top of cloud code. So as cloud code evolves,

**[35:21]** cloud code. So as cloud code evolves,

**[35:21]** cloud code. So as cloud code evolves, you'll get those wins out out of the

**[35:23]** you'll get those wins out out of the

**[35:23]** you'll get those wins out out of the gate. Um but at the same time like you

**[35:28]** gate. Um but at the same time like you

**[35:28]** gate. Um but at the same time like you know things are so different now like

**[35:30]** know things are so different now like

**[35:30]** know things are so different now like than they were a year ago in in terms of

**[35:32]** than they were a year ago in in terms of

**[35:32]** than they were a year ago in in terms of like AI engineering, right? And I think

**[35:35]** like AI engineering, right? And I think

**[35:35]** like AI engineering, right? And I think like a general best practice to me is

**[35:37]** like a general best practice to me is

**[35:37]** like a general best practice to me is sort of like, hey, we can write code 10

**[35:39]** sort of like, hey, we can write code 10

**[35:39]** sort of like, hey, we can write code 10 times faster. We should throw out code

**[35:41]** times faster. We should throw out code

**[35:41]** times faster. We should throw out code 10 times faster as well. Um, and I think

**[35:44]** 10 times faster as well. Um, and I think

**[35:44]** 10 times faster as well. Um, and I think thinking about like not so like hedging

**[35:47]** thinking about like not so like hedging

**[35:47]** thinking about like not so like hedging your bets on like where is the future

**[35:49]** your bets on like where is the future

**[35:49]** your bets on like where is the future right now, but like what can we do today

**[35:51]** right now, but like what can we do today

**[35:51]** right now, but like what can we do today that really works, right? And like like

**[35:54]** that really works, right? And like like

**[35:54]** that really works, right? And like like let's get market share today and not be

**[35:56]** let's get market share today and not be

**[35:56]** let's get market share today and not be afraid to throw out code later. Um, if

**[35:59]** afraid to throw out code later. Um, if

**[35:59]** afraid to throw out code later. Um, if you're a startup, this is arguably your


### [36:00 - 37:00]

**[36:01]** you're a startup, this is arguably your

**[36:01]** you're a startup, this is arguably your largest advantage that you have over

**[36:03]** largest advantage that you have over

**[36:03]** largest advantage that you have over competitors. They're like, you know,

**[36:04]** competitors. They're like, you know,

**[36:04]** competitors. They're like, you know, larger [snorts] companies have like

**[36:06]** larger [snorts] companies have like

**[36:06]** larger [snorts] companies have like six-month incubation cycles. And so

**[36:08]** six-month incubation cycles. And so

**[36:08]** six-month incubation cycles. And so they're always like stuck in the past of

**[36:11]** they're always like stuck in the past of

**[36:11]** they're always like stuck in the past of like the agent capabilities, right? And

**[36:13]** like the agent capabilities, right? And

**[36:13]** like the agent capabilities, right? And so your advantage is that you can like

**[36:15]** so your advantage is that you can like

**[36:15]** so your advantage is that you can like be like, hey, the agent the capabilities

**[36:17]** be like, hey, the agent the capabilities

**[36:17]** be like, hey, the agent the capabilities are here right now. Let me build

**[36:18]** are here right now. Let me build

**[36:18]** are here right now. Let me build something that uses this right now,

**[36:20]** something that uses this right now,

**[36:20]** something that uses this right now, right? So, um, yeah. Uh

**[36:25]** right? So, um, yeah. Uh

**[36:25]** right? So, um, yeah. Uh any any other questions on for we're

**[36:29]** any any other questions on for we're

**[36:29]** any any other questions on for we're talking about skills in bash. Okay. It

**[36:31]** talking about skills in bash. Okay. It

**[36:31]** talking about skills in bash. Okay. It seems like there are a lot of skill

**[36:32]** seems like there are a lot of skill

**[36:32]** seems like there are a lot of skill questions. So um yeah uh I I think at

**[36:37]** questions. So um yeah uh I I think at

**[36:37]** questions. So um yeah uh I I think at the back someone you might have to

**[36:39]** the back someone you might have to

**[36:39]** the back someone you might have to shout.

**[36:40]** shout.

**[36:40]** shout. >> Yeah. So why would you use a skill

**[36:41]** >> Yeah. So why would you use a skill

**[36:42]** >> Yeah. So why would you use a skill versus an API? They look very similar to

**[36:45]** versus an API? They look very similar to

**[36:45]** versus an API? They look very similar to that Python program there could be a

**[36:47]** that Python program there could be a

**[36:47]** that Python program there could be a package, right?

**[36:48]** package, right?

**[36:48]** package, right? >> Yeah. The question was why use a skill

**[36:50]** >> Yeah. The question was why use a skill

**[36:50]** >> Yeah. The question was why use a skill versus an API? Um, good question. I I

**[36:53]** versus an API? Um, good question. I I

**[36:53]** versus an API? Um, good question. I I think that like um when you like these

**[36:57]** think that like um when you like these

**[36:57]** think that like um when you like these are all forms of progressive disclosure

**[36:59]** are all forms of progressive disclosure

**[36:59]** are all forms of progressive disclosure basically to the agent to figure out


### [37:00 - 38:00]

**[37:01]** basically to the agent to figure out

**[37:01]** basically to the agent to figure out what it needs to do. Um, and I'll go

**[37:03]** what it needs to do. Um, and I'll go

**[37:03]** what it needs to do. Um, and I'll go over like uh examples of like you just

**[37:06]** over like uh examples of like you just

**[37:06]** over like uh examples of like you just have an API, right? In in our like in

**[37:09]** have an API, right? In in our like in

**[37:09]** have an API, right? In in our like in our prototyping session. Um, it's

**[37:12]** our prototyping session. Um, it's

**[37:12]** our prototyping session. Um, it's totally like use case dependent, right?

**[37:14]** totally like use case dependent, right?

**[37:14]** totally like use case dependent, right? Like just I think like I don't have a

**[37:17]** Like just I think like I don't have a

**[37:17]** Like just I think like I don't have a like I don't think there's a general

**[37:18]** like I don't think there's a general

**[37:18]** like I don't think there's a general rule. I think it's like read the

**[37:19]** rule. I think it's like read the

**[37:20]** rule. I think it's like read the transcript and see what your agent

**[37:21]** transcript and see what your agent

**[37:21]** transcript and see what your agent wants. If your agent always wants like

**[37:23]** wants. If your agent always wants like

**[37:24]** wants. If your agent always wants like thinks about the API better as like a

**[37:26]** thinks about the API better as like a

**[37:26]** thinks about the API better as like a API.ts file or something or API.py file,

**[37:29]** API.ts file or something or API.py file,

**[37:29]** API.ts file or something or API.py file, do that. You know, that's great. Like I

**[37:30]** do that. You know, that's great. Like I

**[37:30]** do that. You know, that's great. Like I think skills are like like sort of an

**[37:33]** think skills are like like sort of an

**[37:33]** think skills are like like sort of an introduction into like thinking about

**[37:35]** introduction into like thinking about

**[37:35]** introduction into like thinking about the file system as a way of storing

**[37:37]** the file system as a way of storing

**[37:37]** the file system as a way of storing context, right? And they're a great

**[37:38]** context, right? And they're a great

**[37:38]** context, right? And they're a great abstraction. Um, but there are many ways

**[37:41]** abstraction. Um, but there are many ways

**[37:41]** abstraction. Um, but there are many ways to use the system. Um, and I I should

**[37:45]** to use the system. Um, and I I should

**[37:45]** to use the system. Um, and I I should say that like something about skills

**[37:46]** say that like something about skills

**[37:46]** say that like something about skills that like you need the bash tool, you

**[37:48]** that like you need the bash tool, you

**[37:48]** that like you need the bash tool, you need a virtual file system, things like

**[37:49]** need a virtual file system, things like

**[37:50]** need a virtual file system, things like that. So the agent SDK is like basically

**[37:51]** that. So the agent SDK is like basically

**[37:51]** that. So the agent SDK is like basically the only way to really use skills to

**[37:54]** the only way to really use skills to

**[37:54]** the only way to really use skills to like their full extent right now. So um

**[37:57]** like their full extent right now. So um

**[37:57]** like their full extent right now. So um yeah. Yeah. Back there.

**[37:59]** yeah. Yeah. Back there.

**[37:59]** yeah. Yeah. Back there. >> Can we expect a marketplace for skills?


### [38:00 - 39:00]

**[38:02]** >> Can we expect a marketplace for skills?

**[38:02]** >> Can we expect a marketplace for skills? >> Yeah. The question was can we expect a

**[38:03]** >> Yeah. The question was can we expect a

**[38:03]** >> Yeah. The question was can we expect a marketplace for skills? So um yeah,

**[38:06]** marketplace for skills? So um yeah,

**[38:06]** marketplace for skills? So um yeah, clock code has a plug-in marketplace

**[38:09]** clock code has a plug-in marketplace

**[38:09]** clock code has a plug-in marketplace that you can also use with the agent

**[38:10]** that you can also use with the agent

**[38:10]** that you can also use with the agent SDK. Uh we're evolving that over time,

**[38:13]** SDK. Uh we're evolving that over time,

**[38:13]** SDK. Uh we're evolving that over time, you know, like it was like a very much a

**[38:15]** you know, like it was like a very much a

**[38:15]** you know, like it was like a very much a v0ero. Um, and by marketplace, I'm not

**[38:18]** v0ero. Um, and by marketplace, I'm not

**[38:18]** v0ero. Um, and by marketplace, I'm not sure if people will be charging for this

**[38:20]** sure if people will be charging for this

**[38:20]** sure if people will be charging for this exactly. It's more just like a discovery

**[38:21]** exactly. It's more just like a discovery

**[38:21]** exactly. It's more just like a discovery system, I think. Um, but yeah, that

**[38:23]** system, I think. Um, but yeah, that

**[38:24]** system, I think. Um, but yeah, that exists right now. You can do SL plugins

**[38:26]** exists right now. You can do SL plugins

**[38:26]** exists right now. You can do SL plugins in cloud code. Um, and and you can find

**[38:28]** in cloud code. Um, and and you can find

**[38:28]** in cloud code. Um, and and you can find some. So, yeah. Yep.

**[38:30]** some. So, yeah. Yep.

**[38:30]** some. So, yeah. Yep. >> What's your current thinking about when

**[38:32]** >> What's your current thinking about when

**[38:32]** >> What's your current thinking about when you're going to reach for like the SDK,

**[38:34]** you're going to reach for like the SDK,

**[38:34]** you're going to reach for like the SDK, you know, to solve a problem?

**[38:36]** you know, to solve a problem?

**[38:36]** you know, to solve a problem? >> When? Yes. The question is when do I use

**[38:38]** >> When? Yes. The question is when do I use

**[38:38]** >> When? Yes. The question is when do I use the SDK to solve a problem? uh if I'm

**[38:41]** the SDK to solve a problem? uh if I'm

**[38:41]** the SDK to solve a problem? uh if I'm building an agent basically I I think

**[38:44]** building an agent basically I I think

**[38:44]** building an agent basically I I think that like um my overall belief is that

**[38:49]** that like um my overall belief is that

**[38:50]** that like um my overall belief is that like for any agent the bash tool gives

**[38:52]** like for any agent the bash tool gives

**[38:52]** like for any agent the bash tool gives you so much power and flexibility and

**[38:54]** you so much power and flexibility and

**[38:54]** you so much power and flexibility and using the file system gives you so much

**[38:56]** using the file system gives you so much

**[38:56]** using the file system gives you so much power and flexibility that you can

**[38:57]** power and flexibility that you can

**[38:57]** power and flexibility that you can always ek out performance gains over it


### [39:00 - 40:00]

**[39:01]** always ek out performance gains over it

**[39:01]** always ek out performance gains over it right and so uh yeah in the prototyping

**[39:04]** right and so uh yeah in the prototyping

**[39:04]** right and so uh yeah in the prototyping part of this talk we're going to like

**[39:05]** part of this talk we're going to like

**[39:05]** part of this talk we're going to like look at an example with only tools and

**[39:08]** look at an example with only tools and

**[39:08]** look at an example with only tools and an example without with you bash and the

**[39:11]** an example without with you bash and the

**[39:11]** an example without with you bash and the file system and compare those two. Um,

**[39:13]** file system and compare those two. Um,

**[39:13]** file system and compare those two. Um, and yeah, that's what I mean by being

**[39:15]** and yeah, that's what I mean by being

**[39:15]** and yeah, that's what I mean by being bashful to build. I'm like I I just like

**[39:17]** bashful to build. I'm like I I just like

**[39:17]** bashful to build. I'm like I I just like start from the agent SDK, you know, and

**[39:19]** start from the agent SDK, you know, and

**[39:19]** start from the agent SDK, you know, and I think a lot of people at Enthropic

**[39:21]** I think a lot of people at Enthropic

**[39:21]** I think a lot of people at Enthropic have started like doing that as well.

**[39:23]** have started like doing that as well.

**[39:23]** have started like doing that as well. So, um, of course I I do want to say

**[39:25]** So, um, of course I I do want to say

**[39:25]** So, um, of course I I do want to say that there are lots of times where the

**[39:27]** that there are lots of times where the

**[39:27]** that there are lots of times where the agent SDK is kind of annoying because

**[39:28]** agent SDK is kind of annoying because

**[39:28]** agent SDK is kind of annoying because you've got like this network sandbox

**[39:31]** you've got like this network sandbox

**[39:31]** you've got like this network sandbox container and you're like, I hate like I

**[39:32]** container and you're like, I hate like I

**[39:32]** container and you're like, I hate like I don't want to do this, you know? I mean,

**[39:33]** don't want to do this, you know? I mean,

**[39:33]** don't want to do this, you know? I mean, like I want to run on my browser

**[39:36]** like I want to run on my browser

**[39:36]** like I want to run on my browser locally, right? Um, I totally get that.

**[39:38]** locally, right? Um, I totally get that.

**[39:38]** locally, right? Um, I totally get that. And I think it's there is like a real

**[39:39]** And I think it's there is like a real

**[39:40]** And I think it's there is like a real performance trade-off. Um the way I

**[39:42]** performance trade-off. Um the way I

**[39:42]** performance trade-off. Um the way I think about it is sort of like React

**[39:44]** think about it is sort of like React

**[39:44]** think about it is sort of like React versus like jQuery, you know, like I

**[39:47]** versus like jQuery, you know, like I

**[39:47]** versus like jQuery, you know, like I like I when I was coming up, I was like

**[39:49]** like I when I was coming up, I was like

**[39:49]** like I when I was coming up, I was like very into webdev and like you know I was

**[39:51]** very into webdev and like you know I was

**[39:51]** very into webdev and like you know I was using jQuery and Backbone and then React

**[39:53]** using jQuery and Backbone and then React

**[39:53]** using jQuery and Backbone and then React came out and it was by Facebook and

**[39:55]** came out and it was by Facebook and

**[39:55]** came out and it was by Facebook and they're like you have to here's JSX like

**[39:57]** they're like you have to here's JSX like

**[39:57]** they're like you have to here's JSX like we just made this up and and now there's

**[39:58]** we just made this up and and now there's

**[39:58]** we just made this up and and now there's a bundler, right? I'm like it's so


### [40:00 - 41:00]

**[40:00]** a bundler, right? I'm like it's so

**[40:00]** a bundler, right? I'm like it's so annoying. Um, but like they generally

**[40:04]** annoying. Um, but like they generally

**[40:04]** annoying. Um, but like they generally makes the model or it makes it made web

**[40:06]** makes the model or it makes it made web

**[40:06]** makes the model or it makes it made web apps more powerful, right? And I think

**[40:09]** apps more powerful, right? And I think

**[40:09]** apps more powerful, right? And I think we're sort of like the agent SDKs are

**[40:11]** we're sort of like the agent SDKs are

**[40:11]** we're sort of like the agent SDKs are like the react of agent frameworks to me

**[40:13]** like the react of agent frameworks to me

**[40:13]** like the react of agent frameworks to me because it's like we build our own stuff

**[40:16]** because it's like we build our own stuff

**[40:16]** because it's like we build our own stuff on top of it. So, you know, it's real

**[40:18]** on top of it. So, you know, it's real

**[40:18]** on top of it. So, you know, it's real and all the annoying parts of it are

**[40:19]** and all the annoying parts of it are

**[40:19]** and all the annoying parts of it are just like things where we're annoyed

**[40:21]** just like things where we're annoyed

**[40:21]** just like things where we're annoyed about it too, but we're like it just

**[40:23]** about it too, but we're like it just

**[40:23]** about it too, but we're like it just works like you have like got to do this,

**[40:25]** works like you have like got to do this,

**[40:25]** works like you have like got to do this, you know? Um, so yeah.

**[40:28]** you know? Um, so yeah.

**[40:28]** you know? Um, so yeah. Uh, yeah. Okay. more more skill

**[40:31]** Uh, yeah. Okay. more more skill

**[40:31]** Uh, yeah. Okay. more more skill questions I guess. Yeah. Right here.

**[40:33]** questions I guess. Yeah. Right here.

**[40:33]** questions I guess. Yeah. Right here. >> Uh what's the question? Bash.

**[40:35]** >> Uh what's the question? Bash.

**[40:35]** >> Uh what's the question? Bash. >> Oh, sure. Bash question. Great. I love

**[40:36]** >> Oh, sure. Bash question. Great. I love

**[40:36]** >> Oh, sure. Bash question. Great. I love bash.

**[40:36]** bash.

**[40:36]** bash. >> Custom internal like bash tools.

**[40:38]** >> Custom internal like bash tools.

**[40:38]** >> Custom internal like bash tools. >> Yeah.

**[40:39]** >> Yeah.

**[40:39]** >> Yeah. >> How do you let the agent discover that

**[40:41]** >> How do you let the agent discover that

**[40:41]** >> How do you let the agent discover that or do those have to become tool tools?

**[40:44]** or do those have to become tool tools?

**[40:44]** or do those have to become tool tools? >> Okay. The question is if you have custom

**[40:46]** >> Okay. The question is if you have custom

**[40:46]** >> Okay. The question is if you have custom agent bash tools, how do you let the

**[40:47]** agent bash tools, how do you let the

**[40:47]** agent bash tools, how do you let the agent discover that? By custom bash

**[40:49]** agent discover that? By custom bash

**[40:49]** agent discover that? By custom bash tools, you mean like bash scripts?

**[40:51]** tools, you mean like bash scripts?

**[40:51]** tools, you mean like bash scripts? >> We have we have bash scripts. Yeah.

**[40:54]** >> We have we have bash scripts. Yeah.

**[40:54]** >> We have we have bash scripts. Yeah. >> Um yeah. So I I think uh where is it?

**[40:57]** >> Um yeah. So I I think uh where is it?

**[40:57]** >> Um yeah. So I I think uh where is it? you just put it in the file system and

**[40:59]** you just put it in the file system and

**[40:59]** you just put it in the file system and you tell it like hey like here is a


### [41:00 - 42:00]

**[41:01]** you tell it like hey like here is a

**[41:01]** you tell it like hey like here is a script. Uh you can call it you know I

**[41:04]** script. Uh you can call it you know I

**[41:04]** script. Uh you can call it you know I I'm generally thinking in the context of

**[41:06]** I'm generally thinking in the context of

**[41:06]** I'm generally thinking in the context of the cloud agent SDK where it has the

**[41:08]** the cloud agent SDK where it has the

**[41:08]** the cloud agent SDK where it has the file system and the bash tools are tied

**[41:11]** file system and the bash tools are tied

**[41:11]** file system and the bash tools are tied together. This is kind of an anti

**[41:13]** together. This is kind of an anti

**[41:13]** together. This is kind of an anti pattern I see sometimes where people are

**[41:14]** pattern I see sometimes where people are

**[41:14]** pattern I see sometimes where people are like, "Oh, like we're going to host the

**[41:16]** like, "Oh, like we're going to host the

**[41:16]** like, "Oh, like we're going to host the bash tool in this like virtualized place

**[41:19]** bash tool in this like virtualized place

**[41:19]** bash tool in this like virtualized place and it's not going to interact with

**[41:20]** and it's not going to interact with

**[41:20]** and it's not going to interact with other parts of like the agent loop, you

**[41:23]** other parts of like the agent loop, you

**[41:23]** other parts of like the agent loop, you know, and that sort of, you know, makes

**[41:25]** know, and that sort of, you know, makes

**[41:25]** know, and that sort of, you know, makes it hard cuz if if you got a tool result

**[41:26]** it hard cuz if if you got a tool result

**[41:26]** it hard cuz if if you got a tool result that's saving a file, then your bash

**[41:29]** that's saving a file, then your bash

**[41:29]** that's saving a file, then your bash tool can't like uh read it, you know, I

**[41:31]** tool can't like uh read it, you know, I

**[41:31]** tool can't like uh read it, you know, I mean, unless it's all in one one

**[41:33]** mean, unless it's all in one one

**[41:33]** mean, unless it's all in one one container." So, does that answer your

**[41:35]** container." So, does that answer your

**[41:35]** container." So, does that answer your question? Like

**[41:37]** question? Like

**[41:37]** question? Like >> Yeah, kind of. I mean, like, so you're

**[41:38]** >> Yeah, kind of. I mean, like, so you're

**[41:38]** >> Yeah, kind of. I mean, like, so you're just saying you just put it in like

**[41:40]** just saying you just put it in like

**[41:40]** just saying you just put it in like system prompt or something? Yeah, I just

**[41:41]** system prompt or something? Yeah, I just

**[41:41]** system prompt or something? Yeah, I just put in system prompting like hey you

**[41:42]** put in system prompting like hey you

**[41:42]** put in system prompting like hey you have access to this. I would like sort

**[41:44]** have access to this. I would like sort

**[41:44]** have access to this. I would like sort of design all my CLI scripts to have

**[41:46]** of design all my CLI scripts to have

**[41:46]** of design all my CLI scripts to have like a d-help or something so that the

**[41:48]** like a d-help or something so that the

**[41:48]** like a d-help or something so that the model can call that and then it can like

**[41:51]** model can call that and then it can like

**[41:51]** model can call that and then it can like progressively disclose like every like

**[41:53]** progressively disclose like every like

**[41:53]** progressively disclose like every like subcomand inside of the script. Yeah.

**[41:56]** subcomand inside of the script. Yeah.

**[41:56]** subcomand inside of the script. Yeah. >> Uh yeah m

**[41:57]** >> Uh yeah m

**[41:57]** >> Uh yeah m >> yeah so uh like my question is around


### [42:00 - 43:00]

**[42:00]** >> yeah so uh like my question is around

**[42:00]** >> yeah so uh like my question is around when to reach for the agent SDK. So have

**[42:02]** when to reach for the agent SDK. So have

**[42:02]** when to reach for the agent SDK. So have you designed or rather would you

**[42:04]** you designed or rather would you

**[42:04]** you designed or rather would you recommend someone use the agent SDK to

**[42:06]** recommend someone use the agent SDK to

**[42:06]** recommend someone use the agent SDK to build like a generic chat agent as

**[42:09]** build like a generic chat agent as

**[42:10]** build like a generic chat agent as compared to like oh you know I'm

**[42:11]** compared to like oh you know I'm

**[42:11]** compared to like oh you know I'm building an agent where you have some

**[42:13]** building an agent where you have some

**[42:13]** building an agent where you have some input and the agent goes and does some

**[42:15]** input and the agent goes and does some

**[42:15]** input and the agent goes and does some stuff and finally I care about the

**[42:17]** stuff and finally I care about the

**[42:17]** stuff and finally I care about the output as compared to let's say someone

**[42:19]** output as compared to let's say someone

**[42:19]** output as compared to let's say someone like are you using or do you foresee

**[42:21]** like are you using or do you foresee

**[42:21]** like are you using or do you foresee using the agent to build like the agent

**[42:23]** using the agent to build like the agent

**[42:23]** using the agent to build like the agent SDK to build like clot the the app

**[42:26]** SDK to build like clot the the app

**[42:26]** SDK to build like clot the the app rather than clot code. Uh yeah. So the

**[42:29]** rather than clot code. Uh yeah. So the

**[42:30]** rather than clot code. Uh yeah. So the question is when do we reach for the

**[42:31]** question is when do we reach for the

**[42:31]** question is when do we reach for the agent SDK uh does um like uh like would

**[42:38]** agent SDK uh does um like uh like would

**[42:38]** agent SDK uh does um like uh like would we use the agent SDK to build cloud.AI

**[42:40]** we use the agent SDK to build cloud.AI

**[42:40]** we use the agent SDK to build cloud.AI which is a more traditional chatbot uh

**[42:43]** which is a more traditional chatbot uh

**[42:43]** which is a more traditional chatbot uh than cloud code. Um I one I think cloud

**[42:47]** than cloud code. Um I one I think cloud

**[42:47]** than cloud code. Um I one I think cloud code is like a very like like interface

**[42:49]** code is like a very like like interface

**[42:49]** code is like a very like like interface is not a traditional chatbot interface

**[42:51]** is not a traditional chatbot interface

**[42:51]** is not a traditional chatbot interface but like the inputs and outputs are

**[42:54]** but like the inputs and outputs are

**[42:54]** but like the inputs and outputs are right like you input code in you you get

**[42:56]** right like you input code in you you get

**[42:56]** right like you input code in you you get like or you input text in you get text

**[42:58]** like or you input text in you get text

**[42:58]** like or you input text in you get text out and you they take actions along the


### [43:00 - 44:00]

**[43:00]** out and you they take actions along the

**[43:00]** out and you they take actions along the way um you might have seen that like

**[43:03]** way um you might have seen that like

**[43:03]** way um you might have seen that like when we rolled out doc creation for

**[43:05]** when we rolled out doc creation for

**[43:05]** when we rolled out doc creation for cloud.ai AI. Um, now it has the ability

**[43:09]** cloud.ai AI. Um, now it has the ability

**[43:09]** cloud.ai AI. Um, now it has the ability to spin up a file system and like create

**[43:13]** to spin up a file system and like create

**[43:14]** to spin up a file system and like create spreadsheets and PowerPoint files and

**[43:15]** spreadsheets and PowerPoint files and

**[43:15]** spreadsheets and PowerPoint files and things like that by generating code. And

**[43:17]** things like that by generating code. And

**[43:18]** things like that by generating code. And so that is like you know we're in the

**[43:20]** so that is like you know we're in the

**[43:20]** so that is like you know we're in the midst of sort of like um like merging

**[43:23]** midst of sort of like um like merging

**[43:23]** midst of sort of like um like merging our agent loops and stuff like that. But

**[43:24]** our agent loops and stuff like that. But

**[43:24]** our agent loops and stuff like that. But but broadly like uh like yeah cloud.ai

**[43:28]** but broadly like uh like yeah cloud.ai

**[43:28]** but broadly like uh like yeah cloud.ai will like is getting more and more like

**[43:30]** will like is getting more and more like

**[43:30]** will like is getting more and more like you see it with skills and the memory

**[43:32]** you see it with skills and the memory

**[43:32]** you see it with skills and the memory tool and stuff more and more file system

**[43:34]** tool and stuff more and more file system

**[43:34]** tool and stuff more and more file system pills, right? So, uh, we do think this

**[43:36]** pills, right? So, uh, we do think this

**[43:36]** pills, right? So, uh, we do think this like a broad thing that you can use just

**[43:38]** like a broad thing that you can use just

**[43:38]** like a broad thing that you can use just just generally and happy to talk through

**[43:40]** just generally and happy to talk through

**[43:40]** just generally and happy to talk through examples.

**[43:42]** examples.

**[43:42]** examples. Um, yeah, one more question then we'll

**[43:44]** Um, yeah, one more question then we'll

**[43:44]** Um, yeah, one more question then we'll keep going. Yeah.

**[43:44]** keep going. Yeah.

**[43:44]** keep going. Yeah. >> Still trying to understand the rule of

**[43:46]** >> Still trying to understand the rule of

**[43:46]** >> Still trying to understand the rule of thumb on when to build a tool or use a

**[43:49]** thumb on when to build a tool or use a

**[43:49]** thumb on when to build a tool or use a tool, when to

**[43:51]** tool, when to

**[43:51]** tool, when to wrap something with a script or just let

**[43:53]** wrap something with a script or just let

**[43:53]** wrap something with a script or just let the agent go wild on the bash because I

**[43:56]** the agent go wild on the bash because I

**[43:56]** the agent go wild on the bash because I I'll give you an example. Let's say I

**[43:59]** I'll give you an example. Let's say I

**[43:59]** I'll give you an example. Let's say I need to access a database


### [44:00 - 45:00]

**[44:02]** need to access a database

**[44:02]** need to access a database from time to time. I can use an MCP. I

**[44:05]** from time to time. I can use an MCP. I

**[44:05]** from time to time. I can use an MCP. I can wrap it in a script and I can just

**[44:07]** can wrap it in a script and I can just

**[44:07]** can wrap it in a script and I can just let the agent call an endpoint from B

**[44:11]** let the agent call an endpoint from B

**[44:11]** let the agent call an endpoint from B directly from bash, right?

**[44:13]** directly from bash, right?

**[44:13]** directly from bash, right? >> Yeah, great question. Great question.

**[44:14]** >> Yeah, great question. Great question.

**[44:14]** >> Yeah, great question. Great question. So, it still trying to gro like when to

**[44:17]** So, it still trying to gro like when to

**[44:17]** So, it still trying to gro like when to use tools versus bash versus codegen and

**[44:19]** use tools versus bash versus codegen and

**[44:19]** use tools versus bash versus codegen and you gave an example like okay, I have a

**[44:21]** you gave an example like okay, I have a

**[44:21]** you gave an example like okay, I have a database. Um, I want the agent to be

**[44:23]** database. Um, I want the agent to be

**[44:23]** database. Um, I want the agent to be able to access it in some way. What

**[44:24]** able to access it in some way. What

**[44:24]** able to access it in some way. What should I do? Should I create a tool that

**[44:26]** should I do? Should I create a tool that

**[44:26]** should I do? Should I create a tool that queries the database in some way? Um,

**[44:29]** queries the database in some way? Um,

**[44:29]** queries the database in some way? Um, should I use the bash? Should I use

**[44:31]** should I use the bash? Should I use

**[44:31]** should I use the bash? Should I use codegen? Right? These are all these are

**[44:32]** codegen? Right? These are all these are

**[44:32]** codegen? Right? These are all these are three ways of doing it. Um I think that

**[44:35]** three ways of doing it. Um I think that

**[44:35]** three ways of doing it. Um I think that they are like you could use any of them

**[44:37]** they are like you could use any of them

**[44:37]** they are like you could use any of them and I I think like part of it is like I

**[44:40]** and I I think like part of it is like I

**[44:40]** and I I think like part of it is like I I think unfortunately there's no like

**[44:43]** I think unfortunately there's no like

**[44:43]** I think unfortunately there's no like single best practice, right? This is

**[44:45]** single best practice, right? This is

**[44:45]** single best practice, right? This is like kind of a system design problem.

**[44:46]** like kind of a system design problem.

**[44:46]** like kind of a system design problem. But let's say that you want to access

**[44:48]** But let's say that you want to access

**[44:48]** But let's say that you want to access your bash your database via tool. You

**[44:51]** your bash your database via tool. You

**[44:51]** your bash your database via tool. You would do that if your database was very

**[44:52]** would do that if your database was very

**[44:52]** would do that if your database was very very structured and you had to be very

**[44:54]** very structured and you had to be very

**[44:54]** very structured and you had to be very careful about like I don't know you're

**[44:57]** careful about like I don't know you're

**[44:57]** careful about like I don't know you're accessing like user sensitive

**[44:59]** accessing like user sensitive

**[44:59]** accessing like user sensitive information or something like that and


### [45:00 - 46:00]

**[45:01]** information or something like that and

**[45:01]** information or something like that and you're like hey I I can only take in

**[45:04]** you're like hey I I can only take in

**[45:04]** you're like hey I I can only take in this input and I need to like give this

**[45:06]** this input and I need to like give this

**[45:06]** this input and I need to like give this output and I have to mask everything

**[45:08]** output and I have to mask everything

**[45:08]** output and I have to mask everything else about the database from the agent

**[45:11]** else about the database from the agent

**[45:11]** else about the database from the agent right obviously that like sort of limits

**[45:14]** right obviously that like sort of limits

**[45:14]** right obviously that like sort of limits what the agent can do right like it

**[45:16]** what the agent can do right like it

**[45:16]** what the agent can do right like it can't write a very dynamic query right

**[45:19]** can't write a very dynamic query right

**[45:19]** can't write a very dynamic query right um if you're writing a full-on SQL

**[45:21]** um if you're writing a full-on SQL

**[45:21]** um if you're writing a full-on SQL query, I would definitely use bash or

**[45:22]** query, I would definitely use bash or

**[45:22]** query, I would definitely use bash or cogen uh just because when the model is

**[45:26]** cogen uh just because when the model is

**[45:26]** cogen uh just because when the model is writing a SQL query, it can make

**[45:27]** writing a SQL query, it can make

**[45:27]** writing a SQL query, it can make mistakes and the way it fixes it is is

**[45:30]** mistakes and the way it fixes it is is

**[45:30]** mistakes and the way it fixes it is is its mistakes is by like linting or like

**[45:34]** its mistakes is by like linting or like

**[45:34]** its mistakes is by like linting or like running the file, looking at the output,

**[45:36]** running the file, looking at the output,

**[45:36]** running the file, looking at the output, seeing if there are errors and then

**[45:37]** seeing if there are errors and then

**[45:37]** seeing if there are errors and then iterating on it, right? Um, and so I

**[45:41]** iterating on it, right? Um, and so I

**[45:41]** iterating on it, right? Um, and so I generally like if I'm building an agent

**[45:43]** generally like if I'm building an agent

**[45:44]** generally like if I'm building an agent today, I'm giving it as much access to

**[45:46]** today, I'm giving it as much access to

**[45:46]** today, I'm giving it as much access to my database as possible and then I'm

**[45:48]** my database as possible and then I'm

**[45:48]** my database as possible and then I'm like putting in guard rails, right? Like

**[45:50]** like putting in guard rails, right? Like

**[45:50]** like putting in guard rails, right? Like I'm probably limiting its like right

**[45:53]** I'm probably limiting its like right

**[45:53]** I'm probably limiting its like right access in different ways. But what I

**[45:56]** access in different ways. But what I

**[45:56]** access in different ways. But what I probably what I would do is like I would

**[45:58]** probably what I would do is like I would

**[45:58]** probably what I would do is like I would give it right access and put in specific


### [46:00 - 47:00]

**[46:01]** give it right access and put in specific

**[46:01]** give it right access and put in specific rules and then give it feedback if it

**[46:04]** rules and then give it feedback if it

**[46:04]** rules and then give it feedback if it tries to do something it can't do. You

**[46:06]** tries to do something it can't do. You

**[46:06]** tries to do something it can't do. You know what I mean? And so I know this is

**[46:07]** know what I mean? And so I know this is

**[46:07]** know what I mean? And so I know this is like kind of a hard problem, but I think

**[46:09]** like kind of a hard problem, but I think

**[46:09]** like kind of a hard problem, but I think this is the like set of problems for us

**[46:12]** this is the like set of problems for us

**[46:12]** this is the like set of problems for us to solve, right? Like we built a bash

**[46:14]** to solve, right? Like we built a bash

**[46:14]** to solve, right? Like we built a bash tool parser. Um, and that's a super

**[46:17]** tool parser. Um, and that's a super

**[46:17]** tool parser. Um, and that's a super annoying problem. Uh, but we need to

**[46:20]** annoying problem. Uh, but we need to

**[46:20]** annoying problem. Uh, but we need to solve that in order to like let the

**[46:21]** solve that in order to like let the

**[46:22]** solve that in order to like let the agent work generally, right? And same

**[46:24]** agent work generally, right? And same

**[46:24]** agent work generally, right? And same thing with like database like like yes,

**[46:26]** thing with like database like like yes,

**[46:26]** thing with like database like like yes, it's quite hard to understand what is a

**[46:28]** it's quite hard to understand what is a

**[46:28]** it's quite hard to understand what is a query doing, but if you can solve that,

**[46:30]** query doing, but if you can solve that,

**[46:30]** query doing, but if you can solve that, you can let your agent work more

**[46:31]** you can let your agent work more

**[46:31]** you can let your agent work more generally over time. So um yeah I think

**[46:34]** generally over time. So um yeah I think

**[46:34]** generally over time. So um yeah I think thinking about it uh like flexibly as

**[46:37]** thinking about it uh like flexibly as

**[46:38]** thinking about it uh like flexibly as much as possible and keeping tools to be

**[46:39]** much as possible and keeping tools to be

**[46:39]** much as possible and keeping tools to be like very very like sort of atomic

**[46:42]** like very very like sort of atomic

**[46:42]** like very very like sort of atomic actions right that you need a lot of

**[46:43]** actions right that you need a lot of

**[46:43]** actions right that you need a lot of guarantees around.

**[46:45]** guarantees around.

**[46:45]** guarantees around. Um

**[46:46]** Um

**[46:46]** Um >> a follow on the same thing right uh how

**[46:49]** >> a follow on the same thing right uh how

**[46:49]** >> a follow on the same thing right uh how do you ensure the role based access

**[46:51]** do you ensure the role based access

**[46:51]** do you ensure the role based access controls are taken care of

**[46:55]** controls are taken care of

**[46:55]** controls are taken care of >> how do you uh so the question is how do

**[46:57]** >> how do you uh so the question is how do

**[46:57]** >> how do you uh so the question is how do you ensure that the role based act uh

**[46:59]** you ensure that the role based act uh

**[46:59]** you ensure that the role based act uh access controls are taken care of


### [47:00 - 48:00]

**[47:01]** access controls are taken care of

**[47:01]** access controls are taken care of usually that's in like how you provision

**[47:02]** usually that's in like how you provision

**[47:02]** usually that's in like how you provision your API key or your backend service or

**[47:04]** your API key or your backend service or

**[47:04]** your API key or your backend service or something like that right like um I

**[47:07]** something like that right like um I

**[47:07]** something like that right like um I think that like probably what I do is

**[47:09]** think that like probably what I do is

**[47:09]** think that like probably what I do is like I create like temporary API keys

**[47:11]** like I create like temporary API keys

**[47:12]** like I create like temporary API keys sometimes people create proxies in

**[47:13]** sometimes people create proxies in

**[47:13]** sometimes people create proxies in between to insert the API keys

**[47:15]** between to insert the API keys

**[47:16]** between to insert the API keys um if you're concerned about

**[47:17]** um if you're concerned about

**[47:17]** um if you're concerned about excfiltration of that. Um but yeah, I

**[47:18]** excfiltration of that. Um but yeah, I

**[47:18]** excfiltration of that. Um but yeah, I would create like API keys for your

**[47:21]** would create like API keys for your

**[47:21]** would create like API keys for your agents that are scoped in certain ways

**[47:23]** agents that are scoped in certain ways

**[47:23]** agents that are scoped in certain ways and so then on the back end you can sort

**[47:24]** and so then on the back end you can sort

**[47:24]** and so then on the back end you can sort of check it's like you know what it's

**[47:26]** of check it's like you know what it's

**[47:26]** of check it's like you know what it's trying to do and like uh if it's a an

**[47:29]** trying to do and like uh if it's a an

**[47:29]** trying to do and like uh if it's a an agent you can like give it different

**[47:31]** agent you can like give it different

**[47:31]** agent you can like give it different feedback. So yeah.

**[47:33]** feedback. So yeah.

**[47:33]** feedback. So yeah. >> All right. I have one more question.

**[47:34]** >> All right. I have one more question.

**[47:34]** >> All right. I have one more question. >> Um anything you could tell us uh more

**[47:37]** >> Um anything you could tell us uh more

**[47:37]** >> Um anything you could tell us uh more about the the memory tool the internal

**[47:39]** about the the memory tool the internal

**[47:39]** about the the memory tool the internal memory tool? Um,

**[47:42]** memory tool? Um,

**[47:42]** memory tool? Um, I have I I'm not trying to like keep a

**[47:45]** I have I I'm not trying to like keep a

**[47:45]** I have I I'm not trying to like keep a secret. I I don't know exactly like I

**[47:47]** secret. I I don't know exactly like I

**[47:47]** secret. I I don't know exactly like I haven't read the code, but I I think it

**[47:49]** haven't read the code, but I I think it

**[47:49]** haven't read the code, but I I think it generally works on on the file system.

**[47:51]** generally works on on the file system.

**[47:51]** generally works on on the file system. And so, um,

**[47:52]** And so, um,

**[47:52]** And so, um, >> you expose it to uh to the uh SDK or is

**[47:56]** >> you expose it to uh to the uh SDK or is

**[47:56]** >> you expose it to uh to the uh SDK or is it already available?

**[47:57]** it already available?

**[47:57]** it already available? >> Um, I would say that like we we've had


### [48:00 - 49:00]

**[48:00]** >> Um, I would say that like we we've had

**[48:00]** >> Um, I would say that like we we've had this question a bunch. I would just use

**[48:01]** this question a bunch. I would just use

**[48:01]** this question a bunch. I would just use the file system on in the cloud agent

**[48:03]** the file system on in the cloud agent

**[48:03]** the file system on in the cloud agent SDK. I would just create like a memories

**[48:05]** SDK. I would just create like a memories

**[48:05]** SDK. I would just create like a memories folder or something and tell it to write

**[48:06]** folder or something and tell it to write

**[48:06]** folder or something and tell it to write memories there. Um it's like I I don't

**[48:10]** memories there. Um it's like I I don't

**[48:10]** memories there. Um it's like I I don't know the exact implementation of the

**[48:11]** know the exact implementation of the

**[48:11]** know the exact implementation of the memory tool but it does use the file

**[48:13]** memory tool but it does use the file

**[48:13]** memory tool but it does use the file system in in in that way. So yeah

**[48:16]** system in in in that way. So yeah

**[48:16]** system in in in that way. So yeah um all right yeah last question on this.

**[48:18]** um all right yeah last question on this.

**[48:18]** um all right yeah last question on this. Yeah

**[48:19]** Yeah

**[48:19]** Yeah >> yeah how you are manage for the b and

**[48:21]** >> yeah how you are manage for the b and

**[48:21]** >> yeah how you are manage for the b and the code how you are managing the like

**[48:24]** the code how you are managing the like

**[48:24]** the code how you are managing the like reusability suppose the same agent is

**[48:26]** reusability suppose the same agent is

**[48:26]** reusability suppose the same agent is rolled out to hundreds of users and uh

**[48:29]** rolled out to hundreds of users and uh

**[48:29]** rolled out to hundreds of users and uh same code every time it is generating

**[48:31]** same code every time it is generating

**[48:31]** same code every time it is generating and every time it is executing. So how

**[48:34]** and every time it is executing. So how

**[48:34]** and every time it is executing. So how can we use the reusability? Yeah, that's

**[48:36]** can we use the reusability? Yeah, that's

**[48:36]** can we use the reusability? Yeah, that's a really good question. So, uh yeah,

**[48:40]** a really good question. So, uh yeah,

**[48:40]** a really good question. So, uh yeah, let's say you have two agents

**[48:41]** let's say you have two agents

**[48:41]** let's say you have two agents interacting with two different people.

**[48:44]** interacting with two different people.

**[48:44]** interacting with two different people. The question is like how do you think

**[48:45]** The question is like how do you think

**[48:45]** The question is like how do you think about reusability between agents or how

**[48:47]** about reusability between agents or how

**[48:48]** about reusability between agents or how do agents communicate, right? Um I think

**[48:53]** do agents communicate, right? Um I think

**[48:53]** do agents communicate, right? Um I think uh this is a thing to be discovered. I

**[48:56]** uh this is a thing to be discovered. I

**[48:56]** uh this is a thing to be discovered. I think like but I think there's a lot of

**[48:57]** think like but I think there's a lot of

**[48:57]** think like but I think there's a lot of best practices and system design to be

**[48:59]** best practices and system design to be

**[48:59]** best practices and system design to be done on like um because traditionally


### [49:00 - 50:00]

**[49:03]** done on like um because traditionally

**[49:03]** done on like um because traditionally with web apps you're serving one app to

**[49:05]** with web apps you're serving one app to

**[49:05]** with web apps you're serving one app to like a million people right and with

**[49:07]** like a million people right and with

**[49:07]** like a million people right and with agents like with cloud code we serve

**[49:09]** agents like with cloud code we serve

**[49:09]** agents like with cloud code we serve like you know a onetoone like container

**[49:12]** like you know a onetoone like container

**[49:12]** like you know a onetoone like container when you use cloud code on the web it's

**[49:14]** when you use cloud code on the web it's

**[49:14]** when you use cloud code on the web it's like it's your container right and so

**[49:16]** like it's your container right and so

**[49:16]** like it's your container right and so there's not a lot of like communication

**[49:18]** there's not a lot of like communication

**[49:18]** there's not a lot of like communication between containers it's a very very

**[49:20]** between containers it's a very very

**[49:20]** between containers it's a very very different paradigm I'm not going to say

**[49:22]** different paradigm I'm not going to say

**[49:22]** different paradigm I'm not going to say that like I know exactly the best system

**[49:24]** that like I know exactly the best system

**[49:24]** that like I know exactly the best system design to do that right and like I think

**[49:27]** design to do that right and like I think

**[49:27]** design to do that right and like I think there's a lots of best practices on like

**[49:28]** there's a lots of best practices on like

**[49:28]** there's a lots of best practices on like okay these agents are reusing work um

**[49:31]** okay these agents are reusing work um

**[49:31]** okay these agents are reusing work um how can we give them like like

**[49:34]** how can we give them like like

**[49:34]** how can we give them like like general scripts that combine together

**[49:36]** general scripts that combine together

**[49:36]** general scripts that combine together the work that they've done how can we

**[49:37]** the work that they've done how can we

**[49:37]** the work that they've done how can we make them share it um I would generally

**[49:40]** make them share it um I would generally

**[49:40]** make them share it um I would generally think this is sort of like a tangent but

**[49:42]** think this is sort of like a tangent but

**[49:42]** think this is sort of like a tangent but on like agent communication frameworks I

**[49:46]** on like agent communication frameworks I

**[49:46]** on like agent communication frameworks I would say that like we probably don't

**[49:48]** would say that like we probably don't

**[49:48]** would say that like we probably don't need like a whole we don't I I think

**[49:51]** need like a whole we don't I I think

**[49:51]** need like a whole we don't I I think this is more of a personal opinion I

**[49:52]** this is more of a personal opinion I

**[49:52]** this is more of a personal opinion I think like we probably don't need to

**[49:54]** think like we probably don't need to

**[49:54]** think like we probably don't need to reinvent and uh like a new communication

**[49:56]** reinvent and uh like a new communication

**[49:56]** reinvent and uh like a new communication system. There are like the agents are

**[49:58]** system. There are like the agents are

**[49:58]** system. There are like the agents are good at using the things that we have


### [50:00 - 51:00]

**[50:00]** good at using the things that we have

**[50:00]** good at using the things that we have like HTTP requests and hash tools and

**[50:03]** like HTTP requests and hash tools and

**[50:03]** like HTTP requests and hash tools and API keys and uh named pipes and all of

**[50:06]** API keys and uh named pipes and all of

**[50:06]** API keys and uh named pipes and all of these things. And so like probably like

**[50:08]** these things. And so like probably like

**[50:08]** these things. And so like probably like the agents are just making HTTP requests

**[50:10]** the agents are just making HTTP requests

**[50:10]** the agents are just making HTTP requests back and forth from each other, you

**[50:12]** back and forth from each other, you

**[50:12]** back and forth from each other, you know, using HTTP server. Um there's a

**[50:15]** know, using HTTP server. Um there's a

**[50:15]** know, using HTTP server. Um there's a bunch of interesting work there. I've

**[50:16]** bunch of interesting work there. I've

**[50:16]** bunch of interesting work there. I've seen people make like a virtual forum

**[50:20]** seen people make like a virtual forum

**[50:20]** seen people make like a virtual forum for their agents to communicate and they

**[50:23]** for their agents to communicate and they

**[50:23]** for their agents to communicate and they like post topics and like reply and

**[50:26]** like post topics and like reply and

**[50:26]** like post topics and like reply and stuff like that. Um kind of cool. I

**[50:28]** stuff like that. Um kind of cool. I

**[50:28]** stuff like that. Um kind of cool. I think there's a lot of things to explore

**[50:30]** think there's a lot of things to explore

**[50:30]** think there's a lot of things to explore and discover there. Yeah. Okay. Um going

**[50:34]** and discover there. Yeah. Okay. Um going

**[50:34]** and discover there. Yeah. Okay. Um going to keep going a little bit. How are we

**[50:36]** to keep going a little bit. How are we

**[50:36]** to keep going a little bit. How are we doing for time? Okay. It's got an hour

**[50:38]** doing for time? Okay. It's got an hour

**[50:38]** doing for time? Okay. It's got an hour left, I think. Okay. Um

**[50:41]** left, I think. Okay. Um

**[50:41]** left, I think. Okay. Um cool. So, an example of designing an

**[50:44]** cool. So, an example of designing an

**[50:44]** cool. So, an example of designing an agent. Uh this is a like yeah let's this

**[50:48]** agent. Uh this is a like yeah let's this

**[50:48]** agent. Uh this is a like yeah let's this is not the prototyping session but I

**[50:49]** is not the prototyping session but I

**[50:49]** is not the prototyping session but I think this is like will be a good sort

**[50:50]** think this is like will be a good sort

**[50:50]** think this is like will be a good sort of like like lee way into it. Let's say

**[50:54]** of like like lee way into it. Let's say

**[50:54]** of like like lee way into it. Let's say we're making a spreadsheet agent. Uh

**[50:57]** we're making a spreadsheet agent. Uh

**[50:57]** we're making a spreadsheet agent. Uh what is the best way to search a

**[50:58]** what is the best way to search a

**[50:58]** what is the best way to search a spreadsheet? What's the best way to


### [51:00 - 52:00]

**[51:00]** spreadsheet? What's the best way to

**[51:00]** spreadsheet? What's the best way to execute code like or what's the best way

**[51:02]** execute code like or what's the best way

**[51:02]** execute code like or what's the best way to take action in a spreadsheet? What is

**[51:04]** to take action in a spreadsheet? What is

**[51:04]** to take action in a spreadsheet? What is the best way to link a spreadsheet?

**[51:06]** the best way to link a spreadsheet?

**[51:06]** the best way to link a spreadsheet? Right? These are all like really

**[51:07]** Right? These are all like really

**[51:07]** Right? These are all like really interesting things to do. Uh I'm going

**[51:09]** interesting things to do. Uh I'm going

**[51:09]** interesting things to do. Uh I'm going to do like a Figma and we can go over

**[51:11]** to do like a Figma and we can go over

**[51:11]** to do like a Figma and we can go over it. Um, if someone could grab a water as

**[51:14]** it. Um, if someone could grab a water as

**[51:14]** it. Um, if someone could grab a water as well, that'd be great. I like could

**[51:16]** well, that'd be great. I like could

**[51:16]** well, that'd be great. I like could really use water. I'm uh Yeah. Yeah.

**[51:18]** really use water. I'm uh Yeah. Yeah.

**[51:18]** really use water. I'm uh Yeah. Yeah. Okay. Um, thanks. Uh,

**[51:22]** Okay. Um, thanks. Uh,

**[51:22]** Okay. Um, thanks. Uh, okay. So, we're going to um

**[51:26]** okay. So, we're going to um

**[51:26]** okay. So, we're going to um Yeah, let's let's talk through it. Uh,

**[51:28]** Yeah, let's let's talk through it. Uh,

**[51:28]** Yeah, let's let's talk through it. Uh, or why don't you spend like a couple

**[51:30]** or why don't you spend like a couple

**[51:30]** or why don't you spend like a couple minutes yourselves thinking about this

**[51:31]** minutes yourselves thinking about this

**[51:31]** minutes yourselves thinking about this question? You have a spreadsheet agent.

**[51:34]** question? You have a spreadsheet agent.

**[51:34]** question? You have a spreadsheet agent. You want it to be able to search. You

**[51:36]** You want it to be able to search. You

**[51:36]** You want it to be able to search. You want to be able to like gather context,

**[51:38]** want to be able to like gather context,

**[51:38]** want to be able to like gather context, take action, verify its work. How would

**[51:40]** take action, verify its work. How would

**[51:40]** take action, verify its work. How would you think about it? Right? So like just

**[51:41]** you think about it? Right? So like just

**[51:42]** you think about it? Right? So like just spend some time thinking through that.

**[51:43]** spend some time thinking through that.

**[51:43]** spend some time thinking through that. Take some notes or something.


### [53:00 - 54:00]

**[53:00]** Okay. Is everyone get had a little bit

**[53:00]** Okay. Is everyone get had a little bit of time to think about this? Does anyone

**[53:01]** of time to think about this? Does anyone

**[53:01]** of time to think about this? Does anyone want more time or want to just dive into

**[53:03]** want more time or want to just dive into

**[53:03]** want more time or want to just dive into it? Okay. Uh, what's the best way for an

**[53:07]** it? Okay. Uh, what's the best way for an

**[53:07]** it? Okay. Uh, what's the best way for an agent to search a spreadsheet? Realizing

**[53:10]** agent to search a spreadsheet? Realizing

**[53:10]** agent to search a spreadsheet? Realizing I have to type with one hand now. Um,

**[53:14]** I have to type with one hand now. Um,

**[53:14]** I have to type with one hand now. Um, I should figure this out because I'm

**[53:16]** I should figure this out because I'm

**[53:16]** I should figure this out because I'm going to type later. Okay. Um, the Okay,

**[53:19]** going to type later. Okay. Um, the Okay,

**[53:19]** going to type later. Okay. Um, the Okay, searching a spreadsheet. Uh, any any

**[53:22]** searching a spreadsheet. Uh, any any

**[53:22]** searching a spreadsheet. Uh, any any ideas how do you search a spreadsheet?

**[53:23]** ideas how do you search a spreadsheet?

**[53:23]** ideas how do you search a spreadsheet? Like what would you do?

**[53:24]** Like what would you do?

**[53:24]** Like what would you do? >> CSV.

**[53:27]** >> CSV.

**[53:27]** >> CSV. >> Okay. You've got a CSV. Okay. And now

**[53:29]** >> Okay. You've got a CSV. Okay. And now

**[53:29]** >> Okay. You've got a CSV. Okay. And now like your agent wants to like search the

**[53:31]** like your agent wants to like search the

**[53:31]** like your agent wants to like search the CSV. What what does it do?

**[53:34]** CSV. What what does it do?

**[53:34]** CSV. What what does it do? >> A GP. Okay. Uh what does the GP look

**[53:37]** >> A GP. Okay. Uh what does the GP look

**[53:37]** >> A GP. Okay. Uh what does the GP look like?

**[53:38]** like?

**[53:38]** like? >> Needs to look at all the headers.

**[53:39]** >> Needs to look at all the headers.

**[53:39]** >> Needs to look at all the headers. >> Looks at the headers. Okay.

**[53:40]** >> Looks at the headers. Okay.

**[53:40]** >> Looks at the headers. Okay. >> Headers of all sheets.

**[53:43]** >> Headers of all sheets.

**[53:43]** >> Headers of all sheets. >> Okay. Great. Yeah. Yeah. And let's say

**[53:45]** >> Okay. Great. Yeah. Yeah. And let's say

**[53:45]** >> Okay. Great. Yeah. Yeah. And let's say I'm looking for the revenue in 2024 or

**[53:48]** I'm looking for the revenue in 2024 or

**[53:48]** I'm looking for the revenue in 2024 or something. Um

**[53:51]** something. Um

**[53:51]** something. Um now I've got my headers like uh I'm just

**[53:55]** now I've got my headers like uh I'm just

**[53:55]** now I've got my headers like uh I'm just going to pull up a spreadsheet, right?

**[53:57]** going to pull up a spreadsheet, right?

**[53:57]** going to pull up a spreadsheet, right? Um let's say that the revenue is in

**[53:59]** Um let's say that the revenue is in

**[53:59]** Um let's say that the revenue is in there's a revenue column and then


### [54:00 - 55:00]

**[54:02]** there's a revenue column and then

**[54:02]** there's a revenue column and then there's like a

**[54:05]** there's like a

**[54:05]** there's like a uh so yeah let's see

**[54:23]** okay so yeah let's say it's something

**[54:23]** okay so yeah let's say it's something like this right like um How do I get

**[54:27]** like this right like um How do I get

**[54:27]** like this right like um How do I get revenue in 2026? Right? So, this is sort

**[54:29]** revenue in 2026? Right? So, this is sort

**[54:29]** revenue in 2026? Right? So, this is sort of like a tabular problem, right? Like

**[54:32]** of like a tabular problem, right? Like

**[54:32]** of like a tabular problem, right? Like there is revenue here and there's also

**[54:34]** there is revenue here and there's also

**[54:34]** there is revenue here and there's also 2026 here, right? So, it's like a

**[54:36]** 2026 here, right? So, it's like a

**[54:36]** 2026 here, right? So, it's like a multi-dimensional step, right? We could

**[54:39]** multi-dimensional step, right? We could

**[54:39]** multi-dimensional step, right? We could look at the headers that will then give

**[54:40]** look at the headers that will then give

**[54:40]** look at the headers that will then give us uh like if you just pull this, you'll

**[54:43]** us uh like if you just pull this, you'll

**[54:44]** us uh like if you just pull this, you'll get 100, 200, 300, right? So, we need a

**[54:47]** get 100, 200, 300, right? So, we need a

**[54:48]** get 100, 200, 300, right? So, we need a little bit more. Uh any other ideas?

**[54:52]** little bit more. Uh any other ideas?

**[54:52]** little bit more. Uh any other ideas? >> Yeah,

**[54:52]** >> Yeah,

**[54:52]** >> Yeah, >> there's a bash tool for it. Uh, a AWK, I

**[54:56]** >> there's a bash tool for it. Uh, a AWK, I

**[54:56]** >> there's a bash tool for it. Uh, a AWK, I think.

**[54:56]** think.

**[54:56]** think. >> O. Okay. Yeah. Yeah. Yeah. And what

**[54:59]** >> O. Okay. Yeah. Yeah. Yeah. And what

**[54:59]** >> O. Okay. Yeah. Yeah. Yeah. And what would it A for?


### [55:00 - 56:00]

**[55:01]** would it A for?

**[55:01]** would it A for? >> Well, depends on what you what you're

**[55:03]** >> Well, depends on what you what you're

**[55:03]** >> Well, depends on what you what you're looking for.

**[55:03]** looking for.

**[55:03]** looking for. >> Yeah. Yeah. Yeah. That that's a

**[55:05]** >> Yeah. Yeah. Yeah. That that's a

**[55:05]** >> Yeah. Yeah. Yeah. That that's a question, right? Like what is the user

**[55:06]** question, right? Like what is the user

**[55:06]** question, right? Like what is the user looking for, right? They're probably

**[55:07]** looking for, right? They're probably

**[55:07]** looking for, right? They're probably looking for something like this, like

**[55:09]** looking for something like this, like

**[55:09]** looking for something like this, like revenue in 2026, right? Um,

**[55:11]** revenue in 2026, right? Um,

**[55:11]** revenue in 2026, right? Um, >> maybe use the APIs to use the Google

**[55:14]** >> maybe use the APIs to use the Google

**[55:14]** >> maybe use the APIs to use the Google tools to add all the numbers together or

**[55:17]** tools to add all the numbers together or

**[55:17]** tools to add all the numbers together or V look up something like this, right?

**[55:19]** V look up something like this, right?

**[55:19]** V look up something like this, right? >> Yeah. So the idea is like use the APIs

**[55:21]** >> Yeah. So the idea is like use the APIs

**[55:21]** >> Yeah. So the idea is like use the APIs like use the Google APIs to like look it

**[55:23]** like use the Google APIs to like look it

**[55:23]** like use the Google APIs to like look it up. Um that's great. Uh but yeah, let's

**[55:26]** up. Um that's great. Uh but yeah, let's

**[55:26]** up. Um that's great. Uh but yeah, let's say we're working locally. We need to

**[55:27]** say we're working locally. We need to

**[55:27]** say we're working locally. We need to sort of design these APIs. Yeah.

**[55:29]** sort of design these APIs. Yeah.

**[55:29]** sort of design these APIs. Yeah. >> SQLite ord

**[55:32]** >> SQLite ord

**[55:32]** >> SQLite ord CSV directly and work.

**[55:34]** CSV directly and work.

**[55:34]** CSV directly and work. >> Oh, interesting. Okay. Yeah, I didn't

**[55:35]** >> Oh, interesting. Okay. Yeah, I didn't

**[55:35]** >> Oh, interesting. Okay. Yeah, I didn't know that. That's great. So yeah, you

**[55:37]** know that. That's great. So yeah, you

**[55:37]** know that. That's great. So yeah, you you use SQLite to query a CSV. Um that's

**[55:40]** you use SQLite to query a CSV. Um that's

**[55:40]** you use SQLite to query a CSV. Um that's a great like sort of creative way of

**[55:42]** a great like sort of creative way of

**[55:42]** a great like sort of creative way of thinking about API interfaces, right?

**[55:45]** thinking about API interfaces, right?

**[55:45]** thinking about API interfaces, right? like um if you can translate something

**[55:47]** like um if you can translate something

**[55:47]** like um if you can translate something into a interface that the agent knows

**[55:50]** into a interface that the agent knows

**[55:50]** into a interface that the agent knows very well that's great right and so like

**[55:52]** very well that's great right and so like

**[55:52]** very well that's great right and so like if you have a data source if you can

**[55:54]** if you have a data source if you can

**[55:54]** if you have a data source if you can convert it into a SQL query then your

**[55:57]** convert it into a SQL query then your

**[55:57]** convert it into a SQL query then your agent really knows how to search SQL

**[55:59]** agent really knows how to search SQL

**[55:59]** agent really knows how to search SQL right so thinking about this


### [56:00 - 57:00]

**[56:00]** right so thinking about this

**[56:00]** right so thinking about this transformation step is really really

**[56:02]** transformation step is really really

**[56:02]** transformation step is really really interesting it's a great way of like

**[56:03]** interesting it's a great way of like

**[56:04]** interesting it's a great way of like designing like an agentic search

**[56:05]** designing like an agentic search

**[56:05]** designing like an agentic search interface so

**[56:07]** interface so

**[56:07]** interface so >> um yeah over there

**[56:08]** >> um yeah over there

**[56:08]** >> um yeah over there >> sorry real quick while we're talking

**[56:09]** >> sorry real quick while we're talking

**[56:09]** >> sorry real quick while we're talking about tools because you can use TSV for

**[56:10]** about tools because you can use TSV for

**[56:10]** about tools because you can use TSV for some of the stuff as well

**[56:12]** some of the stuff as well

**[56:12]** some of the stuff as well >> um is there any good ranking within the

**[56:14]** >> um is there any good ranking within the

**[56:14]** >> um is there any good ranking within the with Is Cloud smart enough to start

**[56:15]** with Is Cloud smart enough to start

**[56:15]** with Is Cloud smart enough to start ranking the right tool for the right

**[56:17]** ranking the right tool for the right

**[56:17]** ranking the right tool for the right job? Because that's kind of what we're

**[56:18]** job? Because that's kind of what we're

**[56:18]** job? Because that's kind of what we're talking about here is right tool for the

**[56:19]** talking about here is right tool for the

**[56:19]** talking about here is right tool for the right job.

**[56:20]** right job.

**[56:20]** right job. >> Yeah. Is Cloud smart enough to write

**[56:22]** >> Yeah. Is Cloud smart enough to write

**[56:22]** >> Yeah. Is Cloud smart enough to write rank the right cool tool for the right

**[56:23]** rank the right cool tool for the right

**[56:24]** rank the right cool tool for the right job? Uh yeah, if you prompt it, you

**[56:25]** job? Uh yeah, if you prompt it, you

**[56:25]** job? Uh yeah, if you prompt it, you know, like or like I I think that's one

**[56:27]** know, like or like I I think that's one

**[56:27]** know, like or like I I think that's one of those things where like I don't know,

**[56:28]** of those things where like I don't know,

**[56:28]** of those things where like I don't know, let's find out like let's read the

**[56:29]** let's find out like let's read the

**[56:29]** let's find out like let's read the transcript. Uh if it's not like how can

**[56:32]** transcript. Uh if it's not like how can

**[56:32]** transcript. Uh if it's not like how can you help it?

**[56:34]** you help it?

**[56:34]** you help it? >> Yeah. Just sort of like I I think all of

**[56:37]** >> Yeah. Just sort of like I I think all of

**[56:37]** >> Yeah. Just sort of like I I think all of these things are like an intuition, you

**[56:38]** these things are like an intuition, you

**[56:38]** these things are like an intuition, you know? It's like like kind of like riding

**[56:40]** know? It's like like kind of like riding

**[56:40]** know? It's like like kind of like riding a horse. Not that I've ever rode a

**[56:42]** a horse. Not that I've ever rode a

**[56:42]** a horse. Not that I've ever rode a horse, but I know just like I imagine

**[56:45]** horse, but I know just like I imagine

**[56:45]** horse, but I know just like I imagine it's like running.

**[56:50]** [laughter]

**[56:50]** [laughter] >> Yeah. Like you like, you know, you're

**[56:51]** >> Yeah. Like you like, you know, you're

**[56:51]** >> Yeah. Like you like, you know, you're sort of giving these signals to the

**[56:53]** sort of giving these signals to the

**[56:53]** sort of giving these signals to the horse. You're calming it down. You're

**[56:54]** horse. You're calming it down. You're

**[56:54]** horse. You're calming it down. You're trying to understand what it how how do

**[56:56]** trying to understand what it how how do

**[56:56]** trying to understand what it how how do you push it faster? You know what I

**[56:58]** you push it faster? You know what I

**[56:58]** you push it faster? You know what I mean? And sort of like it's a very


### [57:00 - 58:00]

**[57:00]** mean? And sort of like it's a very

**[57:00]** mean? And sort of like it's a very organic like thing, right? Um like I

**[57:04]** organic like thing, right? Um like I

**[57:04]** organic like thing, right? Um like I think we like to say that models are

**[57:06]** think we like to say that models are

**[57:06]** think we like to say that models are grown and not designed, right? And so

**[57:08]** grown and not designed, right? And so

**[57:08]** grown and not designed, right? And so we're like sort of understanding their

**[57:09]** we're like sort of understanding their

**[57:09]** we're like sort of understanding their capabilities. Yeah. Uh yeah what and

**[57:12]** capabilities. Yeah. Uh yeah what and

**[57:12]** capabilities. Yeah. Uh yeah what and where it is. Yeah

**[57:13]** where it is. Yeah

**[57:13]** where it is. Yeah >> quick question. So is a way to add like

**[57:15]** >> quick question. So is a way to add like

**[57:15]** >> quick question. So is a way to add like metadata to the spreadsheet? Can you

**[57:16]** metadata to the spreadsheet? Can you

**[57:16]** metadata to the spreadsheet? Can you give descriptions in a different

**[57:17]** give descriptions in a different

**[57:18]** give descriptions in a different document?

**[57:18]** document?

**[57:18]** document? >> Yeah that's for example KPI

**[57:25]** to build intelligence to ask questions.

**[57:25]** to build intelligence to ask questions. >> Yeah. So that's another great pattern is

**[57:27]** >> Yeah. So that's another great pattern is

**[57:27]** >> Yeah. So that's another great pattern is like okay can you add metadata to a

**[57:29]** like okay can you add metadata to a

**[57:29]** like okay can you add metadata to a spreadsheet? So these are some questions

**[57:31]** spreadsheet? So these are some questions

**[57:31]** spreadsheet? So these are some questions that you might want to think about

**[57:32]** that you might want to think about

**[57:32]** that you might want to think about before like when you're thinking about

**[57:35]** before like when you're thinking about

**[57:35]** before like when you're thinking about search is like what pre-processing can

**[57:37]** search is like what pre-processing can

**[57:37]** search is like what pre-processing can you do to make the search better, right?

**[57:39]** you do to make the search better, right?

**[57:39]** you do to make the search better, right? And so one example is that you translate

**[57:41]** And so one example is that you translate

**[57:42]** And so one example is that you translate it into like a SQL format or something

**[57:44]** it into like a SQL format or something

**[57:44]** it into like a SQL format or something where you use something that can query

**[57:45]** where you use something that can query

**[57:45]** where you use something that can query it, right? That's like a translation

**[57:47]** it, right? That's like a translation

**[57:47]** it, right? That's like a translation step. Another step is like maybe you

**[57:49]** step. Another step is like maybe you

**[57:49]** step. Another step is like maybe you have a tool or um like a a

**[57:52]** have a tool or um like a a

**[57:52]** have a tool or um like a a pre-processing step where another agent

**[57:55]** pre-processing step where another agent

**[57:55]** pre-processing step where another agent annotates the the spreadsheet and and

**[57:57]** annotates the the spreadsheet and and

**[57:57]** annotates the the spreadsheet and and like adds information so that the agent

**[57:59]** like adds information so that the agent

**[57:59]** like adds information so that the agent can then like search across that


### [58:00 - 59:00]

**[58:01]** can then like search across that

**[58:01]** can then like search across that information better. Right. So um yeah,

**[58:04]** information better. Right. So um yeah,

**[58:04]** information better. Right. So um yeah, one more. Um, I was just curious what I

**[58:07]** one more. Um, I was just curious what I

**[58:07]** one more. Um, I was just curious what I mean all those tools sound great, but

**[58:09]** mean all those tools sound great, but

**[58:09]** mean all those tools sound great, but yeah, why can't the agent just,

**[58:11]** yeah, why can't the agent just,

**[58:11]** yeah, why can't the agent just, >> you know, do what was suggested, read

**[58:12]** >> you know, do what was suggested, read

**[58:12]** >> you know, do what was suggested, read the header and then just get the date?

**[58:15]** the header and then just get the date?

**[58:15]** the header and then just get the date? Like I feel like that should pretty

**[58:17]** Like I feel like that should pretty

**[58:17]** Like I feel like that should pretty trivial

**[58:20]** trivial

**[58:20]** trivial or retest.

**[58:21]** or retest.

**[58:21]** or retest. >> Yeah, probably I should have like

**[58:22]** >> Yeah, probably I should have like

**[58:22]** >> Yeah, probably I should have like prepared this in code. But yeah, I I

**[58:25]** prepared this in code. But yeah, I I

**[58:26]** prepared this in code. But yeah, I I built a ton of spreadsheet agents

**[58:27]** built a ton of spreadsheet agents

**[58:27]** built a ton of spreadsheet agents before. Basically, it's

**[58:28]** before. Basically, it's

**[58:28]** before. Basically, it's >> not it's kind of hard to do. Yeah. Yeah.

**[58:30]** >> not it's kind of hard to do. Yeah. Yeah.

**[58:30]** >> not it's kind of hard to do. Yeah. Yeah. So, um, basically what what I would

**[58:33]** So, um, basically what what I would

**[58:33]** So, um, basically what what I would think about is like, so we we've got

**[58:35]** think about is like, so we we've got

**[58:35]** think about is like, so we we've got like Okay, I

**[58:37]** like Okay, I

**[58:38]** like Okay, I Sean, do you have suggestions on how it

**[58:39]** Sean, do you have suggestions on how it

**[58:39]** Sean, do you have suggestions on how it can talk and code at the same time? Go

**[58:42]** can talk and code at the same time? Go

**[58:42]** can talk and code at the same time? Go ahead.

**[58:45]** ahead.

**[58:45]** ahead. >> Oh, I see. Yeah.

**[58:46]** >> Oh, I see. Yeah.

**[58:46]** >> Oh, I see. Yeah. >> Do you work at Whisper Flow or something

**[58:48]** >> Do you work at Whisper Flow or something

**[58:48]** >> Do you work at Whisper Flow or something or

**[58:50]** or

**[58:50]** or >> Stick the mic in your shirt?

**[58:51]** >> Stick the mic in your shirt?

**[58:51]** >> Stick the mic in your shirt? >> There's a microphone button. [laughter]

**[58:54]** >> There's a microphone button. [laughter]

**[58:54]** >> There's a microphone button. [laughter] >> There's a microphone button on the bat.

**[58:56]** >> There's a microphone button on the bat.

**[58:56]** >> There's a microphone button on the bat. >> Stick the mic in your shirt.

**[58:59]** >> Stick the mic in your shirt.

**[58:59]** >> Stick the mic in your shirt. Oh, I I I just don't trust that stuff,


### [59:00 - 01:00:00]

**[59:01]** Oh, I I I just don't trust that stuff,

**[59:01]** Oh, I I I just don't trust that stuff, man. Okay. Um,

**[59:04]** man. Okay. Um,

**[59:04]** man. Okay. Um, [laughter]

**[59:05]** [laughter]

**[59:05]** [laughter] maybe I shouldn't be working in an AI

**[59:07]** maybe I shouldn't be working in an AI

**[59:07]** maybe I shouldn't be working in an AI lab. Um, okay. So,

**[59:11]** lab. Um, okay. So,

**[59:11]** lab. Um, okay. So, uh, let's see.

**[59:19]** >> Hold on. Hold on. Um,

**[59:19]** >> Hold on. Hold on. Um, search. So,

**[59:22]** search. So,

**[59:22]** search. So, >> one way to do it is like

**[59:25]** >> one way to do it is like

**[59:25]** >> one way to do it is like you see in spreadsheets, right? Like you

**[59:27]** you see in spreadsheets, right? Like you

**[59:27]** you see in spreadsheets, right? Like you can say here you can design formulas

**[59:30]** can say here you can design formulas

**[59:30]** can say here you can design formulas right so like B3

**[59:32]** right so like B3

**[59:32]** right so like B3 2

**[59:42]** right so this is a syntax for example

**[59:42]** right so this is a syntax for example that the agent's pretty familiar with

**[59:43]** that the agent's pretty familiar with

**[59:43]** that the agent's pretty familiar with like B3 to B5 right and so you can

**[59:46]** like B3 to B5 right and so you can

**[59:46]** like B3 to B5 right and so you can design an agentic search interface which

**[59:47]** design an agentic search interface which

**[59:47]** design an agentic search interface which is like this right like B3

**[59:51]** is like this right like B3

**[59:51]** is like this right like B3 B5 or something right so like your

**[59:53]** B5 or something right so like your

**[59:53]** B5 or something right so like your agentic search interface can take in a

**[59:55]** agentic search interface can take in a

**[59:55]** agentic search interface can take in a range right it can taking a range

**[59:57]** range right it can taking a range

**[59:57]** range right it can taking a range string, right? And these are things that

**[59:59]** string, right? And these are things that

**[59:59]** string, right? And these are things that like the agent knows pretty well, right?


### [01:00:00 - 01:01:00]

**[01:00:01]** like the agent knows pretty well, right?

**[01:00:01]** like the agent knows pretty well, right? Like you can um do SQL queries, right?

**[01:00:05]** Like you can um do SQL queries, right?

**[01:00:05]** Like you can um do SQL queries, right? Agent knows SQL queries pretty well,

**[01:00:07]** Agent knows SQL queries pretty well,

**[01:00:07]** Agent knows SQL queries pretty well, right? Um and uh like these you can also

**[01:00:13]** right? Um and uh like these you can also

**[01:00:13]** right? Um and uh like these you can also uh do XML, right? Sorry, the font is so

**[01:00:17]** uh do XML, right? Sorry, the font is so

**[01:00:17]** uh do XML, right? Sorry, the font is so small. Um

**[01:00:20]** small. Um

**[01:00:20]** small. Um okay. Uh yeah, you can also do XML.

**[01:00:24]** okay. Uh yeah, you can also do XML.

**[01:00:24]** okay. Uh yeah, you can also do XML. I'm not sure if you guys know but like

**[01:00:26]** I'm not sure if you guys know but like

**[01:00:26]** I'm not sure if you guys know but like uh XLX files are XML in the back end

**[01:00:29]** uh XLX files are XML in the back end

**[01:00:29]** uh XLX files are XML in the back end right and XML is very structured uh you

**[01:00:31]** right and XML is very structured uh you

**[01:00:31]** right and XML is very structured uh you can do like an XML search query uh and

**[01:00:34]** can do like an XML search query uh and

**[01:00:34]** can do like an XML search query uh and there are different libraries that can

**[01:00:35]** there are different libraries that can

**[01:00:35]** there are different libraries that can do that so that's one example right is

**[01:00:37]** do that so that's one example right is

**[01:00:37]** do that so that's one example right is like how do you search and gather

**[01:00:39]** like how do you search and gather

**[01:00:39]** like how do you search and gather context and I hope this sort of like

**[01:00:41]** context and I hope this sort of like

**[01:00:41]** context and I hope this sort of like illustrates to you that like gathering

**[01:00:42]** illustrates to you that like gathering

**[01:00:42]** illustrates to you that like gathering context is really really creative right

**[01:00:44]** context is really really creative right

**[01:00:44]** context is really really creative right like and and like there's so many

**[01:00:46]** like and and like there's so many

**[01:00:46]** like and and like there's so many iterations and if you just if you've

**[01:00:48]** iterations and if you just if you've

**[01:00:48]** iterations and if you just if you've only tried one iteration it's probably

**[01:00:50]** only tried one iteration it's probably

**[01:00:50]** only tried one iteration it's probably not enough right like think about like

**[01:00:52]** not enough right like think about like

**[01:00:52]** not enough right like think about like as many different ways as you can like

**[01:00:54]** as many different ways as you can like

**[01:00:54]** as many different ways as you can like try these out, right? Like try SQL, try

**[01:00:56]** try these out, right? Like try SQL, try

**[01:00:56]** try these out, right? Like try SQL, try try the CER, try try the GP and O and

**[01:00:59]** try the CER, try try the GP and O and

**[01:00:59]** try the CER, try try the GP and O and like all of these things and um have a


### [01:01:00 - 01:02:00]

**[01:01:01]** like all of these things and um have a

**[01:01:02]** like all of these things and um have a few tests that you're trying across

**[01:01:03]** few tests that you're trying across

**[01:01:03]** few tests that you're trying across different things and and see what the

**[01:01:04]** different things and and see what the

**[01:01:04]** different things and and see what the agent likes and what it what it doesn't

**[01:01:06]** agent likes and what it what it doesn't

**[01:01:06]** agent likes and what it what it doesn't like. Um it's going to be different for

**[01:01:08]** like. Um it's going to be different for

**[01:01:08]** like. Um it's going to be different for each case.

**[01:01:08]** each case.

**[01:01:08]** each case. >> Sorry.

**[01:01:10]** >> Sorry.

**[01:01:10]** >> Sorry. When you say agent, you're referring to

**[01:01:14]** When you say agent, you're referring to

**[01:01:14]** When you say agent, you're referring to the the model or because we're building

**[01:01:16]** the the model or because we're building

**[01:01:16]** the the model or because we're building an agent here.

**[01:01:18]** an agent here.

**[01:01:18]** an agent here. >> Yeah. and you're relying on already free

**[01:01:21]** >> Yeah. and you're relying on already free

**[01:01:21]** >> Yeah. and you're relying on already free existing knowledge of how to handle XML

**[01:01:23]** existing knowledge of how to handle XML

**[01:01:23]** existing knowledge of how to handle XML who's who's doing that the model.

**[01:01:26]** who's who's doing that the model.

**[01:01:26]** who's who's doing that the model. >> Yeah, because the question is like who

**[01:01:28]** >> Yeah, because the question is like who

**[01:01:28]** >> Yeah, because the question is like who uh where is the knowledge come from? Is

**[01:01:29]** uh where is the knowledge come from? Is

**[01:01:30]** uh where is the knowledge come from? Is it the model? Is it like what is what do

**[01:01:31]** it the model? Is it like what is what do

**[01:01:31]** it the model? Is it like what is what do I mean by the agent? Yeah, generally I

**[01:01:34]** I mean by the agent? Yeah, generally I

**[01:01:34]** I mean by the agent? Yeah, generally I think what you're looking for is like

**[01:01:35]** think what you're looking for is like

**[01:01:35]** think what you're looking for is like you have a problem you want to make it

**[01:01:37]** you have a problem you want to make it

**[01:01:37]** you have a problem you want to make it as indistribution as possible for the

**[01:01:40]** as indistribution as possible for the

**[01:01:40]** as indistribution as possible for the agent, right? And so the agent knows a

**[01:01:42]** agent, right? And so the agent knows a

**[01:01:42]** agent, right? And so the agent knows a lot about a lot of different things. It

**[01:01:44]** lot about a lot of different things. It

**[01:01:44]** lot about a lot of different things. It knows a lot about for example finance,

**[01:01:46]** knows a lot about for example finance,

**[01:01:46]** knows a lot about for example finance, right? So if you ask it to make a DCF

**[01:01:48]** right? So if you ask it to make a DCF

**[01:01:48]** right? So if you ask it to make a DCF model, it knows what DCF is, right? And

**[01:01:51]** model, it knows what DCF is, right? And

**[01:01:51]** model, it knows what DCF is, right? And you can if if you want to give it more

**[01:01:53]** you can if if you want to give it more

**[01:01:53]** you can if if you want to give it more information, you can make a skill,

**[01:01:55]** information, you can make a skill,

**[01:01:55]** information, you can make a skill, right? But so it knows what DCF is. It

**[01:01:57]** right? But so it knows what DCF is. It

**[01:01:57]** right? But so it knows what DCF is. It knows what SQL is. Can it combine those

**[01:01:59]** knows what SQL is. Can it combine those

**[01:01:59]** knows what SQL is. Can it combine those things together, right? And so like uh


### [01:02:00 - 01:03:00]

**[01:02:02]** things together, right? And so like uh

**[01:02:02]** things together, right? And so like uh ideally you want to like your your

**[01:02:05]** ideally you want to like your your

**[01:02:05]** ideally you want to like your your problem is going to be out of

**[01:02:06]** problem is going to be out of

**[01:02:06]** problem is going to be out of distribution in some way, right? like

**[01:02:08]** distribution in some way, right? like

**[01:02:08]** distribution in some way, right? like like there's some like information

**[01:02:10]** like there's some like information

**[01:02:10]** like there's some like information that's not on the internet or something

**[01:02:11]** that's not on the internet or something

**[01:02:11]** that's not on the internet or something that you have um or something somewhat

**[01:02:14]** that you have um or something somewhat

**[01:02:14]** that you have um or something somewhat unique to you and you want to try and

**[01:02:16]** unique to you and you want to try and

**[01:02:16]** unique to you and you want to try and like massage it to be as in distribution

**[01:02:18]** like massage it to be as in distribution

**[01:02:18]** like massage it to be as in distribution as possible. Um and uh yeah it's it's

**[01:02:21]** as possible. Um and uh yeah it's it's

**[01:02:21]** as possible. Um and uh yeah it's it's very very creative I think like uh you

**[01:02:24]** very very creative I think like uh you

**[01:02:24]** very very creative I think like uh you know it's not like a it's not a science

**[01:02:27]** know it's not like a it's not a science

**[01:02:27]** know it's not like a it's not a science to be [laughter] very much like an art.

**[01:02:31]** to be [laughter] very much like an art.

**[01:02:31]** to be [laughter] very much like an art. So, um, yeah. Okay. So, we we've tried

**[01:02:35]** So, um, yeah. Okay. So, we we've tried

**[01:02:35]** So, um, yeah. Okay. So, we we've tried gathering context, then taking action.

**[01:02:38]** gathering context, then taking action.

**[01:02:38]** gathering context, then taking action. Um, we can probably do a lot of the same

**[01:02:40]** Um, we can probably do a lot of the same

**[01:02:40]** Um, we can probably do a lot of the same stuff here that we've done before,

**[01:02:42]** stuff here that we've done before,

**[01:02:42]** stuff here that we've done before, right? Like we can do like insert

**[01:02:46]** right? Like we can do like insert

**[01:02:46]** right? Like we can do like insert 2D array, right? Um, if we've got like a

**[01:02:52]** 2D array, right? Um, if we've got like a

**[01:02:52]** 2D array, right? Um, if we've got like a SQL interface, right, we can um we can

**[01:02:56]** SQL interface, right, we can um we can

**[01:02:56]** SQL interface, right, we can um we can do a SQL query, we can edit XML. Um,

**[01:02:59]** do a SQL query, we can edit XML. Um,

**[01:02:59]** do a SQL query, we can edit XML. Um, these are like often very similar,


### [01:03:00 - 01:04:00]

**[01:03:01]** these are like often very similar,

**[01:03:01]** these are like often very similar, right? Like taking action and gathering

**[01:03:03]** right? Like taking action and gathering

**[01:03:03]** right? Like taking action and gathering context that that you probably want a

**[01:03:04]** context that that you probably want a

**[01:03:04]** context that that you probably want a similar API back and forth. And then the

**[01:03:06]** similar API back and forth. And then the

**[01:03:06]** similar API back and forth. And then the last thing is verifying work, right?

**[01:03:08]** last thing is verifying work, right?

**[01:03:08]** last thing is verifying work, right? Like how do you think about how do you

**[01:03:10]** Like how do you think about how do you

**[01:03:10]** Like how do you think about how do you think about that? Um, check

**[01:03:14]** think about that? Um, check

**[01:03:14]** think about that? Um, check for null pointers, right, is one of the

**[01:03:17]** for null pointers, right, is one of the

**[01:03:17]** for null pointers, right, is one of the ways to do it. Um, any other ideas on on

**[01:03:21]** ways to do it. Um, any other ideas on on

**[01:03:21]** ways to do it. Um, any other ideas on on verification or Yeah.

**[01:03:23]** verification or Yeah.

**[01:03:23]** verification or Yeah. >> Sorry, I'm I'm a bit confused if you say

**[01:03:27]** >> Sorry, I'm I'm a bit confused if you say

**[01:03:27]** >> Sorry, I'm I'm a bit confused if you say >> like when when you're using other SDKs

**[01:03:30]** >> like when when you're using other SDKs

**[01:03:30]** >> like when when you're using other SDKs to build Asian, I don't need to tell it

**[01:03:32]** to build Asian, I don't need to tell it

**[01:03:32]** to build Asian, I don't need to tell it how it should gather the context.

**[01:03:34]** how it should gather the context.

**[01:03:34]** how it should gather the context. >> Sure.

**[01:03:35]** >> Sure.

**[01:03:35]** >> Sure. >> I just give it the context and explain

**[01:03:37]** >> I just give it the context and explain

**[01:03:37]** >> I just give it the context and explain this is what like basically I explain in

**[01:03:39]** this is what like basically I explain in

**[01:03:39]** this is what like basically I explain in plain English

**[01:03:40]** plain English

**[01:03:40]** plain English >> what is meant to do.

**[01:03:41]** >> what is meant to do.

**[01:03:41]** >> what is meant to do. >> Yeah.

**[01:03:42]** >> Yeah.

**[01:03:42]** >> Yeah. >> And what I tend to do and you tell me if

**[01:03:45]** >> And what I tend to do and you tell me if

**[01:03:46]** >> And what I tend to do and you tell me if I'm wrong, I actually end up creating a

**[01:03:47]** I'm wrong, I actually end up creating a

**[01:03:47]** I'm wrong, I actually end up creating a separate agent for QA.

**[01:03:49]** separate agent for QA.

**[01:03:50]** separate agent for QA. >> Oh, interesting.

**[01:03:51]** >> Oh, interesting.

**[01:03:51]** >> Oh, interesting. >> To to verify because I don't trust the

**[01:03:53]** >> To to verify because I don't trust the

**[01:03:53]** >> To to verify because I don't trust the agent to verify itself.

**[01:03:56]** agent to verify itself.

**[01:03:56]** agent to verify itself. But I'm just I'm I'm just a bit I

**[01:03:59]** But I'm just I'm I'm just a bit I

**[01:03:59]** But I'm just I'm I'm just a bit I confused about the level of detail I


### [01:04:00 - 01:05:00]

**[01:04:01]** confused about the level of detail I

**[01:04:01]** confused about the level of detail I need to provide the agent in that

**[01:04:02]** need to provide the agent in that

**[01:04:02]** need to provide the agent in that example.

**[01:04:03]** example.

**[01:04:03]** example. >> Yeah. Okay. So the question is about um

**[01:04:06]** >> Yeah. Okay. So the question is about um

**[01:04:06]** >> Yeah. Okay. So the question is about um giving context to the agent versus

**[01:04:08]** giving context to the agent versus

**[01:04:08]** giving context to the agent versus having it gather its own context. Uh you

**[01:04:11]** having it gather its own context. Uh you

**[01:04:11]** having it gather its own context. Uh you mentioned that you sometimes use a Q&A

**[01:04:13]** mentioned that you sometimes use a Q&A

**[01:04:13]** mentioned that you sometimes use a Q&A agent. Uh can I ask like what like

**[01:04:16]** agent. Uh can I ask like what like

**[01:04:16]** agent. Uh can I ask like what like domain you you're building your agent in

**[01:04:18]** domain you you're building your agent in

**[01:04:18]** domain you you're building your agent in or

**[01:04:19]** or

**[01:04:19]** or >> in uh cyber security.

**[01:04:21]** >> in uh cyber security.

**[01:04:21]** >> in uh cyber security. >> Okay. Sure. Yeah. Yeah. Um, I think that

**[01:04:26]** >> Okay. Sure. Yeah. Yeah. Um, I think that

**[01:04:26]** >> Okay. Sure. Yeah. Yeah. Um, I think that I I think I need to like look into more

**[01:04:29]** I I think I need to like look into more

**[01:04:29]** I I think I need to like look into more specifics, but the cloud agent SDK is

**[01:04:31]** specifics, but the cloud agent SDK is

**[01:04:31]** specifics, but the cloud agent SDK is great for cyber security and like I

**[01:04:33]** great for cyber security and like I

**[01:04:33]** great for cyber security and like I would generally push people on like let

**[01:04:35]** would generally push people on like let

**[01:04:35]** would generally push people on like let the agent gather context as much as

**[01:04:38]** the agent gather context as much as

**[01:04:38]** the agent gather context as much as possible, you know, like let it find its

**[01:04:40]** possible, you know, like let it find its

**[01:04:40]** possible, you know, like let it find its own work as much as possible. Um, you're

**[01:04:43]** own work as much as possible. Um, you're

**[01:04:43]** own work as much as possible. Um, you're trying to give it the tools to find its

**[01:04:45]** trying to give it the tools to find its

**[01:04:45]** trying to give it the tools to find its own work. The way I think about this is

**[01:04:47]** own work. The way I think about this is

**[01:04:47]** own work. The way I think about this is kind of like let's say that someone

**[01:04:49]** kind of like let's say that someone

**[01:04:49]** kind of like let's say that someone locked you in a room and they were they

**[01:04:51]** locked you in a room and they were they

**[01:04:51]** locked you in a room and they were they were like giving you tasks, you know,

**[01:04:53]** were like giving you tasks, you know,

**[01:04:53]** were like giving you tasks, you know, like that's your what your job was like

**[01:04:55]** like that's your what your job was like

**[01:04:55]** like that's your what your job was like a Mr. Beast sort of like scenario,

**[01:04:57]** a Mr. Beast sort of like scenario,

**[01:04:57]** a Mr. Beast sort of like scenario, right? Like you get $500,000 if you stay


### [01:05:00 - 01:06:00]

**[01:05:00]** right? Like you get $500,000 if you stay

**[01:05:00]** right? Like you get $500,000 if you stay in this room for 6 months. Um then like

**[01:05:03]** in this room for 6 months. Um then like

**[01:05:03]** in this room for 6 months. Um then like like someone's giving you a message,

**[01:05:05]** like someone's giving you a message,

**[01:05:05]** like someone's giving you a message, what tools would you want to be able to

**[01:05:07]** what tools would you want to be able to

**[01:05:07]** what tools would you want to be able to do it, right? Like would you just want

**[01:05:09]** do it, right? Like would you just want

**[01:05:09]** do it, right? Like would you just want like a list of papers or like would you

**[01:05:13]** like a list of papers or like would you

**[01:05:13]** like a list of papers or like would you want a calculator or like a computer?

**[01:05:15]** want a calculator or like a computer?

**[01:05:15]** want a calculator or like a computer? Right? Probably I would want a computer,

**[01:05:17]** Right? Probably I would want a computer,

**[01:05:17]** Right? Probably I would want a computer, right? I'd want Google. I'd want like

**[01:05:18]** right? I'd want Google. I'd want like

**[01:05:18]** right? I'd want Google. I'd want like all of these things, right? And so like

**[01:05:21]** all of these things, right? And so like

**[01:05:21]** all of these things, right? And so like I wouldn't want the person to send me

**[01:05:22]** I wouldn't want the person to send me

**[01:05:22]** I wouldn't want the person to send me like a stack of papers being like, "Hey,

**[01:05:24]** like a stack of papers being like, "Hey,

**[01:05:24]** like a stack of papers being like, "Hey, this is probably all the information you

**[01:05:25]** this is probably all the information you

**[01:05:26]** this is probably all the information you need." I'd rather just be like, "Hey,

**[01:05:27]** need." I'd rather just be like, "Hey,

**[01:05:27]** need." I'd rather just be like, "Hey, just give me a computer. Give me the

**[01:05:29]** just give me a computer. Give me the

**[01:05:29]** just give me a computer. Give me the problem. Let me search it and figure it

**[01:05:31]** problem. Let me search it and figure it

**[01:05:31]** problem. Let me search it and figure it out." Right? And so that's how I think

**[01:05:32]** out." Right? And so that's how I think

**[01:05:32]** out." Right? And so that's how I think about agents as well. like they need

**[01:05:35]** about agents as well. like they need

**[01:05:35]** about agents as well. like they need like like you know they're stuck in a

**[01:05:37]** like like you know they're stuck in a

**[01:05:37]** like like you know they're stuck in a room.

**[01:05:37]** room.

**[01:05:37]** room. >> So I need to give them tools. So if you

**[01:05:39]** >> So I need to give them tools. So if you

**[01:05:39]** >> So I need to give them tools. So if you can go back to the slides you have to

**[01:05:41]** can go back to the slides you have to

**[01:05:41]** can go back to the slides you have to the graph you had

**[01:05:44]** the graph you had

**[01:05:44]** the graph you had >> to the graph like this or

**[01:05:46]** >> to the graph like this or

**[01:05:46]** >> to the graph like this or >> yeah the so basically that gathering

**[01:05:48]** >> yeah the so basically that gathering

**[01:05:48]** >> yeah the so basically that gathering context is basically these are the tools

**[01:05:51]** context is basically these are the tools

**[01:05:51]** context is basically these are the tools I'm offering it.

**[01:05:52]** I'm offering it.

**[01:05:52]** I'm offering it. >> Yeah. Exactly. Yeah. You're I'm giving

**[01:05:54]** >> Yeah. Exactly. Yeah. You're I'm giving

**[01:05:54]** >> Yeah. Exactly. Yeah. You're I'm giving it like maybe an API for code

**[01:05:57]** it like maybe an API for code

**[01:05:57]** it like maybe an API for code generation. Maybe I'm giving it a SQL

**[01:05:58]** generation. Maybe I'm giving it a SQL

**[01:05:58]** generation. Maybe I'm giving it a SQL tool. Maybe I'm giving a bash. These are


### [01:06:00 - 01:07:00]

**[01:06:01]** tool. Maybe I'm giving a bash. These are

**[01:06:01]** tool. Maybe I'm giving a bash. These are all like examples, right? So yeah, you

**[01:06:03]** all like examples, right? So yeah, you

**[01:06:04]** all like examples, right? So yeah, you have one more question

**[01:06:04]** have one more question

**[01:06:04]** have one more question >> question. So for all the agents that

**[01:06:06]** >> question. So for all the agents that

**[01:06:06]** >> question. So for all the agents that you're [clears throat] having,

**[01:06:09]** you're [clears throat] having,

**[01:06:09]** you're [clears throat] having, do they share the same context window?

**[01:06:13]** do they share the same context window?

**[01:06:13]** do they share the same context window? >> Interesting. Yeah. So do agents share

**[01:06:15]** >> Interesting. Yeah. So do agents share

**[01:06:15]** >> Interesting. Yeah. So do agents share the context window? I think I think this

**[01:06:16]** the context window? I think I think this

**[01:06:16]** the context window? I think I think this is like an interesting question just

**[01:06:18]** is like an interesting question just

**[01:06:18]** is like an interesting question just overall about how you manage context. Um

**[01:06:20]** overall about how you manage context. Um

**[01:06:20]** overall about how you manage context. Um I think and I haven't talked about this

**[01:06:22]** I think and I haven't talked about this

**[01:06:22]** I think and I haven't talked about this too much yet, but sub agents are like a

**[01:06:24]** too much yet, but sub agents are like a

**[01:06:24]** too much yet, but sub agents are like a very very important way of managing

**[01:06:27]** very very important way of managing

**[01:06:27]** very very important way of managing context. Um, I think that this is like

**[01:06:30]** context. Um, I think that this is like

**[01:06:30]** context. Um, I think that this is like we're using more and more sub agents

**[01:06:33]** we're using more and more sub agents

**[01:06:33]** we're using more and more sub agents inside of cloud code and I would think

**[01:06:35]** inside of cloud code and I would think

**[01:06:35]** inside of cloud code and I would think about like doing sub agents very

**[01:06:38]** about like doing sub agents very

**[01:06:38]** about like doing sub agents very generally. So like what we might do for

**[01:06:40]** generally. So like what we might do for

**[01:06:40]** generally. So like what we might do for the spreadsheet agent is maybe we have a

**[01:06:42]** the spreadsheet agent is maybe we have a

**[01:06:42]** the spreadsheet agent is maybe we have a search sub agent, right? So like sub

**[01:06:45]** search sub agent, right? So like sub

**[01:06:45]** search sub agent, right? So like sub aents are great for when you need to do

**[01:06:47]** aents are great for when you need to do

**[01:06:47]** aents are great for when you need to do a lot of work and return an answer to

**[01:06:49]** a lot of work and return an answer to

**[01:06:49]** a lot of work and return an answer to the main agent. So for search, let's say

**[01:06:52]** the main agent. So for search, let's say

**[01:06:52]** the main agent. So for search, let's say the question is like how do I find my

**[01:06:53]** the question is like how do I find my

**[01:06:53]** the question is like how do I find my revenue in 2026? Maybe you need to do a

**[01:06:56]** revenue in 2026? Maybe you need to do a

**[01:06:56]** revenue in 2026? Maybe you need to do a bunch of results. Maybe you need to like

**[01:06:58]** bunch of results. Maybe you need to like

**[01:06:58]** bunch of results. Maybe you need to like uh search the internet, maybe you need

**[01:06:59]** uh search the internet, maybe you need


### [01:07:00 - 01:08:00]

**[01:07:00]** uh search the internet, maybe you need to search the spreadsheet, things like

**[01:07:01]** to search the spreadsheet, things like

**[01:07:01]** to search the spreadsheet, things like that. And there's a bunch of things that

**[01:07:03]** that. And there's a bunch of things that

**[01:07:03]** that. And there's a bunch of things that don't need to go into the context of the

**[01:07:05]** don't need to go into the context of the

**[01:07:05]** don't need to go into the context of the main agent. The main agent just needs to

**[01:07:06]** main agent. The main agent just needs to

**[01:07:06]** main agent. The main agent just needs to see the follow result, right? And so

**[01:07:09]** see the follow result, right? And so

**[01:07:09]** see the follow result, right? And so that's a great sub agent task. Um I

**[01:07:12]** that's a great sub agent task. Um I

**[01:07:12]** that's a great sub agent task. Um I don't have a dedicated sub aent slide

**[01:07:14]** don't have a dedicated sub aent slide

**[01:07:14]** don't have a dedicated sub aent slide here, but like yeah, they're very very

**[01:07:16]** here, but like yeah, they're very very

**[01:07:16]** here, but like yeah, they're very very useful and I I think a great way to

**[01:07:17]** useful and I I think a great way to

**[01:07:17]** useful and I I think a great way to think about things. Um yeah,

**[01:07:20]** think about things. Um yeah,

**[01:07:20]** think about things. Um yeah, >> and just to just to build on that

**[01:07:22]** >> and just to just to build on that

**[01:07:22]** >> and just to just to build on that question actually

**[01:07:23]** question actually

**[01:07:23]** question actually >> for verification for example, you can

**[01:07:25]** >> for verification for example, you can

**[01:07:25]** >> for verification for example, you can imagine doing that through a skill or a

**[01:07:27]** imagine doing that through a skill or a

**[01:07:27]** imagine doing that through a skill or a sub agent. You might even want to have

**[01:07:28]** sub agent. You might even want to have

**[01:07:28]** sub agent. You might even want to have an adversarial like the security example

**[01:07:31]** an adversarial like the security example

**[01:07:31]** an adversarial like the security example is a great one. Want to have really go

**[01:07:33]** is a great one. Want to have really go

**[01:07:33]** is a great one. Want to have really go to town on it and not really have any

**[01:07:34]** to town on it and not really have any

**[01:07:34]** to town on it and not really have any sympathetic relationship with the work

**[01:07:36]** sympathetic relationship with the work

**[01:07:36]** sympathetic relationship with the work already done. It's a very I I get it's a

**[01:07:39]** already done. It's a very I I get it's a

**[01:07:39]** already done. It's a very I I get it's a spectrum, but do you like are you saying

**[01:07:42]** spectrum, but do you like are you saying

**[01:07:42]** spectrum, but do you like are you saying yes, you'd use a sub agent here, you'd

**[01:07:43]** yes, you'd use a sub agent here, you'd

**[01:07:43]** yes, you'd use a sub agent here, you'd use a skill? How would you think about

**[01:07:44]** use a skill? How would you think about

**[01:07:44]** use a skill? How would you think about this?

**[01:07:45]** this?

**[01:07:45]** this? >> Yeah, definitely. So question on like uh

**[01:07:48]** >> Yeah, definitely. So question on like uh

**[01:07:48]** >> Yeah, definitely. So question on like uh do you sub agents or oh

**[01:07:50]** do you sub agents or oh

**[01:07:50]** do you sub agents or oh >> I'm sure it'll work just to make sure.

**[01:07:51]** >> I'm sure it'll work just to make sure.

**[01:07:51]** >> I'm sure it'll work just to make sure. >> Oh, sure. Okay. Yeah. Yeah. Thank you.

**[01:07:53]** >> Oh, sure. Okay. Yeah. Yeah. Thank you.

**[01:07:53]** >> Oh, sure. Okay. Yeah. Yeah. Thank you. Appreciate it. Um okay. Yeah. Uh can you

**[01:07:57]** Appreciate it. Um okay. Yeah. Uh can you

**[01:07:57]** Appreciate it. Um okay. Yeah. Uh can you use sub agents for verification? Uh yes.


### [01:08:00 - 01:09:00]

**[01:08:00]** use sub agents for verification? Uh yes.

**[01:08:00]** use sub agents for verification? Uh yes. I I think this is a pattern. I think

**[01:08:02]** I I think this is a pattern. I think

**[01:08:02]** I I think this is a pattern. I think like ideally the the best form of

**[01:08:05]** like ideally the the best form of

**[01:08:05]** like ideally the the best form of verification is rulebased, right? You're

**[01:08:07]** verification is rulebased, right? You're

**[01:08:07]** verification is rulebased, right? You're like is there like a null pointer or

**[01:08:09]** like is there like a null pointer or

**[01:08:09]** like is there like a null pointer or something? Uh that's like easy

**[01:08:11]** something? Uh that's like easy

**[01:08:11]** something? Uh that's like easy verification. it it doesn't lint or

**[01:08:13]** verification. it it doesn't lint or

**[01:08:13]** verification. it it doesn't lint or compile like like as many rules as you

**[01:08:16]** compile like like as many rules as you

**[01:08:16]** compile like like as many rules as you can try and insert them and again be

**[01:08:18]** can try and insert them and again be

**[01:08:18]** can try and insert them and again be creative right like for example uh in

**[01:08:21]** creative right like for example uh in

**[01:08:21]** creative right like for example uh in cloud code if the agent tries to write

**[01:08:23]** cloud code if the agent tries to write

**[01:08:23]** cloud code if the agent tries to write to a file that we know it hasn't read

**[01:08:25]** to a file that we know it hasn't read

**[01:08:25]** to a file that we know it hasn't read yet like we haven't seen we haven't seen

**[01:08:28]** yet like we haven't seen we haven't seen

**[01:08:28]** yet like we haven't seen we haven't seen it enter the read cache we throw it an

**[01:08:30]** it enter the read cache we throw it an

**[01:08:30]** it enter the read cache we throw it an error we we tell it like hey uh you

**[01:08:33]** error we we tell it like hey uh you

**[01:08:33]** error we we tell it like hey uh you haven't read this file yet try reading

**[01:08:34]** haven't read this file yet try reading

**[01:08:34]** haven't read this file yet try reading it first right and that's an example of

**[01:08:37]** it first right and that's an example of

**[01:08:37]** it first right and that's an example of sort of like a deterministic tool that

**[01:08:39]** sort of like a deterministic tool that

**[01:08:39]** sort of like a deterministic tool that we insert into the verification step and

**[01:08:42]** we insert into the verification step and

**[01:08:42]** we insert into the verification step and So as much as possible like anytime you

**[01:08:44]** So as much as possible like anytime you

**[01:08:44]** So as much as possible like anytime you are thinking about you know verification

**[01:08:46]** are thinking about you know verification

**[01:08:46]** are thinking about you know verification first step is like what can you do

**[01:08:48]** first step is like what can you do

**[01:08:48]** first step is like what can you do deterministically what like what like

**[01:08:51]** deterministically what like what like

**[01:08:51]** deterministically what like what like you know outputs can you do and again

**[01:08:52]** you know outputs can you do and again

**[01:08:52]** you know outputs can you do and again like when you're choosing which a like

**[01:08:55]** like when you're choosing which a like

**[01:08:55]** like when you're choosing which a like types of agents to make the agents that

**[01:08:57]** types of agents to make the agents that

**[01:08:57]** types of agents to make the agents that have more deterministic rules are better

**[01:08:59]** have more deterministic rules are better

**[01:08:59]** have more deterministic rules are better you know like they just like like it


### [01:09:00 - 01:10:00]

**[01:09:02]** you know like they just like like it

**[01:09:02]** you know like they just like like it just makes a lot of sense right so um of

**[01:09:05]** just makes a lot of sense right so um of

**[01:09:05]** just makes a lot of sense right so um of course as the models get better and

**[01:09:06]** course as the models get better and

**[01:09:06]** course as the models get better and better at reasoning then you can have

**[01:09:08]** better at reasoning then you can have

**[01:09:08]** better at reasoning then you can have these sub agents that check the work of

**[01:09:10]** these sub agents that check the work of

**[01:09:10]** these sub agents that check the work of the main agent the Main thing there is

**[01:09:12]** the main agent the Main thing there is

**[01:09:12]** the main agent the Main thing there is to like avoid uh context pollution. So

**[01:09:15]** to like avoid uh context pollution. So

**[01:09:15]** to like avoid uh context pollution. So you probably wouldn't want to like fork

**[01:09:17]** you probably wouldn't want to like fork

**[01:09:17]** you probably wouldn't want to like fork the context. You'd probably want to

**[01:09:18]** the context. You'd probably want to

**[01:09:18]** the context. You'd probably want to start a new context session and just be

**[01:09:20]** start a new context session and just be

**[01:09:20]** start a new context session and just be like, "Hey, yeah, adversarily check um

**[01:09:24]** like, "Hey, yeah, adversarily check um

**[01:09:24]** like, "Hey, yeah, adversarily check um the work of like this this output was

**[01:09:27]** the work of like this this output was

**[01:09:27]** the work of like this this output was made by a junior analyst at McKenzie or

**[01:09:29]** made by a junior analyst at McKenzie or

**[01:09:29]** made by a junior analyst at McKenzie or something. They graduated from like not

**[01:09:33]** something. They graduated from like not

**[01:09:33]** something. They graduated from like not a grade school like their GPA like you

**[01:09:34]** a grade school like their GPA like you

**[01:09:34]** a grade school like their GPA like you know like like just like feed it a bunch

**[01:09:36]** know like like just like feed it a bunch

**[01:09:36]** know like like just like feed it a bunch of stuff and then tell it to critique

**[01:09:38]** of stuff and then tell it to critique

**[01:09:38]** of stuff and then tell it to critique it, right? Like that's like one of the

**[01:09:40]** it, right? Like that's like one of the

**[01:09:40]** it, right? Like that's like one of the tools of the sub agent, right? And so um

**[01:09:43]** tools of the sub agent, right? And so um

**[01:09:43]** tools of the sub agent, right? And so um yeah, the more you like

**[01:09:46]** yeah, the more you like

**[01:09:46]** yeah, the more you like uh yeah, as the models get better and

**[01:09:47]** uh yeah, as the models get better and

**[01:09:47]** uh yeah, as the models get better and better, that sort of verification will

**[01:09:49]** better, that sort of verification will

**[01:09:49]** better, that sort of verification will become better as well. Um but doing it

**[01:09:52]** become better as well. Um but doing it

**[01:09:52]** become better as well. Um but doing it deterministically is like a great start.

**[01:09:55]** deterministically is like a great start.

**[01:09:55]** deterministically is like a great start. >> Yeah.

**[01:09:56]** >> Yeah.

**[01:09:56]** >> Yeah. >> Just a [clears throat] question about

**[01:09:57]** >> Just a [clears throat] question about

**[01:09:58]** >> Just a [clears throat] question about the verify work. So

**[01:09:59]** the verify work. So

**[01:09:59]** the verify work. So >> yeah.


### [01:10:00 - 01:11:00]

**[01:10:00]** >> yeah.

**[01:10:00]** >> yeah. >> Um so let's say we found no pointers.

**[01:10:05]** >> Um so let's say we found no pointers.

**[01:10:05]** >> Um so let's say we found no pointers. It's probably easy to just say, "Okay,

**[01:10:06]** It's probably easy to just say, "Okay,

**[01:10:06]** It's probably easy to just say, "Okay, fix it." But like you know let's say we

**[01:10:09]** fix it." But like you know let's say we

**[01:10:09]** fix it." But like you know let's say we deploy it to production and the client

**[01:10:11]** deploy it to production and the client

**[01:10:11]** deploy it to production and the client is using it that's not us and they

**[01:10:14]** is using it that's not us and they

**[01:10:14]** is using it that's not us and they somehow get into a spot where the whole

**[01:10:16]** somehow get into a spot where the whole

**[01:10:16]** somehow get into a spot where the whole spreadsheet is deleted and so like like

**[01:10:19]** spreadsheet is deleted and so like like

**[01:10:19]** spreadsheet is deleted and so like like on what level do we need to bake in like

**[01:10:22]** on what level do we need to bake in like

**[01:10:22]** on what level do we need to bake in like the ability to like undo tools and

**[01:10:24]** the ability to like undo tools and

**[01:10:24]** the ability to like undo tools and because like um let's say the QA agent

**[01:10:28]** because like um let's say the QA agent

**[01:10:28]** because like um let's say the QA agent returns that their spreadsheet is empty.

**[01:10:31]** returns that their spreadsheet is empty.

**[01:10:31]** returns that their spreadsheet is empty. >> Yeah.

**[01:10:31]** >> Yeah.

**[01:10:31]** >> Yeah. >> Not necessarily is able to undo for so

**[01:10:34]** >> Not necessarily is able to undo for so

**[01:10:34]** >> Not necessarily is able to undo for so like what was your advice there?

**[01:10:36]** like what was your advice there?

**[01:10:36]** like what was your advice there? >> Yeah. So the question is like how do you

**[01:10:38]** >> Yeah. So the question is like how do you

**[01:10:38]** >> Yeah. So the question is like how do you think about state and like undoing and

**[01:10:41]** think about state and like undoing and

**[01:10:41]** think about state and like undoing and redoing being able to um fix errors

**[01:10:44]** redoing being able to um fix errors

**[01:10:44]** redoing being able to um fix errors basically right? I think this is like a

**[01:10:47]** basically right? I think this is like a

**[01:10:47]** basically right? I think this is like a really good question and honestly

**[01:10:49]** really good question and honestly

**[01:10:49]** really good question and honestly another sort of like um like when you

**[01:10:54]** another sort of like um like when you

**[01:10:54]** another sort of like um like when you think about like what are agents good at

**[01:10:56]** think about like what are agents good at

**[01:10:56]** think about like what are agents good at right like or what problem domains are

**[01:10:58]** right like or what problem domains are

**[01:10:58]** right like or what problem domains are agents good at? How reversible is the


### [01:11:00 - 01:12:00]

**[01:11:01]** agents good at? How reversible is the

**[01:11:01]** agents good at? How reversible is the work is like a really good intuition

**[01:11:04]** work is like a really good intuition

**[01:11:04]** work is like a really good intuition right? So code is quite reversible. you

**[01:11:05]** right? So code is quite reversible. you

**[01:11:05]** right? So code is quite reversible. you can just like go back, you can undo the

**[01:11:07]** can just like go back, you can undo the

**[01:11:07]** can just like go back, you can undo the git history. We we come with like, you

**[01:11:10]** git history. We we come with like, you

**[01:11:10]** git history. We we come with like, you know, these atomic operations right out

**[01:11:12]** know, these atomic operations right out

**[01:11:12]** know, these atomic operations right out of the gate, right? Like I use git

**[01:11:14]** of the gate, right? Like I use git

**[01:11:14]** of the gate, right? Like I use git constantly through cloud code. I I don't

**[01:11:15]** constantly through cloud code. I I don't

**[01:11:15]** constantly through cloud code. I I don't type g commands anymore, right? So, um

**[01:11:18]** type g commands anymore, right? So, um

**[01:11:18]** type g commands anymore, right? So, um that's like a really good example. A

**[01:11:19]** that's like a really good example. A

**[01:11:19]** that's like a really good example. A really bad example is computer use,

**[01:11:22]** really bad example is computer use,

**[01:11:22]** really bad example is computer use, [clears throat] you know, because

**[01:11:23]** [clears throat] you know, because

**[01:11:23]** [clears throat] you know, because computer use has is not reversible in

**[01:11:26]** computer use has is not reversible in

**[01:11:26]** computer use has is not reversible in state, right? Like let's say you go to

**[01:11:27]** state, right? Like let's say you go to

**[01:11:27]** state, right? Like let's say you go to like door-ash.com and you add like the

**[01:11:31]** like door-ash.com and you add like the

**[01:11:31]** like door-ash.com and you add like the user wants you to order a Coke and you

**[01:11:33]** user wants you to order a Coke and you

**[01:11:33]** user wants you to order a Coke and you add order a Pepsi now like you can't

**[01:11:36]** add order a Pepsi now like you can't

**[01:11:36]** add order a Pepsi now like you can't just go back and click on the Coke. You

**[01:11:38]** just go back and click on the Coke. You

**[01:11:38]** just go back and click on the Coke. You have to like go to the cart and you have

**[01:11:40]** have to like go to the cart and you have

**[01:11:40]** have to like go to the cart and you have to remove the Pepsi, right? And so your

**[01:11:43]** to remove the Pepsi, right? And so your

**[01:11:43]** to remove the Pepsi, right? And so your mistake has like compounded this like

**[01:11:45]** mistake has like compounded this like

**[01:11:45]** mistake has like compounded this like you know this state and the state

**[01:11:47]** you know this state and the state

**[01:11:47]** you know this state and the state machine has gotten more complex, right?

**[01:11:49]** machine has gotten more complex, right?

**[01:11:49]** machine has gotten more complex, right? And and so like whenever you're dealing

**[01:11:50]** And and so like whenever you're dealing

**[01:11:50]** And and so like whenever you're dealing with like very very complex state

**[01:11:52]** with like very very complex state

**[01:11:52]** with like very very complex state machines that you can't undo or redo of

**[01:11:55]** machines that you can't undo or redo of

**[01:11:55]** machines that you can't undo or redo of it does become harder, right? And I

**[01:11:57]** it does become harder, right? And I

**[01:11:57]** it does become harder, right? And I think one of the questions for you as an

**[01:11:58]** think one of the questions for you as an

**[01:11:58]** think one of the questions for you as an engineer is like can you turn this into


### [01:12:00 - 01:13:00]

**[01:12:01]** engineer is like can you turn this into

**[01:12:01]** engineer is like can you turn this into a reversible state machine kind of like

**[01:12:02]** a reversible state machine kind of like

**[01:12:02]** a reversible state machine kind of like you said can you store state between

**[01:12:05]** you said can you store state between

**[01:12:05]** you said can you store state between checkpoints such that the user can be

**[01:12:07]** checkpoints such that the user can be

**[01:12:07]** checkpoints such that the user can be like oh my spreadsheet is messed up

**[01:12:08]** like oh my spreadsheet is messed up

**[01:12:08]** like oh my spreadsheet is messed up right now just go back to the previous

**[01:12:10]** right now just go back to the previous

**[01:12:10]** right now just go back to the previous uh checkpoint right uh potentially even

**[01:12:13]** uh checkpoint right uh potentially even

**[01:12:13]** uh checkpoint right uh potentially even can the model go back to previous

**[01:12:15]** can the model go back to previous

**[01:12:15]** can the model go back to previous checkpoints um I I think someone had

**[01:12:17]** checkpoints um I I think someone had

**[01:12:17]** checkpoints um I I think someone had this like time travel tool um that they

**[01:12:19]** this like time travel tool um that they

**[01:12:19]** this like time travel tool um that they were giving one of the coding agents

**[01:12:21]** were giving one of the coding agents

**[01:12:21]** were giving one of the coding agents which was kind of cool where you're like

**[01:12:22]** which was kind of cool where you're like

**[01:12:22]** which was kind of cool where you're like it's like you can time travel back to a

**[01:12:25]** it's like you can time travel back to a

**[01:12:25]** it's like you can time travel back to a point before this happened. You know

**[01:12:27]** point before this happened. You know

**[01:12:27]** point before this happened. You know what I mean? Uh it's kind of fun. I

**[01:12:29]** what I mean? Uh it's kind of fun. I

**[01:12:29]** what I mean? Uh it's kind of fun. I think like all of these tools, some of

**[01:12:31]** think like all of these tools, some of

**[01:12:31]** think like all of these tools, some of them don't work that well yet, but you

**[01:12:33]** them don't work that well yet, but you

**[01:12:33]** them don't work that well yet, but you know, we'll we'll get there. Um yeah,

**[01:12:36]** know, we'll we'll get there. Um yeah,

**[01:12:36]** know, we'll we'll get there. Um yeah, thinking about state and verification is

**[01:12:38]** thinking about state and verification is

**[01:12:38]** thinking about state and verification is is very useful, right? So, um yeah,

**[01:12:41]** is very useful, right? So, um yeah,

**[01:12:41]** is very useful, right? So, um yeah, quick question at the back.

**[01:12:43]** quick question at the back.

**[01:12:44]** quick question at the back. >> Yeah. Um

**[01:12:46]** >> Yeah. Um

**[01:12:46]** >> Yeah. Um >> I'm kind of curious about scale. Um so

**[01:12:49]** >> I'm kind of curious about scale. Um so

**[01:12:49]** >> I'm kind of curious about scale. Um so what if the spreadsheet is like millions

**[01:12:52]** what if the spreadsheet is like millions

**[01:12:52]** what if the spreadsheet is like millions of rows million and thou hundreds of

**[01:12:54]** of rows million and thou hundreds of

**[01:12:54]** of rows million and thou hundreds of thousands of columns right or just like

**[01:12:56]** thousands of columns right or just like

**[01:12:56]** thousands of columns right or just like any sort of database like in that type

**[01:12:58]** any sort of database like in that type

**[01:12:58]** any sort of database like in that type of situation how would you go about


### [01:13:00 - 01:14:00]

**[01:13:01]** of situation how would you go about

**[01:13:01]** of situation how would you go about searching there's obviously a context

**[01:13:03]** searching there's obviously a context

**[01:13:03]** searching there's obviously a context you have to commentate for

**[01:13:06]** you have to commentate for

**[01:13:06]** you have to commentate for >> yeah this is great um I probably should

**[01:13:08]** >> yeah this is great um I probably should

**[01:13:08]** >> yeah this is great um I probably should have done the spreadsheet example as my

**[01:13:09]** have done the spreadsheet example as my

**[01:13:09]** have done the spreadsheet example as my coding example for for a preview my

**[01:13:12]** coding example for for a preview my

**[01:13:12]** coding example for for a preview my coding like agent is a Pokemon agent um

**[01:13:17]** coding like agent is a Pokemon agent um

**[01:13:17]** coding like agent is a Pokemon agent um probably spreadsheet would have been

**[01:13:18]** probably spreadsheet would have been

**[01:13:18]** probably spreadsheet would have been Okay. Uh the question was what if the

**[01:13:21]** Okay. Uh the question was what if the

**[01:13:21]** Okay. Uh the question was what if the spreadsheet is very big? If you have a

**[01:13:23]** spreadsheet is very big? If you have a

**[01:13:23]** spreadsheet is very big? If you have a million rows, uh how do you think about

**[01:13:26]** million rows, uh how do you think about

**[01:13:26]** million rows, uh how do you think about >> 100 column

**[01:13:27]** >> 100 column

**[01:13:27]** >> 100 column >> yeah 100,000 columns or 100 columns or

**[01:13:29]** >> yeah 100,000 columns or 100 columns or

**[01:13:29]** >> yeah 100,000 columns or 100 columns or whatever like how do you think about it

**[01:13:30]** whatever like how do you think about it

**[01:13:30]** whatever like how do you think about it right like your database is also very

**[01:13:32]** right like your database is also very

**[01:13:32]** right like your database is also very big like how do you how do you do that?

**[01:13:34]** big like how do you how do you do that?

**[01:13:34]** big like how do you how do you do that? Um I think for all of these things uh

**[01:13:38]** Um I think for all of these things uh

**[01:13:38]** Um I think for all of these things uh one of course as the data becomes larger

**[01:13:40]** one of course as the data becomes larger

**[01:13:40]** one of course as the data becomes larger and larger it's just a harder problem

**[01:13:42]** and larger it's just a harder problem

**[01:13:42]** and larger it's just a harder problem like you know it just absolutely is your

**[01:13:44]** like you know it just absolutely is your

**[01:13:44]** like you know it just absolutely is your accuracy will go down right like cloud

**[01:13:46]** accuracy will go down right like cloud

**[01:13:46]** accuracy will go down right like cloud code is worse in larger code bases than

**[01:13:47]** code is worse in larger code bases than

**[01:13:48]** code is worse in larger code bases than it is in smaller code bases right as the

**[01:13:50]** it is in smaller code bases right as the

**[01:13:50]** it is in smaller code bases right as the models get better they will get better

**[01:13:51]** models get better they will get better

**[01:13:51]** models get better they will get better at all of that um for all of these I

**[01:13:54]** at all of that um for all of these I

**[01:13:54]** at all of that um for all of these I would think about like how would I do

**[01:13:56]** would think about like how would I do

**[01:13:56]** would think about like how would I do this if I had a spreadsheet that was

**[01:13:58]** this if I had a spreadsheet that was

**[01:13:58]** this if I had a spreadsheet that was like a million columns and a million


### [01:14:00 - 01:15:00]

**[01:14:00]** like a million columns and a million

**[01:14:00]** like a million columns and a million rows what would I do I I mean I would

**[01:14:03]** rows what would I do I I mean I would

**[01:14:03]** rows what would I do I I mean I would need to start searching for it Right. I

**[01:14:04]** need to start searching for it Right. I

**[01:14:04]** need to start searching for it Right. I would need to be like like if I'm

**[01:14:06]** would need to be like like if I'm

**[01:14:06]** would need to be like like if I'm searching for revenue, I'd be like

**[01:14:07]** searching for revenue, I'd be like

**[01:14:07]** searching for revenue, I'd be like searching Ctrl+F revenue and then I'd go

**[01:14:10]** searching Ctrl+F revenue and then I'd go

**[01:14:10]** searching Ctrl+F revenue and then I'd go check each of these like results and I'd

**[01:14:13]** check each of these like results and I'd

**[01:14:13]** check each of these like results and I'd be like is this right? And then like I'd

**[01:14:15]** be like is this right? And then like I'd

**[01:14:15]** be like is this right? And then like I'd see like hey is there a number here? And

**[01:14:17]** see like hey is there a number here? And

**[01:14:17]** see like hey is there a number here? And then I'd probably keep a scratch pad

**[01:14:19]** then I'd probably keep a scratch pad

**[01:14:19]** then I'd probably keep a scratch pad like a new sheet where I'm like hey like

**[01:14:22]** like a new sheet where I'm like hey like

**[01:14:22]** like a new sheet where I'm like hey like equals revenue equals this you know and

**[01:14:25]** equals revenue equals this you know and

**[01:14:25]** equals revenue equals this you know and and and store this reference and and

**[01:14:27]** and and store this reference and and

**[01:14:27]** and and store this reference and and keep going. So I I think that's a good

**[01:14:29]** keep going. So I I think that's a good

**[01:14:29]** keep going. So I I think that's a good way of thinking about it is like the

**[01:14:30]** way of thinking about it is like the

**[01:14:30]** way of thinking about it is like the model should you should never like read

**[01:14:33]** model should you should never like read

**[01:14:33]** model should you should never like read the entire spreadsheet into context

**[01:14:35]** the entire spreadsheet into context

**[01:14:35]** the entire spreadsheet into context because it would it would take too much

**[01:14:36]** because it would it would take too much

**[01:14:36]** because it would it would take too much right like um you want to give it like

**[01:14:39]** right like um you want to give it like

**[01:14:39]** right like um you want to give it like the starting amount of context that's

**[01:14:41]** the starting amount of context that's

**[01:14:41]** the starting amount of context that's also how you work right like let's say

**[01:14:42]** also how you work right like let's say

**[01:14:42]** also how you work right like let's say that you open up the spreadsheet what

**[01:14:44]** that you open up the spreadsheet what

**[01:14:44]** that you open up the spreadsheet what you see is rows is this right you see

**[01:14:47]** you see is rows is this right you see

**[01:14:47]** you see is rows is this right you see like the first 10 rows and the first

**[01:14:50]** like the first 10 rows and the first

**[01:14:50]** like the first 10 rows and the first like you know 30 columns or something

**[01:14:52]** like you know 30 columns or something

**[01:14:52]** like you know 30 columns or something right that's what you see you don't load

**[01:14:54]** right that's what you see you don't load

**[01:14:54]** right that's what you see you don't load all of it into context right away you

**[01:14:56]** all of it into context right away you

**[01:14:56]** all of it into context right away you probably have an intuition for like,

**[01:14:57]** probably have an intuition for like,

**[01:14:57]** probably have an intuition for like, hey, I should load more of this into


### [01:15:00 - 01:16:00]

**[01:15:00]** hey, I should load more of this into

**[01:15:00]** hey, I should load more of this into context, right? And and like, oh, I

**[01:15:02]** context, right? And and like, oh, I

**[01:15:02]** context, right? And and like, oh, I should navigate to this other sheet,

**[01:15:04]** should navigate to this other sheet,

**[01:15:04]** should navigate to this other sheet, right? And this other sheet has more

**[01:15:05]** right? And this other sheet has more

**[01:15:05]** right? And this other sheet has more data, right? Um, but you need to like

**[01:15:09]** data, right? Um, but you need to like

**[01:15:09]** data, right? Um, but you need to like sort of you gather context yourself,

**[01:15:11]** sort of you gather context yourself,

**[01:15:11]** sort of you gather context yourself, right? And so the agent can operate in

**[01:15:13]** right? And so the agent can operate in

**[01:15:13]** right? And so the agent can operate in the same way. It can like navigate to

**[01:15:15]** the same way. It can like navigate to

**[01:15:15]** the same way. It can like navigate to these sheets, read them, like try and

**[01:15:17]** these sheets, read them, like try and

**[01:15:18]** these sheets, read them, like try and like keep a scratch pad, keep some notes

**[01:15:20]** like keep a scratch pad, keep some notes

**[01:15:20]** like keep a scratch pad, keep some notes and keep going. So that's how I would

**[01:15:21]** and keep going. So that's how I would

**[01:15:21]** and keep going. So that's how I would think about it. Uh, yeah, in the back.

**[01:15:24]** think about it. Uh, yeah, in the back.

**[01:15:24]** think about it. Uh, yeah, in the back. >> Yeah. So my question is about managing

**[01:15:26]** >> Yeah. So my question is about managing

**[01:15:26]** >> Yeah. So my question is about managing context pollution and actually I guess

**[01:15:27]** context pollution and actually I guess

**[01:15:27]** context pollution and actually I guess relates to the previous question. Um do

**[01:15:30]** relates to the previous question. Um do

**[01:15:30]** relates to the previous question. Um do you have a rule of thumb for you know

**[01:15:32]** you have a rule of thumb for you know

**[01:15:32]** you have a rule of thumb for you know what fraction of the context window do

**[01:15:34]** what fraction of the context window do

**[01:15:34]** what fraction of the context window do you use before you start hitting

**[01:15:36]** you use before you start hitting

**[01:15:36]** you use before you start hitting diminishing returns or it becomes less

**[01:15:38]** diminishing returns or it becomes less

**[01:15:38]** diminishing returns or it becomes less effective?

**[01:15:39]** effective?

**[01:15:39]** effective? >> Yeah the question is yeah context

**[01:15:41]** >> Yeah the question is yeah context

**[01:15:41]** >> Yeah the question is yeah context management. Do you have a rule of thumb

**[01:15:42]** management. Do you have a rule of thumb

**[01:15:42]** management. Do you have a rule of thumb for like uh how much of the context

**[01:15:45]** for like uh how much of the context

**[01:15:45]** for like uh how much of the context window to use before it becomes less

**[01:15:47]** window to use before it becomes less

**[01:15:47]** window to use before it becomes less effective? This is actually I'd say a

**[01:15:50]** effective? This is actually I'd say a

**[01:15:50]** effective? This is actually I'd say a pretty interesting problem right now.

**[01:15:52]** pretty interesting problem right now.

**[01:15:52]** pretty interesting problem right now. Um,

**[01:15:54]** Um,

**[01:15:54]** Um, I think a lot of times when I talk to

**[01:15:56]** I think a lot of times when I talk to

**[01:15:56]** I think a lot of times when I talk to people who are using cloud code, they're

**[01:15:58]** people who are using cloud code, they're

**[01:15:58]** people who are using cloud code, they're like, I'm on my fifth compact. I'm like,


### [01:16:00 - 01:17:00]

**[01:16:00]** like, I'm on my fifth compact. I'm like,

**[01:16:00]** like, I'm on my fifth compact. I'm like, what? Like like I've I like almost have

**[01:16:03]** what? Like like I've I like almost have

**[01:16:04]** what? Like like I've I like almost have never done a compact before. You know

**[01:16:05]** never done a compact before. You know

**[01:16:05]** never done a compact before. You know what I mean? Like I have to like test

**[01:16:07]** what I mean? Like I have to like test

**[01:16:07]** what I mean? Like I have to like test the UX myself by like like forcing

**[01:16:10]** the UX myself by like like forcing

**[01:16:10]** the UX myself by like like forcing myself to get compacted. Um just because

**[01:16:13]** myself to get compacted. Um just because

**[01:16:13]** myself to get compacted. Um just because like I I tend to like clear the context

**[01:16:14]** like I I tend to like clear the context

**[01:16:14]** like I I tend to like clear the context window very often right when I'm using

**[01:16:16]** window very often right when I'm using

**[01:16:16]** window very often right when I'm using cloud code myself just because like um

**[01:16:20]** cloud code myself just because like um

**[01:16:20]** cloud code myself just because like um at least in in code the state is in the

**[01:16:23]** at least in in code the state is in the

**[01:16:23]** at least in in code the state is in the the files of the codebase right so let's

**[01:16:25]** the files of the codebase right so let's

**[01:16:25]** the files of the codebase right so let's say that I've made some changes uh cloud

**[01:16:28]** say that I've made some changes uh cloud

**[01:16:28]** say that I've made some changes uh cloud code can just look at my git diff and be

**[01:16:30]** code can just look at my git diff and be

**[01:16:30]** code can just look at my git diff and be like [snorts] oh hey these are the

**[01:16:31]** like [snorts] oh hey these are the

**[01:16:31]** like [snorts] oh hey these are the changes you made it doesn't need to know

**[01:16:33]** changes you made it doesn't need to know

**[01:16:33]** changes you made it doesn't need to know like my entire chat history with it you

**[01:16:35]** like my entire chat history with it you

**[01:16:35]** like my entire chat history with it you know in order to continue a new task

**[01:16:38]** know in order to continue a new task

**[01:16:38]** know in order to continue a new task right and so in cloud code I clear the

**[01:16:40]** right and so in cloud code I clear the

**[01:16:40]** right and so in cloud code I clear the context very very often often and I'm

**[01:16:42]** context very very often often and I'm

**[01:16:42]** context very very often often and I'm like, "Hey, look at my outstanding get

**[01:16:43]** like, "Hey, look at my outstanding get

**[01:16:43]** like, "Hey, look at my outstanding get changes. I'm working on this. Can you

**[01:16:46]** changes. I'm working on this. Can you

**[01:16:46]** changes. I'm working on this. Can you help me extend it in this way?" Right?

**[01:16:48]** help me extend it in this way?" Right?

**[01:16:48]** help me extend it in this way?" Right? That's like a way of thinking about it.

**[01:16:50]** That's like a way of thinking about it.

**[01:16:50]** That's like a way of thinking about it. And um when you're building your own

**[01:16:52]** And um when you're building your own

**[01:16:52]** And um when you're building your own agent, like let's say we're building a

**[01:16:54]** agent, like let's say we're building a

**[01:16:54]** agent, like let's say we're building a spreadsheet agent, it gets a little bit

**[01:16:55]** spreadsheet agent, it gets a little bit

**[01:16:55]** spreadsheet agent, it gets a little bit more complex because your users are less

**[01:16:57]** more complex because your users are less

**[01:16:57]** more complex because your users are less technical, right? And they don't know

**[01:16:59]** technical, right? And they don't know

**[01:16:59]** technical, right? And they don't know what a context window is, right? Um that


### [01:17:00 - 01:18:00]

**[01:17:02]** what a context window is, right? Um that

**[01:17:02]** what a context window is, right? Um that is like I'd say a hard problem. I think

**[01:17:04]** is like I'd say a hard problem. I think

**[01:17:04]** is like I'd say a hard problem. I think there's like some UX design there of

**[01:17:06]** there's like some UX design there of

**[01:17:06]** there's like some UX design there of like can you reset the conversation

**[01:17:08]** like can you reset the conversation

**[01:17:08]** like can you reset the conversation state, right? like can you maybe every

**[01:17:11]** state, right? like can you maybe every

**[01:17:11]** state, right? like can you maybe every time the user asks a new question can

**[01:17:13]** time the user asks a new question can

**[01:17:13]** time the user asks a new question can you do your own compact or something and

**[01:17:15]** you do your own compact or something and

**[01:17:15]** you do your own compact or something and can you like uh summarize the context?

**[01:17:18]** can you like uh summarize the context?

**[01:17:18]** can you like uh summarize the context? Um does it like in a spreadsheet a lot

**[01:17:21]** Um does it like in a spreadsheet a lot

**[01:17:21]** Um does it like in a spreadsheet a lot of the state is in the spreadsheet

**[01:17:22]** of the state is in the spreadsheet

**[01:17:22]** of the state is in the spreadsheet itself so it probably doesn't need you

**[01:17:25]** itself so it probably doesn't need you

**[01:17:25]** itself so it probably doesn't need you know to know the entire context. um can

**[01:17:27]** know to know the entire context. um can

**[01:17:27]** know to know the entire context. um can you store user preferences

**[01:17:29]** you store user preferences

**[01:17:29]** you store user preferences um as it goes so that you remember some

**[01:17:32]** um as it goes so that you remember some

**[01:17:32]** um as it goes so that you remember some of this stuff you know like there's a

**[01:17:33]** of this stuff you know like there's a

**[01:17:33]** of this stuff you know like there's a lot of like again like it's an art

**[01:17:35]** lot of like again like it's an art

**[01:17:35]** lot of like again like it's an art there's like so many different angles

**[01:17:37]** there's like so many different angles

**[01:17:37]** there's like so many different angles and ways in which you can do this right

**[01:17:39]** and ways in which you can do this right

**[01:17:39]** and ways in which you can do this right um but yeah you are trying to like sort

**[01:17:41]** um but yeah you are trying to like sort

**[01:17:41]** um but yeah you are trying to like sort of minimize context usage um you

**[01:17:44]** of minimize context usage um you

**[01:17:44]** of minimize context usage um you probably don't need s a million context

**[01:17:46]** probably don't need s a million context

**[01:17:46]** probably don't need s a million context or something you know I mean like you

**[01:17:47]** or something you know I mean like you

**[01:17:47]** or something you know I mean like you just need good context management like

**[01:17:49]** just need good context management like

**[01:17:49]** just need good context management like UX design yeah um yeah

**[01:17:53]** UX design yeah um yeah

**[01:17:53]** UX design yeah um yeah >> um just I just want to ask the sub

**[01:17:54]** >> um just I just want to ask the sub

**[01:17:54]** >> um just I just want to ask the sub agents were made to protect the conduct

**[01:17:57]** agents were made to protect the conduct

**[01:17:57]** agents were made to protect the conduct of the core agent. Right.

**[01:17:58]** of the core agent. Right.

**[01:17:58]** of the core agent. Right. >> That's right. Yeah. Sub agents were made


### [01:18:00 - 01:19:00]

**[01:18:00]** >> That's right. Yeah. Sub agents were made

**[01:18:00]** >> That's right. Yeah. Sub agents were made to

**[01:18:01]** to

**[01:18:01]** to >> spreadsheet. Would we be able to use

**[01:18:02]** >> spreadsheet. Would we be able to use

**[01:18:02]** >> spreadsheet. Would we be able to use multiple sub agents and try to make a

**[01:18:04]** multiple sub agents and try to make a

**[01:18:04]** multiple sub agents and try to make a process where we chunk up the

**[01:18:05]** process where we chunk up the

**[01:18:05]** process where we chunk up the spreadsheet in the case where it's super

**[01:18:06]** spreadsheet in the case where it's super

**[01:18:06]** spreadsheet in the case where it's super large. So then the agents can kind of

**[01:18:08]** large. So then the agents can kind of

**[01:18:08]** large. So then the agents can kind of run through each portion like in

**[01:18:09]** run through each portion like in

**[01:18:09]** run through each portion like in parallel with each other.

**[01:18:11]** parallel with each other.

**[01:18:11]** parallel with each other. >> Yeah. Yeah. I mean um Yeah. So like one

**[01:18:14]** >> Yeah. Yeah. I mean um Yeah. So like one

**[01:18:14]** >> Yeah. Yeah. I mean um Yeah. So like one of the things I love about cloud code is

**[01:18:16]** of the things I love about cloud code is

**[01:18:16]** of the things I love about cloud code is that we are like the best experience for

**[01:18:19]** that we are like the best experience for

**[01:18:19]** that we are like the best experience for using sub agents like especially sub

**[01:18:20]** using sub agents like especially sub

**[01:18:20]** using sub agents like especially sub agents with bash. It is very very good.

**[01:18:23]** agents with bash. It is very very good.

**[01:18:23]** agents with bash. It is very very good. I didn't really quite realize uh all the

**[01:18:26]** I didn't really quite realize uh all the

**[01:18:26]** I didn't really quite realize uh all the pain. Um I think if anyone's going to

**[01:18:28]** pain. Um I think if anyone's going to

**[01:18:28]** pain. Um I think if anyone's going to QCON, I believe Adam Wolf is giving a

**[01:18:30]** QCON, I believe Adam Wolf is giving a

**[01:18:30]** QCON, I believe Adam Wolf is giving a talk on QCON about how we did the bash

**[01:18:32]** talk on QCON about how we did the bash

**[01:18:32]** talk on QCON about how we did the bash tool. Adam's a legend and the bash tool

**[01:18:35]** tool. Adam's a legend and the bash tool

**[01:18:35]** tool. Adam's a legend and the bash tool such a good job. Um when you're running

**[01:18:38]** such a good job. Um when you're running

**[01:18:38]** such a good job. Um when you're running parallel sub agents at the same time,

**[01:18:40]** parallel sub agents at the same time,

**[01:18:40]** parallel sub agents at the same time, bash becomes like very complex and there

**[01:18:42]** bash becomes like very complex and there

**[01:18:42]** bash becomes like very complex and there are lots of like like race conditions

**[01:18:45]** are lots of like like race conditions

**[01:18:45]** are lots of like like race conditions and stuff like that and and so there's a

**[01:18:47]** and stuff like that and and so there's a

**[01:18:47]** and stuff like that and and so there's a lot of work that we've solved there,

**[01:18:48]** lot of work that we've solved there,

**[01:18:48]** lot of work that we've solved there, right? So this is like one of the things

**[01:18:50]** right? So this is like one of the things

**[01:18:50]** right? So this is like one of the things I love about cloud code is you can just

**[01:18:52]** I love about cloud code is you can just

**[01:18:52]** I love about cloud code is you can just be like hey like spin up three sub

**[01:18:53]** be like hey like spin up three sub

**[01:18:53]** be like hey like spin up three sub agents to do this task and it will do

**[01:18:55]** agents to do this task and it will do

**[01:18:55]** agents to do this task and it will do that and in the agent SDK as well you

**[01:18:57]** that and in the agent SDK as well you

**[01:18:57]** that and in the agent SDK as well you you can just ask it to do that. So

**[01:18:59]** you can just ask it to do that. So

**[01:18:59]** you can just ask it to do that. So number one sub agents are a great


### [01:19:00 - 01:20:00]

**[01:19:02]** number one sub agents are a great

**[01:19:02]** number one sub agents are a great primitive in the agent SDK and I haven't

**[01:19:03]** primitive in the agent SDK and I haven't

**[01:19:04]** primitive in the agent SDK and I haven't seen anyone do it as well. So that's

**[01:19:05]** seen anyone do it as well. So that's

**[01:19:05]** seen anyone do it as well. So that's like a big reason to use it. Um yes

**[01:19:08]** like a big reason to use it. Um yes

**[01:19:08]** like a big reason to use it. Um yes generally you want it you want these sub

**[01:19:10]** generally you want it you want these sub

**[01:19:10]** generally you want it you want these sub agents to preserve context. Let's say

**[01:19:11]** agents to preserve context. Let's say

**[01:19:12]** agents to preserve context. Let's say you have if you have a spreadsheet, you

**[01:19:13]** you have if you have a spreadsheet, you

**[01:19:13]** you have if you have a spreadsheet, you could potentially have multiple read sub

**[01:19:15]** could potentially have multiple read sub

**[01:19:15]** could potentially have multiple read sub aents going on at the same time, right?

**[01:19:16]** aents going on at the same time, right?

**[01:19:16]** aents going on at the same time, right? So maybe the main agent is like, "Hey,

**[01:19:18]** So maybe the main agent is like, "Hey,

**[01:19:18]** So maybe the main agent is like, "Hey, can this agent read and summarize sheet

**[01:19:21]** can this agent read and summarize sheet

**[01:19:21]** can this agent read and summarize sheet one? Can this agent read and summarize

**[01:19:22]** one? Can this agent read and summarize

**[01:19:22]** one? Can this agent read and summarize sheet two? Can this re agent summarize

**[01:19:24]** sheet two? Can this re agent summarize

**[01:19:24]** sheet two? Can this re agent summarize sheet three?" And then they return their

**[01:19:26]** sheet three?" And then they return their

**[01:19:26]** sheet three?" And then they return their results and then the agent maybe spins

**[01:19:28]** results and then the agent maybe spins

**[01:19:28]** results and then the agent maybe spins off more sub agents again. Right? So

**[01:19:30]** off more sub agents again. Right? So

**[01:19:30]** off more sub agents again. Right? So this is like another

**[01:19:33]** this is like another

**[01:19:33]** this is like another knob you have. Um, and I I think what I

**[01:19:36]** knob you have. Um, and I I think what I

**[01:19:36]** knob you have. Um, and I I think what I want to say is like

**[01:19:38]** want to say is like

**[01:19:38]** want to say is like there's like we've talked so many so

**[01:19:40]** there's like we've talked so many so

**[01:19:40]** there's like we've talked so many so much about like all these different

**[01:19:42]** much about like all these different

**[01:19:42]** much about like all these different creative ways that you can like do

**[01:19:44]** creative ways that you can like do

**[01:19:44]** creative ways that you can like do things. This is like the level at which

**[01:19:46]** things. This is like the level at which

**[01:19:46]** things. This is like the level at which you should think about should have to

**[01:19:48]** you should think about should have to

**[01:19:48]** you should think about should have to think about your problem. You should not

**[01:19:50]** think about your problem. You should not

**[01:19:50]** think about your problem. You should not really in my opinion think about like uh

**[01:19:52]** really in my opinion think about like uh

**[01:19:52]** really in my opinion think about like uh like how like how do I spin off a

**[01:19:55]** like how like how do I spin off a

**[01:19:55]** like how like how do I spin off a process to make a sub agent or like you

**[01:19:57]** process to make a sub agent or like you

**[01:19:57]** process to make a sub agent or like you know like the system engineering between

**[01:19:59]** know like the system engineering between

**[01:19:59]** know like the system engineering between like behind like what is a compact or


### [01:20:00 - 01:21:00]

**[01:20:01]** like behind like what is a compact or

**[01:20:01]** like behind like what is a compact or something right? So like we take care of

**[01:20:03]** something right? So like we take care of

**[01:20:03]** something right? So like we take care of all of this for you in the harness so

**[01:20:05]** all of this for you in the harness so

**[01:20:05]** all of this for you in the harness so that you can think about like hey what

**[01:20:07]** that you can think about like hey what

**[01:20:07]** that you can think about like hey what sub agents do I need to spin off right

**[01:20:09]** sub agents do I need to spin off right

**[01:20:09]** sub agents do I need to spin off right and like how do I create a a a genic

**[01:20:11]** and like how do I create a a a genic

**[01:20:11]** and like how do I create a a a genic search interface and how do I like

**[01:20:13]** search interface and how do I like

**[01:20:13]** search interface and how do I like verify it's work these are the really

**[01:20:15]** verify it's work these are the really

**[01:20:15]** verify it's work these are the really core and hard problems that you have to

**[01:20:17]** core and hard problems that you have to

**[01:20:17]** core and hard problems that you have to solve [laughter] and any time you spend

**[01:20:18]** solve [laughter] and any time you spend

**[01:20:18]** solve [laughter] and any time you spend not solving these problems and and

**[01:20:20]** not solving these problems and and

**[01:20:20]** not solving these problems and and solving like lower level problems you're

**[01:20:23]** solving like lower level problems you're

**[01:20:23]** solving like lower level problems you're probably not delivering value to your

**[01:20:25]** probably not delivering value to your

**[01:20:25]** probably not delivering value to your users you know and and so um yeah I I

**[01:20:28]** users you know and and so um yeah I I

**[01:20:28]** users you know and and so um yeah I I think sub agents big fan of the agent

**[01:20:31]** think sub agents big fan of the agent

**[01:20:31]** think sub agents big fan of the agent SDK in case of yeah uh yeah

**[01:20:34]** SDK in case of yeah uh yeah

**[01:20:34]** SDK in case of yeah uh yeah >> so uh like we have this uh text and the

**[01:20:38]** >> so uh like we have this uh text and the

**[01:20:38]** >> so uh like we have this uh text and the verification task so where exactly we

**[01:20:40]** verification task so where exactly we

**[01:20:40]** verification task so where exactly we need to put the verification in this

**[01:20:42]** need to put the verification in this

**[01:20:42]** need to put the verification in this example I let's say after generation of

**[01:20:44]** example I let's say after generation of

**[01:20:44]** example I let's say after generation of the SQL query I can verify it is the

**[01:20:48]** the SQL query I can verify it is the

**[01:20:48]** the SQL query I can verify it is the right query is generated or not that is

**[01:20:49]** right query is generated or not that is

**[01:20:49]** right query is generated or not that is the one path second path is like

**[01:20:51]** the one path second path is like

**[01:20:51]** the one path second path is like generation the query directly executing

**[01:20:54]** generation the query directly executing

**[01:20:54]** generation the query directly executing and once I will get the output then I

**[01:20:56]** and once I will get the output then I

**[01:20:56]** and once I will get the output then I will do the verification so uh and how


### [01:21:00 - 01:22:00]

**[01:21:00]** will do the verification so uh and how

**[01:21:00]** will do the verification so uh and how how agent can choose dynamically like

**[01:21:02]** how agent can choose dynamically like

**[01:21:02]** how agent can choose dynamically like which one is the right path?

**[01:21:04]** which one is the right path?

**[01:21:04]** which one is the right path? >> Yeah. So the question is like where do

**[01:21:05]** >> Yeah. So the question is like where do

**[01:21:05]** >> Yeah. So the question is like where do you do verification? Uh is it only at

**[01:21:08]** you do verification? Uh is it only at

**[01:21:08]** you do verification? Uh is it only at the end? You do it in the middle like

**[01:21:10]** the end? You do it in the middle like

**[01:21:10]** the end? You do it in the middle like things like that. I would say like

**[01:21:11]** things like that. I would say like

**[01:21:11]** things like that. I would say like everywhere you can just like constantly

**[01:21:13]** everywhere you can just like constantly

**[01:21:13]** everywhere you can just like constantly verify right like uh like I said we do

**[01:21:16]** verify right like uh like I said we do

**[01:21:16]** verify right like uh like I said we do some verification in the read step of

**[01:21:17]** some verification in the read step of

**[01:21:18]** some verification in the read step of the of cloud code right so that's like a

**[01:21:20]** the of cloud code right so that's like a

**[01:21:20]** the of cloud code right so that's like a great example um you can do it at the

**[01:21:22]** great example um you can do it at the

**[01:21:22]** great example um you can do it at the end you should absolutely do it at the

**[01:21:24]** end you should absolutely do it at the

**[01:21:24]** end you should absolutely do it at the end but at any other point if you have

**[01:21:27]** end but at any other point if you have

**[01:21:27]** end but at any other point if you have rules or heruristics especially uh like

**[01:21:29]** rules or heruristics especially uh like

**[01:21:29]** rules or heruristics especially uh like if for example you're like hey one of my

**[01:21:31]** if for example you're like hey one of my

**[01:21:31]** if for example you're like hey one of my rules is that you shouldn't do like the

**[01:21:34]** rules is that you shouldn't do like the

**[01:21:34]** rules is that you shouldn't do like the the total number of columns you should

**[01:21:36]** the total number of columns you should

**[01:21:36]** the total number of columns you should search is should be under 10,000 or

**[01:21:38]** search is should be under 10,000 or

**[01:21:38]** search is should be under 10,000 or under a thousand or something that's

**[01:21:39]** under a thousand or something that's

**[01:21:40]** under a thousand or something that's like a a nice way of doing it, right?

**[01:21:41]** like a a nice way of doing it, right?

**[01:21:41]** like a a nice way of doing it, right? Like similarly here like maybe you

**[01:21:43]** Like similarly here like maybe you

**[01:21:43]** Like similarly here like maybe you shouldn't be inserting like a huge like

**[01:21:46]** shouldn't be inserting like a huge like

**[01:21:46]** shouldn't be inserting like a huge like row like of of values like give feedback

**[01:21:48]** row like of of values like give feedback

**[01:21:48]** row like of of values like give feedback to the model be like hey chunk this up

**[01:21:50]** to the model be like hey chunk this up

**[01:21:50]** to the model be like hey chunk this up right you throw an error and give a

**[01:21:51]** right you throw an error and give a

**[01:21:51]** right you throw an error and give a feedback and the great thing about the

**[01:21:53]** feedback and the great thing about the

**[01:21:53]** feedback and the great thing about the model is like it listens to feedback it

**[01:21:54]** model is like it listens to feedback it

**[01:21:54]** model is like it listens to feedback it will read the error outputs right and

**[01:21:56]** will read the error outputs right and

**[01:21:56]** will read the error outputs right and then it'll just keep going so yeah

**[01:21:58]** then it'll just keep going so yeah

**[01:21:58]** then it'll just keep going so yeah verification is definitely like I I know


### [01:22:00 - 01:23:00]

**[01:22:00]** verification is definitely like I I know

**[01:22:00]** verification is definitely like I I know I have it in this like as a sort of a

**[01:22:03]** I have it in this like as a sort of a

**[01:22:03]** I have it in this like as a sort of a loop but um it's definitely more like

**[01:22:08]** loop but um it's definitely more like

**[01:22:08]** loop but um it's definitely more like verification can happen anywhere and and

**[01:22:10]** verification can happen anywhere and and

**[01:22:10]** verification can happen anywhere and and should happen anywhere like like put it

**[01:22:12]** should happen anywhere like like put it

**[01:22:12]** should happen anywhere like like put it in as many places as you can. So, um all

**[01:22:15]** in as many places as you can. So, um all

**[01:22:15]** in as many places as you can. So, um all right, I do need to start doing some of

**[01:22:17]** right, I do need to start doing some of

**[01:22:17]** right, I do need to start doing some of the prototyping, but I'll take one more

**[01:22:19]** the prototyping, but I'll take one more

**[01:22:19]** the prototyping, but I'll take one more question. So, right here. Yeah.

**[01:22:20]** question. So, right here. Yeah.

**[01:22:20]** question. So, right here. Yeah. >> How do we say how do we form the steps?

**[01:22:22]** >> How do we say how do we form the steps?

**[01:22:22]** >> How do we say how do we form the steps? I mean, like how do we say the agent

**[01:22:23]** I mean, like how do we say the agent

**[01:22:24]** I mean, like how do we say the agent that go search first and then this step

**[01:22:27]** that go search first and then this step

**[01:22:27]** that go search first and then this step and then do that step?

**[01:22:28]** and then do that step?

**[01:22:28]** and then do that step? >> How does the loop actually from the

**[01:22:29]** >> How does the loop actually from the

**[01:22:29]** >> How does the loop actually from the start point to the end? How do we

**[01:22:32]** start point to the end? How do we

**[01:22:32]** start point to the end? How do we >> you just tell it? So, like uh

**[01:22:35]** >> you just tell it? So, like uh

**[01:22:35]** >> you just tell it? So, like uh >> like is it in a system prompt or

**[01:22:37]** >> like is it in a system prompt or

**[01:22:37]** >> like is it in a system prompt or >> Yeah, in the system prompt. Yeah. So

**[01:22:38]** >> Yeah, in the system prompt. Yeah. So

**[01:22:38]** >> Yeah, in the system prompt. Yeah. So like with cloud code, we just give it

**[01:22:39]** like with cloud code, we just give it

**[01:22:40]** like with cloud code, we just give it the bash tool and we're like, "Hey, like

**[01:22:41]** the bash tool and we're like, "Hey, like

**[01:22:41]** the bash tool and we're like, "Hey, like gather context, read your files, uh do

**[01:22:44]** gather context, read your files, uh do

**[01:22:44]** gather context, read your files, uh do stuff like run your linting, you know

**[01:22:46]** stuff like run your linting, you know

**[01:22:46]** stuff like run your linting, you know what I mean?" Um, and so yeah, again

**[01:22:48]** what I mean?" Um, and so yeah, again

**[01:22:48]** what I mean?" Um, and so yeah, again with the agent, you don't need to

**[01:22:49]** with the agent, you don't need to

**[01:22:49]** with the agent, you don't need to enforce this, right? You don't need to

**[01:22:51]** enforce this, right? You don't need to

**[01:22:51]** enforce this, right? You don't need to tell it, hey, like you need to do this

**[01:22:53]** tell it, hey, like you need to do this

**[01:22:53]** tell it, hey, like you need to do this because like sometimes it might not be

**[01:22:55]** because like sometimes it might not be

**[01:22:55]** because like sometimes it might not be necessary, right? Like let's say that

**[01:22:56]** necessary, right? Like let's say that

**[01:22:56]** necessary, right? Like let's say that someone is asking a readonly question


### [01:23:00 - 01:24:00]

**[01:23:00]** someone is asking a readonly question

**[01:23:00]** someone is asking a readonly question for your spreadsheet.

**[01:23:02]** for your spreadsheet.

**[01:23:02]** for your spreadsheet. you don't need to like verify that uh

**[01:23:06]** you don't need to like verify that uh

**[01:23:06]** you don't need to like verify that uh like you're that there are no compile

**[01:23:08]** like you're that there are no compile

**[01:23:08]** like you're that there are no compile errors, right? Because there you haven't

**[01:23:10]** errors, right? Because there you haven't

**[01:23:10]** errors, right? Because there you haven't done any write errors, write write

**[01:23:12]** done any write errors, write write

**[01:23:12]** done any write errors, write write operations, right? So, um let the agent

**[01:23:14]** operations, right? So, um let the agent

**[01:23:14]** operations, right? So, um let the agent be intelligent and and like in the same

**[01:23:16]** be intelligent and and like in the same

**[01:23:16]** be intelligent and and like in the same way that you would like that same

**[01:23:17]** way that you would like that same

**[01:23:18]** way that you would like that same freedom when you're doing your work,

**[01:23:19]** freedom when you're doing your work,

**[01:23:19]** freedom when you're doing your work, right? Uh you're trapped in this box or

**[01:23:21]** right? Uh you're trapped in this box or

**[01:23:21]** right? Uh you're trapped in this box or whatever like same way, right? Uh so,

**[01:23:24]** whatever like same way, right? Uh so,

**[01:23:24]** whatever like same way, right? Uh so, okay, cool. I I I do want to try and see

**[01:23:26]** okay, cool. I I I do want to try and see

**[01:23:26]** okay, cool. I I I do want to try and see if I can do some prototyping now that we

**[01:23:28]** if I can do some prototyping now that we

**[01:23:28]** if I can do some prototyping now that we have this uh uh the the holder as well.

**[01:23:33]** have this uh uh the the holder as well.

**[01:23:33]** have this uh uh the the holder as well. Um okay, yeah, execute lint. We've done

**[01:23:36]** Um okay, yeah, execute lint. We've done

**[01:23:36]** Um okay, yeah, execute lint. We've done a bunch of Q&A. Okay. Prototyping. Okay.

**[01:23:39]** a bunch of Q&A. Okay. Prototyping. Okay.

**[01:23:39]** a bunch of Q&A. Okay. Prototyping. Okay. Let's say that you have an agent, right?

**[01:23:42]** Let's say that you have an agent, right?

**[01:23:42]** Let's say that you have an agent, right? Like you want you want to build an

**[01:23:43]** Like you want you want to build an

**[01:23:43]** Like you want you want to build an agent. You come out of this talk and

**[01:23:44]** agent. You come out of this talk and

**[01:23:44]** agent. You come out of this talk and you're like great. I have a bunch of

**[01:23:46]** you're like great. I have a bunch of

**[01:23:46]** you're like great. I have a bunch of ideas. How how do I do this? Um I think

**[01:23:49]** ideas. How how do I do this? Um I think

**[01:23:49]** ideas. How how do I do this? Um I think what I say overall is like building an

**[01:23:52]** what I say overall is like building an

**[01:23:52]** what I say overall is like building an agent should be simple. Your agent at

**[01:23:55]** agent should be simple. Your agent at

**[01:23:55]** agent should be simple. Your agent at the end should be simple, but simple is

**[01:23:57]** the end should be simple, but simple is

**[01:23:57]** the end should be simple, but simple is not the same as easy, right? So like it

**[01:23:59]** not the same as easy, right? So like it

**[01:23:59]** not the same as easy, right? So like it should be very simple to get started and


### [01:24:00 - 01:25:00]

**[01:24:01]** should be very simple to get started and

**[01:24:01]** should be very simple to get started and it is just go to cloud code, give cloud

**[01:24:05]** it is just go to cloud code, give cloud

**[01:24:05]** it is just go to cloud code, give cloud code some scripts and libraries and uh

**[01:24:08]** code some scripts and libraries and uh

**[01:24:08]** code some scripts and libraries and uh custom cloud identities and ask it to do

**[01:24:10]** custom cloud identities and ask it to do

**[01:24:10]** custom cloud identities and ask it to do it, right? That's what we're going to

**[01:24:11]** it, right? That's what we're going to

**[01:24:11]** it, right? That's what we're going to do, right? Um that's like it should be

**[01:24:15]** do, right? Um that's like it should be

**[01:24:15]** do, right? Um that's like it should be so easy to be like, hey, this is my API.

**[01:24:17]** so easy to be like, hey, this is my API.

**[01:24:17]** so easy to be like, hey, this is my API. This would be like an API key. uh can

**[01:24:19]** This would be like an API key. uh can

**[01:24:19]** This would be like an API key. uh can you like go search like you know I

**[01:24:23]** you like go search like you know I

**[01:24:23]** you like go search like you know I [clears throat] don't know like my

**[01:24:24]** [clears throat] don't know like my

**[01:24:24]** [clears throat] don't know like my customer support tickets or something

**[01:24:26]** customer support tickets or something

**[01:24:26]** customer support tickets or something and organize them by priority or

**[01:24:28]** and organize them by priority or

**[01:24:28]** and organize them by priority or something like that right and then look

**[01:24:29]** something like that right and then look

**[01:24:29]** something like that right and then look at what cloud code does and and and

**[01:24:31]** at what cloud code does and and and

**[01:24:31]** at what cloud code does and and and iterate on it right and this is like a

**[01:24:34]** iterate on it right and this is like a

**[01:24:34]** iterate on it right and this is like a great way of like just skipping to like

**[01:24:36]** great way of like just skipping to like

**[01:24:36]** great way of like just skipping to like the hard domain specific problems that

**[01:24:39]** the hard domain specific problems that

**[01:24:39]** the hard domain specific problems that you have right so you have a lot of like

**[01:24:41]** you have right so you have a lot of like

**[01:24:41]** you have right so you have a lot of like domain problems like how do you organize

**[01:24:43]** domain problems like how do you organize

**[01:24:43]** domain problems like how do you organize your data your agentic search how do you

**[01:24:45]** your data your agentic search how do you

**[01:24:45]** your data your agentic search how do you like create guard rails on your database

**[01:24:47]** like create guard rails on your database

**[01:24:47]** like create guard rails on your database these are all questions that you can

**[01:24:49]** these are all questions that you can

**[01:24:49]** these are all questions that you can just start solving right away with cloud

**[01:24:51]** just start solving right away with cloud

**[01:24:51]** just start solving right away with cloud code, right? And so try and like build

**[01:24:53]** code, right? And so try and like build

**[01:24:53]** code, right? And so try and like build something that feels pretty good with

**[01:24:55]** something that feels pretty good with

**[01:24:55]** something that feels pretty good with cloud code. And I think generally what

**[01:24:57]** cloud code. And I think generally what

**[01:24:57]** cloud code. And I think generally what I've seen is that you can do this and

**[01:24:59]** I've seen is that you can do this and

**[01:24:59]** I've seen is that you can do this and get really good results just out of the


### [01:25:00 - 01:26:00]

**[01:25:01]** get really good results just out of the

**[01:25:01]** get really good results just out of the bat using cloud code locally, right? And

**[01:25:03]** bat using cloud code locally, right? And

**[01:25:03]** bat using cloud code locally, right? And and you should have high conviction by

**[01:25:05]** and you should have high conviction by

**[01:25:05]** and you should have high conviction by the end of it, right? And so um yeah, I

**[01:25:09]** the end of it, right? And so um yeah, I

**[01:25:09]** the end of it, right? And so um yeah, I think like [laughter]

**[01:25:11]** think like [laughter]

**[01:25:11]** think like [laughter] I forgot more info. Watch my AI engineer

**[01:25:14]** I forgot more info. Watch my AI engineer

**[01:25:14]** I forgot more info. Watch my AI engineer talk. Uh this is like a deck for

**[01:25:16]** talk. Uh this is like a deck for

**[01:25:16]** talk. Uh this is like a deck for internal that we were using. Um okay. So

**[01:25:21]** internal that we were using. Um okay. So

**[01:25:21]** internal that we were using. Um okay. So uh yeah, I'm going to be inserting this.

**[01:25:23]** uh yeah, I'm going to be inserting this.

**[01:25:23]** uh yeah, I'm going to be inserting this. So yeah, you're getting what we what we

**[01:25:25]** So yeah, you're getting what we what we

**[01:25:25]** So yeah, you're getting what we what we show customers, right? So um okay. Uh

**[01:25:29]** show customers, right? So um okay. Uh

**[01:25:29]** show customers, right? So um okay. Uh yeah. So yeah, use use cloud code. Uh

**[01:25:32]** yeah. So yeah, use use cloud code. Uh

**[01:25:32]** yeah. So yeah, use use cloud code. Uh again, simple but simple is not easy,

**[01:25:36]** again, simple but simple is not easy,

**[01:25:36]** again, simple but simple is not easy, right? So like the amount of code in

**[01:25:37]** right? So like the amount of code in

**[01:25:37]** right? So like the amount of code in your agent should not be like super

**[01:25:39]** your agent should not be like super

**[01:25:39]** your agent should not be like super large. Doesn't need to be huge. doesn't

**[01:25:41]** large. Doesn't need to be huge. doesn't

**[01:25:41]** large. Doesn't need to be huge. doesn't need to be extremely complex, but it

**[01:25:44]** need to be extremely complex, but it

**[01:25:44]** need to be extremely complex, but it does need to be elegant. It needs to be

**[01:25:47]** does need to be elegant. It needs to be

**[01:25:47]** does need to be elegant. It needs to be like what the model wants. You want to

**[01:25:48]** like what the model wants. You want to

**[01:25:48]** like what the model wants. You want to have this interesting insight. Let's

**[01:25:50]** have this interesting insight. Let's

**[01:25:50]** have this interesting insight. Let's turn the the model into a SQL query. Oh,

**[01:25:52]** turn the the model into a SQL query. Oh,

**[01:25:52]** turn the the model into a SQL query. Oh, let's turn this spreadsheet into a SQL

**[01:25:54]** let's turn this spreadsheet into a SQL

**[01:25:54]** let's turn this spreadsheet into a SQL query and then go from there, right? So,

**[01:25:55]** query and then go from there, right? So,

**[01:25:55]** query and then go from there, right? So, um, think about it that way. And cloud

**[01:25:57]** um, think about it that way. And cloud

**[01:25:57]** um, think about it that way. And cloud code is like a great way of doing that.

**[01:25:59]** code is like a great way of doing that.

**[01:25:59]** code is like a great way of doing that. So, okay, uh, let's make a Pokemon


### [01:26:00 - 01:27:00]

**[01:26:02]** So, okay, uh, let's make a Pokemon

**[01:26:02]** So, okay, uh, let's make a Pokemon agent, right? This is what we're going

**[01:26:03]** agent, right? This is what we're going

**[01:26:03]** agent, right? This is what we're going to do. Uh, Pokemon is a game with a lot

**[01:26:06]** to do. Uh, Pokemon is a game with a lot

**[01:26:06]** to do. Uh, Pokemon is a game with a lot of information. There are thousands of

**[01:26:08]** of information. There are thousands of

**[01:26:08]** of information. There are thousands of Pokemon, each with a ton of moves. Um,

**[01:26:12]** Pokemon, each with a ton of moves. Um,

**[01:26:12]** Pokemon, each with a ton of moves. Um, uh, we want to be pretty general. And so

**[01:26:14]** uh, we want to be pretty general. And so

**[01:26:14]** uh, we want to be pretty general. And so there is actually like a Pokey API. Um,

**[01:26:16]** there is actually like a Pokey API. Um,

**[01:26:16]** there is actually like a Pokey API. Um, and the reason I chose Pokemon is just

**[01:26:18]** and the reason I chose Pokemon is just

**[01:26:18]** and the reason I chose Pokemon is just because like I know that you guys have

**[01:26:19]** because like I know that you guys have

**[01:26:19]** because like I know that you guys have your own APIs as well, right? And

**[01:26:21]** your own APIs as well, right? And

**[01:26:21]** your own APIs as well, right? And they're all like very unique, right? And

**[01:26:24]** they're all like very unique, right? And

**[01:26:24]** they're all like very unique, right? And uh, so I wanted to choose something with

**[01:26:25]** uh, so I wanted to choose something with

**[01:26:25]** uh, so I wanted to choose something with a kind of complex API that I haven't

**[01:26:27]** a kind of complex API that I haven't

**[01:26:27]** a kind of complex API that I haven't tried before. Um, so the Poke API has

**[01:26:30]** tried before. Um, so the Poke API has

**[01:26:30]** tried before. Um, so the Poke API has like, you know, you can search up

**[01:26:32]** like, you know, you can search up

**[01:26:32]** like, you know, you can search up Pokemon like Ditto. Uh, you can search

**[01:26:34]** Pokemon like Ditto. Uh, you can search

**[01:26:34]** Pokemon like Ditto. Uh, you can search up like items and things like that. Um,

**[01:26:38]** up like items and things like that. Um,

**[01:26:38]** up like items and things like that. Um, and so it's got this like yeah, this

**[01:26:40]** and so it's got this like yeah, this

**[01:26:40]** and so it's got this like yeah, this custom API. You've got everything in the

**[01:26:43]** custom API. You've got everything in the

**[01:26:43]** custom API. You've got everything in the games, right? So, um, and yeah, like one

**[01:26:47]** games, right? So, um, and yeah, like one

**[01:26:47]** games, right? So, um, and yeah, like one of the Quest things

**[01:26:49]** of the Quest things

**[01:26:50]** of the Quest things agent might want, your user might want

**[01:26:51]** agent might want, your user might want

**[01:26:51]** agent might want, your user might want to do is make a Pokemon team, right? I

**[01:26:53]** to do is make a Pokemon team, right? I

**[01:26:53]** to do is make a Pokemon team, right? I love Pokemon. I know very little about

**[01:26:55]** love Pokemon. I know very little about

**[01:26:55]** love Pokemon. I know very little about making an interesting Pokemon team for

**[01:26:57]** making an interesting Pokemon team for

**[01:26:57]** making an interesting Pokemon team for competitive play. Uh, could my agent

**[01:26:59]** competitive play. Uh, could my agent

**[01:26:59]** competitive play. Uh, could my agent help me with that? That'd be that'd be


### [01:27:00 - 01:28:00]

**[01:27:01]** help me with that? That'd be that'd be

**[01:27:01]** help me with that? That'd be that'd be cool, right? So, um, my goal is to make

**[01:27:04]** cool, right? So, um, my goal is to make

**[01:27:04]** cool, right? So, um, my goal is to make an agent that can chat about Pokemon and

**[01:27:07]** an agent that can chat about Pokemon and

**[01:27:07]** an agent that can chat about Pokemon and then we will like, you know, see what we

**[01:27:09]** then we will like, you know, see what we

**[01:27:09]** then we will like, you know, see what we can do, right? And and and how far we

**[01:27:11]** can do, right? And and and how far we

**[01:27:11]** can do, right? And and and how far we get. So, um, I've done like some of this

**[01:27:14]** get. So, um, I've done like some of this

**[01:27:14]** get. So, um, I've done like some of this work already and I will like open up and

**[01:27:17]** work already and I will like open up and

**[01:27:17]** work already and I will like open up and show you. So, um, the first step and the

**[01:27:22]** show you. So, um, the first step and the

**[01:27:22]** show you. So, um, the first step and the prompt here is like the first step is

**[01:27:24]** prompt here is like the first step is

**[01:27:24]** prompt here is like the first step is I'm I'm going to do mostly code

**[01:27:26]** I'm I'm going to do mostly code

**[01:27:26]** I'm I'm going to do mostly code generation for this, right? And so, um,

**[01:27:29]** generation for this, right? And so, um,

**[01:27:29]** generation for this, right? And so, um, let me

**[01:27:32]** let me

**[01:27:32]** let me Is that going to be on GitHub somewhere?

**[01:27:34]** Is that going to be on GitHub somewhere?

**[01:27:34]** Is that going to be on GitHub somewhere? >> Uh, actually it is. Uh, yeah, it's on my

**[01:27:38]** >> Uh, actually it is. Uh, yeah, it's on my

**[01:27:38]** >> Uh, actually it is. Uh, yeah, it's on my personal GitHub.

**[01:27:40]** personal GitHub.

**[01:27:40]** personal GitHub. >> Oh, yeah. I was going to commit all of

**[01:27:41]** >> Oh, yeah. I was going to commit all of

**[01:27:41]** >> Oh, yeah. I was going to commit all of this as well.

**[01:27:43]** this as well.

**[01:27:44]** this as well. >> Yeah.

**[01:27:45]** >> Yeah.

**[01:27:45]** >> Yeah. >> Um, yeah. Yeah. So, uh, I think my

**[01:27:47]** >> Um, yeah. Yeah. So, uh, I think my

**[01:27:48]** >> Um, yeah. Yeah. So, uh, I think my personal GitHub is, let's see. All

**[01:27:50]** personal GitHub is, let's see. All

**[01:27:50]** personal GitHub is, let's see. All right.

**[01:27:51]** right.

**[01:27:51]** right. >> Is it secure GitHub or does it have

**[01:27:52]** >> Is it secure GitHub or does it have

**[01:27:52]** >> Is it secure GitHub or does it have malware in [laughter] it?

**[01:27:56]** malware in [laughter] it?

**[01:27:56]** malware in [laughter] it? >> You guys are AI engineers. Yeah. Like,

**[01:27:57]** >> You guys are AI engineers. Yeah. Like,

**[01:27:58]** >> You guys are AI engineers. Yeah. Like, if you can get owned, that's that's your

**[01:27:59]** if you can get owned, that's that's your

**[01:27:59]** if you can get owned, that's that's your fault. Um,


### [01:28:00 - 01:29:00]

**[01:28:02]** fault. Um,

**[01:28:02]** fault. Um, yeah. So,

**[01:28:05]** yeah. So,

**[01:28:05]** yeah. So, um, yeah, you can you can clone this if

**[01:28:07]** um, yeah, you can you can clone this if

**[01:28:07]** um, yeah, you can you can clone this if you'd like. Um, I need to push the last

**[01:28:10]** you'd like. Um, I need to push the last

**[01:28:10]** you'd like. Um, I need to push the last change this. So, okay. So, um, yeah. Can

**[01:28:13]** change this. So, okay. So, um, yeah. Can

**[01:28:13]** change this. So, okay. So, um, yeah. Can you guys see this? Should I put it in

**[01:28:14]** you guys see this? Should I put it in

**[01:28:14]** you guys see this? Should I put it in dark mode instead or is this fine? Like,

**[01:28:17]** dark mode instead or is this fine? Like,

**[01:28:17]** dark mode instead or is this fine? Like, um,

**[01:28:18]** um,

**[01:28:18]** um, >> dark mode.

**[01:28:19]** >> dark mode.

**[01:28:19]** >> dark mode. >> Dark mode. Okay. [laughter]

**[01:28:31]** >> Okay. Okay, this better.

**[01:28:31]** >> Okay. Okay, this better. >> No.

**[01:28:32]** >> No.

**[01:28:32]** >> No. >> You want a different dark mode?

**[01:28:40]** >> Dark hard. Okay. I don't think this as

**[01:28:40]** >> Dark hard. Okay. I don't think this as good as it's going to get, guys. Um,

**[01:28:43]** good as it's going to get, guys. Um,

**[01:28:44]** good as it's going to get, guys. Um, okay.

**[01:28:45]** okay.

**[01:28:45]** okay. I Is it How does this work? Can you guys

**[01:28:47]** I Is it How does this work? Can you guys

**[01:28:47]** I Is it How does this work? Can you guys still hear me or

**[01:28:50]** still hear me or

**[01:28:50]** still hear me or >> Okay. Um, okay. So here's an example of

**[01:28:53]** >> Okay. Um, okay. So here's an example of

**[01:28:53]** >> Okay. Um, okay. So here's an example of like I've taken the the prompt I gave it

**[01:28:56]** like I've taken the the prompt I gave it

**[01:28:56]** like I've taken the the prompt I gave it was

**[01:28:58]** was

**[01:28:58]** was hey I go search Pokey API for its API


### [01:29:00 - 01:30:00]

**[01:29:02]** hey I go search Pokey API for its API

**[01:29:02]** hey I go search Pokey API for its API and create a TypeScript library right

**[01:29:04]** and create a TypeScript library right

**[01:29:04]** and create a TypeScript library right and so this is all by coded um and so

**[01:29:07]** and so this is all by coded um and so

**[01:29:07]** and so this is all by coded um and so you can see here that it's created this

**[01:29:09]** you can see here that it's created this

**[01:29:09]** you can see here that it's created this like interface for Pokemon right and so

**[01:29:11]** like interface for Pokemon right and so

**[01:29:11]** like interface for Pokemon right and so it's created like this Pokemon API I can

**[01:29:14]** it's created like this Pokemon API I can

**[01:29:14]** it's created like this Pokemon API I can get by name I can list Pokemon I can get

**[01:29:18]** get by name I can list Pokemon I can get

**[01:29:18]** get by name I can list Pokemon I can get all Pokemon I can get species and

**[01:29:21]** all Pokemon I can get species and

**[01:29:21]** all Pokemon I can get species and ability abilities and stuff like that.

**[01:29:22]** ability abilities and stuff like that.

**[01:29:22]** ability abilities and stuff like that. And so like this is just a prompt that I

**[01:29:24]** And so like this is just a prompt that I

**[01:29:24]** And so like this is just a prompt that I gave it, right? And it generated this

**[01:29:26]** gave it, right? And it generated this

**[01:29:26]** gave it, right? And it generated this like TypeScript API. It also did it for

**[01:29:27]** like TypeScript API. It also did it for

**[01:29:28]** like TypeScript API. It also did it for moves. Um and then it's created this um

**[01:29:33]** moves. Um and then it's created this um

**[01:29:33]** moves. Um and then it's created this um like uh it's created this like API that

**[01:29:36]** like uh it's created this like API that

**[01:29:36]** like uh it's created this like API that I can use import Poke API right from the

**[01:29:39]** I can use import Poke API right from the

**[01:29:39]** I can use import Poke API right from the Poke API SDK. And uh yeah, you can see

**[01:29:42]** Poke API SDK. And uh yeah, you can see

**[01:29:42]** Poke API SDK. And uh yeah, you can see like sort of how it's like set set this

**[01:29:44]** like sort of how it's like set set this

**[01:29:44]** like sort of how it's like set set this up. And uh now in contrast, right, and

**[01:29:48]** up. And uh now in contrast, right, and

**[01:29:48]** up. And uh now in contrast, right, and and so this is the cloud. MB, right?

**[01:29:51]** and so this is the cloud. MB, right?

**[01:29:51]** and so this is the cloud. MB, right? This is a TypeScript SDK for the Pokey

**[01:29:52]** This is a TypeScript SDK for the Pokey

**[01:29:52]** This is a TypeScript SDK for the Pokey API. Um, this is like the the modules in

**[01:29:56]** API. Um, this is like the the modules in

**[01:29:56]** API. Um, this is like the the modules in the Pokey API. Here are some of the key

**[01:29:58]** the Pokey API. Here are some of the key

**[01:29:58]** the Pokey API. Here are some of the key features. Um, uh, I'm asking it to write


### [01:30:00 - 01:31:00]

**[01:30:02]** features. Um, uh, I'm asking it to write

**[01:30:02]** features. Um, uh, I'm asking it to write scripts in the examples directory and

**[01:30:05]** scripts in the examples directory and

**[01:30:05]** scripts in the examples directory and then it will execute those scripts to

**[01:30:07]** then it will execute those scripts to

**[01:30:07]** then it will execute those scripts to help me with my queries, right? Um, and

**[01:30:10]** help me with my queries, right? Um, and

**[01:30:10]** help me with my queries, right? Um, and I give it some example scripts. It

**[01:30:12]** I give it some example scripts. It

**[01:30:12]** I give it some example scripts. It doesn't always need all this

**[01:30:13]** doesn't always need all this

**[01:30:13]** doesn't always need all this information, right? Like, uh, but yeah,

**[01:30:15]** information, right? Like, uh, but yeah,

**[01:30:15]** information, right? Like, uh, but yeah, fetching Pokemon, listing the resources,

**[01:30:17]** fetching Pokemon, listing the resources,

**[01:30:17]** fetching Pokemon, listing the resources, getting data, things like that. So this

**[01:30:19]** getting data, things like that. So this

**[01:30:19]** getting data, things like that. So this is like my agent really. It's like a

**[01:30:22]** is like my agent really. It's like a

**[01:30:22]** is like my agent really. It's like a prompt I gave it to generate a

**[01:30:23]** prompt I gave it to generate a

**[01:30:24]** prompt I gave it to generate a TypeScript library and then this

**[01:30:25]** TypeScript library and then this

**[01:30:25]** TypeScript library and then this cloud.md and I I can chat with it in

**[01:30:27]** cloud.md and I I can chat with it in

**[01:30:27]** cloud.md and I I can chat with it in cloud code. I'll also show you a version

**[01:30:30]** cloud code. I'll also show you a version

**[01:30:30]** cloud code. I'll also show you a version of it that is just tools, right? So here

**[01:30:33]** of it that is just tools, right? So here

**[01:30:33]** of it that is just tools, right? So here I'm using the messages completion API,

**[01:30:36]** I'm using the messages completion API,

**[01:30:36]** I'm using the messages completion API, right? And I've given it a bunch of

**[01:30:38]** right? And I've given it a bunch of

**[01:30:38]** right? And I've given it a bunch of tools from the API. So like get Pokemon,

**[01:30:41]** tools from the API. So like get Pokemon,

**[01:30:41]** tools from the API. So like get Pokemon, get Pokemon species, uh get Pokemon

**[01:30:43]** get Pokemon species, uh get Pokemon

**[01:30:43]** get Pokemon species, uh get Pokemon ability, get Pokemon type, get move. So

**[01:30:46]** ability, get Pokemon type, get move. So

**[01:30:46]** ability, get Pokemon type, get move. So you've defined all of these tools and

**[01:30:48]** you've defined all of these tools and

**[01:30:48]** you've defined all of these tools and you can see that like you know I also

**[01:30:50]** you can see that like you know I also

**[01:30:50]** you can see that like you know I also just gave it a prompt and told it to

**[01:30:52]** just gave it a prompt and told it to

**[01:30:52]** just gave it a prompt and told it to make the tools. Um it doesn't want to

**[01:30:54]** make the tools. Um it doesn't want to

**[01:30:54]** make the tools. Um it doesn't want to make a 100 tools right like there's a

**[01:30:56]** make a 100 tools right like there's a

**[01:30:56]** make a 100 tools right like there's a ton of smoke on or sorry um pokey API


### [01:31:00 - 01:32:00]

**[01:31:00]** ton of smoke on or sorry um pokey API

**[01:31:00]** ton of smoke on or sorry um pokey API data. Um but like it you know there's

**[01:31:04]** data. Um but like it you know there's

**[01:31:04]** data. Um but like it you know there's only so many parameters it can do. So

**[01:31:06]** only so many parameters it can do. So

**[01:31:06]** only so many parameters it can do. So it's got this like tool call and now um

**[01:31:10]** it's got this like tool call and now um

**[01:31:10]** it's got this like tool call and now um and I I made like a little chat

**[01:31:12]** and I I made like a little chat

**[01:31:12]** and I I made like a little chat interface with it. Right. So let me now

**[01:31:14]** interface with it. Right. So let me now

**[01:31:14]** interface with it. Right. So let me now go here and say like uh this is my tool

**[01:31:19]** go here and say like uh this is my tool

**[01:31:19]** go here and say like uh this is my tool calling.

**[01:31:21]** calling.

**[01:31:21]** calling. Um

**[01:31:33]** great. So yeah, here we've got this

**[01:31:33]** great. So yeah, here we've got this chat.ts, right? Um

**[01:31:37]** chat.ts, right? Um

**[01:31:37]** chat.ts, right? Um I I use bun when I'm prototyping stuff

**[01:31:39]** I I use bun when I'm prototyping stuff

**[01:31:39]** I I use bun when I'm prototyping stuff just cuz like I don't want to compile

**[01:31:41]** just cuz like I don't want to compile

**[01:31:41]** just cuz like I don't want to compile from Typescript to JavaScript. Um and uh

**[01:31:45]** from Typescript to JavaScript. Um and uh

**[01:31:45]** from Typescript to JavaScript. Um and uh again bun has like linting built into

**[01:31:47]** again bun has like linting built into

**[01:31:47]** again bun has like linting built into it. Uh it's a way of like simplifying

**[01:31:49]** it. Uh it's a way of like simplifying

**[01:31:49]** it. Uh it's a way of like simplifying for the agent so the agent doesn't need

**[01:31:51]** for the agent so the agent doesn't need

**[01:31:51]** for the agent so the agent doesn't need to remember to compile but TypeScript is

**[01:31:53]** to remember to compile but TypeScript is

**[01:31:53]** to remember to compile but TypeScript is better for generation because it has

**[01:31:54]** better for generation because it has

**[01:31:54]** better for generation because it has types right. I'm going to start this

**[01:31:56]** types right. I'm going to start this

**[01:31:56]** types right. I'm going to start this like fun chat and then I'm going to try

**[01:31:58]** like fun chat and then I'm going to try

**[01:31:58]** like fun chat and then I'm going to try like, okay, what are the generation


### [01:32:00 - 01:33:00]

**[01:32:02]** like, okay, what are the generation

**[01:32:02]** like, okay, what are the generation two water Pokemon?

**[01:32:05]** two water Pokemon?

**[01:32:05]** two water Pokemon? Um, and you'll see that it's it's

**[01:32:08]** Um, and you'll see that it's it's

**[01:32:08]** Um, and you'll see that it's it's starting to like search and I'm logging

**[01:32:11]** starting to like search and I'm logging

**[01:32:11]** starting to like search and I'm logging all the tool calls here. This is very

**[01:32:12]** all the tool calls here. This is very

**[01:32:12]** all the tool calls here. This is very very important, right? Because like it

**[01:32:14]** very important, right? Because like it

**[01:32:14]** very important, right? Because like it needs to like do the tool calls. And so

**[01:32:16]** needs to like do the tool calls. And so

**[01:32:16]** needs to like do the tool calls. And so you can see that what it's doing is like

**[01:32:18]** you can see that what it's doing is like

**[01:32:18]** you can see that what it's doing is like it's searching a bunch of Pokemon. Um,

**[01:32:21]** it's searching a bunch of Pokemon. Um,

**[01:32:21]** it's searching a bunch of Pokemon. Um, and then it told me, okay, here are the

**[01:32:23]** and then it told me, okay, here are the

**[01:32:23]** and then it told me, okay, here are the water Pokemon for Gen 2, right? It's got

**[01:32:25]** water Pokemon for Gen 2, right? It's got

**[01:32:26]** water Pokemon for Gen 2, right? It's got Toadile, Crocenoff, or alligator. You

**[01:32:28]** Toadile, Crocenoff, or alligator. You

**[01:32:28]** Toadile, Crocenoff, or alligator. You can see sort of like how it's thought

**[01:32:30]** can see sort of like how it's thought

**[01:32:30]** can see sort of like how it's thought like in between each step, it's thinking

**[01:32:32]** like in between each step, it's thinking

**[01:32:32]** like in between each step, it's thinking through um the previous steps. Right

**[01:32:36]** through um the previous steps. Right

**[01:32:36]** through um the previous steps. Right now, like let's say that I want to do

**[01:32:39]** now, like let's say that I want to do

**[01:32:39]** now, like let's say that I want to do with claw code. I think I might need to

**[01:32:43]** with claw code. I think I might need to

**[01:32:43]** with claw code. I think I might need to >> uh

**[01:32:45]** >> uh

**[01:32:45]** >> uh I need to delete this example.

**[01:32:47]** I need to delete this example.

**[01:32:47]** I need to delete this example. >> Um Oh, yeah.

**[01:32:49]** >> Um Oh, yeah.

**[01:32:49]** >> Um Oh, yeah. >> Small question. How do you log the the

**[01:32:52]** >> Small question. How do you log the the

**[01:32:52]** >> Small question. How do you log the the tool calls? It's like there's just an

**[01:32:55]** tool calls? It's like there's just an

**[01:32:55]** tool calls? It's like there's just an argument you can

**[01:32:55]** argument you can

**[01:32:55]** argument you can >> Oh yeah, this is um this is like in the

**[01:32:59]** >> Oh yeah, this is um this is like in the

**[01:32:59]** >> Oh yeah, this is um this is like in the normal API, right? So I just like uh in


### [01:33:00 - 01:34:00]

**[01:33:03]** normal API, right? So I just like uh in

**[01:33:03]** normal API, right? So I just like uh in the model every time it logs it, I just

**[01:33:05]** the model every time it logs it, I just

**[01:33:05]** the model every time it logs it, I just call this this is in the like normal

**[01:33:07]** call this this is in the like normal

**[01:33:07]** call this this is in the like normal anthropic API um in the SDK. I I'll get

**[01:33:12]** anthropic API um in the SDK. I I'll get

**[01:33:12]** anthropic API um in the SDK. I I'll get back to get to the SDK. Um it's just

**[01:33:14]** back to get to the SDK. Um it's just

**[01:33:14]** back to get to the SDK. Um it's just like you just log every system message.

**[01:33:16]** like you just log every system message.

**[01:33:16]** like you just log every system message. So, um, just doing it in console logs.

**[01:33:19]** So, um, just doing it in console logs.

**[01:33:19]** So, um, just doing it in console logs. Does that make sense or Yeah. Okay.

**[01:33:22]** Does that make sense or Yeah. Okay.

**[01:33:22]** Does that make sense or Yeah. Okay. Yeah.

**[01:33:22]** Yeah.

**[01:33:22]** Yeah. >> So, so that chat interface you were

**[01:33:24]** >> So, so that chat interface you were

**[01:33:24]** >> So, so that chat interface you were showing, is that just using the regular

**[01:33:25]** showing, is that just using the regular

**[01:33:25]** showing, is that just using the regular API or

**[01:33:26]** API or

**[01:33:26]** API or >> Yeah, that's using the regular API.

**[01:33:27]** >> Yeah, that's using the regular API.

**[01:33:27]** >> Yeah, that's using the regular API. >> So, not the agent SK,

**[01:33:28]** >> So, not the agent SK,

**[01:33:28]** >> So, not the agent SK, >> not the agent SDK. Yeah. Yeah. And so,

**[01:33:31]** >> not the agent SDK. Yeah. Yeah. And so,

**[01:33:31]** >> not the agent SDK. Yeah. Yeah. And so, what I'm going to do here is um here I'm

**[01:33:34]** what I'm going to do here is um here I'm

**[01:33:34]** what I'm going to do here is um here I'm going to delete the script

**[01:33:36]** going to delete the script

**[01:33:36]** going to delete the script because I don't want it to cheat. Um,

**[01:33:39]** because I don't want it to cheat. Um,

**[01:33:39]** because I don't want it to cheat. Um, but okay. So, here you know that um I've

**[01:33:43]** but okay. So, here you know that um I've

**[01:33:43]** but okay. So, here you know that um I've I'm just opening cloud code. I've

**[01:33:45]** I'm just opening cloud code. I've

**[01:33:45]** I'm just opening cloud code. I've created a bunch of files here. I'm going

**[01:33:47]** created a bunch of files here. I'm going

**[01:33:47]** created a bunch of files here. I'm going to say like, can you tell me all the

**[01:33:49]** to say like, can you tell me all the

**[01:33:49]** to say like, can you tell me all the generation 2 water Pokemon?

**[01:33:52]** generation 2 water Pokemon?

**[01:33:52]** generation 2 water Pokemon? Um, and then we'll see what it can do,

**[01:33:54]** Um, and then we'll see what it can do,

**[01:33:54]** Um, and then we'll see what it can do, right? So, um, [clears throat] I forget

**[01:33:57]** right? So, um, [clears throat] I forget

**[01:33:57]** right? So, um, [clears throat] I forget if I need to prompt it to write a script

**[01:33:58]** if I need to prompt it to write a script

**[01:33:58]** if I need to prompt it to write a script or something. I think it'll be fine.


### [01:34:00 - 01:35:00]

**[01:34:00]** or something. I think it'll be fine.

**[01:34:00]** or something. I think it'll be fine. We'll see what happens.

**[01:34:00]** We'll see what happens.

**[01:34:00]** We'll see what happens. >> Do you mind going to the core SDK file

**[01:34:03]** >> Do you mind going to the core SDK file

**[01:34:03]** >> Do you mind going to the core SDK file and just showing you talked about

**[01:34:05]** and just showing you talked about

**[01:34:05]** and just showing you talked about getting context and then action and then

**[01:34:07]** getting context and then action and then

**[01:34:07]** getting context and then action and then verification? Can you show that in the

**[01:34:09]** verification? Can you show that in the

**[01:34:10]** verification? Can you show that in the code and how we're configuring the tool

**[01:34:12]** code and how we're configuring the tool

**[01:34:12]** code and how we're configuring the tool description?

**[01:34:13]** description?

**[01:34:13]** description? >> Yeah. So, uh, we haven't done the SDK

**[01:34:17]** >> Yeah. So, uh, we haven't done the SDK

**[01:34:17]** >> Yeah. So, uh, we haven't done the SDK part yet. So, so far I've just put put

**[01:34:20]** part yet. So, so far I've just put put

**[01:34:20]** part yet. So, so far I've just put put some APIs in cloud code. Yeah. Yeah.

**[01:34:23]** some APIs in cloud code. Yeah. Yeah.

**[01:34:23]** some APIs in cloud code. Yeah. Yeah. >> Sorry, I thought I missed that. That's

**[01:34:25]** >> Sorry, I thought I missed that. That's

**[01:34:25]** >> Sorry, I thought I missed that. That's >> Yeah. Yeah. Yeah. Of course. Okay. Um,

**[01:34:27]** >> Yeah. Yeah. Yeah. Of course. Okay. Um,

**[01:34:28]** >> Yeah. Yeah. Yeah. Of course. Okay. Um, but yeah. So, okay. You can see here um

**[01:34:31]** but yeah. So, okay. You can see here um

**[01:34:31]** but yeah. So, okay. You can see here um it's it's given me a lot more, right?

**[01:34:33]** it's it's given me a lot more, right?

**[01:34:33]** it's it's given me a lot more, right? And um

**[01:34:41]** >> yeah, it's given me a lot more. So, it

**[01:34:41]** >> yeah, it's given me a lot more. So, it it it's it's saying there's 20 water

**[01:34:43]** it it's it's saying there's 20 water

**[01:34:43]** it it's it's saying there's 20 water Pokemon, right? And I think this is

**[01:34:45]** Pokemon, right? And I think this is

**[01:34:45]** Pokemon, right? And I think this is roughly right. I've like um

**[01:34:49]** roughly right. I've like um

**[01:34:49]** roughly right. I've like um uh what did it do?

**[01:34:56]** I think it just knows. Okay.

**[01:34:56]** I think it just knows. Okay. That's funny. Live this. Um


### [01:35:00 - 01:36:00]

**[01:35:07]** um anyways uh

**[01:35:07]** um anyways uh yeah Pokemon is slightly in distribution

**[01:35:09]** yeah Pokemon is slightly in distribution

**[01:35:09]** yeah Pokemon is slightly in distribution which is which is I I guess good

**[01:35:12]** which is which is I I guess good

**[01:35:12]** which is which is I I guess good [laughter]

**[01:35:13]** [laughter]

**[01:35:13]** [laughter] um but yeah so like what what it will do

**[01:35:16]** um but yeah so like what what it will do

**[01:35:16]** um but yeah so like what what it will do is like it will try and like write like

**[01:35:17]** is like it will try and like write like

**[01:35:18]** is like it will try and like write like a script and uh because you don't want

**[01:35:20]** a script and uh because you don't want

**[01:35:20]** a script and uh because you don't want it to think as much right so here it's

**[01:35:22]** it to think as much right so here it's

**[01:35:22]** it to think as much right so here it's like okay what I'm going to do is

**[01:35:26]** like okay what I'm going to do is

**[01:35:26]** like okay what I'm going to do is um let's see gen two water type Pokemon

**[01:35:30]** um let's see gen two water type Pokemon

**[01:35:30]** um let's see gen two water type Pokemon and where is it?

**[01:35:36]** Okay. So, yeah, you can see here it

**[01:35:36]** Okay. So, yeah, you can see here it knows like, okay, the start of the

**[01:35:38]** knows like, okay, the start of the

**[01:35:38]** knows like, okay, the start of the generations. It fetches these uh per

**[01:35:41]** generations. It fetches these uh per

**[01:35:41]** generations. It fetches these uh per API. Um I guess this decided not to use

**[01:35:44]** API. Um I guess this decided not to use

**[01:35:44]** API. Um I guess this decided not to use like my pre-built API here. Um

**[01:35:48]** like my pre-built API here. Um

**[01:35:48]** like my pre-built API here. Um and then uh yeah, and and then runs it,

**[01:35:51]** and then uh yeah, and and then runs it,

**[01:35:51]** and then uh yeah, and and then runs it, right? So, um I think I need to like

**[01:35:54]** right? So, um I think I need to like

**[01:35:54]** right? So, um I think I need to like improve the cloud. MV for this. But

**[01:35:55]** improve the cloud. MV for this. But

**[01:35:55]** improve the cloud. MV for this. But anyways, you can see that like it's able

**[01:35:58]** anyways, you can see that like it's able

**[01:35:58]** anyways, you can see that like it's able to like check 200 plus Pokémon and then


### [01:36:00 - 01:37:00]

**[01:36:02]** to like check 200 plus Pokémon and then

**[01:36:02]** to like check 200 plus Pokémon and then check for their type and and you know

**[01:36:04]** check for their type and and you know

**[01:36:04]** check for their type and and you know get their get their information, right?

**[01:36:05]** get their get their information, right?

**[01:36:05]** get their get their information, right? So this is like uh just a quick example

**[01:36:09]** So this is like uh just a quick example

**[01:36:09]** So this is like uh just a quick example on like how to do codegen and how to use

**[01:36:10]** on like how to do codegen and how to use

**[01:36:10]** on like how to do codegen and how to use cloud code to do it, right? So um we'll

**[01:36:14]** cloud code to do it, right? So um we'll

**[01:36:14]** cloud code to do it, right? So um we'll run this script and then like uh um like

**[01:36:18]** run this script and then like uh um like

**[01:36:18]** run this script and then like uh um like keep going, right? So, uh it will give

**[01:36:21]** keep going, right? So, uh it will give

**[01:36:21]** keep going, right? So, uh it will give me the output and um yeah, basically

**[01:36:25]** me the output and um yeah, basically

**[01:36:25]** me the output and um yeah, basically what I want to show, let's see, we have

**[01:36:28]** what I want to show, let's see, we have

**[01:36:28]** what I want to show, let's see, we have roughly 15 minutes left. Um

**[01:36:33]** roughly 15 minutes left. Um

**[01:36:33]** roughly 15 minutes left. Um >> play Pokemon.

**[01:36:34]** >> play Pokemon.

**[01:36:34]** >> play Pokemon. >> The time play Pokemon. Yeah. Yeah.

**[01:36:35]** >> The time play Pokemon. Yeah. Yeah.

**[01:36:35]** >> The time play Pokemon. Yeah. Yeah. Actually, this is one of the demos I was

**[01:36:37]** Actually, this is one of the demos I was

**[01:36:37]** Actually, this is one of the demos I was thinking of doing. Um Cloud Code plays

**[01:36:40]** thinking of doing. Um Cloud Code plays

**[01:36:40]** thinking of doing. Um Cloud Code plays Pokemon. So, like let's say you want to

**[01:36:41]** Pokemon. So, like let's say you want to

**[01:36:42]** Pokemon. So, like let's say you want to do like an agentic version of Cloud

**[01:36:44]** do like an agentic version of Cloud

**[01:36:44]** do like an agentic version of Cloud Plays Pokemon. How would you do it?

**[01:36:46]** Plays Pokemon. How would you do it?

**[01:36:46]** Plays Pokemon. How would you do it? um

**[01:36:47]** um

**[01:36:47]** um what you would do I think is like you

**[01:36:49]** what you would do I think is like you

**[01:36:49]** what you would do I think is like you would give it access to the internal

**[01:36:52]** would give it access to the internal

**[01:36:52]** would give it access to the internal memory of the uh the ROM right and so

**[01:36:56]** memory of the uh the ROM right and so

**[01:36:56]** memory of the uh the ROM right and so let's say that it wanted to find its

**[01:36:58]** let's say that it wanted to find its

**[01:36:58]** let's say that it wanted to find its party it could search that in memory and


### [01:37:00 - 01:38:00]

**[01:37:00]** party it could search that in memory and

**[01:37:00]** party it could search that in memory and Pokémon Red is like a very well in

**[01:37:02]** Pokémon Red is like a very well in

**[01:37:02]** Pokémon Red is like a very well in distribution uh reverse engineered uh

**[01:37:05]** distribution uh reverse engineered uh

**[01:37:05]** distribution uh reverse engineered uh game right and so it could search in

**[01:37:07]** game right and so it could search in

**[01:37:07]** game right and so it could search in memory to be like hey these are the

**[01:37:09]** memory to be like hey these are the

**[01:37:09]** memory to be like hey these are the Pokemon um these are like this is how I

**[01:37:12]** Pokemon um these are like this is how I

**[01:37:12]** Pokemon um these are like this is how I figure out where the map is this how I

**[01:37:14]** figure out where the map is this how I

**[01:37:14]** figure out where the map is this how I navigate it right so this is like maybe

**[01:37:16]** navigate it right so this is like maybe

**[01:37:16]** navigate it right so this is like maybe exercise to the reader if you want to

**[01:37:18]** exercise to the reader if you want to

**[01:37:18]** exercise to the reader if you want to try it out. It's like um there is like a

**[01:37:20]** try it out. It's like um there is like a

**[01:37:20]** try it out. It's like um there is like a no.js GBA emulator. Um I think I have to

**[01:37:24]** no.js GBA emulator. Um I think I have to

**[01:37:24]** no.js GBA emulator. Um I think I have to legally say you have to go buy Pokemon

**[01:37:26]** legally say you have to go buy Pokemon

**[01:37:26]** legally say you have to go buy Pokemon Red and try it. Um but yeah, I think

**[01:37:29]** Red and try it. Um but yeah, I think

**[01:37:29]** Red and try it. Um but yeah, I think like uh yeah, good example. Anyways,

**[01:37:32]** like uh yeah, good example. Anyways,

**[01:37:32]** like uh yeah, good example. Anyways, here so it's it's fetched all of them

**[01:37:34]** here so it's it's fetched all of them

**[01:37:34]** here so it's it's fetched all of them and it's listed all their types and um

**[01:37:37]** and it's listed all their types and um

**[01:37:37]** and it's listed all their types and um yeah, you can see how it's like used

**[01:37:39]** yeah, you can see how it's like used

**[01:37:39]** yeah, you can see how it's like used code generation to do this, right? So um

**[01:37:41]** code generation to do this, right? So um

**[01:37:41]** code generation to do this, right? So um a quick example of using cloud code to

**[01:37:43]** a quick example of using cloud code to

**[01:37:43]** a quick example of using cloud code to prototype this. Um now there can be like

**[01:37:46]** prototype this. Um now there can be like

**[01:37:46]** prototype this. Um now there can be like more interesting like data here. So um I

**[01:37:51]** more interesting like data here. So um I

**[01:37:51]** more interesting like data here. So um I do want to leave time for example. So I

**[01:37:53]** do want to leave time for example. So I

**[01:37:53]** do want to leave time for example. So I think I'll just sort of like for

**[01:37:54]** think I'll just sort of like for

**[01:37:54]** think I'll just sort of like for questions. So I'll just sort of go

**[01:37:56]** questions. So I'll just sort of go

**[01:37:56]** questions. So I'll just sort of go through like an example. Let's say

**[01:37:59]** through like an example. Let's say

**[01:37:59]** through like an example. Let's say you're making competitive Pokemon.


### [01:38:00 - 01:39:00]

**[01:38:00]** you're making competitive Pokemon.

**[01:38:00]** you're making competitive Pokemon. Competitive Pokemon has a lot of

**[01:38:02]** Competitive Pokemon has a lot of

**[01:38:02]** Competitive Pokemon has a lot of different variables and data. So, this

**[01:38:04]** different variables and data. So, this

**[01:38:04]** different variables and data. So, this is like a a

**[01:38:07]** is like a a

**[01:38:07]** is like a a text file from this online like a

**[01:38:10]** text file from this online like a

**[01:38:10]** text file from this online like a library basically which stores like all

**[01:38:13]** library basically which stores like all

**[01:38:13]** library basically which stores like all of the Pokemon and their like moves and

**[01:38:17]** of the Pokemon and their like moves and

**[01:38:17]** of the Pokemon and their like moves and who they work well with and don't work

**[01:38:19]** who they work well with and don't work

**[01:38:19]** who they work well with and don't work well with and you know like who they're

**[01:38:22]** well with and you know like who they're

**[01:38:22]** well with and you know like who they're countered by and all of these things,

**[01:38:23]** countered by and all of these things,

**[01:38:23]** countered by and all of these things, right? So, there's a ton of data here,

**[01:38:25]** right? So, there's a ton of data here,

**[01:38:25]** right? So, there's a ton of data here, right? And it's all in text file. Um,

**[01:38:28]** right? And it's all in text file. Um,

**[01:38:28]** right? And it's all in text file. Um, which is actually pretty good for cloud

**[01:38:30]** which is actually pretty good for cloud

**[01:38:30]** which is actually pretty good for cloud code, right? because I can say like,

**[01:38:31]** code, right? because I can say like,

**[01:38:31]** code, right? because I can say like, okay, um, hey, I'm going to give it a

**[01:38:34]** okay, um, hey, I'm going to give it a

**[01:38:34]** okay, um, hey, I'm going to give it a little bit more data. Normally, I put

**[01:38:35]** little bit more data. Normally, I put

**[01:38:35]** little bit more data. Normally, I put this in the, um, check the data folder.

**[01:38:39]** this in the, um, check the data folder.

**[01:38:39]** this in the, um, check the data folder. Tell me,

**[01:38:41]** Tell me,

**[01:38:41]** Tell me, I I want to make a team around Venusaur.

**[01:38:46]** I I want to make a team around Venusaur.

**[01:38:46]** I I want to make a team around Venusaur. Can you give me some suggestions based

**[01:38:49]** Can you give me some suggestions based

**[01:38:49]** Can you give me some suggestions based on the Smogon data? Um,

**[01:38:53]** on the Smogon data? Um,

**[01:38:53]** on the Smogon data? Um, and Smoke on is like this online API.

**[01:38:55]** and Smoke on is like this online API.

**[01:38:55]** and Smoke on is like this online API. And so I'm I'm not entirely sure what

**[01:38:56]** And so I'm I'm not entirely sure what

**[01:38:56]** And so I'm I'm not entirely sure what it'll do here yet. I haven't done this

**[01:38:59]** it'll do here yet. I haven't done this

**[01:38:59]** it'll do here yet. I haven't done this query before. Uh, but we'll see. I think


### [01:39:00 - 01:40:00]

**[01:39:01]** query before. Uh, but we'll see. I think

**[01:39:01]** query before. Uh, but we'll see. I think it'll be it'll be fun. Um,

**[01:39:05]** it'll be it'll be fun. Um,

**[01:39:05]** it'll be it'll be fun. Um, where am I? Oh, I see.

**[01:39:16]** Um, yeah. But what I wanted to do is

**[01:39:16]** Um, yeah. But what I wanted to do is sort of grapple through this this data,

**[01:39:19]** sort of grapple through this this data,

**[01:39:19]** sort of grapple through this this data, right? And and sort of figure out from

**[01:39:21]** right? And and sort of figure out from

**[01:39:21]** right? And and sort of figure out from itself from first principles, not having

**[01:39:23]** itself from first principles, not having

**[01:39:23]** itself from first principles, not having seen this data before, how can I like

**[01:39:25]** seen this data before, how can I like

**[01:39:25]** seen this data before, how can I like answer my query, right? So um while it

**[01:39:28]** answer my query, right? So um while it

**[01:39:28]** answer my query, right? So um while it does does that I'll I'll take any

**[01:39:30]** does does that I'll I'll take any

**[01:39:30]** does does that I'll I'll take any questions. Yeah.

**[01:39:31]** questions. Yeah.

**[01:39:32]** questions. Yeah. >> Um first of all great work job. Uh so

**[01:39:35]** >> Um first of all great work job. Uh so

**[01:39:35]** >> Um first of all great work job. Uh so this is like really on top of cloud code

**[01:39:37]** this is like really on top of cloud code

**[01:39:38]** this is like really on top of cloud code >> and so my question is if we were to

**[01:39:41]** >> and so my question is if we were to

**[01:39:41]** >> and so my question is if we were to deploy this customer basically

**[01:39:43]** deploy this customer basically

**[01:39:44]** deploy this customer basically >> are we supposed to have cloud code

**[01:39:45]** >> are we supposed to have cloud code

**[01:39:46]** >> are we supposed to have cloud code running in like a like a swarm or are we

**[01:39:49]** running in like a like a swarm or are we

**[01:39:49]** running in like a like a swarm or are we somehow able to take the cloud code part

**[01:39:51]** somehow able to take the cloud code part

**[01:39:51]** somehow able to take the cloud code part out just bot and the agent SDK?

**[01:39:55]** out just bot and the agent SDK?

**[01:39:55]** out just bot and the agent SDK? >> Yeah. So, let me show you like very

**[01:39:57]** >> Yeah. So, let me show you like very

**[01:39:57]** >> Yeah. So, let me show you like very quickly like what the what it looks like


### [01:40:00 - 01:41:00]

**[01:40:00]** quickly like what the what it looks like

**[01:40:00]** quickly like what the what it looks like to use the agent SDK here. Um, so I've

**[01:40:04]** to use the agent SDK here. Um, so I've

**[01:40:04]** to use the agent SDK here. Um, so I've already done this file system, right?

**[01:40:06]** already done this file system, right?

**[01:40:06]** already done this file system, right? And again, I want you to think about the

**[01:40:08]** And again, I want you to think about the

**[01:40:08]** And again, I want you to think about the file system as a way of doing context

**[01:40:09]** file system as a way of doing context

**[01:40:10]** file system as a way of doing context engineering, right? Like this is like a

**[01:40:11]** engineering, right? Like this is like a

**[01:40:11]** engineering, right? Like this is like a lot of the inputs into the agent. So, my

**[01:40:13]** lot of the inputs into the agent. So, my

**[01:40:13]** lot of the inputs into the agent. So, my actual agent file is like 50 lines,

**[01:40:15]** actual agent file is like 50 lines,

**[01:40:15]** actual agent file is like 50 lines, right? Um, and it's mostly just like

**[01:40:18]** right? Um, and it's mostly just like

**[01:40:18]** right? Um, and it's mostly just like random like boiler plate, right? Like I

**[01:40:21]** random like boiler plate, right? Like I

**[01:40:21]** random like boiler plate, right? Like I guess, yeah, it's decided to stop it

**[01:40:23]** guess, yeah, it's decided to stop it

**[01:40:23]** guess, yeah, it's decided to stop it from

**[01:40:25]** from

**[01:40:25]** from uh writing scripts outside of the custom

**[01:40:27]** uh writing scripts outside of the custom

**[01:40:27]** uh writing scripts outside of the custom scripts directory. Again, fully

**[01:40:29]** scripts directory. Again, fully

**[01:40:29]** scripts directory. Again, fully backcoded. So, um yeah, you can see like

**[01:40:32]** backcoded. So, um yeah, you can see like

**[01:40:32]** backcoded. So, um yeah, you can see like it just runs this query, takes in the

**[01:40:34]** it just runs this query, takes in the

**[01:40:34]** it just runs this query, takes in the working directory

**[01:40:36]** working directory

**[01:40:36]** working directory um and uh like like runs it in a loop,

**[01:40:39]** um and uh like like runs it in a loop,

**[01:40:39]** um and uh like like runs it in a loop, right? And so probably I'd want to like

**[01:40:42]** right? And so probably I'd want to like

**[01:40:42]** right? And so probably I'd want to like turn into like some allowed tools here

**[01:40:44]** turn into like some allowed tools here

**[01:40:44]** turn into like some allowed tools here and stuff, but it it's very simple. And

**[01:40:46]** and stuff, but it it's very simple. And

**[01:40:46]** and stuff, but it it's very simple. And and so um if I were to like

**[01:40:49]** and so um if I were to like

**[01:40:49]** and so um if I were to like productionize this, the first step I do

**[01:40:51]** productionize this, the first step I do

**[01:40:51]** productionize this, the first step I do is like okay, I I've tested it on cloud

**[01:40:54]** is like okay, I I've tested it on cloud

**[01:40:54]** is like okay, I I've tested it on cloud cloud code. It seems to do pretty well.

**[01:40:56]** cloud code. It seems to do pretty well.

**[01:40:56]** cloud code. It seems to do pretty well. I write this file. Then I put it there

**[01:40:59]** I write this file. Then I put it there

**[01:40:59]** I write this file. Then I put it there are two ways to do it. So one is I do


### [01:41:00 - 01:42:00]

**[01:41:01]** are two ways to do it. So one is I do

**[01:41:01]** are two ways to do it. So one is I do think that like local apps might be

**[01:41:05]** think that like local apps might be

**[01:41:05]** think that like local apps might be coming back with AI because I think that

**[01:41:07]** coming back with AI because I think that

**[01:41:07]** coming back with AI because I think that like there's such an overhead to running

**[01:41:09]** like there's such an overhead to running

**[01:41:09]** like there's such an overhead to running it. Like for example, cloud code is a

**[01:41:11]** it. Like for example, cloud code is a

**[01:41:11]** it. Like for example, cloud code is a front-end app, right? Like it works on

**[01:41:13]** front-end app, right? Like it works on

**[01:41:13]** front-end app, right? Like it works on your computer. So maybe the way I shift

**[01:41:15]** your computer. So maybe the way I shift

**[01:41:15]** your computer. So maybe the way I shift this as a Pokemon app is like hey I have

**[01:41:17]** this as a Pokemon app is like hey I have

**[01:41:17]** this as a Pokemon app is like hey I have like an app that you install and it

**[01:41:19]** like an app that you install and it

**[01:41:19]** like an app that you install and it works locally on your computer and

**[01:41:21]** works locally on your computer and

**[01:41:21]** works locally on your computer and writing scripts. I think that's one way

**[01:41:22]** writing scripts. I think that's one way

**[01:41:22]** writing scripts. I think that's one way of doing it, right? Um the other way is

**[01:41:25]** of doing it, right? Um the other way is

**[01:41:25]** of doing it, right? Um the other way is yeah you have you [clears throat] host

**[01:41:26]** yeah you have you [clears throat] host

**[01:41:26]** yeah you have you [clears throat] host it in a sandbox. Um and again there's a

**[01:41:29]** it in a sandbox. Um and again there's a

**[01:41:29]** it in a sandbox. Um and again there's a bunch of different sandbox providers

**[01:41:30]** bunch of different sandbox providers

**[01:41:30]** bunch of different sandbox providers that make it really easy like Cloudflare

**[01:41:33]** that make it really easy like Cloudflare

**[01:41:33]** that make it really easy like Cloudflare has a good example um of using the agent

**[01:41:35]** has a good example um of using the agent

**[01:41:35]** has a good example um of using the agent SDK and it's just like sandbox.st start

**[01:41:39]** SDK and it's just like sandbox.st start

**[01:41:39]** SDK and it's just like sandbox.st start you know and then like bun agent.ts ts

**[01:41:42]** you know and then like bun agent.ts ts

**[01:41:42]** you know and then like bun agent.ts ts and that's kind of all it takes, right?

**[01:41:44]** and that's kind of all it takes, right?

**[01:41:44]** and that's kind of all it takes, right? Like it's like like they've abstracted

**[01:41:46]** Like it's like like they've abstracted

**[01:41:46]** Like it's like like they've abstracted away a lot of it. Um so you run like the

**[01:41:48]** away a lot of it. Um so you run like the

**[01:41:48]** away a lot of it. Um so you run like the sandbox um and then you communicate with

**[01:41:51]** sandbox um and then you communicate with

**[01:41:51]** sandbox um and then you communicate with it and um yeah I think there is like

**[01:41:54]** it and um yeah I think there is like

**[01:41:54]** it and um yeah I think there is like some very interesting stuff that I'm not

**[01:41:56]** some very interesting stuff that I'm not

**[01:41:56]** some very interesting stuff that I'm not sure I had time to get to but um like I


### [01:42:00 - 01:43:00]

**[01:42:01]** sure I had time to get to but um like I

**[01:42:01]** sure I had time to get to but um like I I think some interesting questions are

**[01:42:03]** I think some interesting questions are

**[01:42:03]** I think some interesting questions are like um

**[01:42:05]** like um

**[01:42:05]** like um yeah like how do you do this sort of

**[01:42:07]** yeah like how do you do this sort of

**[01:42:07]** yeah like how do you do this sort of like service now you're just spinning up

**[01:42:08]** like service now you're just spinning up

**[01:42:08]** like service now you're just spinning up a sub like a sandbox per user. Um,

**[01:42:11]** a sub like a sandbox per user. Um,

**[01:42:11]** a sub like a sandbox per user. Um, there's a lot of like I'd say best

**[01:42:12]** there's a lot of like I'd say best

**[01:42:12]** there's a lot of like I'd say best practices to solve here. One thing I

**[01:42:15]** practices to solve here. One thing I

**[01:42:16]** practices to solve here. One thing I just want to call out for you guys to

**[01:42:17]** just want to call out for you guys to

**[01:42:17]** just want to call out for you guys to think about, um, if you're making a an

**[01:42:20]** think about, um, if you're making a an

**[01:42:20]** think about, um, if you're making a an agent with a UI, like let's say that you

**[01:42:22]** agent with a UI, like let's say that you

**[01:42:22]** agent with a UI, like let's say that you have, uh, yeah, my Pokemon agent and I

**[01:42:26]** have, uh, yeah, my Pokemon agent and I

**[01:42:26]** have, uh, yeah, my Pokemon agent and I wanted to have an UI that is adaptable

**[01:42:28]** wanted to have an UI that is adaptable

**[01:42:28]** wanted to have an UI that is adaptable to the user, right? Like maybe some

**[01:42:30]** to the user, right? Like maybe some

**[01:42:30]** to the user, right? Like maybe some users are doing team building, some

**[01:42:31]** users are doing team building, some

**[01:42:31]** users are doing team building, some users are helping it with their game,

**[01:42:33]** users are helping it with their game,

**[01:42:33]** users are helping it with their game, some users just want pictures of

**[01:42:35]** some users just want pictures of

**[01:42:35]** some users just want pictures of Pokemon. How would how would I have an

**[01:42:37]** Pokemon. How would how would I have an

**[01:42:37]** Pokemon. How would how would I have an agent that adapts in in real time to my

**[01:42:39]** agent that adapts in in real time to my

**[01:42:40]** agent that adapts in in real time to my user, right? Um the way I would do it is

**[01:42:42]** user, right? Um the way I would do it is

**[01:42:42]** user, right? Um the way I would do it is in my sandbox, I would have a dev

**[01:42:44]** in my sandbox, I would have a dev

**[01:42:44]** in my sandbox, I would have a dev server, right? And the dev server would

**[01:42:46]** server, right? And the dev server would

**[01:42:46]** server, right? And the dev server would expose a port. Um it would run on bun or

**[01:42:50]** expose a port. Um it would run on bun or

**[01:42:50]** expose a port. Um it would run on bun or node or something. It would like expose

**[01:42:52]** node or something. It would like expose

**[01:42:52]** node or something. It would like expose a port. The agent could edit code and it

**[01:42:54]** a port. The agent could edit code and it

**[01:42:54]** a port. The agent could edit code and it would live refresh and and your user

**[01:42:57]** would live refresh and and your user

**[01:42:57]** would live refresh and and your user would be interacting with that website.

**[01:42:58]** would be interacting with that website.

**[01:42:58]** would be interacting with that website. This is how a lot of like site builders


### [01:43:00 - 01:44:00]

**[01:43:00]** This is how a lot of like site builders

**[01:43:00]** This is how a lot of like site builders like lovable and stuff work, right? they

**[01:43:03]** like lovable and stuff work, right? they

**[01:43:03]** like lovable and stuff work, right? they they use sandboxes and they host

**[01:43:05]** they use sandboxes and they host

**[01:43:06]** they use sandboxes and they host essentially a dev server. And so

**[01:43:08]** essentially a dev server. And so

**[01:43:08]** essentially a dev server. And so thinking about this for your users, if

**[01:43:10]** thinking about this for your users, if

**[01:43:10]** thinking about this for your users, if you want a customized interface, this is

**[01:43:12]** you want a customized interface, this is

**[01:43:12]** you want a customized interface, this is a great way to do it. Um, okay, let's

**[01:43:15]** a great way to do it. Um, okay, let's

**[01:43:15]** a great way to do it. Um, okay, let's see. Let's see what it did. Um,

**[01:43:27]** okay, cool. Okay. So, um it's like

**[01:43:27]** okay, cool. Okay. So, um it's like written this like script has generated

**[01:43:29]** written this like script has generated

**[01:43:30]** written this like script has generated like show me some base stats and

**[01:43:32]** like show me some base stats and

**[01:43:32]** like show me some base stats and suggested it a like um uh a move set and

**[01:43:37]** suggested it a like um uh a move set and

**[01:43:38]** suggested it a like um uh a move set and some teammates and you can see sort of

**[01:43:40]** some teammates and you can see sort of

**[01:43:40]** some teammates and you can see sort of like see what did it do? Um control E.

**[01:43:47]** like see what did it do? Um control E.

**[01:43:47]** like see what did it do? Um control E. Um

**[01:43:49]** Um

**[01:43:50]** Um yeah. Okay. Okay. So, you can see here

**[01:43:51]** yeah. Okay. Okay. So, you can see here

**[01:43:51]** yeah. Okay. Okay. So, you can see here what it started doing is like it started

**[01:43:52]** what it started doing is like it started

**[01:43:52]** what it started doing is like it started searching for Venusaur, right? And it

**[01:43:54]** searching for Venusaur, right? And it

**[01:43:54]** searching for Venusaur, right? And it started finding uh those types the like

**[01:43:58]** started finding uh those types the like

**[01:43:58]** started finding uh those types the like those Pokemon and when it does that it


### [01:44:00 - 01:45:00]

**[01:44:00]** those Pokemon and when it does that it

**[01:44:00]** those Pokemon and when it does that it also gets other Pokemon that mentioned

**[01:44:03]** also gets other Pokemon that mentioned

**[01:44:03]** also gets other Pokemon that mentioned Venusaur. So, it gets like its teammates

**[01:44:05]** Venusaur. So, it gets like its teammates

**[01:44:05]** Venusaur. So, it gets like its teammates and it counters and stuff, right? And

**[01:44:07]** and it counters and stuff, right? And

**[01:44:07]** and it counters and stuff, right? And it's sort of over this time found

**[01:44:10]** it's sort of over this time found

**[01:44:10]** it's sort of over this time found interesting Pokemon, right, that like it

**[01:44:12]** interesting Pokemon, right, that like it

**[01:44:12]** interesting Pokemon, right, that like it might work with, right? So, it's done a

**[01:44:13]** might work with, right? So, it's done a

**[01:44:13]** might work with, right? So, it's done a bunch of these searches and it's gone

**[01:44:15]** bunch of these searches and it's gone

**[01:44:15]** bunch of these searches and it's gone these profile. It's found most common

**[01:44:17]** these profile. It's found most common

**[01:44:17]** these profile. It's found most common teammates and and written a script to to

**[01:44:20]** teammates and and written a script to to

**[01:44:20]** teammates and and written a script to to analyze it, right? And so this is all

**[01:44:21]** analyze it, right? And so this is all

**[01:44:22]** analyze it, right? And so this is all based on a text file. Of course, I could

**[01:44:23]** based on a text file. Of course, I could

**[01:44:23]** based on a text file. Of course, I could have pre-processed a text file a little

**[01:44:25]** have pre-processed a text file a little

**[01:44:25]** have pre-processed a text file a little bit more. Um, but yeah, it's like done

**[01:44:29]** bit more. Um, but yeah, it's like done

**[01:44:29]** bit more. Um, but yeah, it's like done this sort of like interesting

**[01:44:32]** this sort of like interesting

**[01:44:32]** this sort of like interesting um analysis for me, right? And again,

**[01:44:34]** um analysis for me, right? And again,

**[01:44:34]** um analysis for me, right? And again, I'll I'll push out more code to the

**[01:44:35]** I'll I'll push out more code to the

**[01:44:35]** I'll I'll push out more code to the GitHub repo. And um I'll also tweet

**[01:44:38]** GitHub repo. And um I'll also tweet

**[01:44:38]** GitHub repo. And um I'll also tweet about this. I'm on Twitter. I'm uh

**[01:44:40]** about this. I'm on Twitter. I'm uh

**[01:44:40]** about this. I'm on Twitter. I'm uh TRQ212.

**[01:44:42]** TRQ212.

**[01:44:42]** TRQ212. Uh I tweet a lot. So, uh, definitely

**[01:44:44]** Uh I tweet a lot. So, uh, definitely

**[01:44:44]** Uh I tweet a lot. So, uh, definitely like mostly about agent SDK stuff. Um,

**[01:44:47]** like mostly about agent SDK stuff. Um,

**[01:44:47]** like mostly about agent SDK stuff. Um, but yeah, we have about 8 minutes left,

**[01:44:48]** but yeah, we have about 8 minutes left,

**[01:44:48]** but yeah, we have about 8 minutes left, so I want to spend the rest of time

**[01:44:50]** so I want to spend the rest of time

**[01:44:50]** so I want to spend the rest of time taking questions about kind of anything,

**[01:44:52]** taking questions about kind of anything,

**[01:44:52]** taking questions about kind of anything, you know, and I'm sorry we didn't get to

**[01:44:53]** you know, and I'm sorry we didn't get to

**[01:44:53]** you know, and I'm sorry we didn't get to do more prototyping. Um, but, uh, yeah,

**[01:44:57]** do more prototyping. Um, but, uh, yeah,

**[01:44:57]** do more prototyping. Um, but, uh, yeah, over there.

**[01:44:57]** over there.

**[01:44:58]** over there. >> Yeah, I was going to say it's a flaw

**[01:44:59]** >> Yeah, I was going to say it's a flaw

**[01:44:59]** >> Yeah, I was going to say it's a flaw play. Can you uh sort of plug this in


### [01:45:00 - 01:46:00]

**[01:45:01]** play. Can you uh sort of plug this in

**[01:45:01]** play. Can you uh sort of plug this in with that just to see if the agent will

**[01:45:03]** with that just to see if the agent will

**[01:45:03]** with that just to see if the agent will uh be more selective with the team it uh

**[01:45:05]** uh be more selective with the team it uh

**[01:45:05]** uh be more selective with the team it uh tries to capture?

**[01:45:06]** tries to capture?

**[01:45:06]** tries to capture? >> Yeah, put it in in Cloud Play's Pokemon.

**[01:45:08]** >> Yeah, put it in in Cloud Play's Pokemon.

**[01:45:08]** >> Yeah, put it in in Cloud Play's Pokemon. Yeah. Yeah, I do want to play CL

**[01:45:10]** Yeah. Yeah, I do want to play CL

**[01:45:10]** Yeah. Yeah, I do want to play CL codeplays Pokemon. I think that would be

**[01:45:11]** codeplays Pokemon. I think that would be

**[01:45:11]** codeplays Pokemon. I think that would be fun. Yeah. Yeah. I I think cloud plays

**[01:45:13]** fun. Yeah. Yeah. I I think cloud plays

**[01:45:13]** fun. Yeah. Yeah. I I think cloud plays Pokemon. I think we try and keep it like

**[01:45:14]** Pokemon. I think we try and keep it like

**[01:45:14]** Pokemon. I think we try and keep it like a pure reasoning task as much as

**[01:45:16]** a pure reasoning task as much as

**[01:45:16]** a pure reasoning task as much as possible. Yeah. Um other questions?

**[01:45:18]** possible. Yeah. Um other questions?

**[01:45:18]** possible. Yeah. Um other questions? Yeah.

**[01:45:19]** Yeah.

**[01:45:19]** Yeah. >> I was curious about how people are

**[01:45:20]** >> I was curious about how people are

**[01:45:20]** >> I was curious about how people are monetizing

**[01:45:21]** monetizing

**[01:45:22]** monetizing like

**[01:45:23]** like

**[01:45:23]** like you know kind of like

**[01:45:26]** you know kind of like

**[01:45:26]** you know kind of like you kind of like lose the opportunity to

**[01:45:27]** you kind of like lose the opportunity to

**[01:45:27]** you kind of like lose the opportunity to get all the margins.

**[01:45:30]** get all the margins.

**[01:45:30]** get all the margins. >> Yeah. I'm curious like

**[01:45:32]** >> Yeah. I'm curious like

**[01:45:32]** >> Yeah. I'm curious like shipping your own SDK so that they kind

**[01:45:35]** shipping your own SDK so that they kind

**[01:45:35]** shipping your own SDK so that they kind of take the usage base.

**[01:45:38]** of take the usage base.

**[01:45:38]** of take the usage base. >> Yeah. I I do think overall, especially

**[01:45:40]** >> Yeah. I I do think overall, especially

**[01:45:40]** >> Yeah. I I do think overall, especially right now, agents are kind of pricey,

**[01:45:43]** right now, agents are kind of pricey,

**[01:45:43]** right now, agents are kind of pricey, you know what I mean? Because like um

**[01:45:46]** you know what I mean? Because like um

**[01:45:46]** you know what I mean? Because like um the models are have just started to get

**[01:45:48]** the models are have just started to get

**[01:45:48]** the models are have just started to get agentic. We really focus on like having

**[01:45:50]** agentic. We really focus on like having

**[01:45:50]** agentic. We really focus on like having the most intelligent models, you know,

**[01:45:52]** the most intelligent models, you know,

**[01:45:52]** the most intelligent models, you know, and like you generally this is just like

**[01:45:55]** and like you generally this is just like

**[01:45:55]** and like you generally this is just like an overall like SAS business software

**[01:45:58]** an overall like SAS business software

**[01:45:58]** an overall like SAS business software thing. You'd rather charge fewer people


### [01:46:00 - 01:47:00]

**[01:46:00]** thing. You'd rather charge fewer people

**[01:46:00]** thing. You'd rather charge fewer people more money that really have like a hard

**[01:46:02]** more money that really have like a hard

**[01:46:02]** more money that really have like a hard problem, you know? And so I think this

**[01:46:04]** problem, you know? And so I think this

**[01:46:04]** problem, you know? And so I think this is still good. like you probably should

**[01:46:05]** is still good. like you probably should

**[01:46:06]** is still good. like you probably should find um you know these hard use cases

**[01:46:09]** find um you know these hard use cases

**[01:46:09]** find um you know these hard use cases but I would say like number one make

**[01:46:10]** but I would say like number one make

**[01:46:10]** but I would say like number one make sure you're solving a problem that

**[01:46:12]** sure you're solving a problem that

**[01:46:12]** sure you're solving a problem that people want to pay for right is like the

**[01:46:14]** people want to pay for right is like the

**[01:46:14]** people want to pay for right is like the number one step right and then number

**[01:46:16]** number one step right and then number

**[01:46:16]** number one step right and then number two um yeah I think you could do

**[01:46:19]** two um yeah I think you could do

**[01:46:19]** two um yeah I think you could do subscription or token based I I think

**[01:46:21]** subscription or token based I I think

**[01:46:21]** subscription or token based I I think this kind of comes down to like how much

**[01:46:23]** this kind of comes down to like how much

**[01:46:23]** this kind of comes down to like how much you expect people to use your product uh

**[01:46:25]** you expect people to use your product uh

**[01:46:26]** you expect people to use your product uh versus like how much you expect them to

**[01:46:28]** versus like how much you expect them to

**[01:46:28]** versus like how much you expect them to like use it occasionally like cloud code

**[01:46:30]** like use it occasionally like cloud code

**[01:46:30]** like use it occasionally like cloud code obviously people use a lot and in order

**[01:46:32]** obviously people use a lot and in order

**[01:46:32]** obviously people use a lot and in order to like we do a mix of like if we give

**[01:46:34]** to like we do a mix of like if we give

**[01:46:34]** to like we do a mix of like if we give you some rate limits and if you exceed

**[01:46:36]** you some rate limits and if you exceed

**[01:46:36]** you some rate limits and if you exceed it we do uh usage based pricing. Um I

**[01:46:41]** it we do uh usage based pricing. Um I

**[01:46:41]** it we do uh usage based pricing. Um I think that like yeah it's very like

**[01:46:43]** think that like yeah it's very like

**[01:46:43]** think that like yeah it's very like dependent on your own user base and kind

**[01:46:45]** dependent on your own user base and kind

**[01:46:45]** dependent on your own user base and kind of like what they will do but I will say

**[01:46:47]** of like what they will do but I will say

**[01:46:47]** of like what they will do but I will say monetization is something you should

**[01:46:49]** monetization is something you should

**[01:46:49]** monetization is something you should think about up front and design your you

**[01:46:52]** think about up front and design your you

**[01:46:52]** think about up front and design your you know agent around because it's hard to

**[01:46:55]** know agent around because it's hard to

**[01:46:55]** know agent around because it's hard to walk back these promises.

**[01:46:57]** walk back these promises.

**[01:46:57]** walk back these promises. Um, yeah, back there.

**[01:46:59]** Um, yeah, back there.

**[01:46:59]** Um, yeah, back there. >> I haven't heard you talk at all about


### [01:47:00 - 01:48:00]

**[01:47:01]** >> I haven't heard you talk at all about

**[01:47:01]** >> I haven't heard you talk at all about hooks and be curious to hear your take

**[01:47:03]** hooks and be curious to hear your take

**[01:47:03]** hooks and be curious to hear your take on how

**[01:47:05]** on how

**[01:47:05]** on how >> uh Yeah, there's so much to talk about.

**[01:47:07]** >> uh Yeah, there's so much to talk about.

**[01:47:07]** >> uh Yeah, there's so much to talk about. Um, hooks are great. We we do ship with

**[01:47:10]** Um, hooks are great. We we do ship with

**[01:47:10]** Um, hooks are great. We we do ship with hooks. Um, hooks are a way of doing

**[01:47:13]** hooks. Um, hooks are a way of doing

**[01:47:13]** hooks. Um, hooks are a way of doing deterministic verification in particular

**[01:47:16]** deterministic verification in particular

**[01:47:16]** deterministic verification in particular or inserting context. So, um, you know,

**[01:47:18]** or inserting context. So, um, you know,

**[01:47:18]** or inserting context. So, um, you know, we fire these hooks as events and you

**[01:47:20]** we fire these hooks as events and you

**[01:47:20]** we fire these hooks as events and you can register them in the in the agent

**[01:47:22]** can register them in the in the agent

**[01:47:22]** can register them in the in the agent SDK. There's like a guide on how to do

**[01:47:24]** SDK. There's like a guide on how to do

**[01:47:24]** SDK. There's like a guide on how to do that. Um, examples of things you might

**[01:47:26]** that. Um, examples of things you might

**[01:47:26]** that. Um, examples of things you might use hooks for is like for example, um,

**[01:47:29]** use hooks for is like for example, um,

**[01:47:29]** use hooks for is like for example, um, yeah, you can run it to verify the like

**[01:47:31]** yeah, you can run it to verify the like

**[01:47:31]** yeah, you can run it to verify the like a spreadsheet each time. Uh, you can

**[01:47:33]** a spreadsheet each time. Uh, you can

**[01:47:33]** a spreadsheet each time. Uh, you can also like let's say I'm working with an

**[01:47:35]** also like let's say I'm working with an

**[01:47:35]** also like let's say I'm working with an agent and, uh, I'm the agent is doing

**[01:47:38]** agent and, uh, I'm the agent is doing

**[01:47:38]** agent and, uh, I'm the agent is doing some spreadsheet operations and the user

**[01:47:39]** some spreadsheet operations and the user

**[01:47:39]** some spreadsheet operations and the user has also changed the spreadsheet. This

**[01:47:41]** has also changed the spreadsheet. This

**[01:47:41]** has also changed the spreadsheet. This is an interesting like place to use a

**[01:47:43]** is an interesting like place to use a

**[01:47:43]** is an interesting like place to use a hook because you can be like hey has

**[01:47:46]** hook because you can be like hey has

**[01:47:46]** hook because you can be like hey has after every tool call insert changes

**[01:47:48]** after every tool call insert changes

**[01:47:48]** after every tool call insert changes that the user has made uh and and so

**[01:47:51]** that the user has made uh and and so

**[01:47:51]** that the user has made uh and and so you're giving it kind of live context

**[01:47:53]** you're giving it kind of live context

**[01:47:53]** you're giving it kind of live context changes um in an interesting way. So um

**[01:47:57]** changes um in an interesting way. So um

**[01:47:57]** changes um in an interesting way. So um yeah I think uh uh yeah there there's


### [01:48:00 - 01:49:00]

**[01:48:01]** yeah I think uh uh yeah there there's

**[01:48:01]** yeah I think uh uh yeah there there's more stuff on like the docs about hooks

**[01:48:04]** more stuff on like the docs about hooks

**[01:48:04]** more stuff on like the docs about hooks um and happy to like talk about it

**[01:48:06]** um and happy to like talk about it

**[01:48:06]** um and happy to like talk about it afterwards as well. Yeah, more

**[01:48:08]** afterwards as well. Yeah, more

**[01:48:08]** afterwards as well. Yeah, more questions. Yeah.

**[01:48:10]** questions. Yeah.

**[01:48:10]** questions. Yeah. like I do

**[01:48:18]** in

**[01:48:18]** in >> I realize it's working.

**[01:48:19]** >> I realize it's working.

**[01:48:20]** >> I realize it's working. >> I want to take the same conversation

**[01:48:21]** >> I want to take the same conversation

**[01:48:21]** >> I want to take the same conversation that I've already done because I'm going

**[01:48:22]** that I've already done because I'm going

**[01:48:22]** that I've already done because I'm going through

**[01:48:24]** through

**[01:48:24]** through >> and convert that into a new

**[01:48:26]** >> and convert that into a new

**[01:48:26]** >> and convert that into a new >> okay

**[01:48:27]** >> okay

**[01:48:27]** >> okay >> which is that I followed a few steps now

**[01:48:29]** >> which is that I followed a few steps now

**[01:48:29]** >> which is that I followed a few steps now it's actually working but I don't want

**[01:48:30]** it's actually working but I don't want

**[01:48:30]** it's actually working but I don't want to rewrite all of the code to write

**[01:48:34]** to rewrite all of the code to write

**[01:48:34]** to rewrite all of the code to write [clears throat] it

**[01:48:36]** [clears throat] it

**[01:48:36]** [clears throat] it like because it works.

**[01:48:38]** like because it works.

**[01:48:38]** like because it works. >> Yeah. Sure. Yeah. So like let's say

**[01:48:40]** >> Yeah. Sure. Yeah. So like let's say

**[01:48:40]** >> Yeah. Sure. Yeah. So like let's say you've done this prototyping, you found

**[01:48:41]** you've done this prototyping, you found

**[01:48:41]** you've done this prototyping, you found something that works. What I would do is

**[01:48:42]** something that works. What I would do is

**[01:48:42]** something that works. What I would do is like I somewhere the cloud MD like

**[01:48:44]** like I somewhere the cloud MD like

**[01:48:44]** like I somewhere the cloud MD like obviously like when I tried doing this

**[01:48:47]** obviously like when I tried doing this

**[01:48:47]** obviously like when I tried doing this one time it like didn't use my API

**[01:48:49]** one time it like didn't use my API

**[01:48:49]** one time it like didn't use my API directly and it wrote JavaScript. I

**[01:48:51]** directly and it wrote JavaScript. I

**[01:48:51]** directly and it wrote JavaScript. I should have been more specific in my

**[01:48:52]** should have been more specific in my

**[01:48:52]** should have been more specific in my cloud. Mmd to be like hey you should use

**[01:48:54]** cloud. Mmd to be like hey you should use

**[01:48:54]** cloud. Mmd to be like hey you should use this. Um [snorts]

**[01:48:56]** this. Um [snorts]

**[01:48:56]** this. Um [snorts] I yeah I think like that's one thing. Um


### [01:49:00 - 01:50:00]

**[01:49:00]** I yeah I think like that's one thing. Um

**[01:49:00]** I yeah I think like that's one thing. Um the second thing is uh yeah do summarize

**[01:49:04]** the second thing is uh yeah do summarize

**[01:49:04]** the second thing is uh yeah do summarize in terms have the helper scripts that

**[01:49:07]** in terms have the helper scripts that

**[01:49:07]** in terms have the helper scripts that you need and then like write something

**[01:49:09]** you need and then like write something

**[01:49:09]** you need and then like write something like this agent.ts script for like to

**[01:49:12]** like this agent.ts script for like to

**[01:49:12]** like this agent.ts script for like to run the test again. Uh yeah more

**[01:49:14]** run the test again. Uh yeah more

**[01:49:14]** run the test again. Uh yeah more questions in the grade. Uh yeah, I just

**[01:49:17]** questions in the grade. Uh yeah, I just

**[01:49:17]** questions in the grade. Uh yeah, I just put it a Pokemon and I think it's lying

**[01:49:19]** put it a Pokemon and I think it's lying

**[01:49:19]** put it a Pokemon and I think it's lying about using the scripts answer. It tries

**[01:49:22]** about using the scripts answer. It tries

**[01:49:22]** about using the scripts answer. It tries a couple times like my SDK isn't very

**[01:49:24]** a couple times like my SDK isn't very

**[01:49:24]** a couple times like my SDK isn't very good it tries twice and then it's like

**[01:49:27]** good it tries twice and then it's like

**[01:49:27]** good it tries twice and then it's like oh here's your comparison table but it's

**[01:49:29]** oh here's your comparison table but it's

**[01:49:29]** oh here's your comparison table but it's just because it's a distribution. Do you

**[01:49:31]** just because it's a distribution. Do you

**[01:49:31]** just because it's a distribution. Do you have any advice for that kind of

**[01:49:32]** have any advice for that kind of

**[01:49:32]** have any advice for that kind of problem?

**[01:49:32]** problem?

**[01:49:32]** problem? >> Yeah, this is a good question and and

**[01:49:34]** >> Yeah, this is a good question and and

**[01:49:34]** >> Yeah, this is a good question and and you know like I'm I think there is some

**[01:49:36]** you know like I'm I think there is some

**[01:49:36]** you know like I'm I think there is some messiness, right? Like I I think one of

**[01:49:38]** messiness, right? Like I I think one of

**[01:49:38]** messiness, right? Like I I think one of the things if an agent knows an answer

**[01:49:42]** the things if an agent knows an answer

**[01:49:42]** the things if an agent knows an answer um and you want to like sort of like

**[01:49:43]** um and you want to like sort of like

**[01:49:43]** um and you want to like sort of like fight it kind of to be like okay like no

**[01:49:46]** fight it kind of to be like okay like no

**[01:49:46]** fight it kind of to be like okay like no it's generation 9 now and like Venusaur

**[01:49:48]** it's generation 9 now and like Venusaur

**[01:49:48]** it's generation 9 now and like Venusaur stats have changed and there's like this

**[01:49:50]** stats have changed and there's like this

**[01:49:50]** stats have changed and there's like this new like charact like um this is hard I

**[01:49:54]** new like charact like um this is hard I

**[01:49:54]** new like charact like um this is hard I actually think uh one of the ways of

**[01:49:56]** actually think uh one of the ways of

**[01:49:56]** actually think uh one of the ways of doing that is hooks. So you can say for

**[01:49:58]** doing that is hooks. So you can say for

**[01:49:58]** doing that is hooks. So you can say for example like hey uh don't if if you've


### [01:50:00 - 01:51:00]

**[01:50:01]** example like hey uh don't if if you've

**[01:50:01]** example like hey uh don't if if you've like returned a response without writing

**[01:50:05]** like returned a response without writing

**[01:50:05]** like returned a response without writing a script you know you can check that you

**[01:50:07]** a script you know you can check that you

**[01:50:07]** a script you know you can check that you can be like give feedback to bit like

**[01:50:08]** can be like give feedback to bit like

**[01:50:08]** can be like give feedback to bit like please make sure you write a script

**[01:50:10]** please make sure you write a script

**[01:50:10]** please make sure you write a script please make sure you read this data

**[01:50:12]** please make sure you read this data

**[01:50:12]** please make sure you read this data right and and you can use hooks to like

**[01:50:13]** right and and you can use hooks to like

**[01:50:13]** right and and you can use hooks to like give that feedback in in the same way

**[01:50:14]** give that feedback in in the same way

**[01:50:14]** give that feedback in in the same way that in cloud code uh we have these like

**[01:50:17]** that in cloud code uh we have these like

**[01:50:17]** that in cloud code uh we have these like rules like make sure you read a file

**[01:50:19]** rules like make sure you read a file

**[01:50:19]** rules like make sure you read a file before you write to it right so add some

**[01:50:21]** before you write to it right so add some

**[01:50:21]** before you write to it right so add some determinism uh it can definitely be like

**[01:50:23]** determinism uh it can definitely be like

**[01:50:23]** determinism uh it can definitely be like I said it's an art you know sometimes

**[01:50:25]** I said it's an art you know sometimes

**[01:50:25]** I said it's an art you know sometimes you know yeah maybe like like writing

**[01:50:28]** you know yeah maybe like like writing

**[01:50:28]** you know yeah maybe like like writing course I guess probably um [laughter]

**[01:50:31]** course I guess probably um [laughter]

**[01:50:31]** course I guess probably um [laughter] yeah and the gray

**[01:50:32]** yeah and the gray

**[01:50:32]** yeah and the gray >> how are you guys dealing with like large

**[01:50:34]** >> how are you guys dealing with like large

**[01:50:34]** >> how are you guys dealing with like large code bases I'm working like a 50 million

**[01:50:36]** code bases I'm working like a 50 million

**[01:50:36]** code bases I'm working like a 50 million plus code base and so

**[01:50:38]** plus code base and so

**[01:50:38]** plus code base and so >> bre tool doesn't work really

**[01:50:40]** >> bre tool doesn't work really

**[01:50:40]** >> bre tool doesn't work really >> um so I'm having to build like my own

**[01:50:42]** >> um so I'm having to build like my own

**[01:50:42]** >> um so I'm having to build like my own like semantic indexing type thing to

**[01:50:44]** like semantic indexing type thing to

**[01:50:44]** like semantic indexing type thing to kind of help with that right

**[01:50:46]** kind of help with that right

**[01:50:46]** kind of help with that right >> is there any kind of like addthropic

**[01:50:48]** >> is there any kind of like addthropic

**[01:50:48]** >> is there any kind of like addthropic maybe thinking about how that can be

**[01:50:50]** maybe thinking about how that can be

**[01:50:50]** maybe thinking about how that can be more native to the product like you know

**[01:50:52]** more native to the product like you know

**[01:50:52]** more native to the product like you know in a couple months is the thing I'm

**[01:50:53]** in a couple months is the thing I'm

**[01:50:53]** in a couple months is the thing I'm writing just going to go away or like

**[01:50:55]** writing just going to go away or like

**[01:50:55]** writing just going to go away or like how how do you guys think about

**[01:50:57]** how how do you guys think about

**[01:50:57]** how how do you guys think about Okay, your last question in a couple

**[01:50:58]** Okay, your last question in a couple

**[01:50:58]** Okay, your last question in a couple months is you're thinking to go away


### [01:51:00 - 01:52:00]

**[01:51:00]** months is you're thinking to go away

**[01:51:00]** months is you're thinking to go away generally. Yes. Yeah. [laughter] Anytime

**[01:51:02]** generally. Yes. Yeah. [laughter] Anytime

**[01:51:02]** generally. Yes. Yeah. [laughter] Anytime you ask about AI, yeah. Uh I think that

**[01:51:06]** you ask about AI, yeah. Uh I think that

**[01:51:06]** you ask about AI, yeah. Uh I think that um

**[01:51:07]** um

**[01:51:07]** um semantic search this is a cloud code

**[01:51:09]** semantic search this is a cloud code

**[01:51:09]** semantic search this is a cloud code question more than a security question,

**[01:51:11]** question more than a security question,

**[01:51:11]** question more than a security question, but happy to answer it. Like um we you

**[01:51:14]** but happy to answer it. Like um we you

**[01:51:14]** but happy to answer it. Like um we you know there are trade-offs of semantic

**[01:51:15]** know there are trade-offs of semantic

**[01:51:15]** know there are trade-offs of semantic search. It's more brittle. Um I think

**[01:51:17]** search. It's more brittle. Um I think

**[01:51:17]** search. It's more brittle. Um I think you have to like index and and and

**[01:51:19]** you have to like index and and and

**[01:51:19]** you have to like index and and and search and we it's not necessar the

**[01:51:22]** search and we it's not necessar the

**[01:51:22]** search and we it's not necessar the model is not trained on semantic search

**[01:51:24]** model is not trained on semantic search

**[01:51:24]** model is not trained on semantic search and so I think that's sort of like a

**[01:51:25]** and so I think that's sort of like a

**[01:51:25]** and so I think that's sort of like a problem like you know grap it's trained

**[01:51:27]** problem like you know grap it's trained

**[01:51:27]** problem like you know grap it's trained on because it's like it's easy to do

**[01:51:29]** on because it's like it's easy to do

**[01:51:29]** on because it's like it's easy to do that but like semantic search you're

**[01:51:31]** that but like semantic search you're

**[01:51:31]** that but like semantic search you're implementing your bespoke query um for

**[01:51:34]** implementing your bespoke query um for

**[01:51:34]** implementing your bespoke query um for like very large code bases you know we

**[01:51:36]** like very large code bases you know we

**[01:51:36]** like very large code bases you know we have lots of customers that work in

**[01:51:37]** have lots of customers that work in

**[01:51:37]** have lots of customers that work in large code bases I think what I've seen

**[01:51:40]** large code bases I think what I've seen

**[01:51:40]** large code bases I think what I've seen is sort of like they just do like good

**[01:51:43]** is sort of like they just do like good

**[01:51:43]** is sort of like they just do like good claw mds you start in you know trying

**[01:51:46]** claw mds you start in you know trying

**[01:51:46]** claw mds you start in you know trying Make sure you start in the directory you

**[01:51:48]** Make sure you start in the directory you

**[01:51:48]** Make sure you start in the directory you want, have like good like verification

**[01:51:50]** want, have like good like verification

**[01:51:50]** want, have like good like verification steps and hooks and links and things

**[01:51:52]** steps and hooks and links and things

**[01:51:52]** steps and hooks and links and things like that. And so u you know that's what

**[01:51:54]** like that. And so u you know that's what

**[01:51:54]** like that. And so u you know that's what we do. We don't have you know a custom

**[01:51:57]** we do. We don't have you know a custom

**[01:51:57]** we do. We don't have you know a custom we dog food clunk code, right? So um

**[01:51:59]** we dog food clunk code, right? So um

**[01:51:59]** we dog food clunk code, right? So um yeah.


### [01:52:00 - 01:53:00]

**[01:52:00]** yeah.

**[01:52:00]** yeah. >> Okay. Yeah. Last question.

**[01:52:02]** >> Okay. Yeah. Last question.

**[01:52:02]** >> Okay. Yeah. Last question. >> We have to close unfortunately actually.

**[01:52:04]** >> We have to close unfortunately actually.

**[01:52:04]** >> We have to close unfortunately actually. Give it up for Tariq everyone.

**[01:52:06]** Give it up for Tariq everyone.

**[01:52:06]** Give it up for Tariq everyone. [applause]

**[01:52:08]** [applause]

**[01:52:08]** [applause] [music]


