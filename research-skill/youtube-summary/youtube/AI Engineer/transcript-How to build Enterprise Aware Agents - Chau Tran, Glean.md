# How to build Enterprise Aware Agents - Chau Tran, Glean

**Video URL:** https://www.youtube.com/watch?v=hxFpUcvWPcU

---

## Full Transcript

### [00:00 - 01:00]

**[00:16]** Thanks Alex for the introduction. That

**[00:16]** Thanks Alex for the introduction. That was a very impressive LLM generated

**[00:18]** was a very impressive LLM generated

**[00:18]** was a very impressive LLM generated summary of me. Uh I've never heard it

**[00:21]** summary of me. Uh I've never heard it

**[00:21]** summary of me. Uh I've never heard it before but uh nice. Um so um today I'm

**[00:25]** before but uh nice. Um so um today I'm

**[00:25]** before but uh nice. Um so um today I'm going to talk to you about something

**[00:28]** going to talk to you about something

**[00:28]** going to talk to you about something that has been keeping me up at night. Uh

**[00:31]** that has been keeping me up at night. Uh

**[00:31]** that has been keeping me up at night. Uh probably some of you too. So how to

**[00:33]** probably some of you too. So how to

**[00:33]** probably some of you too. So how to build enterprise aware agents. How to

**[00:36]** build enterprise aware agents. How to

**[00:36]** build enterprise aware agents. How to bring the brilliance of AI into the

**[00:38]** bring the brilliance of AI into the

**[00:38]** bring the brilliance of AI into the messy complex realities of uh how your

**[00:41]** messy complex realities of uh how your

**[00:41]** messy complex realities of uh how your business operated.

**[00:43]** business operated.

**[00:43]** business operated. So let's jump straight to the hottest

**[00:45]** So let's jump straight to the hottest

**[00:45]** So let's jump straight to the hottest question of the month for AI builders.

**[00:47]** question of the month for AI builders.

**[00:47]** question of the month for AI builders. Uh should I build workflows or should I

**[00:50]** Uh should I build workflows or should I

**[00:50]** Uh should I build workflows or should I build agents?

**[00:52]** build agents?

**[00:52]** build agents? So what are workflows? Workflows are

**[00:55]** So what are workflows? Workflows are

**[00:55]** So what are workflows? Workflows are system where LLMs and tools are

**[00:57]** system where LLMs and tools are

**[00:57]** system where LLMs and tools are orchestrated through predefined code


### [01:00 - 02:00]

**[01:00]** orchestrated through predefined code

**[01:00]** orchestrated through predefined code paths. So there are two main ways where

**[01:03]** paths. So there are two main ways where

**[01:04]** paths. So there are two main ways where you can um represent the workflows. The

**[01:07]** you can um represent the workflows. The

**[01:07]** you can um represent the workflows. The first way is through uh imperative code

**[01:09]** first way is through uh imperative code

**[01:09]** first way is through uh imperative code base. So these are the workflows where

**[01:12]** base. So these are the workflows where

**[01:12]** base. So these are the workflows where you you know write a program that calls

**[01:15]** you you know write a program that calls

**[01:15]** you you know write a program that calls LMS uh read the response and then call

**[01:18]** LMS uh read the response and then call

**[01:18]** LMS uh read the response and then call tools and so like uh do this in a

**[01:20]** tools and so like uh do this in a

**[01:20]** tools and so like uh do this in a traditional programming flow and then

**[01:23]** traditional programming flow and then

**[01:23]** traditional programming flow and then here you get have like direct control of

**[01:25]** here you get have like direct control of

**[01:25]** here you get have like direct control of the execution of uh all the steps. The

**[01:30]** the execution of uh all the steps. The

**[01:30]** the execution of uh all the steps. The second way to represent workflow is

**[01:32]** second way to represent workflow is

**[01:32]** second way to represent workflow is through uh declarative graphs. So in

**[01:35]** through uh declarative graphs. So in

**[01:35]** through uh declarative graphs. So in this way you sort of um represent your

**[01:38]** this way you sort of um represent your

**[01:38]** this way you sort of um represent your workflow as like a graph of where nodes

**[01:41]** workflow as like a graph of where nodes

**[01:41]** workflow as like a graph of where nodes are sort of like steps where you can

**[01:42]** are sort of like steps where you can

**[01:42]** are sort of like steps where you can call tools or call llms and then there

**[01:45]** call tools or call llms and then there

**[01:45]** call tools or call llms and then there sort of edge between nodes. Um so you

**[01:48]** sort of edge between nodes. Um so you

**[01:48]** sort of edge between nodes. Um so you kind of define the structure but not

**[01:50]** kind of define the structure but not

**[01:50]** kind of define the structure but not execution and the execution of this is

**[01:52]** execution and the execution of this is

**[01:52]** execution and the execution of this is usually handled by some framework uh

**[01:55]** usually handled by some framework uh

**[01:55]** usually handled by some framework uh workflow frameworks. So I'm not going to

**[01:57]** workflow frameworks. So I'm not going to

**[01:57]** workflow frameworks. So I'm not going to go into the details of pros and cons for

**[01:59]** go into the details of pros and cons for

**[01:59]** go into the details of pros and cons for these two approaches but um the main


### [02:00 - 03:00]

**[02:03]** these two approaches but um the main

**[02:03]** these two approaches but um the main point here is like for workflows you get

**[02:05]** point here is like for workflows you get

**[02:05]** point here is like for workflows you get structure and predictability. So if you

**[02:08]** structure and predictability. So if you

**[02:08]** structure and predictability. So if you run a workflow today it will mostly

**[02:10]** run a workflow today it will mostly

**[02:10]** run a workflow today it will mostly behave the same way uh if you run it

**[02:12]** behave the same way uh if you run it

**[02:12]** behave the same way uh if you run it tomorrow.

**[02:15]** tomorrow.

**[02:15]** tomorrow. On the other hand, um we have agents

**[02:18]** On the other hand, um we have agents

**[02:18]** On the other hand, um we have agents which are systems where LLM sort of

**[02:22]** which are systems where LLM sort of

**[02:22]** which are systems where LLM sort of dynamically direct their own processes

**[02:25]** dynamically direct their own processes

**[02:25]** dynamically direct their own processes of like decide how to achieve a task

**[02:27]** of like decide how to achieve a task

**[02:27]** of like decide how to achieve a task like decides what tools to go uh what

**[02:30]** like decides what tools to go uh what

**[02:30]** like decides what tools to go uh what step to take depends on the task itself.

**[02:33]** step to take depends on the task itself.

**[02:33]** step to take depends on the task itself. Um so the core agent loop is pretty

**[02:35]** Um so the core agent loop is pretty

**[02:36]** Um so the core agent loop is pretty simple. So it receive a task or like a

**[02:38]** simple. So it receive a task or like a

**[02:38]** simple. So it receive a task or like a goal from a human and then it uh sort of

**[02:41]** goal from a human and then it uh sort of

**[02:41]** goal from a human and then it uh sort of enter this iterative loop where it uh

**[02:44]** enter this iterative loop where it uh

**[02:44]** enter this iterative loop where it uh plan what to do and then execute the

**[02:47]** plan what to do and then execute the

**[02:47]** plan what to do and then execute the action and then read the results from

**[02:49]** action and then read the results from

**[02:49]** action and then read the results from the environment and sort of iterate

**[02:51]** the environment and sort of iterate

**[02:51]** the environment and sort of iterate until uh it uh gets all the result. It's

**[02:54]** until uh it uh gets all the result. It's

**[02:54]** until uh it uh gets all the result. It's one and then uh respond to the user.

**[02:58]** one and then uh respond to the user.

**[02:58]** one and then uh respond to the user. So what are the tradeoffs between


### [03:00 - 04:00]

**[03:02]** So what are the tradeoffs between

**[03:02]** So what are the tradeoffs between workflows and agents? Um workflows are

**[03:05]** workflows and agents? Um workflows are

**[03:05]** workflows and agents? Um workflows are sort of like the Toyota of AI systems.

**[03:08]** sort of like the Toyota of AI systems.

**[03:08]** sort of like the Toyota of AI systems. Uh it's very predictable. Um it's good

**[03:12]** Uh it's very predictable. Um it's good

**[03:12]** Uh it's very predictable. Um it's good for when you want to automate uh

**[03:14]** for when you want to automate uh

**[03:14]** for when you want to automate uh repetitive tasks uh or like encode

**[03:16]** repetitive tasks uh or like encode

**[03:16]** repetitive tasks uh or like encode existing best practice or like know how

**[03:18]** existing best practice or like know how

**[03:18]** existing best practice or like know how in your in your business. This is

**[03:20]** in your in your business. This is

**[03:20]** in your in your business. This is usually lower cost and lower latency

**[03:22]** usually lower cost and lower latency

**[03:22]** usually lower cost and lower latency because you don't have to spend time on

**[03:24]** because you don't have to spend time on

**[03:24]** because you don't have to spend time on this all this LLM calls to decide what

**[03:26]** this all this LLM calls to decide what

**[03:26]** this all this LLM calls to decide what to do. And they're also also easier to

**[03:29]** to do. And they're also also easier to

**[03:29]** to do. And they're also also easier to debug because like you have this code or

**[03:31]** debug because like you have this code or

**[03:31]** debug because like you have this code or this graph that you can manually

**[03:33]** this graph that you can manually

**[03:34]** this graph that you can manually pinpoint uh at which step is going wrong

**[03:36]** pinpoint uh at which step is going wrong

**[03:36]** pinpoint uh at which step is going wrong in in the execution. And in building

**[03:39]** in in the execution. And in building

**[03:39]** in in the execution. And in building workflows uh humans are sort of in

**[03:42]** workflows uh humans are sort of in

**[03:42]** workflows uh humans are sort of in control like you can control your

**[03:44]** control like you can control your

**[03:44]** control like you can control your destiny like given even given u

**[03:47]** destiny like given even given u

**[03:47]** destiny like given even given u imperfect LMS uh you can sort of do

**[03:51]** imperfect LMS uh you can sort of do

**[03:51]** imperfect LMS uh you can sort of do tweaks and engineering so that your task

**[03:53]** tweaks and engineering so that your task

**[03:53]** tweaks and engineering so that your task work right now. On the other hand,

**[03:55]** work right now. On the other hand,

**[03:56]** work right now. On the other hand, agents are sort of like the Tesla of AI

**[03:58]** agents are sort of like the Tesla of AI

**[03:58]** agents are sort of like the Tesla of AI systems. Like it's more uh you know


### [04:00 - 05:00]

**[04:00]** systems. Like it's more uh you know

**[04:00]** systems. Like it's more uh you know open-ended. This is good for like

**[04:03]** open-ended. This is good for like

**[04:03]** open-ended. This is good for like researching unsolved problems. Uh it's

**[04:05]** researching unsolved problems. Uh it's

**[04:05]** researching unsolved problems. Uh it's also usually good at taking advantage of

**[04:08]** also usually good at taking advantage of

**[04:08]** also usually good at taking advantage of um better and better LM capabilities

**[04:10]** um better and better LM capabilities

**[04:10]** um better and better LM capabilities because here the AI is in control. Um

**[04:14]** because here the AI is in control. Um

**[04:14]** because here the AI is in control. Um generally it's higher cost and latency

**[04:16]** generally it's higher cost and latency

**[04:16]** generally it's higher cost and latency because you need LLM to like figure out

**[04:18]** because you need LLM to like figure out

**[04:18]** because you need LLM to like figure out what to do and then but the uh upside is

**[04:22]** what to do and then but the uh upside is

**[04:22]** what to do and then but the uh upside is like there's less logic to maintain the

**[04:24]** like there's less logic to maintain the

**[04:24]** like there's less logic to maintain the call loop is very simple and u sometimes

**[04:27]** call loop is very simple and u sometimes

**[04:27]** call loop is very simple and u sometimes you get like this uh hints of brilliance

**[04:29]** you get like this uh hints of brilliance

**[04:29]** you get like this uh hints of brilliance that always feels like you know

**[04:30]** that always feels like you know

**[04:30]** that always feels like you know everything is going to be automated in a

**[04:32]** everything is going to be automated in a

**[04:32]** everything is going to be automated in a few months. Um the problem is like your

**[04:36]** few months. Um the problem is like your

**[04:36]** few months. Um the problem is like your your Tesla like it's works very well

**[04:39]** your Tesla like it's works very well

**[04:39]** your Tesla like it's works very well most of the time but sometime it still

**[04:41]** most of the time but sometime it still

**[04:41]** most of the time but sometime it still take the wrong exit on the highway and

**[04:43]** take the wrong exit on the highway and

**[04:43]** take the wrong exit on the highway and that's when you kind of miss your toa so

**[04:47]** that's when you kind of miss your toa so

**[04:47]** that's when you kind of miss your toa so and the decision to build workflows or

**[04:50]** and the decision to build workflows or

**[04:50]** and the decision to build workflows or agents is a pretty tricky one because it

**[04:54]** agents is a pretty tricky one because it

**[04:54]** agents is a pretty tricky one because it depends highly on the state of the LLM.

**[04:58]** depends highly on the state of the LLM.

**[04:58]** depends highly on the state of the LLM. Um so some workflows that doesn't work


### [05:00 - 06:00]

**[05:01]** Um so some workflows that doesn't work

**[05:01]** Um so some workflows that doesn't work in the agentic loop now might start to

**[05:03]** in the agentic loop now might start to

**[05:04]** in the agentic loop now might start to work later in a few months when the new

**[05:05]** work later in a few months when the new

**[05:05]** work later in a few months when the new model has come out. So it's uh it's a

**[05:09]** model has come out. So it's uh it's a

**[05:09]** model has come out. So it's uh it's a really huge dilemma.

**[05:11]** really huge dilemma.

**[05:11]** really huge dilemma. Um but recently one thought um that's

**[05:16]** Um but recently one thought um that's

**[05:16]** Um but recently one thought um that's sort of really changed how I think about

**[05:18]** sort of really changed how I think about

**[05:18]** sort of really changed how I think about it is what if you don't really have to

**[05:20]** it is what if you don't really have to

**[05:20]** it is what if you don't really have to choose right so if you think of agent

**[05:24]** choose right so if you think of agent

**[05:24]** choose right so if you think of agent what they do is when you give the agent

**[05:27]** what they do is when you give the agent

**[05:27]** what they do is when you give the agent a task it will figure out the steps that

**[05:31]** a task it will figure out the steps that

**[05:31]** a task it will figure out the steps that needs to be done to achieve that task.

**[05:34]** needs to be done to achieve that task.

**[05:34]** needs to be done to achieve that task. Right? So um you give it the task you

**[05:37]** Right? So um you give it the task you

**[05:37]** Right? So um you give it the task you figure out the one step take the action

**[05:40]** figure out the one step take the action

**[05:40]** figure out the one step take the action figure out the next steps and then at

**[05:42]** figure out the next steps and then at

**[05:42]** figure out the next steps and then at the end when the agent finish the

**[05:44]** the end when the agent finish the

**[05:44]** the end when the agent finish the execution and then you look at the trace

**[05:46]** execution and then you look at the trace

**[05:46]** execution and then you look at the trace of what happened all those series of

**[05:49]** of what happened all those series of

**[05:49]** of what happened all those series of steps is a workflow. So if I represent

**[05:52]** steps is a workflow. So if I represent

**[05:52]** steps is a workflow. So if I represent this in like a uh programming kind of

**[05:56]** this in like a uh programming kind of

**[05:56]** this in like a uh programming kind of way then agent takes a st a task and

**[05:59]** way then agent takes a st a task and

**[05:59]** way then agent takes a st a task and then generate a workflow to achieve that


### [06:00 - 07:00]

**[06:01]** then generate a workflow to achieve that

**[06:01]** then generate a workflow to achieve that task. Um

**[06:04]** task. Um

**[06:04]** task. Um so if we think of it this way agent take

**[06:08]** so if we think of it this way agent take

**[06:08]** so if we think of it this way agent take a task and generate a workflow then you

**[06:12]** a task and generate a workflow then you

**[06:12]** a task and generate a workflow then you can sort of see like there are really

**[06:14]** can sort of see like there are really

**[06:14]** can sort of see like there are really good synergies between workflows and

**[06:16]** good synergies between workflows and

**[06:16]** good synergies between workflows and agent. So the first thing is you can

**[06:18]** agent. So the first thing is you can

**[06:18]** agent. So the first thing is you can actually use workflows as uh evaluation

**[06:22]** actually use workflows as uh evaluation

**[06:22]** actually use workflows as uh evaluation for your agents right so uh let's say in

**[06:25]** for your agents right so uh let's say in

**[06:25]** for your agents right so uh let's say in in your company you can collect a huge

**[06:27]** in your company you can collect a huge

**[06:27]** in your company you can collect a huge amount of um golden workflows like given

**[06:31]** amount of um golden workflows like given

**[06:31]** amount of um golden workflows like given a task this is the steps that uh needs

**[06:34]** a task this is the steps that uh needs

**[06:34]** a task this is the steps that uh needs to be done to solve that task and you

**[06:37]** to be done to solve that task and you

**[06:37]** to be done to solve that task and you have a huge list of uh of those uh sort

**[06:39]** have a huge list of uh of those uh sort

**[06:40]** have a huge list of uh of those uh sort of handbook on on how um to do things in

**[06:43]** of handbook on on how um to do things in

**[06:43]** of handbook on on how um to do things in your company then you can actually

**[06:46]** your company then you can actually

**[06:46]** your company then you can actually evaluate your agents by uh you know like

**[06:49]** evaluate your agents by uh you know like

**[06:49]** evaluate your agents by uh you know like give it a task see what it did and

**[06:52]** give it a task see what it did and

**[06:52]** give it a task see what it did and compare it to the the golden workflow

**[06:53]** compare it to the the golden workflow

**[06:53]** compare it to the the golden workflow like did it actually figure out the

**[06:55]** like did it actually figure out the

**[06:55]** like did it actually figure out the right steps. So this is a little bit

**[06:58]** right steps. So this is a little bit

**[06:58]** right steps. So this is a little bit different from evaluating end to end.


### [07:00 - 08:00]

**[07:00]** different from evaluating end to end.

**[07:00]** different from evaluating end to end. You are not judging agent by uh the end

**[07:03]** You are not judging agent by uh the end

**[07:03]** You are not judging agent by uh the end response but like by uh whether it

**[07:05]** response but like by uh whether it

**[07:05]** response but like by uh whether it actually did the right step to get to

**[07:07]** actually did the right step to get to

**[07:07]** actually did the right step to get to that end response.

**[07:10]** that end response.

**[07:10]** that end response. Um the second and uh even better way uh

**[07:13]** Um the second and uh even better way uh

**[07:14]** Um the second and uh even better way uh for workflows to help help agents is you

**[07:16]** for workflows to help help agents is you

**[07:16]** for workflows to help help agents is you know given that same golden uh workflows

**[07:19]** know given that same golden uh workflows

**[07:19]** know given that same golden uh workflows library you can also use it to train

**[07:22]** library you can also use it to train

**[07:22]** library you can also use it to train your agents. Um so here you truly get

**[07:26]** your agents. Um so here you truly get

**[07:26]** your agents. Um so here you truly get the best of both worlds where you know

**[07:29]** the best of both worlds where you know

**[07:29]** the best of both worlds where you know with the data feeding you can uh your

**[07:32]** with the data feeding you can uh your

**[07:32]** with the data feeding you can uh your agents will be able to execute the exact

**[07:34]** agents will be able to execute the exact

**[07:34]** agents will be able to execute the exact workflow that you have in your library

**[07:37]** workflow that you have in your library

**[07:37]** workflow that you have in your library for the known task. Um but then Oracle

**[07:41]** for the known task. Um but then Oracle

**[07:41]** for the known task. Um but then Oracle um it can also rely on its own uh

**[07:45]** um it can also rely on its own uh

**[07:45]** um it can also rely on its own uh internal reasoning capabilities to sort

**[07:47]** internal reasoning capabilities to sort

**[07:47]** internal reasoning capabilities to sort of compose different workflows together

**[07:49]** of compose different workflows together

**[07:49]** of compose different workflows together to uh achieve new tasks and even use its

**[07:53]** to uh achieve new tasks and even use its

**[07:53]** to uh achieve new tasks and even use its own reasoning to kind of extend uh what

**[07:56]** own reasoning to kind of extend uh what

**[07:56]** own reasoning to kind of extend uh what you teach it but like make it better.


### [08:00 - 09:00]

**[08:00]** you teach it but like make it better.

**[08:00]** you teach it but like make it better. Um and then agents can also help

**[08:05]** Um and then agents can also help

**[08:05]** Um and then agents can also help workflows as well. Uh one way to do that

**[08:07]** workflows as well. Uh one way to do that

**[08:07]** workflows as well. Uh one way to do that is um for workflow building platforms uh

**[08:11]** is um for workflow building platforms uh

**[08:11]** is um for workflow building platforms uh you can use an agent to generate the

**[08:13]** you can use an agent to generate the

**[08:13]** you can use an agent to generate the workflows. Um so this is sort of how uh

**[08:16]** workflows. Um so this is sort of how uh

**[08:16]** workflows. Um so this is sort of how uh glean agents work under the hood where

**[08:19]** glean agents work under the hood where

**[08:19]** glean agents work under the hood where the user can give uh the workflow video

**[08:22]** the user can give uh the workflow video

**[08:22]** the user can give uh the workflow video like a sort of natural language

**[08:24]** like a sort of natural language

**[08:24]** like a sort of natural language description of the task it is trying to

**[08:26]** description of the task it is trying to

**[08:26]** description of the task it is trying to achieve and then we run an agent

**[08:28]** achieve and then we run an agent

**[08:28]** achieve and then we run an agent implementation to figure out the steps

**[08:30]** implementation to figure out the steps

**[08:30]** implementation to figure out the steps that are needed to achieve that

**[08:31]** that are needed to achieve that

**[08:31]** that are needed to achieve that workflow. then the user can sort of like

**[08:36]** workflow. then the user can sort of like

**[08:36]** workflow. then the user can sort of like uh make edit or like add change uh the

**[08:39]** uh make edit or like add change uh the

**[08:39]** uh make edit or like add change uh the workflow that that the the agent was uh

**[08:41]** workflow that that the the agent was uh

**[08:41]** workflow that that the the agent was uh proposing.

**[08:49]** Um and lastly and I think is like uh the

**[08:49]** Um and lastly and I think is like uh the most powerful

**[08:51]** most powerful

**[08:51]** most powerful um synergy is you can use agents as a

**[08:54]** um synergy is you can use agents as a

**[08:54]** um synergy is you can use agents as a workflow discovery engine, right? So you

**[08:58]** workflow discovery engine, right? So you

**[08:58]** workflow discovery engine, right? So you ship an agent uh users try to accomplish


### [09:00 - 10:00]

**[09:02]** ship an agent uh users try to accomplish

**[09:02]** ship an agent uh users try to accomplish new task with your agent and then when

**[09:04]** new task with your agent and then when

**[09:04]** new task with your agent and then when they find that the agent did a good job

**[09:07]** they find that the agent did a good job

**[09:07]** they find that the agent did a good job then you can sort of save that workflow

**[09:10]** then you can sort of save that workflow

**[09:10]** then you can sort of save that workflow as like okay this is how you do this

**[09:12]** as like okay this is how you do this

**[09:12]** as like okay this is how you do this task in my company and then over time

**[09:14]** task in my company and then over time

**[09:14]** task in my company and then over time you can use this um as like training

**[09:16]** you can use this um as like training

**[09:16]** you can use this um as like training data to help agents get better.

**[09:20]** data to help agents get better.

**[09:20]** data to help agents get better. Cool. Um so that was the main points of

**[09:24]** Cool. Um so that was the main points of

**[09:24]** Cool. Um so that was the main points of my talk. Um, I guess maybe some of you

**[09:28]** my talk. Um, I guess maybe some of you

**[09:28]** my talk. Um, I guess maybe some of you are thinking, do we still need this kind

**[09:31]** are thinking, do we still need this kind

**[09:31]** are thinking, do we still need this kind of stuff in a world where we have AGI?

**[09:34]** of stuff in a world where we have AGI?

**[09:34]** of stuff in a world where we have AGI? Um, so here's here's my thought

**[09:37]** Um, so here's here's my thought

**[09:37]** Um, so here's here's my thought experiment and uh why I think this maybe

**[09:40]** experiment and uh why I think this maybe

**[09:40]** experiment and uh why I think this maybe still needed after AGI. So AGI is going

**[09:44]** still needed after AGI. So AGI is going

**[09:44]** still needed after AGI. So AGI is going to be a super intelligent employee,

**[09:46]** to be a super intelligent employee,

**[09:46]** to be a super intelligent employee, right? Um but if they if AI doesn't know

**[09:49]** right? Um but if they if AI doesn't know

**[09:50]** right? Um but if they if AI doesn't know about uh how your company works, it's

**[09:52]** about uh how your company works, it's

**[09:52]** about uh how your company works, it's sort of like uh a really good employee

**[09:54]** sort of like uh a really good employee

**[09:54]** sort of like uh a really good employee who just joined and doesn't know about

**[09:57]** who just joined and doesn't know about

**[09:57]** who just joined and doesn't know about all the business practices and still

**[09:59]** all the business practices and still

**[09:59]** all the business practices and still needs on boarding needs to know like who


### [10:00 - 11:00]

**[10:02]** needs on boarding needs to know like who

**[10:02]** needs on boarding needs to know like who to talk to to get unblocked and like uh

**[10:04]** to talk to to get unblocked and like uh

**[10:04]** to talk to to get unblocked and like uh all the very nuanced ways of doing

**[10:07]** all the very nuanced ways of doing

**[10:07]** all the very nuanced ways of doing things in the enterprise. Um so what is

**[10:11]** things in the enterprise. Um so what is

**[10:11]** things in the enterprise. Um so what is enterprise aware AGI? So enterprise a

**[10:14]** enterprise aware AGI? So enterprise a

**[10:14]** enterprise aware AGI? So enterprise a aware AGI is fully on boarded, very

**[10:17]** aware AGI is fully on boarded, very

**[10:17]** aware AGI is fully on boarded, very intelligent, knows the ways your company

**[10:19]** intelligent, knows the ways your company

**[10:19]** intelligent, knows the ways your company do things and um

**[10:23]** do things and um

**[10:23]** do things and um one one key kind of insight that I um I

**[10:27]** one one key kind of insight that I um I

**[10:27]** one one key kind of insight that I um I think is like sort there are many

**[10:29]** think is like sort there are many

**[10:29]** think is like sort there are many acceptable ways to achieve a task. Um

**[10:32]** acceptable ways to achieve a task. Um

**[10:32]** acceptable ways to achieve a task. Um but there's a gap between an acceptable

**[10:35]** but there's a gap between an acceptable

**[10:35]** but there's a gap between an acceptable output versus a great output. Um one

**[10:38]** output versus a great output. Um one

**[10:38]** output versus a great output. Um one example is like you know competitor

**[10:40]** example is like you know competitor

**[10:40]** example is like you know competitor analysis like sure it can do some basic

**[10:44]** analysis like sure it can do some basic

**[10:44]** analysis like sure it can do some basic Google search and like uh read some uh

**[10:48]** Google search and like uh read some uh

**[10:48]** Google search and like uh read some uh notes out outside to like do some compet

**[10:50]** notes out outside to like do some compet

**[10:50]** notes out outside to like do some compet analysis but does it actually follow uh

**[10:53]** analysis but does it actually follow uh

**[10:53]** analysis but does it actually follow uh the protocols or the processes that your

**[10:55]** the protocols or the processes that your

**[10:55]** the protocols or the processes that your company define and does it actually

**[10:58]** company define and does it actually

**[10:58]** company define and does it actually address all the key metrics that your

**[10:59]** address all the key metrics that your

**[10:59]** address all the key metrics that your executive uh really care about.


### [11:00 - 12:00]

**[11:03]** executive uh really care about.

**[11:03]** executive uh really care about. So um

**[11:06]** So um

**[11:06]** So um given all these data you know like tasks

**[11:09]** given all these data you know like tasks

**[11:09]** given all these data you know like tasks and golden workflows how do you actually

**[11:11]** and golden workflows how do you actually

**[11:11]** and golden workflows how do you actually train your agents um using those data.

**[11:14]** train your agents um using those data.

**[11:14]** train your agents um using those data. So this is uh the second part of my

**[11:16]** So this is uh the second part of my

**[11:16]** So this is uh the second part of my talk.

**[11:18]** talk.

**[11:18]** talk. Um so there are two main ways we have um

**[11:22]** Um so there are two main ways we have um

**[11:22]** Um so there are two main ways we have um experimented with the first one is

**[11:24]** experimented with the first one is

**[11:24]** experimented with the first one is through fine-tuning. Um there are sort

**[11:28]** through fine-tuning. Um there are sort

**[11:28]** through fine-tuning. Um there are sort of two main flavor of fine-tuning here.

**[11:30]** of two main flavor of fine-tuning here.

**[11:30]** of two main flavor of fine-tuning here. is uh you know supervised fine-tuning

**[11:33]** is uh you know supervised fine-tuning

**[11:33]** is uh you know supervised fine-tuning where you give uh give an input and an

**[11:35]** where you give uh give an input and an

**[11:35]** where you give uh give an input and an expected output and you train your model

**[11:38]** expected output and you train your model

**[11:38]** expected output and you train your model to just um mimic that uh behavior. The

**[11:43]** to just um mimic that uh behavior. The

**[11:43]** to just um mimic that uh behavior. The second way is through all RHF where you

**[11:46]** second way is through all RHF where you

**[11:46]** second way is through all RHF where you don't have a golden label but you sort

**[11:48]** don't have a golden label but you sort

**[11:48]** don't have a golden label but you sort of have a a rating or a reward when you

**[11:51]** of have a a rating or a reward when you

**[11:51]** of have a a rating or a reward when you know like this task this workflow is it

**[11:53]** know like this task this workflow is it

**[11:53]** know like this task this workflow is it a good one or is it a a bad one. So then

**[11:55]** a good one or is it a a bad one. So then

**[11:56]** a good one or is it a a bad one. So then you can sort of run your uh favorite

**[11:58]** you can sort of run your uh favorite

**[11:58]** you can sort of run your uh favorite optimization algorithms to fine-tune the


### [12:00 - 13:00]

**[12:00]** optimization algorithms to fine-tune the

**[12:00]** optimization algorithms to fine-tune the LLM.

**[12:02]** LLM.

**[12:02]** LLM. So the pros of this method is that it

**[12:05]** So the pros of this method is that it

**[12:05]** So the pros of this method is that it can learn really well when you have a

**[12:07]** can learn really well when you have a

**[12:08]** can learn really well when you have a lot of data. Um um if you have a huge

**[12:11]** lot of data. Um um if you have a huge

**[12:12]** lot of data. Um um if you have a huge amount of uh tasks and workflows, it can

**[12:14]** amount of uh tasks and workflows, it can

**[12:14]** amount of uh tasks and workflows, it can really learn um like sort of generalize

**[12:17]** really learn um like sort of generalize

**[12:17]** really learn um like sort of generalize across different tasks and like combined

**[12:19]** across different tasks and like combined

**[12:19]** across different tasks and like combined workflows. Um the problem here is one uh

**[12:25]** workflows. Um the problem here is one uh

**[12:25]** workflows. Um the problem here is one uh you kind of have to create a fork from

**[12:26]** you kind of have to create a fork from

**[12:26]** you kind of have to create a fork from the from the frontier LLM right so you

**[12:29]** the from the frontier LLM right so you

**[12:29]** the from the frontier LLM right so you start with some LLM you do some

**[12:31]** start with some LLM you do some

**[12:31]** start with some LLM you do some finetuning and then by the time the fine

**[12:33]** finetuning and then by the time the fine

**[12:33]** finetuning and then by the time the fine tuning finishes maybe there's a new and

**[12:36]** tuning finishes maybe there's a new and

**[12:36]** tuning finishes maybe there's a new and better model already come out then you

**[12:37]** better model already come out then you

**[12:37]** better model already come out then you have to like redo this whole process

**[12:39]** have to like redo this whole process

**[12:39]** have to like redo this whole process again and the second is like any change

**[12:42]** again and the second is like any change

**[12:42]** again and the second is like any change to your training data uh like you need

**[12:44]** to your training data uh like you need

**[12:44]** to your training data uh like you need to do retraining right so if you have a

**[12:47]** to do retraining right so if you have a

**[12:47]** to do retraining right so if you have a new tool then maybe some of the existing

**[12:49]** new tool then maybe some of the existing

**[12:49]** new tool then maybe some of the existing workflow is outdated then you have to

**[12:51]** workflow is outdated then you have to

**[12:51]** workflow is outdated then you have to retrain. Uh if you do change some

**[12:54]** retrain. Uh if you do change some

**[12:54]** retrain. Uh if you do change some business priorities or business

**[12:55]** business priorities or business

**[12:55]** business priorities or business processes then you have to like redo the

**[12:57]** processes then you have to like redo the

**[12:57]** processes then you have to like redo the training again and it also not super


### [13:00 - 14:00]

**[13:02]** training again and it also not super

**[13:02]** training again and it also not super flexible for personalization. Um so

**[13:05]** flexible for personalization. Um so

**[13:05]** flexible for personalization. Um so given the same task maybe different

**[13:07]** given the same task maybe different

**[13:07]** given the same task maybe different teams or different employees might

**[13:09]** teams or different employees might

**[13:09]** teams or different employees might actually have a different optimal

**[13:11]** actually have a different optimal

**[13:11]** actually have a different optimal workflows to to do those tasks and

**[13:13]** workflows to to do those tasks and

**[13:13]** workflows to to do those tasks and fine-tuning is not super well suited for

**[13:16]** fine-tuning is not super well suited for

**[13:16]** fine-tuning is not super well suited for for those use cases.

**[13:18]** for those use cases.

**[13:18]** for those use cases. Um then comes the second option uh which

**[13:21]** Um then comes the second option uh which

**[13:21]** Um then comes the second option uh which is dynamic prompting through search. So

**[13:25]** is dynamic prompting through search. So

**[13:25]** is dynamic prompting through search. So um given the same label data uh from

**[13:27]** um given the same label data uh from

**[13:27]** um given the same label data uh from task to a golden workflow you build a

**[13:30]** task to a golden workflow you build a

**[13:30]** task to a golden workflow you build a really good search engine for task um so

**[13:33]** really good search engine for task um so

**[13:33]** really good search engine for task um so that you can find similar task given a

**[13:35]** that you can find similar task given a

**[13:35]** that you can find similar task given a new task. So then at runtime uh to

**[13:39]** new task. So then at runtime uh to

**[13:39]** new task. So then at runtime uh to accomplish a new task we'll find the

**[13:41]** accomplish a new task we'll find the

**[13:42]** accomplish a new task we'll find the most similar task in the training data

**[13:44]** most similar task in the training data

**[13:44]** most similar task in the training data and then you feed the representation of

**[13:46]** and then you feed the representation of

**[13:46]** and then you feed the representation of those workflows to the LM as the

**[13:49]** those workflows to the LM as the

**[13:49]** those workflows to the LM as the examples. Right? So here you really have

**[13:51]** examples. Right? So here you really have

**[13:51]** examples. Right? So here you really have a spectrum of uh determinism and

**[13:55]** a spectrum of uh determinism and

**[13:55]** a spectrum of uh determinism and creativity.

**[13:56]** creativity.

**[13:56]** creativity. So when there's no workflow that sort of

**[13:59]** So when there's no workflow that sort of

**[13:59]** So when there's no workflow that sort of match your input task then


### [14:00 - 15:00]

**[14:03]** match your input task then

**[14:03]** match your input task then are in control like it can use this

**[14:05]** are in control like it can use this

**[14:05]** are in control like it can use this creativity to generate a new workflow

**[14:07]** creativity to generate a new workflow

**[14:07]** creativity to generate a new workflow but when there's a high confidence match

**[14:10]** but when there's a high confidence match

**[14:10]** but when there's a high confidence match of something that you have done before

**[14:12]** of something that you have done before

**[14:12]** of something that you have done before then the LM will sort of give you a

**[14:15]** then the LM will sort of give you a

**[14:15]** then the LM will sort of give you a workflow that's very similar to what was

**[14:17]** workflow that's very similar to what was

**[14:17]** workflow that's very similar to what was in the training data.

**[14:20]** in the training data.

**[14:20]** in the training data. Um so one very concrete example uh come

**[14:24]** Um so one very concrete example uh come

**[14:24]** Um so one very concrete example uh come back to the competitor analysis uh

**[14:27]** back to the competitor analysis uh

**[14:27]** back to the competitor analysis uh example before so you collected this

**[14:30]** example before so you collected this

**[14:30]** example before so you collected this huge list of task to workflow

**[14:33]** huge list of task to workflow

**[14:33]** huge list of task to workflow uh and then when a new task like say

**[14:36]** uh and then when a new task like say

**[14:36]** uh and then when a new task like say what what competitors have we've been

**[14:38]** what what competitors have we've been

**[14:38]** what what competitors have we've been running into recently then it will

**[14:40]** running into recently then it will

**[14:40]** running into recently then it will retrieve you know how to analyze each

**[14:42]** retrieve you know how to analyze each

**[14:42]** retrieve you know how to analyze each competitor and then you will find a work

**[14:45]** competitor and then you will find a work

**[14:45]** competitor and then you will find a work on how to find uh your recent customer

**[14:48]** on how to find uh your recent customer

**[14:48]** on how to find uh your recent customer calls and then the LLM So take those

**[14:50]** calls and then the LLM So take those

**[14:50]** calls and then the LLM So take those example and then sort of generate a

**[14:53]** example and then sort of generate a

**[14:53]** example and then sort of generate a composed workflow where it read customer

**[14:56]** composed workflow where it read customer

**[14:56]** composed workflow where it read customer calls, read uh internal messages,

**[14:58]** calls, read uh internal messages,

**[14:58]** calls, read uh internal messages, extract competitors and then run


### [15:00 - 16:00]

**[15:00]** extract competitors and then run

**[15:00]** extract competitors and then run analysis for each of them.

**[15:04]** analysis for each of them.

**[15:04]** analysis for each of them. Um okay so comparison time um

**[15:07]** Um okay so comparison time um

**[15:07]** Um okay so comparison time um fine-tuning RHF is very strong uh when

**[15:12]** fine-tuning RHF is very strong uh when

**[15:12]** fine-tuning RHF is very strong uh when you have a lot of data that you want to

**[15:14]** you have a lot of data that you want to

**[15:14]** you have a lot of data that you want to generalize.

**[15:15]** generalize.

**[15:15]** generalize. dynamic prompting research is more

**[15:17]** dynamic prompting research is more

**[15:17]** dynamic prompting research is more flexible. Uh also give you better

**[15:20]** flexible. Uh also give you better

**[15:20]** flexible. Uh also give you better interpretivity uh that you can sort of

**[15:22]** interpretivity uh that you can sort of

**[15:22]** interpretivity uh that you can sort of look into the exact examples that was

**[15:25]** look into the exact examples that was

**[15:25]** look into the exact examples that was affecting your outputs and um

**[15:28]** affecting your outputs and um

**[15:28]** affecting your outputs and um fine-tuning is good for learning

**[15:30]** fine-tuning is good for learning

**[15:30]** fine-tuning is good for learning generalized behaviors uh where the

**[15:32]** generalized behaviors uh where the

**[15:32]** generalized behaviors uh where the ground truth labels don't change over

**[15:35]** ground truth labels don't change over

**[15:35]** ground truth labels don't change over time or like across different users. um

**[15:38]** time or like across different users. um

**[15:38]** time or like across different users. um dynamic prompting with search is better

**[15:40]** dynamic prompting with search is better

**[15:40]** dynamic prompting with search is better for learning customized behaviors or

**[15:42]** for learning customized behaviors or

**[15:42]** for learning customized behaviors or like the last mile quality gap where you

**[15:44]** like the last mile quality gap where you

**[15:44]** like the last mile quality gap where you know uh requirements are changing

**[15:46]** know uh requirements are changing

**[15:46]** know uh requirements are changing quickly. Um one one sort of analogy I

**[15:50]** quickly. Um one one sort of analogy I

**[15:50]** quickly. Um one one sort of analogy I think about fine-tuning versus dynamic

**[15:53]** think about fine-tuning versus dynamic

**[15:53]** think about fine-tuning versus dynamic prompting is um fine-tuning is very

**[15:55]** prompting is um fine-tuning is very

**[15:55]** prompting is um fine-tuning is very similar to like building customized

**[15:58]** similar to like building customized

**[15:58]** similar to like building customized hardware. So when you know when you have


### [16:00 - 17:00]

**[16:00]** hardware. So when you know when you have

**[16:00]** hardware. So when you know when you have a sort of task that you really want to

**[16:04]** a sort of task that you really want to

**[16:04]** a sort of task that you really want to optimize for and the requirements don't

**[16:05]** optimize for and the requirements don't

**[16:05]** optimize for and the requirements don't change over time like you can really

**[16:07]** change over time like you can really

**[16:07]** change over time like you can really build custom hardware that do it very

**[16:09]** build custom hardware that do it very

**[16:09]** build custom hardware that do it very well. Uh but it's sort of costly when

**[16:11]** well. Uh but it's sort of costly when

**[16:11]** well. Uh but it's sort of costly when you uh change your requirements compared

**[16:13]** you uh change your requirements compared

**[16:14]** you uh change your requirements compared to dynamic prompting is more like

**[16:15]** to dynamic prompting is more like

**[16:15]** to dynamic prompting is more like writing software uh not as uh optimized

**[16:20]** writing software uh not as uh optimized

**[16:20]** writing software uh not as uh optimized but like you can just change them very

**[16:22]** but like you can just change them very

**[16:22]** but like you can just change them very quickly.

**[16:24]** quickly.

**[16:24]** quickly. Um last point uh so how do we actually

**[16:27]** Um last point uh so how do we actually

**[16:28]** Um last point uh so how do we actually build this workflow search right so how

**[16:30]** build this workflow search right so how

**[16:30]** build this workflow search right so how do you give it a task like find similar

**[16:32]** do you give it a task like find similar

**[16:32]** do you give it a task like find similar task uh I would say it's very similar to

**[16:36]** task uh I would say it's very similar to

**[16:36]** task uh I would say it's very similar to building document search right um and

**[16:39]** building document search right um and

**[16:39]** building document search right um and there are two main components to this

**[16:41]** there are two main components to this

**[16:42]** there are two main components to this the first one uh is what everyone

**[16:45]** the first one uh is what everyone

**[16:45]** the first one uh is what everyone usually think of when they think of

**[16:46]** usually think of when they think of

**[16:46]** usually think of when they think of search which is a textual similarity

**[16:49]** search which is a textual similarity

**[16:49]** search which is a textual similarity right um given this task what are some

**[16:51]** right um given this task what are some

**[16:51]** right um given this task what are some the similar sounding tasks that are in

**[16:55]** the similar sounding tasks that are in

**[16:55]** the similar sounding tasks that are in the training data. Um, and here the sort

**[16:58]** the training data. Um, and here the sort

**[16:58]** the training data. Um, and here the sort of uh

**[16:59]** of uh


### [17:00 - 18:00]

**[17:00]** of uh golden recipe is like like hybrid search

**[17:02]** golden recipe is like like hybrid search

**[17:02]** golden recipe is like like hybrid search between lexical vector embeddings uh

**[17:04]** between lexical vector embeddings uh

**[17:04]** between lexical vector embeddings uh reranking late interaction all that.

**[17:07]** reranking late interaction all that.

**[17:07]** reranking late interaction all that. But uh what I found is in in the

**[17:11]** But uh what I found is in in the

**[17:11]** But uh what I found is in in the enterprise settings uh pure text

**[17:13]** enterprise settings uh pure text

**[17:13]** enterprise settings uh pure text similarity is not enough. when uh when

**[17:16]** similarity is not enough. when uh when

**[17:16]** similarity is not enough. when uh when you give users the choice to create

**[17:19]** you give users the choice to create

**[17:19]** you give users the choice to create workflows and write documents

**[17:21]** workflows and write documents

**[17:21]** workflows and write documents when you want to search for something

**[17:23]** when you want to search for something

**[17:23]** when you want to search for something there will be like hundreds or thousand

**[17:25]** there will be like hundreds or thousand

**[17:25]** there will be like hundreds or thousand of similar looking documents or

**[17:27]** of similar looking documents or

**[17:27]** of similar looking documents or workflows and uh the problem becomes how

**[17:30]** workflows and uh the problem becomes how

**[17:30]** workflows and uh the problem becomes how do you choose the right one uh right so

**[17:33]** do you choose the right one uh right so

**[17:33]** do you choose the right one uh right so uh which is what I call as uh

**[17:35]** uh which is what I call as uh

**[17:35]** uh which is what I call as uh authoritiveness here and to solve this

**[17:38]** authoritiveness here and to solve this

**[17:38]** authoritiveness here and to solve this problem then you kind of have to go into

**[17:41]** problem then you kind of have to go into

**[17:41]** problem then you kind of have to go into uh knowledge graph right so if this

**[17:44]** uh knowledge graph right so if this

**[17:44]** uh knowledge graph right so if this workflow is created by someone who I

**[17:46]** workflow is created by someone who I

**[17:46]** workflow is created by someone who I work closely with uh it has high success

**[17:49]** work closely with uh it has high success

**[17:49]** work closely with uh it has high success rate and like people post about it um on

**[17:52]** rate and like people post about it um on

**[17:52]** rate and like people post about it um on Slack then it's more likely to be the

**[17:54]** Slack then it's more likely to be the

**[17:54]** Slack then it's more likely to be the right one. So all the tricks in uh the

**[17:56]** right one. So all the tricks in uh the

**[17:56]** right one. So all the tricks in uh the recommended system uh um world also


### [18:00 - 19:00]

**[18:01]** recommended system uh um world also

**[18:01]** recommended system uh um world also applies here for for workflow search and

**[18:04]** applies here for for workflow search and

**[18:04]** applies here for for workflow search and um this kind of authoritiveness signals

**[18:07]** um this kind of authoritiveness signals

**[18:07]** um this kind of authoritiveness signals are very hard to encode directly into an

**[18:09]** are very hard to encode directly into an

**[18:09]** are very hard to encode directly into an LLM which is why we sort of have to have

**[18:12]** LLM which is why we sort of have to have

**[18:12]** LLM which is why we sort of have to have like a separate system that does the the

**[18:14]** like a separate system that does the the

**[18:14]** like a separate system that does the the search for workflows.

**[18:18]** search for workflows.

**[18:18]** search for workflows. Cool. Um so key takeaways uh workflows

**[18:22]** Cool. Um so key takeaways uh workflows

**[18:22]** Cool. Um so key takeaways uh workflows good for determinism human are in

**[18:24]** good for determinism human are in

**[18:24]** good for determinism human are in control agents more open-ended AI is in

**[18:28]** control agents more open-ended AI is in

**[18:28]** control agents more open-ended AI is in control and um the synergy between a

**[18:31]** control and um the synergy between a

**[18:31]** control and um the synergy between a agents and workflows is workflows can be

**[18:34]** agents and workflows is workflows can be

**[18:34]** agents and workflows is workflows can be used for agents evaluation. Uh workflow

**[18:37]** used for agents evaluation. Uh workflow

**[18:37]** used for agents evaluation. Uh workflow is used for agents training and agents

**[18:40]** is used for agents training and agents

**[18:40]** is used for agents training and agents is used for workflows discovery. Um,

**[18:43]** is used for workflows discovery. Um,

**[18:43]** is used for workflows discovery. Um, fine-tuning is good for generalized

**[18:45]** fine-tuning is good for generalized

**[18:46]** fine-tuning is good for generalized behaviors. Dynamic prompting with search

**[18:48]** behaviors. Dynamic prompting with search

**[18:48]** behaviors. Dynamic prompting with search is good for personalized behaviors.

**[18:51]** is good for personalized behaviors.

**[18:52]** is good for personalized behaviors. All right. Uh, I still have 1 minute and

**[18:54]** All right. Uh, I still have 1 minute and

**[18:54]** All right. Uh, I still have 1 minute and uh 30 seconds. Uh, maybe time for one

**[18:57]** uh 30 seconds. Uh, maybe time for one

**[18:57]** uh 30 seconds. Uh, maybe time for one question.


### [19:00 - 20:00]

**[19:19]** So the question was uh I tried to

**[19:19]** So the question was uh I tried to reinterpret it. Let me know if it's

**[19:21]** reinterpret it. Let me know if it's

**[19:21]** reinterpret it. Let me know if it's wrong. uh how much data do we need to do

**[19:24]** wrong. uh how much data do we need to do

**[19:24]** wrong. uh how much data do we need to do finetuning given the new

**[19:26]** finetuning given the new

**[19:26]** finetuning given the new RLVR

**[19:27]** RLVR

**[19:27]** RLVR RLVR

**[19:29]** RLVR

**[19:29]** RLVR that's a very difficult question to

**[19:32]** that's a very difficult question to

**[19:32]** that's a very difficult question to answer because uh it really depends on

**[19:35]** answer because uh it really depends on

**[19:36]** answer because uh it really depends on how out out distribution your task is

**[19:38]** how out out distribution your task is

**[19:38]** how out out distribution your task is compared to the internal uh knowledge of

**[19:40]** compared to the internal uh knowledge of

**[19:40]** compared to the internal uh knowledge of the LM um but I'll catch you after and

**[19:43]** the LM um but I'll catch you after and

**[19:43]** the LM um but I'll catch you after and we can talk more thank you too difficult

**[19:46]** we can talk more thank you too difficult

**[19:46]** we can talk more thank you too difficult of a

**[19:47]** of a

**[19:47]** of a [Music]


