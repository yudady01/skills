# Human seeded Evals — Samuel Colvin, Pydantic

**Video URL:** https://www.youtube.com/watch?v=o_LRtAomJCs

---

## Full Transcript

### [00:00 - 01:00]

**[00:15]** [Music]

**[00:15]** [Music] I'll assume given the time we have that

**[00:16]** I'll assume given the time we have that

**[00:16]** I'll assume given the time we have that you kind of get who I am and what

**[00:18]** you kind of get who I am and what

**[00:18]** you kind of get who I am and what Pyantic is to some extent. So I will I

**[00:20]** Pyantic is to some extent. So I will I

**[00:20]** Pyantic is to some extent. So I will I will move on. This is this I'm using the

**[00:22]** will move on. This is this I'm using the

**[00:22]** will move on. This is this I'm using the talk I gave at Pyon. So uh it it was

**[00:25]** talk I gave at Pyon. So uh it it was

**[00:25]** talk I gave at Pyon. So uh it it was building uh AI applications the pantic

**[00:27]** building uh AI applications the pantic

**[00:27]** building uh AI applications the pantic way which is uh I guess somewhat akin as

**[00:30]** way which is uh I guess somewhat akin as

**[00:30]** way which is uh I guess somewhat akin as I say I'm not going to be able to get to

**[00:31]** I say I'm not going to be able to get to

**[00:31]** I say I'm not going to be able to get to the eval stuff today. Um but I I can

**[00:34]** the eval stuff today. Um but I I can

**[00:34]** the eval stuff today. Um but I I can talk about these two. So everything is

**[00:37]** talk about these two. So everything is

**[00:37]** talk about these two. So everything is changing really fast as we all get told

**[00:38]** changing really fast as we all get told

**[00:38]** changing really fast as we all get told repeatedly in ever more hysterical terms

**[00:42]** repeatedly in ever more hysterical terms

**[00:42]** repeatedly in ever more hysterical terms actually some things are not changing.

**[00:43]** actually some things are not changing.

**[00:44]** actually some things are not changing. We still want to build reliable scalable

**[00:45]** We still want to build reliable scalable

**[00:45]** We still want to build reliable scalable applications and that is still hard

**[00:47]** applications and that is still hard

**[00:47]** applications and that is still hard arguably it's actually harder with Gen

**[00:49]** arguably it's actually harder with Gen

**[00:49]** arguably it's actually harder with Gen AI than it was before. Whether that is

**[00:51]** AI than it was before. Whether that is

**[00:51]** AI than it was before. Whether that is using Genai to build it or using Genai

**[00:53]** using Genai to build it or using Genai

**[00:53]** using Genai to build it or using Genai within your application.

**[00:55]** within your application.

**[00:55]** within your application. Um so what we're trying to talk about

**[00:57]** Um so what we're trying to talk about

**[00:57]** Um so what we're trying to talk about here is is uh some techniques that you

**[00:59]** here is is uh some techniques that you


### [01:00 - 02:00]

**[01:00]** here is is uh some techniques that you can use to build applications uh quickly

**[01:02]** can use to build applications uh quickly

**[01:02]** can use to build applications uh quickly but also somewhat more safely than than

**[01:05]** but also somewhat more safely than than

**[01:05]** but also somewhat more safely than than you might you might do if you otherwise.

**[01:08]** you might you might do if you otherwise.

**[01:08]** you might you might do if you otherwise. Um I'm a strong believer that type

**[01:11]** Um I'm a strong believer that type

**[01:11]** Um I'm a strong believer that type safety is one of the really important

**[01:12]** safety is one of the really important

**[01:12]** safety is one of the really important parts of that not just for in production

**[01:14]** parts of that not just for in production

**[01:14]** parts of that not just for in production avoiding bugs but if you no one starts

**[01:17]** avoiding bugs but if you no one starts

**[01:17]** avoiding bugs but if you no one starts off building an AI application knowing

**[01:19]** off building an AI application knowing

**[01:19]** off building an AI application knowing what it's going to look like. So you are

**[01:20]** what it's going to look like. So you are

**[01:20]** what it's going to look like. So you are going to have to end up refactoring your

**[01:21]** going to have to end up refactoring your

**[01:21]** going to have to end up refactoring your application multiple times. If you build

**[01:23]** application multiple times. If you build

**[01:23]** application multiple times. If you build your application in a type safe way, if

**[01:25]** your application in a type safe way, if

**[01:25]** your application in a type safe way, if you use frameworks that allow it to be

**[01:26]** you use frameworks that allow it to be

**[01:26]** you use frameworks that allow it to be type safe, you can refactor it with

**[01:28]** type safe, you can refactor it with

**[01:28]** type safe, you can refactor it with confidence much more quickly. If you're

**[01:30]** confidence much more quickly. If you're

**[01:30]** confidence much more quickly. If you're using a coding agent like cursor, it can

**[01:32]** using a coding agent like cursor, it can

**[01:32]** using a coding agent like cursor, it can use type safety or running type type

**[01:34]** use type safety or running type type

**[01:34]** use type safety or running type type checking to get get basically mark its

**[01:36]** checking to get get basically mark its

**[01:36]** checking to get get basically mark its own homework and work out what it's

**[01:37]** own homework and work out what it's

**[01:37]** own homework and work out what it's doing right in a way that you can't do

**[01:39]** doing right in a way that you can't do

**[01:39]** doing right in a way that you can't do if you use a framework like Langchain or

**[01:41]** if you use a framework like Langchain or

**[01:41]** if you use a framework like Langchain or Langraph who either through decision or

**[01:43]** Langraph who either through decision or

**[01:43]** Langraph who either through decision or inability decided not to build something

**[01:45]** inability decided not to build something

**[01:45]** inability decided not to build something that's type safe. Um, I'll talk a bit

**[01:48]** that's type safe. Um, I'll talk a bit

**[01:48]** that's type safe. Um, I'll talk a bit about MCTP if I have a moment. Um, and I

**[01:51]** about MCTP if I have a moment. Um, and I

**[01:51]** about MCTP if I have a moment. Um, and I won't talk about how eval split in

**[01:53]** won't talk about how eval split in

**[01:53]** won't talk about how eval split in because I don't have time. Um, so before

**[01:56]** because I don't have time. Um, so before

**[01:56]** because I don't have time. Um, so before look, nothing I'm going to say here on

**[01:57]** look, nothing I'm going to say here on

**[01:57]** look, nothing I'm going to say here on what an agent is is controversial. This

**[01:59]** what an agent is is controversial. This

**[01:59]** what an agent is is controversial. This is um reasonably well accepted now by by


### [02:00 - 03:00]

**[02:03]** is um reasonably well accepted now by by

**[02:03]** is um reasonably well accepted now by by most people as a definition of an agent.

**[02:05]** most people as a definition of an agent.

**[02:05]** most people as a definition of an agent. This uh

**[02:12]** image here is from Barry Zang's talk at

**[02:12]** image here is from Barry Zang's talk at AI engineer in New York in February.

**[02:15]** AI engineer in New York in February.

**[02:15]** AI engineer in New York in February. This is his definition or the the the

**[02:17]** This is his definition or the the the

**[02:17]** This is his definition or the the the anthropic definition of what an agent is

**[02:19]** anthropic definition of what an agent is

**[02:19]** anthropic definition of what an agent is now being copied by us by OpenAI by

**[02:22]** now being copied by us by OpenAI by

**[02:22]** now being copied by us by OpenAI by Google's ADK. I think generally the

**[02:24]** Google's ADK. I think generally the

**[02:24]** Google's ADK. I think generally the accepted definition of an agent. This

**[02:26]** accepted definition of an agent. This

**[02:26]** accepted definition of an agent. This although very neat doesn't really make

**[02:27]** although very neat doesn't really make

**[02:28]** although very neat doesn't really make any sense to me. This however does make

**[02:30]** any sense to me. This however does make

**[02:30]** any sense to me. This however does make sense. So what what they say is that an

**[02:32]** sense. So what what they say is that an

**[02:32]** sense. So what what they say is that an agent is effectively something that has

**[02:34]** agent is effectively something that has

**[02:34]** agent is effectively something that has has an environment.

**[02:36]** has an environment.

**[02:36]** has an environment. There are some tools which may have

**[02:38]** There are some tools which may have

**[02:38]** There are some tools which may have access to the environment. There is some

**[02:39]** access to the environment. There is some

**[02:39]** access to the environment. There is some system prompt that describes to it what

**[02:41]** system prompt that describes to it what

**[02:41]** system prompt that describes to it what it's supposed to do. And then you have a

**[02:43]** it's supposed to do. And then you have a

**[02:43]** it's supposed to do. And then you have a while loop where you call the LLM, get

**[02:46]** while loop where you call the LLM, get

**[02:46]** while loop where you call the LLM, get back some actions to run in the tool,

**[02:48]** back some actions to run in the tool,

**[02:48]** back some actions to run in the tool, run the tools that updates the state uh

**[02:50]** run the tools that updates the state uh

**[02:50]** run the tools that updates the state uh and then you call the LLM again. There

**[02:53]** and then you call the LLM again. There

**[02:53]** and then you call the LLM again. There is however even in his whatever it is

**[02:56]** is however even in his whatever it is

**[02:56]** is however even in his whatever it is six line pseudo code a bug which is

**[02:59]** six line pseudo code a bug which is

**[02:59]** six line pseudo code a bug which is there is no exit from that loop and sure


### [03:00 - 04:00]

**[03:01]** there is no exit from that loop and sure

**[03:01]** there is no exit from that loop and sure enough that points towards a real

**[03:02]** enough that points towards a real

**[03:02]** enough that points towards a real problem which is there is it is not

**[03:04]** problem which is there is it is not

**[03:04]** problem which is there is it is not clear when you should exit that loop

**[03:06]** clear when you should exit that loop

**[03:06]** clear when you should exit that loop that that loop and so there are there

**[03:08]** that that loop and so there are there

**[03:08]** that that loop and so there are there are a number of different things you can

**[03:09]** are a number of different things you can

**[03:09]** are a number of different things you can do. You can say when the LLM returns

**[03:11]** do. You can say when the LLM returns

**[03:11]** do. You can say when the LLM returns plain text rather than calling the tool

**[03:14]** plain text rather than calling the tool

**[03:14]** plain text rather than calling the tool that is the end or you can have certain

**[03:15]** that is the end or you can have certain

**[03:15]** that is the end or you can have certain tools which are kind of uh what we call

**[03:18]** tools which are kind of uh what we call

**[03:18]** tools which are kind of uh what we call final result tools which basically

**[03:20]** final result tools which basically

**[03:20]** final result tools which basically trigger the end end of the run or if you

**[03:22]** trigger the end end of the run or if you

**[03:22]** trigger the end end of the run or if you have models like OpenAI or Google which

**[03:25]** have models like OpenAI or Google which

**[03:25]** have models like OpenAI or Google which have structured output types you can use

**[03:27]** have structured output types you can use

**[03:27]** have structured output types you can use that to end your run but it is it's not

**[03:29]** that to end your run but it is it's not

**[03:29]** that to end your run but it is it's not necessarily trivial to work out when the

**[03:30]** necessarily trivial to work out when the

**[03:30]** necessarily trivial to work out when the end is. So enough pseudo code let me run

**[03:33]** end is. So enough pseudo code let me run

**[03:33]** end is. So enough pseudo code let me run a real minimal example of pantic AI. So

**[03:36]** a real minimal example of pantic AI. So

**[03:36]** a real minimal example of pantic AI. So this is uh a very simple um padantic

**[03:40]** this is uh a very simple um padantic

**[03:40]** this is uh a very simple um padantic based model with three fields. Uh and

**[03:43]** based model with three fields. Uh and

**[03:43]** based model with three fields. Uh and then we're going to use pantic AI to

**[03:44]** then we're going to use pantic AI to

**[03:44]** then we're going to use pantic AI to extract structured data that fits that

**[03:46]** extract structured data that fits that

**[03:46]** extract structured data that fits that that person uh schema from unstructured

**[03:49]** that person uh schema from unstructured

**[03:49]** that person uh schema from unstructured data. This sentence here now here

**[03:51]** data. This sentence here now here

**[03:51]** data. This sentence here now here obviously to fit this into on screen. Uh

**[03:53]** obviously to fit this into on screen. Uh

**[03:53]** obviously to fit this into on screen. Uh this is um a very very simple example

**[03:57]** this is um a very very simple example

**[03:57]** this is um a very very simple example but this could be a PDF uh tens of


### [04:00 - 05:00]

**[04:00]** but this could be a PDF uh tens of

**[04:00]** but this could be a PDF uh tens of megabytes. Well, probably not tens of

**[04:02]** megabytes. Well, probably not tens of

**[04:02]** megabytes. Well, probably not tens of megabytes necessarily in context, but

**[04:03]** megabytes necessarily in context, but

**[04:03]** megabytes necessarily in context, but like definitely, you know, enormous

**[04:05]** like definitely, you know, enormous

**[04:05]** like definitely, you know, enormous documents and and the schema is very

**[04:07]** documents and and the schema is very

**[04:07]** documents and and the schema is very simple, but this could be an incredibly

**[04:09]** simple, but this could be an incredibly

**[04:09]** simple, but this could be an incredibly complex nested schema models are still

**[04:11]** complex nested schema models are still

**[04:11]** complex nested schema models are still able to do it. And sure enough, if we go

**[04:13]** able to do it. And sure enough, if we go

**[04:13]** able to do it. And sure enough, if we go and run this example and the gods of the

**[04:14]** and run this example and the gods of the

**[04:14]** and run this example and the gods of the internet are with us, sure enough, we

**[04:17]** internet are with us, sure enough, we

**[04:17]** internet are with us, sure enough, we get the the pyantic model uh printed

**[04:19]** get the the pyantic model uh printed

**[04:19]** get the the pyantic model uh printed out. So, but some of you will notice

**[04:21]** out. So, but some of you will notice

**[04:22]** out. So, but some of you will notice that this example is simple enough that

**[04:23]** that this example is simple enough that

**[04:23]** that this example is simple enough that we don't actually need an agent or this

**[04:25]** we don't actually need an agent or this

**[04:25]** we don't actually need an agent or this loop. We're doing one shot. We make one

**[04:27]** loop. We're doing one shot. We make one

**[04:28]** loop. We're doing one shot. We make one call to the LM returns the structured

**[04:30]** call to the LM returns the structured

**[04:30]** call to the LM returns the structured data. We call under the hood. We call a

**[04:32]** data. We call under the hood. We call a

**[04:32]** data. We call under the hood. We call a final result tool. Pyantic AI performs a

**[04:35]** final result tool. Pyantic AI performs a

**[04:35]** final result tool. Pyantic AI performs a validation and we get back the data. But

**[04:37]** validation and we get back the data. But

**[04:37]** validation and we get back the data. But we don't have to change that example

**[04:39]** we don't have to change that example

**[04:39]** we don't have to change that example very much to start seeing the value of

**[04:41]** very much to start seeing the value of

**[04:41]** very much to start seeing the value of the agantic loop. So here I'm being a

**[04:43]** the agantic loop. So here I'm being a

**[04:43]** the agantic loop. So here I'm being a little bit unfair to the to the model.

**[04:45]** little bit unfair to the to the model.

**[04:45]** little bit unfair to the to the model. I've added a field validator to my

**[04:48]** I've added a field validator to my

**[04:48]** I've added a field validator to my person model which says the date of

**[04:51]** person model which says the date of

**[04:51]** person model which says the date of birth needs to be before 1900. And

**[04:53]** birth needs to be before 1900. And

**[04:53]** birth needs to be before 1900. And obviously the the actual definition here

**[04:55]** obviously the the actual definition here

**[04:55]** obviously the the actual definition here is abstract uh is uh doesn't define what

**[04:59]** is abstract uh is uh doesn't define what

**[04:59]** is abstract uh is uh doesn't define what year we're going to be um well sorry


### [05:00 - 06:00]

**[05:03]** year we're going to be um well sorry

**[05:03]** year we're going to be um well sorry what which century we're talking about.

**[05:04]** what which century we're talking about.

**[05:04]** what which century we're talking about. You would obviously the model will for

**[05:06]** You would obviously the model will for

**[05:06]** You would obviously the model will for the most part assume 87 is 1987. will

**[05:09]** the most part assume 87 is 1987. will

**[05:09]** the most part assume 87 is 1987. will then get a validation error when you do

**[05:11]** then get a validation error when you do

**[05:11]** then get a validation error when you do the validation and that's where the

**[05:12]** the validation and that's where the

**[05:12]** the validation and that's where the agantic bit kicks in because we will

**[05:14]** agantic bit kicks in because we will

**[05:14]** agantic bit kicks in because we will take those validation errors and return

**[05:17]** take those validation errors and return

**[05:17]** take those validation errors and return them to the model basically as a

**[05:18]** them to the model basically as a

**[05:18]** them to the model basically as a definition and say please try again as

**[05:19]** definition and say please try again as

**[05:20]** definition and say please try again as I'll show you in a moment and the model

**[05:21]** I'll show you in a moment and the model

**[05:21]** I'll show you in a moment and the model is then able to use the information from

**[05:22]** is then able to use the information from

**[05:22]** is then able to use the information from the validation error to to try again.

**[05:25]** the validation error to to try again.

**[05:25]** the validation error to to try again. Obviously, if you were trying to do this

**[05:26]** Obviously, if you were trying to do this

**[05:26]** Obviously, if you were trying to do this case in production, you would add a a

**[05:29]** case in production, you would add a a

**[05:29]** case in production, you would add a a dock string to the do field saying it

**[05:31]** dock string to the do field saying it

**[05:31]** dock string to the do field saying it must be in the 19th century. But there

**[05:32]** must be in the 19th century. But there

**[05:32]** must be in the 19th century. But there are definitely cases where models, even

**[05:34]** are definitely cases where models, even

**[05:34]** are definitely cases where models, even the smartest models, don't uh pass

**[05:37]** the smartest models, don't uh pass

**[05:38]** the smartest models, don't uh pass validation. And being able to use this

**[05:39]** validation. And being able to use this

**[05:39]** validation. And being able to use this trick of returning validation errors um

**[05:42]** trick of returning validation errors um

**[05:42]** trick of returning validation errors um to the model is is a very effective way

**[05:44]** to the model is is a very effective way

**[05:44]** to the model is is a very effective way of fixing a lot of the simplest use

**[05:45]** of fixing a lot of the simplest use

**[05:45]** of fixing a lot of the simplest use cases. So, if we run this,

**[05:49]** cases. So, if we run this,

**[05:49]** cases. So, if we run this, you see we had two calls to Gemini here.

**[05:51]** you see we had two calls to Gemini here.

**[05:51]** you see we had two calls to Gemini here. And if I come and open you other thing

**[05:53]** And if I come and open you other thing

**[05:53]** And if I come and open you other thing you'll see in this example is we

**[05:54]** you'll see in this example is we

**[05:54]** you'll see in this example is we instrumented um this code with uh with

**[05:59]** instrumented um this code with uh with

**[05:59]** instrumented um this code with uh with logfire our observability platform. So


### [06:00 - 07:00]

**[06:01]** logfire our observability platform. So

**[06:01]** logfire our observability platform. So we can actually go in and see exactly

**[06:03]** we can actually go in and see exactly

**[06:03]** we can actually go in and see exactly what happened. So you'll see our agent

**[06:05]** what happened. So you'll see our agent

**[06:05]** what happened. So you'll see our agent run we had two

**[06:07]** run we had two

**[06:07]** run we had two uh two calls to the model in this case

**[06:09]** uh two calls to the model in this case

**[06:09]** uh two calls to the model in this case Gemini flash. And if we go and look at

**[06:12]** Gemini flash. And if we go and look at

**[06:12]** Gemini flash. And if we go and look at the the exchange you can see what's

**[06:15]** the the exchange you can see what's

**[06:15]** the the exchange you can see what's happened here. So

**[06:17]** happened here. So

**[06:17]** happened here. So we I just try and make it big enough

**[06:18]** we I just try and make it big enough

**[06:18]** we I just try and make it big enough that you can see it. We first of all had

**[06:20]** that you can see it. We first of all had

**[06:20]** that you can see it. We first of all had the user prompt the description. It

**[06:22]** the user prompt the description. It

**[06:22]** the user prompt the description. It called the final result tool as you

**[06:23]** called the final result tool as you

**[06:23]** called the final result tool as you might expect with the date of birth

**[06:25]** might expect with the date of birth

**[06:25]** might expect with the date of birth being 1987. Uh we then responded. The

**[06:28]** being 1987. Uh we then responded. The

**[06:28]** being 1987. Uh we then responded. The tool response was validation error

**[06:31]** tool response was validation error

**[06:31]** tool response was validation error incorrect. Please try and then we we add

**[06:33]** incorrect. Please try and then we we add

**[06:33]** incorrect. Please try and then we we add on the end please fix the error and try

**[06:35]** on the end please fix the error and try

**[06:35]** on the end please fix the error and try again. And sure enough it was then able

**[06:37]** again. And sure enough it was then able

**[06:37]** again. And sure enough it was then able to

**[06:39]** to

**[06:39]** to return uh correctly call the final

**[06:41]** return uh correctly call the final

**[06:41]** return uh correctly call the final result tool with the right date of birth

**[06:43]** result tool with the right date of birth

**[06:43]** result tool with the right date of birth and succeed. Cool. I've got five

**[06:45]** and succeed. Cool. I've got five

**[06:45]** and succeed. Cool. I've got five minutes. I feel like I'm in one of

**[06:46]** minutes. I feel like I'm in one of

**[06:46]** minutes. I feel like I'm in one of those. Uh see how fast I can go. Uh I'm

**[06:50]** those. Uh see how fast I can go. Uh I'm

**[06:50]** those. Uh see how fast I can go. Uh I'm on the wrong window am I? I am here we

**[06:54]** on the wrong window am I? I am here we

**[06:54]** on the wrong window am I? I am here we are. Um I think the other thing that's

**[06:58]** are. Um I think the other thing that's

**[06:58]** are. Um I think the other thing that's worth worth saying here even if I don't


### [07:00 - 08:00]

**[07:00]** worth worth saying here even if I don't

**[07:00]** worth worth saying here even if I don't have that much time is if you take a

**[07:03]** have that much time is if you take a

**[07:03]** have that much time is if you take a look at the this example I talked about

**[07:05]** look at the this example I talked about

**[07:05]** look at the this example I talked about type safety. If you look the way that

**[07:06]** type safety. If you look the way that

**[07:06]** type safety. If you look the way that we're doing this under the hood agent

**[07:08]** we're doing this under the hood agent

**[07:08]** we're doing this under the hood agent because of the output type is generic in

**[07:11]** because of the output type is generic in

**[07:11]** because of the output type is generic in in this case person. And so we can act

**[07:13]** in this case person. And so we can act

**[07:13]** in this case person. And so we can act when we access uh result output both in

**[07:17]** when we access uh result output both in

**[07:17]** when we access uh result output both in typing terms it's an instance of person

**[07:19]** typing terms it's an instance of person

**[07:19]** typing terms it's an instance of person and uh a runtime will guaranteed from

**[07:21]** and uh a runtime will guaranteed from

**[07:21]** and uh a runtime will guaranteed from the pyantic validation that it will

**[07:23]** the pyantic validation that it will

**[07:23]** the pyantic validation that it will really be an instance of person. So if I

**[07:25]** really be an instance of person. So if I

**[07:25]** really be an instance of person. So if I access herename

**[07:27]** access herename

**[07:27]** access herename all will be well if I access first name

**[07:30]** all will be well if I access first name

**[07:30]** all will be well if I access first name uh we suddenly get a validation we get a

**[07:33]** uh we suddenly get a validation we get a

**[07:33]** uh we suddenly get a validation we get a runtime we get the the nice error from

**[07:35]** runtime we get the the nice error from

**[07:35]** runtime we get the the nice error from typing saying this is a incorrect field.

**[07:37]** typing saying this is a incorrect field.

**[07:37]** typing saying this is a incorrect field. So that's the kind of the the kind of

**[07:39]** So that's the kind of the the kind of

**[07:39]** So that's the kind of the the kind of very beginning of the value of static

**[07:41]** very beginning of the value of static

**[07:41]** very beginning of the value of static typing uh of of our typing support. We

**[07:44]** typing uh of of our typing support. We

**[07:44]** typing uh of of our typing support. We go a lot further. You will have seen or

**[07:46]** go a lot further. You will have seen or

**[07:46]** go a lot further. You will have seen or some of you might have noticed there's a

**[07:47]** some of you might have noticed there's a

**[07:47]** some of you might have noticed there's a second generic on agent um which is the

**[07:50]** second generic on agent um which is the

**[07:50]** second generic on agent um which is the depths type. And so if you register

**[07:52]** depths type. And so if you register

**[07:52]** depths type. And so if you register tools with this agent they you can have

**[07:55]** tools with this agent they you can have

**[07:55]** tools with this agent they you can have type safe dependencies to tools which I

**[07:57]** type safe dependencies to tools which I

**[07:57]** type safe dependencies to tools which I will show you in a moment.

**[07:59]** will show you in a moment.

**[07:59]** will show you in a moment. Um so the other thing you will you will


### [08:00 - 09:00]

**[08:01]** Um so the other thing you will you will

**[08:01]** Um so the other thing you will you will notice is missing from this example is

**[08:03]** notice is missing from this example is

**[08:03]** notice is missing from this example is any tools. So let's look at an example

**[08:05]** any tools. So let's look at an example

**[08:05]** any tools. So let's look at an example with tools. So if I open this example

**[08:09]** with tools. So if I open this example

**[08:09]** with tools. So if I open this example here, we have this is an example of

**[08:12]** here, we have this is an example of

**[08:12]** here, we have this is an example of memory, long-term memory in particular

**[08:13]** memory, long-term memory in particular

**[08:14]** memory, long-term memory in particular where we're using a tool to record

**[08:15]** where we're using a tool to record

**[08:15]** where we're using a tool to record memories and then uh another tool to be

**[08:18]** memories and then uh another tool to be

**[08:18]** memories and then uh another tool to be able to retrieve memories. So you'll see

**[08:20]** able to retrieve memories. So you'll see

**[08:20]** able to retrieve memories. So you'll see we have these two tools here, record

**[08:22]** we have these two tools here, record

**[08:22]** we have these two tools here, record memory and retrieve memory tools are set

**[08:24]** memory and retrieve memory tools are set

**[08:24]** memory and retrieve memory tools are set up by registering them with the agent.

**[08:28]** up by registering them with the agent.

**[08:28]** up by registering them with the agent. Decorate uh decorator. But this is where

**[08:30]** Decorate uh decorator. But this is where

**[08:30]** Decorate uh decorator. But this is where the typing as I say gets more complex.

**[08:32]** the typing as I say gets more complex.

**[08:32]** the typing as I say gets more complex. Now you will see that we've set depths

**[08:34]** Now you will see that we've set depths

**[08:34]** Now you will see that we've set depths type when we've defined the agent and so

**[08:36]** type when we've defined the agent and so

**[08:36]** type when we've defined the agent and so our agent is now generic in that depths

**[08:38]** our agent is now generic in that depths

**[08:38]** our agent is now generic in that depths type the return type is string because

**[08:40]** type the return type is string because

**[08:40]** type the return type is string because that's the default and so we when we

**[08:43]** that's the default and so we when we

**[08:43]** that's the default and so we when we call the tool decorator we have to set

**[08:45]** call the tool decorator we have to set

**[08:45]** call the tool decorator we have to set the first argument to be this run

**[08:46]** the first argument to be this run

**[08:46]** the first argument to be this run context to parameterize with our depths

**[08:49]** context to parameterize with our depths

**[08:49]** context to parameterize with our depths type and so when we access context.eps

**[08:51]** type and so when we access context.eps

**[08:51]** type and so when we access context.eps deps that is an instance of our of our

**[08:54]** deps that is an instance of our of our

**[08:54]** deps that is an instance of our of our depths data class that you see there and

**[08:55]** depths data class that you see there and

**[08:55]** depths data class that you see there and if we access one of its attributes we

**[08:57]** if we access one of its attributes we

**[08:57]** if we access one of its attributes we get the actual type and if we change

**[08:59]** get the actual type and if we change

**[08:59]** get the actual type and if we change this to be


### [09:00 - 10:00]

**[09:01]** this to be

**[09:01]** this to be int let's say suddenly we get an error

**[09:03]** int let's say suddenly we get an error

**[09:03]** int let's say suddenly we get an error saying we've used the wrong the wrong

**[09:05]** saying we've used the wrong the wrong

**[09:05]** saying we've used the wrong the wrong type. So we get this guarantee that the

**[09:08]** type. So we get this guarantee that the

**[09:08]** type. So we get this guarantee that the type here matches the type here matches

**[09:10]** type here matches the type here matches

**[09:10]** type here matches the type here matches the attributes you can access here and

**[09:12]** the attributes you can access here and

**[09:12]** the attributes you can access here and then when we come to run the agent we

**[09:14]** then when we come to run the agent we

**[09:14]** then when we come to run the agent we need our depths to be an instance of

**[09:15]** need our depths to be an instance of

**[09:15]** need our depths to be an instance of that depths type. So again, if we put

**[09:17]** that depths type. So again, if we put

**[09:17]** that depths type. So again, if we put gave it the wrong type, we would get a a

**[09:19]** gave it the wrong type, we would get a a

**[09:19]** gave it the wrong type, we would get a a typing error saying you're using the

**[09:21]** typing error saying you're using the

**[09:21]** typing error saying you're using the wrong type. And as far as I know, we're

**[09:23]** wrong type. And as far as I know, we're

**[09:23]** wrong type. And as far as I know, we're what the only

**[09:25]** what the only

**[09:25]** what the only agent framework that works this hard to

**[09:26]** agent framework that works this hard to

**[09:26]** agent framework that works this hard to be type safe. And it is quite a lot of

**[09:29]** be type safe. And it is quite a lot of

**[09:29]** be type safe. And it is quite a lot of work on our side. I'll be honest,

**[09:30]** work on our side. I'll be honest,

**[09:30]** work on our side. I'll be honest, there's a little bit of work on your

**[09:31]** there's a little bit of work on your

**[09:31]** there's a little bit of work on your side as well as in it's not necessarily

**[09:32]** side as well as in it's not necessarily

**[09:32]** side as well as in it's not necessarily as trivial to set up, but it makes it

**[09:35]** as trivial to set up, but it makes it

**[09:35]** as trivial to set up, but it makes it incredibly easy to go and refactor your

**[09:36]** incredibly easy to go and refactor your

**[09:36]** incredibly easy to go and refactor your code. Um, and yeah, you we run this here

**[09:39]** code. Um, and yeah, you we run this here

**[09:39]** code. Um, and yeah, you we run this here and we give it the the I'm pretty sure I

**[09:42]** and we give it the the I'm pretty sure I

**[09:42]** and we give it the the I'm pretty sure I don't have Postgress running.

**[09:45]** don't have Postgress running.

**[09:45]** don't have Postgress running. Uh, do I have Docker running? I don't

**[09:46]** Uh, do I have Docker running? I don't

**[09:46]** Uh, do I have Docker running? I don't know if I have time to make that work.

**[09:50]** know if I have time to make that work.

**[09:50]** know if I have time to make that work. I will. That's Docker running. I'll just

**[09:52]** I will. That's Docker running. I'll just

**[09:52]** I will. That's Docker running. I'll just try and run this very quickly.

**[09:55]** try and run this very quickly.

**[09:55]** try and run this very quickly. Uh, docker run.

**[09:58]** Uh, docker run.

**[09:58]** Uh, docker run. Hopefully that is enough. If I now come


### [10:00 - 11:00]

**[10:01]** Hopefully that is enough. If I now come

**[10:01]** Hopefully that is enough. If I now come and run this example,

**[10:03]** and run this example,

**[10:03]** and run this example, what you will see

**[10:06]** what you will see

**[10:06]** what you will see is

**[10:07]** is

**[10:07]** is it successfully failed. Great. Um, I

**[10:12]** it successfully failed. Great. Um, I

**[10:12]** it successfully failed. Great. Um, I will try one more time and see if I get

**[10:14]** will try one more time and see if I get

**[10:14]** will try one more time and see if I get lucky. I don't know quite what was going

**[10:15]** lucky. I don't know quite what was going

**[10:15]** lucky. I don't know quite what was going on there.

**[10:21]** Ah, and I have no Well, we can look in

**[10:21]** Ah, and I have no Well, we can look in logfire and see what happened uh to make

**[10:23]** logfire and see what happened uh to make

**[10:23]** logfire and see what happened uh to make it fail. I promise you I hadn't set that

**[10:25]** it fail. I promise you I hadn't set that

**[10:25]** it fail. I promise you I hadn't set that up to fail the first time to demonstrate

**[10:26]** up to fail the first time to demonstrate

**[10:26]** up to fail the first time to demonstrate the value of observability, but maybe it

**[10:28]** the value of observability, but maybe it

**[10:28]** the value of observability, but maybe it can help here. So if you look um this

**[10:32]** can help here. So if you look um this

**[10:32]** can help here. So if you look um this first time we um our first agent run

**[10:37]** first time we um our first agent run

**[10:37]** first time we um our first agent run you'll see that we

**[10:40]** you'll see that we

**[10:40]** you'll see that we use the uh the tool called uh record

**[10:44]** use the uh the tool called uh record

**[10:44]** use the uh the tool called uh record memory the user's name is Samuel um and

**[10:46]** memory the user's name is Samuel um and

**[10:46]** memory the user's name is Samuel um and then it it returned finished and then

**[10:48]** then it it returned finished and then

**[10:48]** then it it returned finished and then the second time

**[10:50]** the second time

**[10:50]** the second time uh you can see that the when it did

**[10:53]** uh you can see that the when it did

**[10:53]** uh you can see that the when it did retrieve memory where it called the that

**[10:56]** retrieve memory where it called the that

**[10:56]** retrieve memory where it called the that tool the parameter or the argument it

**[10:59]** tool the parameter or the argument it

**[10:59]** tool the parameter or the argument it gave was your name. Um, which was not is


### [11:00 - 12:00]

**[11:03]** gave was your name. Um, which was not is

**[11:03]** gave was your name. Um, which was not is not contained within the the query the

**[11:05]** not contained within the the query the

**[11:05]** not contained within the the query the previous time. We're just doing a very

**[11:06]** previous time. We're just doing a very

**[11:06]** previous time. We're just doing a very simple I like here. So your name is not

**[11:09]** simple I like here. So your name is not

**[11:09]** simple I like here. So your name is not a substring of user's name is Samuel.

**[11:13]** a substring of user's name is Samuel.

**[11:13]** a substring of user's name is Samuel. And so that's why why it failed that

**[11:14]** And so that's why why it failed that

**[11:14]** And so that's why why it failed that time. Um, so this has turned into a very

**[11:17]** time. Um, so this has turned into a very

**[11:17]** time. Um, so this has turned into a very useful example of where where Logfire

**[11:18]** useful example of where where Logfire

**[11:18]** useful example of where where Logfire can help. And if we look at the that

**[11:21]** can help. And if we look at the that

**[11:21]** can help. And if we look at the that second time,

**[11:23]** second time,

**[11:23]** second time, you'll see user's name is Samuel. And

**[11:25]** you'll see user's name is Samuel. And

**[11:25]** you'll see user's name is Samuel. And then when it when it ran the

**[11:28]** then when it when it ran the

**[11:28]** then when it when it ran the agent, it just asked for name. N name is

**[11:30]** agent, it just asked for name. N name is

**[11:30]** agent, it just asked for name. N name is obviously a substring of of the user's

**[11:32]** obviously a substring of of the user's

**[11:32]** obviously a substring of of the user's name is Samuel. And so it was able it

**[11:34]** name is Samuel. And so it was able it

**[11:34]** name is Samuel. And so it was able it got the response. User's name is Samuel.

**[11:36]** got the response. User's name is Samuel.

**[11:36]** got the response. User's name is Samuel. And therefore succeeded. The other thing

**[11:39]** And therefore succeeded. The other thing

**[11:39]** And therefore succeeded. The other thing we get here is like obviously we get

**[11:40]** we get here is like obviously we get

**[11:40]** we get here is like obviously we get this tracing information. So we can see

**[11:41]** this tracing information. So we can see

**[11:41]** this tracing information. So we can see how long each of those calls took. Um

**[11:44]** how long each of those calls took. Um

**[11:44]** how long each of those calls took. Um and we also get pricing on both

**[11:47]** and we also get pricing on both

**[11:47]** and we also get pricing on both aggregate across the whole of the trace

**[11:49]** aggregate across the whole of the trace

**[11:49]** aggregate across the whole of the trace and individual spans. Um I am told that

**[11:52]** and individual spans. Um I am told that

**[11:52]** and individual spans. Um I am told that I am running out of time. So, thank you

**[11:55]** I am running out of time. So, thank you

**[11:55]** I am running out of time. So, thank you very much.


