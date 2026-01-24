# Building AI Products That Actually Work — Ben Hylak (Raindrop), Sid Bendre (Oleve)

**Video URL:** https://www.youtube.com/watch?v=eSvXbb2EBYc

---

## Full Transcript

### [00:00 - 01:00]

**[00:18]** Uh my name is Ben Hilac and uh also just

**[00:18]** Uh my name is Ben Hilac and uh also just feeling really grateful to be with all

**[00:19]** feeling really grateful to be with all

**[00:19]** feeling really grateful to be with all of you guys today. Uh it's pretty

**[00:21]** of you guys today. Uh it's pretty

**[00:21]** of you guys today. Uh it's pretty exciting and we're here to talk about

**[00:24]** exciting and we're here to talk about

**[00:24]** exciting and we're here to talk about building AI products that actually work.

**[00:27]** building AI products that actually work.

**[00:27]** building AI products that actually work. Um I'll introduce this guy in a second.

**[00:29]** Um I'll introduce this guy in a second.

**[00:29]** Um I'll introduce this guy in a second. Sorry, wasn't the right word. Uh, so I

**[00:31]** Sorry, wasn't the right word. Uh, so I

**[00:31]** Sorry, wasn't the right word. Uh, so I tweeted last night. I was kind of like,

**[00:32]** tweeted last night. I was kind of like,

**[00:32]** tweeted last night. I was kind of like, what should we uh what should we talk

**[00:34]** what should we uh what should we talk

**[00:34]** what should we uh what should we talk about today? Uh, and the overwhelming

**[00:36]** about today? Uh, and the overwhelming

**[00:36]** about today? Uh, and the overwhelming response I got was like, please no more

**[00:38]** response I got was like, please no more

**[00:38]** response I got was like, please no more evals. Uh, apparently there's a lot of

**[00:40]** evals. Uh, apparently there's a lot of

**[00:40]** evals. Uh, apparently there's a lot of eval tracks. We'll touch on eval still

**[00:42]** eval tracks. We'll touch on eval still

**[00:42]** eval tracks. We'll touch on eval still just a little bit, but mainly we're

**[00:44]** just a little bit, but mainly we're

**[00:44]** just a little bit, but mainly we're going to be focusing on how to iterate

**[00:47]** going to be focusing on how to iterate

**[00:47]** going to be focusing on how to iterate on AI products. And so I think iteration

**[00:50]** on AI products. And so I think iteration

**[00:50]** on AI products. And so I think iteration is actually one of the most important

**[00:52]** is actually one of the most important

**[00:52]** is actually one of the most important parts of building AI products that

**[00:54]** parts of building AI products that

**[00:54]** parts of building AI products that actually work. So again, just a little

**[00:56]** actually work. So again, just a little

**[00:56]** actually work. So again, just a little bit about us. So, I'm the CTO of a

**[00:58]** bit about us. So, I'm the CTO of a

**[00:58]** bit about us. So, I'm the CTO of a company called Raindrop. And Raindrop


### [01:00 - 02:00]

**[01:00]** company called Raindrop. And Raindrop

**[01:00]** company called Raindrop. And Raindrop helps companies find and fix issues in

**[01:03]** helps companies find and fix issues in

**[01:03]** helps companies find and fix issues in their AI products. Uh, before that, I

**[01:06]** their AI products. Uh, before that, I

**[01:06]** their AI products. Uh, before that, I was actually kind of a weird background,

**[01:07]** was actually kind of a weird background,

**[01:08]** was actually kind of a weird background, but I used to be really into robotics. I

**[01:09]** but I used to be really into robotics. I

**[01:09]** but I used to be really into robotics. I did avionics at SpaceX for a little bit.

**[01:12]** did avionics at SpaceX for a little bit.

**[01:12]** did avionics at SpaceX for a little bit. Um, and then most recently, I was an

**[01:14]** Um, and then most recently, I was an

**[01:14]** Um, and then most recently, I was an engineer and then on the design team at

**[01:16]** engineer and then on the design team at

**[01:16]** engineer and then on the design team at Apple for almost four years. And, uh, we

**[01:19]** Apple for almost four years. And, uh, we

**[01:19]** Apple for almost four years. And, uh, we also have Sid. So, uh, in the spirit of

**[01:23]** also have Sid. So, uh, in the spirit of

**[01:23]** also have Sid. So, uh, in the spirit of sharing how to build things that

**[01:25]** sharing how to build things that

**[01:25]** sharing how to build things that actually work, uh, I brought Sid, who

**[01:28]** actually work, uh, I brought Sid, who

**[01:28]** actually work, uh, I brought Sid, who actually knows how to build products

**[01:29]** actually knows how to build products

**[01:29]** actually knows how to build products that actually work. So, I think Sid is

**[01:31]** that actually work. So, I think Sid is

**[01:31]** that actually work. So, I think Sid is like, uh, the co-founder of a company

**[01:33]** like, uh, the co-founder of a company

**[01:33]** like, uh, the co-founder of a company called Alie. Um, with just four people,

**[01:37]** called Alie. Um, with just four people,

**[01:37]** called Alie. Um, with just four people, they grew a suite of viral apps to over

**[01:39]** they grew a suite of viral apps to over

**[01:39]** they grew a suite of viral apps to over 6 million AR. So, Sid is going to share

**[01:42]** 6 million AR. So, Sid is going to share

**[01:42]** 6 million AR. So, Sid is going to share again how to build products that

**[01:44]** again how to build products that

**[01:44]** again how to build products that actually work.

**[01:49]** I think it's actually a really exciting

**[01:49]** I think it's actually a really exciting time for AI products. And I say it's an

**[01:51]** time for AI products. And I say it's an

**[01:51]** time for AI products. And I say it's an exciting time because in the last year,

**[01:54]** exciting time because in the last year,

**[01:54]** exciting time because in the last year, we've seen that it's possible to really

**[01:57]** we've seen that it's possible to really

**[01:57]** we've seen that it's possible to really focus on a use case, really focus on

**[01:59]** focus on a use case, really focus on

**[01:59]** focus on a use case, really focus on something and make that thing


### [02:00 - 03:00]

**[02:01]** something and make that thing

**[02:01]** something and make that thing exceptional, like really really crack

**[02:03]** exceptional, like really really crack

**[02:03]** exceptional, like really really crack it. Um, we've seen that it's possible to

**[02:06]** it. Um, we've seen that it's possible to

**[02:06]** it. Um, we've seen that it's possible to train like small models, really really

**[02:08]** train like small models, really really

**[02:08]** train like small models, really really tiny models to just be exceptional at

**[02:11]** tiny models to just be exceptional at

**[02:11]** tiny models to just be exceptional at specific tasks if you focus on a

**[02:13]** specific tasks if you focus on a

**[02:13]** specific tasks if you focus on a specific use case. And we're also seeing

**[02:15]** specific use case. And we're also seeing

**[02:15]** specific use case. And we're also seeing that increasingly providers right are

**[02:18]** that increasingly providers right are

**[02:18]** that increasingly providers right are actually focusing on on launching those

**[02:19]** actually focusing on on launching those

**[02:20]** actually focusing on on launching those sort of products which is you know that

**[02:21]** sort of products which is you know that

**[02:21]** sort of products which is you know that might be the scary part. Um but deep

**[02:24]** might be the scary part. Um but deep

**[02:24]** might be the scary part. Um but deep research is a great example right where

**[02:26]** research is a great example right where

**[02:26]** research is a great example right where chatpt just focused on how do we you

**[02:29]** chatpt just focused on how do we you

**[02:29]** chatpt just focused on how do we you know how do we collect a data set how do

**[02:31]** know how do we collect a data set how do

**[02:31]** know how do we collect a data set how do we train something to just be

**[02:33]** we train something to just be

**[02:33]** we train something to just be exceptionally good at searching the web

**[02:35]** exceptionally good at searching the web

**[02:35]** exceptionally good at searching the web and they were I think it's one of the

**[02:36]** and they were I think it's one of the

**[02:36]** and they were I think it's one of the best products that they've released

**[02:39]** best products that they've released

**[02:39]** best products that they've released but even openai is not immune to

**[02:42]** but even openai is not immune to

**[02:42]** but even openai is not immune to shipping like not so great products

**[02:44]** shipping like not so great products

**[02:44]** shipping like not so great products right I think like to me I I don't know

**[02:47]** right I think like to me I I don't know

**[02:47]** right I think like to me I I don't know uh what your guys' experience is but I

**[02:48]** uh what your guys' experience is but I

**[02:48]** uh what your guys' experience is but I think that like I've actually had a lot

**[02:49]** think that like I've actually had a lot

**[02:49]** think that like I've actually had a lot of trouble with codeex and I don't know

**[02:51]** of trouble with codeex and I don't know

**[02:51]** of trouble with codeex and I don't know that it's like exceptionally better than

**[02:54]** that it's like exceptionally better than

**[02:54]** that it's like exceptionally better than uh other things that exist. Like this is

**[02:55]** uh other things that exist. Like this is

**[02:55]** uh other things that exist. Like this is kind of a funny one. I was like write

**[02:56]** kind of a funny one. I was like write

**[02:56]** kind of a funny one. I was like write some tests and it it actually correctly

**[02:59]** some tests and it it actually correctly


### [03:00 - 04:00]

**[03:00]** some tests and it it actually correctly generated this hash for the word hello,

**[03:02]** generated this hash for the word hello,

**[03:02]** generated this hash for the word hello, you know, but it's like I'm not sure

**[03:03]** you know, but it's like I'm not sure

**[03:03]** you know, but it's like I'm not sure this is like, you know, when I think

**[03:04]** this is like, you know, when I think

**[03:04]** this is like, you know, when I think about writing tests for my back end, I'm

**[03:05]** about writing tests for my back end, I'm

**[03:05]** about writing tests for my back end, I'm not sure that this is what I wanted,

**[03:07]** not sure that this is what I wanted,

**[03:07]** not sure that this is what I wanted, right? Um

**[03:09]** right? Um

**[03:09]** right? Um and it's not just open AI, right? Like I

**[03:12]** and it's not just open AI, right? Like I

**[03:12]** and it's not just open AI, right? Like I think that increasingly in the last

**[03:14]** think that increasingly in the last

**[03:14]** think that increasingly in the last year, AI products still even in the last

**[03:17]** year, AI products still even in the last

**[03:17]** year, AI products still even in the last couple months, couple weeks, like

**[03:18]** couple months, couple weeks, like

**[03:18]** couple months, couple weeks, like there's all these weird issues like

**[03:20]** there's all these weird issues like

**[03:20]** there's all these weird issues like Yeah, this is a funny one, right? So,

**[03:22]** Yeah, this is a funny one, right? So,

**[03:22]** Yeah, this is a funny one, right? So, Virgin Money, their chatbot was

**[03:24]** Virgin Money, their chatbot was

**[03:24]** Virgin Money, their chatbot was threatening to cut off their customers

**[03:26]** threatening to cut off their customers

**[03:26]** threatening to cut off their customers for using the word virgin, right? So, uh

**[03:31]** for using the word virgin, right? So, uh

**[03:31]** for using the word virgin, right? So, uh just the other day I was using uh uh

**[03:33]** just the other day I was using uh uh

**[03:33]** just the other day I was using uh uh Google Cloud and I asked it where my

**[03:34]** Google Cloud and I asked it where my

**[03:34]** Google Cloud and I asked it where my credits are and it was like, "Are you

**[03:35]** credits are and it was like, "Are you

**[03:35]** credits are and it was like, "Are you talking about Azure credits or Roblox

**[03:37]** talking about Azure credits or Roblox

**[03:37]** talking about Azure credits or Roblox credits?" You know, and I was like,

**[03:38]** credits?" You know, and I was like,

**[03:38]** credits?" You know, and I was like, "What? How is this possible?" It's funny

**[03:40]** "What? How is this possible?" It's funny

**[03:40]** "What? How is this possible?" It's funny because I tweeted this and it's like,

**[03:41]** because I tweeted this and it's like,

**[03:41]** because I tweeted this and it's like, "This isn't just a one-off thing,

**[03:43]** "This isn't just a one-off thing,

**[03:43]** "This isn't just a one-off thing, right?" Like, someone's like, "Oh, yeah.

**[03:44]** right?" Like, someone's like, "Oh, yeah.

**[03:44]** right?" Like, someone's like, "Oh, yeah. This exact same thing happened to me,

**[03:46]** This exact same thing happened to me,

**[03:46]** This exact same thing happened to me, right?"

**[03:48]** right?"

**[03:48]** right?" Um

**[03:49]** Um

**[03:49]** Um just a few weeks ago Grock had this

**[03:51]** just a few weeks ago Grock had this

**[03:51]** just a few weeks ago Grock had this crazy thing right where people were

**[03:52]** crazy thing right where people were

**[03:52]** crazy thing right where people were asking in this case about enterprise

**[03:54]** asking in this case about enterprise

**[03:54]** asking in this case about enterprise software and it's like oh by the way you

**[03:57]** software and it's like oh by the way you

**[03:57]** software and it's like oh by the way you know let's talk about uh the you know

**[03:58]** know let's talk about uh the you know

**[03:58]** know let's talk about uh the you know claims of white genocide in South Africa


### [04:00 - 05:00]

**[04:01]** claims of white genocide in South Africa

**[04:01]** claims of white genocide in South Africa you know just completely off off the

**[04:02]** you know just completely off off the

**[04:02]** you know just completely off off the rails here and we only see we only

**[04:05]** rails here and we only see we only

**[04:05]** rails here and we only see we only caught something like this only kind of

**[04:07]** caught something like this only kind of

**[04:07]** caught something like this only kind of entered the public you know awareness

**[04:09]** entered the public you know awareness

**[04:09]** entered the public you know awareness because Grock is public and because you

**[04:11]** because Grock is public and because you

**[04:11]** because Grock is public and because you can kind of see everything. Funny

**[04:13]** can kind of see everything. Funny

**[04:13]** can kind of see everything. Funny enough, um I I actually tweet a lot

**[04:15]** enough, um I I actually tweet a lot

**[04:15]** enough, um I I actually tweet a lot about, if you follow me, you know I

**[04:16]** about, if you follow me, you know I

**[04:16]** about, if you follow me, you know I tweet a lot about AI products and where

**[04:18]** tweet a lot about AI products and where

**[04:18]** tweet a lot about AI products and where they fail. And so last night when I was

**[04:20]** they fail. And so last night when I was

**[04:20]** they fail. And so last night when I was like rushing to get this presentation,

**[04:22]** like rushing to get this presentation,

**[04:22]** like rushing to get this presentation, my part of Hit done, uh I asked it to

**[04:25]** my part of Hit done, uh I asked it to

**[04:25]** my part of Hit done, uh I asked it to find tweets of mine about AI failures

**[04:26]** find tweets of mine about AI failures

**[04:26]** find tweets of mine about AI failures and it says, "I don't have access to

**[04:28]** and it says, "I don't have access to

**[04:28]** and it says, "I don't have access to your personal Twitter. I can't search

**[04:29]** your personal Twitter. I can't search

**[04:29]** your personal Twitter. I can't search tweets." I was like, "I think I can." So

**[04:31]** tweets." I was like, "I think I can." So

**[04:31]** tweets." I was like, "I think I can." So I I doubled down. I'm like, "You are

**[04:33]** I I doubled down. I'm like, "You are

**[04:33]** I I doubled down. I'm like, "You are literally Grock, you know, like this is

**[04:34]** literally Grock, you know, like this is

**[04:34]** literally Grock, you know, like this is what you're made for." And it's like,

**[04:35]** what you're made for." And it's like,

**[04:35]** what you're made for." And it's like, "Oh, you're right. I can I just don't

**[04:37]** "Oh, you're right. I can I just don't

**[04:37]** "Oh, you're right. I can I just don't have your username, you know?" So it's

**[04:40]** have your username, you know?" So it's

**[04:40]** have your username, you know?" So it's absurd. And I actually like like this is

**[04:41]** absurd. And I actually like like this is

**[04:41]** absurd. And I actually like like this is this is yesterday, right? this still a

**[04:43]** this is yesterday, right? this still a

**[04:43]** this is yesterday, right? this still a bug that they have.

**[04:46]** bug that they have.

**[04:46]** bug that they have. So, I feel really lucky to be, you know,

**[04:48]** So, I feel really lucky to be, you know,

**[04:48]** So, I feel really lucky to be, you know, like like I mentioned, I I I'm a CTO,

**[04:51]** like like I mentioned, I I I'm a CTO,

**[04:51]** like like I mentioned, I I I'm a CTO, co-founder of a company called Raindrop

**[04:53]** co-founder of a company called Raindrop

**[04:53]** co-founder of a company called Raindrop and we're in this really cool position

**[04:55]** and we're in this really cool position

**[04:55]** and we're in this really cool position where we get to work with some of the

**[04:56]** where we get to work with some of the

**[04:56]** where we get to work with some of the coolest, fastest growing companies in

**[04:58]** coolest, fastest growing companies in

**[04:58]** coolest, fastest growing companies in the world and just a huge range of


### [05:00 - 06:00]

**[05:00]** the world and just a huge range of

**[05:00]** the world and just a huge range of companies. So it's everything from you

**[05:02]** companies. So it's everything from you

**[05:02]** companies. So it's everything from you know apps like SIDS which he'll share

**[05:04]** know apps like SIDS which he'll share

**[05:04]** know apps like SIDS which he'll share about to things like clay.com you know

**[05:06]** about to things like clay.com you know

**[05:06]** about to things like clay.com you know which is like a sales sort of outreach

**[05:08]** which is like a sales sort of outreach

**[05:08]** which is like a sales sort of outreach tool to like alien companion apps to

**[05:12]** tool to like alien companion apps to

**[05:12]** tool to like alien companion apps to coding assistance. It's just this insane

**[05:13]** coding assistance. It's just this insane

**[05:13]** coding assistance. It's just this insane range of products and so I get I think

**[05:16]** range of products and so I get I think

**[05:16]** range of products and so I get I think we get to see so much of like what works

**[05:19]** we get to see so much of like what works

**[05:19]** we get to see so much of like what works what doesn't work.

**[05:21]** what doesn't work.

**[05:21]** what doesn't work. We are also like it's not just all

**[05:23]** We are also like it's not just all

**[05:23]** We are also like it's not just all secondhand like we also have a massive

**[05:26]** secondhand like we also have a massive

**[05:26]** secondhand like we also have a massive uh AI pipeline where you know every

**[05:28]** uh AI pipeline where you know every

**[05:28]** uh AI pipeline where you know every single event that we receive is being

**[05:30]** single event that we receive is being

**[05:30]** single event that we receive is being analyzed is being kind of divvied up in

**[05:32]** analyzed is being kind of divvied up in

**[05:32]** analyzed is being kind of divvied up in some way and we're kind of like you know

**[05:34]** some way and we're kind of like you know

**[05:34]** some way and we're kind of like you know we have this product we're also kind of

**[05:36]** we have this product we're also kind of

**[05:36]** we have this product we're also kind of this like stealth frontier lab of some

**[05:38]** this like stealth frontier lab of some

**[05:38]** this like stealth frontier lab of some sort of where we are kind of shipping

**[05:40]** sort of where we are kind of shipping

**[05:40]** sort of where we are kind of shipping some of the coolest AI features I've

**[05:41]** some of the coolest AI features I've

**[05:41]** some of the coolest AI features I've ever seen. Um we have like tools like

**[05:43]** ever seen. Um we have like tools like

**[05:43]** ever seen. Um we have like tools like deep search that allows people to go

**[05:45]** deep search that allows people to go

**[05:45]** deep search that allows people to go really deep into their production data

**[05:46]** really deep into their production data

**[05:46]** really deep into their production data and build just classifiers from just a

**[05:48]** and build just classifiers from just a

**[05:48]** and build just classifiers from just a few examples. So, it's been cool to sort

**[05:52]** few examples. So, it's been cool to sort

**[05:52]** few examples. So, it's been cool to sort of build this intuition both from

**[05:53]** of build this intuition both from

**[05:53]** of build this intuition both from firsthand from our customers and kind of

**[05:55]** firsthand from our customers and kind of

**[05:56]** firsthand from our customers and kind of merge that and I think we've we've have

**[05:58]** merge that and I think we've we've have

**[05:58]** merge that and I think we've we've have a pretty good intuition of what actually

**[05:59]** a pretty good intuition of what actually

**[05:59]** a pretty good intuition of what actually works right now.


### [06:00 - 07:00]

**[06:02]** works right now.

**[06:02]** works right now. One question I get a lot is

**[06:05]** One question I get a lot is

**[06:05]** One question I get a lot is will it get easier to make AI products,

**[06:07]** will it get easier to make AI products,

**[06:07]** will it get easier to make AI products, right? Like how much of this is just a

**[06:09]** right? Like how much of this is just a

**[06:09]** right? Like how much of this is just a moment in time? I think this is a very

**[06:11]** moment in time? I think this is a very

**[06:11]** moment in time? I think this is a very very interesting question and I think

**[06:12]** very interesting question and I think

**[06:12]** very interesting question and I think the answer is actually twofold, right?

**[06:15]** the answer is actually twofold, right?

**[06:15]** the answer is actually twofold, right? So, the first answer is yes. Like yes,

**[06:17]** So, the first answer is yes. Like yes,

**[06:17]** So, the first answer is yes. Like yes, it will get easier. Uh, and we know this

**[06:19]** it will get easier. Uh, and we know this

**[06:19]** it will get easier. Uh, and we know this because we've seen it. A year ago, you

**[06:21]** because we've seen it. A year ago, you

**[06:21]** because we've seen it. A year ago, you had to give, you know, threaten to kill

**[06:23]** had to give, you know, threaten to kill

**[06:23]** had to give, you know, threaten to kill your, you know, GPT4 in order to get it

**[06:26]** your, you know, GPT4 in order to get it

**[06:26]** your, you know, GPT4 in order to get it to output JSON, right? Like it was like

**[06:28]** to output JSON, right? Like it was like

**[06:28]** to output JSON, right? Like it was like you had to threaten to kill its

**[06:29]** you had to threaten to kill its

**[06:29]** you had to threaten to kill its firstborn or something. And now it's

**[06:30]** firstborn or something. And now it's

**[06:30]** firstborn or something. And now it's just like a parameter in the API. Like

**[06:32]** just like a parameter in the API. Like

**[06:32]** just like a parameter in the API. Like you're just like, in fact, here's the

**[06:34]** you're just like, in fact, here's the

**[06:34]** you're just like, in fact, here's the exact schema I want you to output. It

**[06:35]** exact schema I want you to output. It

**[06:35]** exact schema I want you to output. It just works. So those sort of things will

**[06:37]** just works. So those sort of things will

**[06:37]** just works. So those sort of things will get easier. But I think the second part

**[06:39]** get easier. But I think the second part

**[06:40]** get easier. But I think the second part of this answer is actually no. Like like

**[06:41]** of this answer is actually no. Like like

**[06:41]** of this answer is actually no. Like like in a lot of ways, it's not going to get

**[06:43]** in a lot of ways, it's not going to get

**[06:43]** in a lot of ways, it's not going to get easier. And I think that comes from the

**[06:45]** easier. And I think that comes from the

**[06:46]** easier. And I think that comes from the fact that communication is hard. like

**[06:47]** fact that communication is hard. like

**[06:47]** fact that communication is hard. like communication is a hard thing. Um, what

**[06:51]** communication is a hard thing. Um, what

**[06:51]** communication is a hard thing. Um, what do I mean by this? I actually um I'm a

**[06:54]** do I mean by this? I actually um I'm a

**[06:54]** do I mean by this? I actually um I'm a big Paul Graham fan. I'm sure a lot of a

**[06:56]** big Paul Graham fan. I'm sure a lot of a

**[06:56]** big Paul Graham fan. I'm sure a lot of a lot of us are, but I actually really

**[06:57]** lot of us are, but I actually really

**[06:57]** lot of us are, but I actually really really disagree with this. And the

**[06:59]** really disagree with this. And the

**[06:59]** really disagree with this. And the reason why is so so he says it seems to


### [07:00 - 08:00]

**[07:01]** reason why is so so he says it seems to

**[07:01]** reason why is so so he says it seems to me AGI would mean the end of prompt

**[07:03]** me AGI would mean the end of prompt

**[07:03]** me AGI would mean the end of prompt engineering. Moderately intelligent

**[07:04]** engineering. Moderately intelligent

**[07:04]** engineering. Moderately intelligent humans can figure out what you want

**[07:05]** humans can figure out what you want

**[07:05]** humans can figure out what you want without elaborate prompts. I don't think

**[07:07]** without elaborate prompts. I don't think

**[07:07]** without elaborate prompts. I don't think that's true. Like I I think that if you

**[07:10]** that's true. Like I I think that if you

**[07:10]** that's true. Like I I think that if you can think of all the times, you know,

**[07:11]** can think of all the times, you know,

**[07:11]** can think of all the times, you know, you've your partner has told you

**[07:12]** you've your partner has told you

**[07:12]** you've your partner has told you something and you've gotten it wrong,

**[07:14]** something and you've gotten it wrong,

**[07:14]** something and you've gotten it wrong, right? like you completely

**[07:16]** right? like you completely

**[07:16]** right? like you completely misinterpreted what they wanted, right?

**[07:17]** misinterpreted what they wanted, right?

**[07:17]** misinterpreted what they wanted, right? What their goal was. If you think about

**[07:19]** What their goal was. If you think about

**[07:19]** What their goal was. If you think about onboarding a new hire, right? And like

**[07:21]** onboarding a new hire, right? And like

**[07:21]** onboarding a new hire, right? And like like you told them to do something and

**[07:22]** like you told them to do something and

**[07:22]** like you told them to do something and they come back, what what the hell is

**[07:24]** they come back, what what the hell is

**[07:24]** they come back, what what the hell is this? Right? Um I think it's really

**[07:27]** this? Right? Um I think it's really

**[07:27]** this? Right? Um I think it's really really hard to communicate what you want

**[07:29]** really hard to communicate what you want

**[07:29]** really hard to communicate what you want to someone, especially someone that

**[07:30]** to someone, especially someone that

**[07:30]** to someone, especially someone that doesn't have a lot of context.

**[07:33]** doesn't have a lot of context.

**[07:33]** doesn't have a lot of context. So yes, I think this is wrong.

**[07:36]** So yes, I think this is wrong.

**[07:36]** So yes, I think this is wrong. The other reason why I'm not sure it's

**[07:38]** The other reason why I'm not sure it's

**[07:38]** The other reason why I'm not sure it's going to get that much easier in a lot

**[07:40]** going to get that much easier in a lot

**[07:40]** going to get that much easier in a lot of ways is that as these models, as our

**[07:43]** of ways is that as these models, as our

**[07:43]** of ways is that as these models, as our products become more capable, there's

**[07:45]** products become more capable, there's

**[07:45]** products become more capable, there's just more undefined behavior, right?

**[07:47]** just more undefined behavior, right?

**[07:47]** just more undefined behavior, right? There's more edge cases you didn't think

**[07:49]** There's more edge cases you didn't think

**[07:49]** There's more edge cases you didn't think about. And this is only becoming more

**[07:50]** about. And this is only becoming more

**[07:50]** about. And this is only becoming more true, you know, as our products have to

**[07:54]** true, you know, as our products have to

**[07:54]** true, you know, as our products have to start integrating with other tools

**[07:55]** start integrating with other tools

**[07:55]** start integrating with other tools through like MCP, for example. There's

**[07:57]** through like MCP, for example. There's

**[07:57]** through like MCP, for example. There's going to be new data formats, new ways

**[07:59]** going to be new data formats, new ways

**[07:59]** going to be new data formats, new ways of doing things. So I I think that as


### [08:00 - 09:00]

**[08:01]** of doing things. So I I think that as

**[08:01]** of doing things. So I I think that as our products become more capable, as the

**[08:03]** our products become more capable, as the

**[08:03]** our products become more capable, as the a as these models get more intelligent,

**[08:05]** a as these models get more intelligent,

**[08:05]** a as these models get more intelligent, we're it's a little bit uh we're kind of

**[08:07]** we're it's a little bit uh we're kind of

**[08:07]** we're it's a little bit uh we're kind of stuck in the same same situation.

**[08:10]** stuck in the same same situation.

**[08:10]** stuck in the same same situation. So this is this is how I like to think

**[08:12]** So this is this is how I like to think

**[08:12]** So this is this is how I like to think about it. I think you can't define the

**[08:13]** about it. I think you can't define the

**[08:14]** about it. I think you can't define the entire scope of your product's behavior

**[08:16]** entire scope of your product's behavior

**[08:16]** entire scope of your product's behavior up front anymore. You can't just say

**[08:18]** up front anymore. You can't just say

**[08:18]** up front anymore. You can't just say like, you know, here's the PRD, here's

**[08:19]** like, you know, here's the PRD, here's

**[08:19]** like, you know, here's the PRD, here's the document of everything I want my

**[08:21]** the document of everything I want my

**[08:21]** the document of everything I want my product to do. Like you actually have to

**[08:24]** product to do. Like you actually have to

**[08:24]** product to do. Like you actually have to iterate on it. You have to kind of ship

**[08:25]** iterate on it. You have to kind of ship

**[08:26]** iterate on it. You have to kind of ship it, see what it does, and then iterate

**[08:27]** it, see what it does, and then iterate

**[08:27]** it, see what it does, and then iterate on it.

**[08:30]** on it.

**[08:30]** on it. So

**[08:31]** So

**[08:31]** So I think eval are a very very important

**[08:34]** I think eval are a very very important

**[08:34]** I think eval are a very very important part of this actually but I also think

**[08:37]** part of this actually but I also think

**[08:37]** part of this actually but I also think there's a lot of confusion. You know I

**[08:39]** there's a lot of confusion. You know I

**[08:39]** there's a lot of confusion. You know I use the word lie is a little spicy but I

**[08:41]** use the word lie is a little spicy but I

**[08:41]** use the word lie is a little spicy but I think there's there's a lot of sort of

**[08:43]** think there's there's a lot of sort of

**[08:43]** think there's there's a lot of sort of misinformation around evals. So I'm not

**[08:45]** misinformation around evals. So I'm not

**[08:45]** misinformation around evals. So I'm not going to share I'm not going to like

**[08:46]** going to share I'm not going to like

**[08:46]** going to share I'm not going to like rehash what eval are. I'm not going to

**[08:48]** rehash what eval are. I'm not going to

**[08:48]** rehash what eval are. I'm not going to kind of go into all the details but I

**[08:50]** kind of go into all the details but I

**[08:50]** kind of go into all the details but I will talk about I think some like common

**[08:51]** will talk about I think some like common

**[08:52]** will talk about I think some like common misconceptions I've seen around evals.

**[08:54]** misconceptions I've seen around evals.

**[08:54]** misconceptions I've seen around evals. So, one is that this idea that eval are

**[08:58]** So, one is that this idea that eval are

**[08:58]** So, one is that this idea that eval are going to tell you how good your product

**[08:59]** going to tell you how good your product

**[08:59]** going to tell you how good your product is. They're not. Um, they're really not.


### [09:00 - 10:00]

**[09:01]** is. They're not. Um, they're really not.

**[09:01]** is. They're not. Um, they're really not. Uh, if you're not familiar with

**[09:02]** Uh, if you're not familiar with

**[09:02]** Uh, if you're not familiar with Goodart's law, it's like kind of the

**[09:03]** Goodart's law, it's like kind of the

**[09:03]** Goodart's law, it's like kind of the reason for this. Um,

**[09:06]** reason for this. Um,

**[09:06]** reason for this. Um, the eval that you collect are only the

**[09:08]** the eval that you collect are only the

**[09:08]** the eval that you collect are only the things you already know of. It's going

**[09:09]** things you already know of. It's going

**[09:09]** things you already know of. It's going to be easy to saturate them. If you look

**[09:11]** to be easy to saturate them. If you look

**[09:11]** to be easy to saturate them. If you look at recent model launches, a lot of them

**[09:13]** at recent model launches, a lot of them

**[09:13]** at recent model launches, a lot of them are actually performing lower on eval,

**[09:15]** are actually performing lower on eval,

**[09:15]** are actually performing lower on eval, you know, previous ones, but they're

**[09:16]** you know, previous ones, but they're

**[09:16]** you know, previous ones, but they're just way better in real world use. So,

**[09:18]** just way better in real world use. So,

**[09:18]** just way better in real world use. So, it's not going to do this.

**[09:21]** it's not going to do this.

**[09:21]** it's not going to do this. The other lie is this idea that like oh

**[09:24]** The other lie is this idea that like oh

**[09:24]** The other lie is this idea that like oh okay well if you have a sort of like

**[09:26]** okay well if you have a sort of like

**[09:26]** okay well if you have a sort of like imagine you have something like how

**[09:27]** imagine you have something like how

**[09:27]** imagine you have something like how funny is my joke you know that my app is

**[09:29]** funny is my joke you know that my app is

**[09:29]** funny is my joke you know that my app is generating. This is the example I always

**[09:30]** generating. This is the example I always

**[09:30]** generating. This is the example I always hear used. You'll just like ask an LM to

**[09:32]** hear used. You'll just like ask an LM to

**[09:32]** hear used. You'll just like ask an LM to judge how funny your joke is. Um I this

**[09:36]** judge how funny your joke is. Um I this

**[09:36]** judge how funny your joke is. Um I this doesn't work like largely does not work.

**[09:39]** doesn't work like largely does not work.

**[09:39]** doesn't work like largely does not work. Uh uh they're tempting because you know

**[09:43]** Uh uh they're tempting because you know

**[09:43]** Uh uh they're tempting because you know these LM judges take text as an input

**[09:45]** these LM judges take text as an input

**[09:45]** these LM judges take text as an input and they output a score they output a

**[09:46]** and they output a score they output a

**[09:46]** and they output a score they output a decision whatever it is. um like largely

**[09:50]** decision whatever it is. um like largely

**[09:50]** decision whatever it is. um like largely the best companies are not doing this.

**[09:52]** the best companies are not doing this.

**[09:52]** the best companies are not doing this. They're they're not they're they're the

**[09:54]** They're they're not they're they're the

**[09:54]** They're they're not they're they're the best companies are using highly curated

**[09:55]** best companies are using highly curated

**[09:55]** best companies are using highly curated data sets. They're using autogradable

**[09:57]** data sets. They're using autogradable

**[09:57]** data sets. They're using autogradable evals. Autogradable here meaning like

**[09:59]** evals. Autogradable here meaning like

**[09:59]** evals. Autogradable here meaning like you know there's some way of in some


### [10:00 - 11:00]

**[10:01]** you know there's some way of in some

**[10:01]** you know there's some way of in some deterministic way figuring out if the

**[10:03]** deterministic way figuring out if the

**[10:03]** deterministic way figuring out if the model passed or not. Um they're not

**[10:05]** model passed or not. Um they're not

**[10:05]** model passed or not. Um they're not really using LM as judges. Um there's

**[10:07]** really using LM as judges. Um there's

**[10:08]** really using LM as judges. Um there's some edge cases here but just like

**[10:09]** some edge cases here but just like

**[10:09]** some edge cases here but just like largely this is not the thing you should

**[10:10]** largely this is not the thing you should

**[10:10]** largely this is not the thing you should reach for.

**[10:12]** reach for.

**[10:12]** reach for. The last one I see, which also really

**[10:14]** The last one I see, which also really

**[10:14]** The last one I see, which also really confuses me, which I don't think is

**[10:15]** confuses me, which I don't think is

**[10:15]** confuses me, which I don't think is real, is like eval production data. Um,

**[10:18]** real, is like eval production data. Um,

**[10:18]** real, is like eval production data. Um, there's this idea that you should just

**[10:19]** there's this idea that you should just

**[10:19]** there's this idea that you should just move your offline evals online. You use

**[10:21]** move your offline evals online. You use

**[10:22]** move your offline evals online. You use the same judges, the same scoring. Um,

**[10:25]** the same judges, the same scoring. Um,

**[10:25]** the same judges, the same scoring. Um, largely doesn't work either. I think

**[10:27]** largely doesn't work either. I think

**[10:27]** largely doesn't work either. I think that a it could be very expensive,

**[10:29]** that a it could be very expensive,

**[10:29]** that a it could be very expensive, especially if you're, you know, you have

**[10:30]** especially if you're, you know, you have

**[10:30]** especially if you're, you know, you have some sort of judge that requires the

**[10:32]** some sort of judge that requires the

**[10:32]** some sort of judge that requires the model to be a lot smarter. Um, so it's

**[10:34]** model to be a lot smarter. Um, so it's

**[10:34]** model to be a lot smarter. Um, so it's either it's really expensive or you're

**[10:36]** either it's really expensive or you're

**[10:36]** either it's really expensive or you're only doing a small percentage of

**[10:37]** only doing a small percentage of

**[10:37]** only doing a small percentage of production traffic. Um, it's really hard

**[10:39]** production traffic. Um, it's really hard

**[10:39]** production traffic. Um, it's really hard to set up accurately. you're not really

**[10:41]** to set up accurately. you're not really

**[10:41]** to set up accurately. you're not really getting the patterns that are emerging.

**[10:44]** getting the patterns that are emerging.

**[10:44]** getting the patterns that are emerging. Um, it's often limited to what you

**[10:45]** Um, it's often limited to what you

**[10:46]** Um, it's often limited to what you already know. Even OpenAI talks about

**[10:48]** already know. Even OpenAI talks about

**[10:48]** already know. Even OpenAI talks about this or they have like this kind of

**[10:50]** this or they have like this kind of

**[10:50]** this or they have like this kind of really weird behavioral issue with

**[10:51]** really weird behavioral issue with

**[10:51]** really weird behavioral issue with chatbt recently and they talk about this

**[10:54]** chatbt recently and they talk about this

**[10:54]** chatbt recently and they talk about this in their postmortem. They're like, you

**[10:56]** in their postmortem. They're like, you

**[10:56]** in their postmortem. They're like, you know, our evals aren't going to catch

**[10:57]** know, our evals aren't going to catch

**[10:57]** know, our evals aren't going to catch everything, right? The eval are catching

**[10:58]** everything, right? The eval are catching

**[10:58]** everything, right? The eval are catching things we already knew and real world


### [11:00 - 12:00]

**[11:01]** things we already knew and real world

**[11:01]** things we already knew and real world use is what helps us spot problems.

**[11:04]** use is what helps us spot problems.

**[11:04]** use is what helps us spot problems. And so to build reliable AI apps, you

**[11:06]** And so to build reliable AI apps, you

**[11:06]** And so to build reliable AI apps, you really need signals.

**[11:09]** really need signals.

**[11:09]** really need signals. If you think about issues in an app like

**[11:10]** If you think about issues in an app like

**[11:10]** If you think about issues in an app like Sentry,

**[11:13]** Sentry,

**[11:13]** Sentry, you have what the issue is, but then you

**[11:15]** you have what the issue is, but then you

**[11:15]** you have what the issue is, but then you have how many times it happened and how

**[11:16]** have how many times it happened and how

**[11:16]** have how many times it happened and how many users it affected.

**[11:19]** many users it affected.

**[11:19]** many users it affected. But for AI apps, there is no concrete

**[11:22]** But for AI apps, there is no concrete

**[11:22]** But for AI apps, there is no concrete error, right? There's no exception being

**[11:23]** error, right? There's no exception being

**[11:23]** error, right? There's no exception being thrown. And that's why like I think

**[11:26]** thrown. And that's why like I think

**[11:26]** thrown. And that's why like I think signals are really the thing you need to

**[11:27]** signals are really the thing you need to

**[11:27]** signals are really the thing you need to be looking at.

**[11:30]** be looking at.

**[11:30]** be looking at. And signals I define as like and at

**[11:32]** And signals I define as like and at

**[11:32]** And signals I define as like and at Rindrop we call them like ground truthy

**[11:34]** Rindrop we call them like ground truthy

**[11:34]** Rindrop we call them like ground truthy indicators of your app's performance.

**[11:37]** indicators of your app's performance.

**[11:37]** indicators of your app's performance. And so the anatomy of an AI issue looks

**[11:39]** And so the anatomy of an AI issue looks

**[11:39]** And so the anatomy of an AI issue looks like some combination of signals

**[11:41]** like some combination of signals

**[11:41]** like some combination of signals implicit and explicit and then intents

**[11:43]** implicit and explicit and then intents

**[11:43]** implicit and explicit and then intents which what which are what the users are

**[11:45]** which what which are what the users are

**[11:45]** which what which are what the users are trying to do.

**[11:48]** trying to do.

**[11:48]** trying to do. And there's this process of essentially

**[11:49]** And there's this process of essentially

**[11:50]** And there's this process of essentially defining these signals, exploring these

**[11:52]** defining these signals, exploring these

**[11:52]** defining these signals, exploring these signals and refining them.

**[11:54]** signals and refining them.

**[11:54]** signals and refining them. So briefly let's talk about defining

**[11:57]** So briefly let's talk about defining

**[11:57]** So briefly let's talk about defining signals. There's explicit signals which


### [12:00 - 13:00]

**[12:00]** signals. There's explicit signals which

**[12:00]** signals. There's explicit signals which is almost like an analytics event your

**[12:01]** is almost like an analytics event your

**[12:01]** is almost like an analytics event your app can send. And then there's implicit

**[12:03]** app can send. And then there's implicit

**[12:03]** app can send. And then there's implicit data that's sort of hiding in your data.

**[12:05]** data that's sort of hiding in your data.

**[12:05]** data that's sort of hiding in your data. uh sorry, implicit signals.

**[12:08]** uh sorry, implicit signals.

**[12:08]** uh sorry, implicit signals. So a common explicit signal is thumbs

**[12:09]** So a common explicit signal is thumbs

**[12:10]** So a common explicit signal is thumbs up, thumbs down, but there really are

**[12:12]** up, thumbs down, but there really are

**[12:12]** up, thumbs down, but there really are way more signals than that. So chatbt

**[12:14]** way more signals than that. So chatbt

**[12:14]** way more signals than that. So chatbt themselves actually track what portion

**[12:16]** themselves actually track what portion

**[12:16]** themselves actually track what portion of a message you copy out of chatbt.

**[12:19]** of a message you copy out of chatbt.

**[12:19]** of a message you copy out of chatbt. That's something that they track. That's

**[12:20]** That's something that they track. That's

**[12:20]** That's something that they track. That's a signal that they're tracking.

**[12:23]** a signal that they're tracking.

**[12:23]** a signal that they're tracking. They do preference data, right? You may

**[12:24]** They do preference data, right? You may

**[12:24]** They do preference data, right? You may have seen this sort of AB, which

**[12:26]** have seen this sort of AB, which

**[12:26]** have seen this sort of AB, which response do you prefer.

**[12:28]** response do you prefer.

**[12:28]** response do you prefer. There's a whole host of possible both

**[12:30]** There's a whole host of possible both

**[12:30]** There's a whole host of possible both positive and negative signals.

**[12:31]** positive and negative signals.

**[12:31]** positive and negative signals. Everything from errors to regenerating

**[12:34]** Everything from errors to regenerating

**[12:34]** Everything from errors to regenerating to like syntax errors if you're a coding

**[12:35]** to like syntax errors if you're a coding

**[12:36]** to like syntax errors if you're a coding assistant to copy, sharing, suggesting.

**[12:42]** We actually use this. So we have a flow

**[12:42]** We actually use this. So we have a flow where users can search for data and we

**[12:43]** where users can search for data and we

**[12:44]** where users can search for data and we actually look at how many were marked

**[12:45]** actually look at how many were marked

**[12:45]** actually look at how many were marked correct, how many were marked wrong and

**[12:47]** correct, how many were marked wrong and

**[12:47]** correct, how many were marked wrong and we can use that to figure out an RL on

**[12:49]** we can use that to figure out an RL on

**[12:50]** we can use that to figure out an RL on like and improve the quality of our

**[12:51]** like and improve the quality of our

**[12:51]** like and improve the quality of our searches. It's a super interesting

**[12:53]** searches. It's a super interesting

**[12:53]** searches. It's a super interesting signal. But there's also implicit

**[12:55]** signal. But there's also implicit

**[12:55]** signal. But there's also implicit signals which are like essentially

**[12:58]** signals which are like essentially

**[12:58]** signals which are like essentially detecting rather than judging. So we


### [13:00 - 14:00]

**[13:00]** detecting rather than judging. So we

**[13:00]** detecting rather than judging. So we detect things like refusals, task

**[13:02]** detect things like refusals, task

**[13:02]** detect things like refusals, task failure, user frustration. And if you

**[13:04]** failure, user frustration. And if you

**[13:04]** failure, user frustration. And if you think about like the Grock example, when

**[13:06]** think about like the Grock example, when

**[13:06]** think about like the Grock example, when you cluster them, it gets very

**[13:07]** you cluster them, it gets very

**[13:07]** you cluster them, it gets very interesting. So we can look at and say,

**[13:09]** interesting. So we can look at and say,

**[13:09]** interesting. So we can look at and say, okay, there's this cluster of user

**[13:11]** okay, there's this cluster of user

**[13:11]** okay, there's this cluster of user frustration and it's all around people

**[13:13]** frustration and it's all around people

**[13:13]** frustration and it's all around people trying to search for tweets.

**[13:15]** trying to search for tweets.

**[13:15]** trying to search for tweets. And that's where exploring comes in. So

**[13:17]** And that's where exploring comes in. So

**[13:17]** And that's where exploring comes in. So just like you can explore tags in

**[13:18]** just like you can explore tags in

**[13:18]** just like you can explore tags in Sentry, you need some way of exploring

**[13:21]** Sentry, you need some way of exploring

**[13:21]** Sentry, you need some way of exploring tags and metadata

**[13:24]** tags and metadata

**[13:24]** tags and metadata for us that's like properties, models,

**[13:26]** for us that's like properties, models,

**[13:26]** for us that's like properties, models, etc. keywords and intents because like I

**[13:30]** etc. keywords and intents because like I

**[13:30]** etc. keywords and intents because like I just said the intent really changes what

**[13:31]** just said the intent really changes what

**[13:31]** just said the intent really changes what the actual issue is. So again that's why

**[13:33]** the actual issue is. So again that's why

**[13:33]** the actual issue is. So again that's why we talk about the anatomy of an AI issue

**[13:35]** we talk about the anatomy of an AI issue

**[13:35]** we talk about the anatomy of an AI issue being a the signal with the intent.

**[13:39]** being a the signal with the intent.

**[13:39]** being a the signal with the intent. Just parting thoughts here. You really

**[13:41]** Just parting thoughts here. You really

**[13:41]** Just parting thoughts here. You really need a constant IV of your app's data.

**[13:43]** need a constant IV of your app's data.

**[13:43]** need a constant IV of your app's data. We send Slack notifications. You can do

**[13:45]** We send Slack notifications. You can do

**[13:45]** We send Slack notifications. You can do whatever you want but you need to be

**[13:46]** whatever you want but you need to be

**[13:46]** whatever you want but you need to be looking at your data whether that's

**[13:47]** looking at your data whether that's

**[13:47]** looking at your data whether that's searching it etc.

**[13:50]** searching it etc.

**[13:50]** searching it etc. And then you really need to just refine

**[13:51]** And then you really need to just refine

**[13:51]** And then you really need to just refine and define new issues which means you

**[13:53]** and define new issues which means you

**[13:53]** and define new issues which means you look find these patterns. Look at your

**[13:55]** look find these patterns. Look at your

**[13:55]** look find these patterns. Look at your data. talk to your users, find new

**[13:57]** data. talk to your users, find new

**[13:57]** data. talk to your users, find new definitions of issues you weren't

**[13:58]** definitions of issues you weren't

**[13:58]** definitions of issues you weren't expecting, and then start tracking them.


### [14:00 - 15:00]

**[14:01]** expecting, and then start tracking them.

**[14:01]** expecting, and then start tracking them. So, I'm going to cut this part. If you

**[14:03]** So, I'm going to cut this part. If you

**[14:03]** So, I'm going to cut this part. If you want to know how to fix these things,

**[14:05]** want to know how to fix these things,

**[14:05]** want to know how to fix these things, I'm happy to talk about some of the

**[14:06]** I'm happy to talk about some of the

**[14:06]** I'm happy to talk about some of the advancements in SFT and things I've seen

**[14:07]** advancements in SFT and things I've seen

**[14:07]** advancements in SFT and things I've seen work, but let's uh move over to Sid.

**[14:10]** work, but let's uh move over to Sid.

**[14:10]** work, but let's uh move over to Sid. Cool. Thanks, Ben. Hey, everybody. I'm

**[14:12]** Cool. Thanks, Ben. Hey, everybody. I'm

**[14:12]** Cool. Thanks, Ben. Hey, everybody. I'm Sid. I'm the co-founder of Aliv, and

**[14:14]** Sid. I'm the co-founder of Aliv, and

**[14:14]** Sid. I'm the co-founder of Aliv, and we're building a portfolio of consumer

**[14:16]** we're building a portfolio of consumer

**[14:16]** we're building a portfolio of consumer products that have with the aim of

**[14:19]** products that have with the aim of

**[14:19]** products that have with the aim of building products that are fulfilling

**[14:21]** building products that are fulfilling

**[14:21]** building products that are fulfilling and productive for people's lives. We're

**[14:22]** and productive for people's lives. We're

**[14:22]** and productive for people's lives. We're a tiny team based out of New York that

**[14:24]** a tiny team based out of New York that

**[14:24]** a tiny team based out of New York that successfully scaled viral products

**[14:26]** successfully scaled viral products

**[14:26]** successfully scaled viral products around $6 million an hour profitably and

**[14:28]** around $6 million an hour profitably and

**[14:28]** around $6 million an hour profitably and generated about half a billion views on

**[14:29]** generated about half a billion views on

**[14:29]** generated about half a billion views on socials.

**[14:31]** socials.

**[14:32]** socials. Today I'm going to talk about the

**[14:33]** Today I'm going to talk about the

**[14:33]** Today I'm going to talk about the framework that drives the success which

**[14:34]** framework that drives the success which

**[14:34]** framework that drives the success which is powered by raindrop.

**[14:37]** is powered by raindrop.

**[14:37]** is powered by raindrop. There are two features of a viral AI

**[14:39]** There are two features of a viral AI

**[14:39]** There are two features of a viral AI product for it to be successful. The

**[14:42]** product for it to be successful. The

**[14:42]** product for it to be successful. The first part is a wow factor for virality

**[14:44]** first part is a wow factor for virality

**[14:44]** first part is a wow factor for virality and the second part is reliable

**[14:45]** and the second part is reliable

**[14:46]** and the second part is reliable consistent user experiences. The problem

**[14:48]** consistent user experiences. The problem

**[14:48]** consistent user experiences. The problem is AI is chaotic and nondeterministic.

**[14:50]** is AI is chaotic and nondeterministic.

**[14:50]** is AI is chaotic and nondeterministic. And this begs for a structure and

**[14:52]** And this begs for a structure and

**[14:52]** And this begs for a structure and approach that allows us to create some

**[14:54]** approach that allows us to create some

**[14:54]** approach that allows us to create some sort of scaling system that still caters

**[14:57]** sort of scaling system that still caters

**[14:57]** sort of scaling system that still caters to the AI magic that is

**[14:58]** to the AI magic that is

**[14:58]** to the AI magic that is nondeterministic.


### [15:00 - 16:00]

**[15:03]** The idea is that we want to have a

**[15:03]** The idea is that we want to have a systematic approach for continuously

**[15:04]** systematic approach for continuously

**[15:04]** systematic approach for continuously improving our AI experiences so that we

**[15:07]** improving our AI experiences so that we

**[15:07]** improving our AI experiences so that we can scale to millions of users worldwide

**[15:08]** can scale to millions of users worldwide

**[15:08]** can scale to millions of users worldwide and keep experiences reliable without

**[15:11]** and keep experiences reliable without

**[15:11]** and keep experiences reliable without taking away the magic of AI that people

**[15:13]** taking away the magic of AI that people

**[15:13]** taking away the magic of AI that people fall in love with. We need some way to

**[15:15]** fall in love with. We need some way to

**[15:15]** fall in love with. We need some way to guide the chaos instead of eliminating

**[15:16]** guide the chaos instead of eliminating

**[15:16]** guide the chaos instead of eliminating it.

**[15:17]** it.

**[15:17]** it. This is why we came up with Trellis.

**[15:19]** This is why we came up with Trellis.

**[15:19]** This is why we came up with Trellis. Trellis is our framework for

**[15:21]** Trellis is our framework for

**[15:21]** Trellis is our framework for continuously refining our AI experiences

**[15:23]** continuously refining our AI experiences

**[15:23]** continuously refining our AI experiences so that we can systematically improve

**[15:24]** so that we can systematically improve

**[15:24]** so that we can systematically improve the user experiences across our AI

**[15:26]** the user experiences across our AI

**[15:26]** the user experiences across our AI products at scale designed specifically

**[15:28]** products at scale designed specifically

**[15:28]** products at scale designed specifically around our virality engine. There are

**[15:30]** around our virality engine. There are

**[15:30]** around our virality engine. There are three core axioms to trus. One is

**[15:32]** three core axioms to trus. One is

**[15:32]** three core axioms to trus. One is discretization where we take the

**[15:34]** discretization where we take the

**[15:34]** discretization where we take the infinite output space and break it down

**[15:36]** infinite output space and break it down

**[15:36]** infinite output space and break it down into specific buckets of focus. Then we

**[15:39]** into specific buckets of focus. Then we

**[15:39]** into specific buckets of focus. Then we prioritize. This involves ranking those

**[15:41]** prioritize. This involves ranking those

**[15:41]** prioritize. This involves ranking those bucket spaces by what will drive the

**[15:43]** bucket spaces by what will drive the

**[15:43]** bucket spaces by what will drive the most impact for your business. And

**[15:45]** most impact for your business. And

**[15:45]** most impact for your business. And finally, recursive refinement. We repeat

**[15:47]** finally, recursive refinement. We repeat

**[15:47]** finally, recursive refinement. We repeat this process within those buckets of

**[15:49]** this process within those buckets of

**[15:49]** this process within those buckets of output spaces so that we can continue to

**[15:50]** output spaces so that we can continue to

**[15:50]** output spaces so that we can continue to create structure and order within the

**[15:52]** create structure and order within the

**[15:52]** create structure and order within the chaotic uh output plane. There

**[15:56]** chaotic uh output plane. There

**[15:56]** chaotic uh output plane. There effectively six steps to trus. A lot of

**[15:58]** effectively six steps to trus. A lot of

**[15:58]** effectively six steps to trus. A lot of this has been shared by Ben in terms of


### [16:00 - 17:00]

**[16:00]** this has been shared by Ben in terms of

**[16:00]** this has been shared by Ben in terms of the the grounding principles of it. The

**[16:02]** the the grounding principles of it. The

**[16:02]** the the grounding principles of it. The first is you want to initialize an

**[16:04]** first is you want to initialize an

**[16:04]** first is you want to initialize an output space by launching an MVP agent

**[16:06]** output space by launching an MVP agent

**[16:06]** output space by launching an MVP agent that is informed by some product priors

**[16:08]** that is informed by some product priors

**[16:08]** that is informed by some product priors and some product expectations. But the

**[16:10]** and some product expectations. But the

**[16:10]** and some product expectations. But the goal is really to collect a lot of user

**[16:11]** goal is really to collect a lot of user

**[16:11]** goal is really to collect a lot of user data. The second step is once you've

**[16:14]** data. The second step is once you've

**[16:14]** data. The second step is once you've unders on once you have all this user

**[16:15]** unders on once you have all this user

**[16:15]** unders on once you have all this user data, you want to correctly classify

**[16:17]** data, you want to correctly classify

**[16:17]** data, you want to correctly classify these into intents based on usage

**[16:18]** these into intents based on usage

**[16:18]** these into intents based on usage patterns. The goal is you want to

**[16:20]** patterns. The goal is you want to

**[16:20]** patterns. The goal is you want to understand exactly why people are

**[16:22]** understand exactly why people are

**[16:22]** understand exactly why people are sticking to your product and what

**[16:23]** sticking to your product and what

**[16:23]** sticking to your product and what they're using in your product,

**[16:24]** they're using in your product,

**[16:24]** they're using in your product, especially when it's a conversational

**[16:26]** especially when it's a conversational

**[16:26]** especially when it's a conversational open-ended AI agent experience. The

**[16:28]** open-ended AI agent experience. The

**[16:28]** open-ended AI agent experience. The third step is converting these intents

**[16:30]** third step is converting these intents

**[16:30]** third step is converting these intents into dedicated semi- semi-deterministic

**[16:33]** into dedicated semi- semi-deterministic

**[16:33]** into dedicated semi- semi-deterministic workflows. A workflow is a predefined

**[16:35]** workflows. A workflow is a predefined

**[16:35]** workflows. A workflow is a predefined set of steps that allows you to achieve

**[16:37]** set of steps that allows you to achieve

**[16:37]** set of steps that allows you to achieve a certain output. The goal is you want

**[16:39]** a certain output. The goal is you want

**[16:39]** a certain output. The goal is you want these workflows to be broad enough to be

**[16:41]** these workflows to be broad enough to be

**[16:41]** these workflows to be broad enough to be useful for many possibilities but narrow

**[16:43]** useful for many possibilities but narrow

**[16:43]** useful for many possibilities but narrow enough to be reliable. After you have

**[16:45]** enough to be reliable. After you have

**[16:45]** enough to be reliable. After you have your workflows, you want to prioritize

**[16:46]** your workflows, you want to prioritize

**[16:46]** your workflows, you want to prioritize them by some scoring mechanism. This has

**[16:48]** them by some scoring mechanism. This has

**[16:48]** them by some scoring mechanism. This has to be something that's tied to your

**[16:50]** to be something that's tied to your

**[16:50]** to be something that's tied to your company's KPIs. Um, and finally, you

**[16:52]** company's KPIs. Um, and finally, you

**[16:52]** company's KPIs. Um, and finally, you want to analyze these workflows from

**[16:54]** want to analyze these workflows from

**[16:54]** want to analyze these workflows from within. You want to understand the

**[16:55]** within. You want to understand the

**[16:55]** within. You want to understand the failure patterns within them. You want

**[16:56]** failure patterns within them. You want

**[16:56]** failure patterns within them. You want to understand the sub intents and you

**[16:58]** to understand the sub intents and you

**[16:58]** to understand the sub intents and you want to keep recursing from there, which

**[16:59]** want to keep recursing from there, which

**[16:59]** want to keep recursing from there, which is what step six involves.


### [17:00 - 18:00]

**[17:02]** is what step six involves.

**[17:02]** is what step six involves. A quick note on prioritization. There's

**[17:04]** A quick note on prioritization. There's

**[17:04]** A quick note on prioritization. There's a simple and naive way to do it, which

**[17:05]** a simple and naive way to do it, which

**[17:05]** a simple and naive way to do it, which is volume only. This involves focusing

**[17:07]** is volume only. This involves focusing

**[17:07]** is volume only. This involves focusing on the workflows that have the most

**[17:09]** on the workflows that have the most

**[17:09]** on the workflows that have the most volume. However, this leaves a lot of

**[17:11]** volume. However, this leaves a lot of

**[17:11]** volume. However, this leaves a lot of room on the table for improving general

**[17:13]** room on the table for improving general

**[17:13]** room on the table for improving general satisfaction across your product. A more

**[17:15]** satisfaction across your product. A more

**[17:15]** satisfaction across your product. A more recommended approach is volume times

**[17:17]** recommended approach is volume times

**[17:17]** recommended approach is volume times negative sentiment score. In this, we

**[17:19]** negative sentiment score. In this, we

**[17:20]** negative sentiment score. In this, we try to score the ex the expected lift

**[17:22]** try to score the ex the expected lift

**[17:22]** try to score the ex the expected lift we'd like to get by focusing on a

**[17:24]** we'd like to get by focusing on a

**[17:24]** we'd like to get by focusing on a workflow that might be generating a lot

**[17:25]** workflow that might be generating a lot

**[17:26]** workflow that might be generating a lot of negative satisfaction on your

**[17:27]** of negative satisfaction on your

**[17:27]** of negative satisfaction on your product. An even more informed score is

**[17:29]** product. An even more informed score is

**[17:29]** product. An even more informed score is negative sentiment times volume times

**[17:31]** negative sentiment times volume times

**[17:31]** negative sentiment times volume times estimated achievable delta times some

**[17:33]** estimated achievable delta times some

**[17:33]** estimated achievable delta times some strategic relevance. The idea of

**[17:34]** strategic relevance. The idea of

**[17:34]** strategic relevance. The idea of estimated achievable delta is comes down

**[17:37]** estimated achievable delta is comes down

**[17:37]** estimated achievable delta is comes down to you coming up with a way to score the

**[17:39]** to you coming up with a way to score the

**[17:39]** to you coming up with a way to score the actual achievable delta you can gain

**[17:41]** actual achievable delta you can gain

**[17:41]** actual achievable delta you can gain from working on that workflow and

**[17:43]** from working on that workflow and

**[17:43]** from working on that workflow and improving the product. If you're going

**[17:44]** improving the product. If you're going

**[17:44]** improving the product. If you're going to need to train a foundational model to

**[17:45]** to need to train a foundational model to

**[17:45]** to need to train a foundational model to improve something, its achievable delta

**[17:47]** improve something, its achievable delta

**[17:47]** improve something, its achievable delta is probably near zero depending on the

**[17:49]** is probably near zero depending on the

**[17:49]** is probably near zero depending on the kind of company you are. All in all, the

**[17:52]** kind of company you are. All in all, the

**[17:52]** kind of company you are. All in all, the goal is once you have these intents

**[17:53]** goal is once you have these intents

**[17:53]** goal is once you have these intents identified, you can build structured

**[17:54]** identified, you can build structured

**[17:54]** identified, you can build structured workflows where each workflow is

**[17:56]** workflows where each workflow is

**[17:56]** workflows where each workflow is self-attributable, deterministic,

**[17:59]** self-attributable, deterministic,

**[17:59]** self-attributable, deterministic, and is self-bound, which means which


### [18:00 - 19:00]

**[18:02]** and is self-bound, which means which

**[18:02]** and is self-bound, which means which which allows your teams to move much

**[18:03]** which allows your teams to move much

**[18:03]** which allows your teams to move much more quickly because when you when you

**[18:06]** more quickly because when you when you

**[18:06]** more quickly because when you when you uh improve a specific workflow,

**[18:09]** uh improve a specific workflow,

**[18:09]** uh improve a specific workflow, all those changes are contained and self

**[18:11]** all those changes are contained and self

**[18:11]** all those changes are contained and self accountable to that one workflow instead

**[18:12]** accountable to that one workflow instead

**[18:12]** accountable to that one workflow instead of spilling over into other workflows.

**[18:14]** of spilling over into other workflows.

**[18:14]** of spilling over into other workflows. This allows your team to move more

**[18:15]** This allows your team to move more

**[18:15]** This allows your team to move more reliably.

**[18:17]** reliably.

**[18:17]** reliably. And uh while we have a few more seconds,

**[18:19]** And uh while we have a few more seconds,

**[18:19]** And uh while we have a few more seconds, you can continue to further refine this

**[18:20]** you can continue to further refine this

**[18:20]** you can continue to further refine this process going deeper and deeper into all

**[18:22]** process going deeper and deeper into all

**[18:22]** process going deeper and deeper into all your workflows. And at the end of the

**[18:24]** your workflows. And at the end of the

**[18:24]** your workflows. And at the end of the day, you create magic which is

**[18:25]** day, you create magic which is

**[18:25]** day, you create magic which is engineered, repeatable, testable, and

**[18:27]** engineered, repeatable, testable, and

**[18:27]** engineered, repeatable, testable, and attributable, but not accidental. If

**[18:29]** attributable, but not accidental. If

**[18:29]** attributable, but not accidental. If you'd like to read more about this, feel

**[18:30]** you'd like to read more about this, feel

**[18:30]** you'd like to read more about this, feel free to scan this QR code to read about

**[18:32]** free to scan this QR code to read about

**[18:32]** free to scan this QR code to read about our blog post on the Trellis framework.

**[18:35]** our blog post on the Trellis framework.

**[18:35]** our blog post on the Trellis framework. Thank you for having me.


