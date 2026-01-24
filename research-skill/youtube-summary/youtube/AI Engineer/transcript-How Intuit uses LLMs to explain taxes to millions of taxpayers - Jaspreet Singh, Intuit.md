# How Intuit uses LLMs to explain taxes to millions of taxpayers - Jaspreet Singh, Intuit

**Video URL:** https://www.youtube.com/watch?v=_zl_zimMRak

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** Hi, I'm Jaspit. I'm a senior staff

**[00:17]** Hi, I'm Jaspit. I'm a senior staff engineer in it. I work on Genifi for

**[00:19]** engineer in it. I work on Genifi for

**[00:19]** engineer in it. I work on Genifi for Turboax. And today we'll be talking

**[00:22]** Turboax. And today we'll be talking

**[00:22]** Turboax. And today we'll be talking about how we use LLMs at Inuit to well

**[00:25]** about how we use LLMs at Inuit to well

**[00:25]** about how we use LLMs at Inuit to well help you understand your taxes better.

**[00:28]** help you understand your taxes better.

**[00:28]** help you understand your taxes better. So I think uh

**[00:31]** So I think uh

**[00:31]** So I think uh to just to understand the scale right uh

**[00:33]** to just to understand the scale right uh

**[00:33]** to just to understand the scale right uh into Turboax successfully processed 44

**[00:36]** into Turboax successfully processed 44

**[00:36]** into Turboax successfully processed 44 million tax returns for tax year 23

**[00:40]** million tax returns for tax year 23

**[00:40]** million tax returns for tax year 23 and that's really the scale we're going

**[00:42]** and that's really the scale we're going

**[00:42]** and that's really the scale we're going for. We want everybody to be have high

**[00:44]** for. We want everybody to be have high

**[00:44]** for. We want everybody to be have high confidence in how their taxes are filed

**[00:47]** confidence in how their taxes are filed

**[00:47]** confidence in how their taxes are filed and understand them that they are

**[00:48]** and understand them that they are

**[00:48]** and understand them that they are getting the best deductions uh that they

**[00:51]** getting the best deductions uh that they

**[00:51]** getting the best deductions uh that they can.

**[00:52]** can.

**[00:52]** can. So,


### [01:00 - 02:00]

**[01:01]** so this is the experience that we work

**[01:01]** so this is the experience that we work on. So uh you go into Turboax, you uh

**[01:05]** on. So uh you go into Turboax, you uh

**[01:05]** on. So uh you go into Turboax, you uh enter your information, then you go

**[01:06]** enter your information, then you go

**[01:06]** enter your information, then you go through what credits you are eligible

**[01:08]** through what credits you are eligible

**[01:08]** through what credits you are eligible for and so on. And we basically help you

**[01:11]** for and so on. And we basically help you

**[01:11]** for and so on. And we basically help you exp uh expand onto how you are getting

**[01:14]** exp uh expand onto how you are getting

**[01:14]** exp uh expand onto how you are getting the tax breaks that you are, help you

**[01:16]** the tax breaks that you are, help you

**[01:16]** the tax breaks that you are, help you understand them better uh and so on. And

**[01:27]** and this is another example. This is

**[01:27]** and this is another example. This is basically the overall tax outcome like

**[01:29]** basically the overall tax outcome like

**[01:29]** basically the overall tax outcome like what is your overall refund for this

**[01:31]** what is your overall refund for this

**[01:31]** what is your overall refund for this year.

**[01:40]** Now into it geni experiences are built

**[01:40]** Now into it geni experiences are built on top of our propriety genos that's the

**[01:42]** on top of our propriety genos that's the

**[01:42]** on top of our propriety genos that's the generative OS that we have built as a

**[01:45]** generative OS that we have built as a

**[01:45]** generative OS that we have built as a platform capability and it has a lot of

**[01:48]** platform capability and it has a lot of

**[01:48]** platform capability and it has a lot of different pieces uh that you see over

**[01:50]** different pieces uh that you see over

**[01:50]** different pieces uh that you see over here. Uh the key goal is that we found

**[01:55]** here. Uh the key goal is that we found

**[01:55]** here. Uh the key goal is that we found that a lot of the genos tooling that

**[01:56]** that a lot of the genos tooling that

**[01:56]** that a lot of the genos tooling that comes out of the box is not supporting

**[01:58]** comes out of the box is not supporting

**[01:58]** comes out of the box is not supporting all our use cases. We want to most


### [02:00 - 03:00]

**[02:01]** all our use cases. We want to most

**[02:01]** all our use cases. We want to most prominently working in tax we are in the

**[02:03]** prominently working in tax we are in the

**[02:03]** prominently working in tax we are in the regulatory business uh safety security

**[02:06]** regulatory business uh safety security

**[02:06]** regulatory business uh safety security uh is very very important. So we want to

**[02:09]** uh is very very important. So we want to

**[02:09]** uh is very very important. So we want to focus on that. At the same time we want

**[02:11]** focus on that. At the same time we want

**[02:11]** focus on that. At the same time we want to build a piece that company at the

**[02:13]** to build a piece that company at the

**[02:13]** to build a piece that company at the scale of in it can use end to end really

**[02:16]** scale of in it can use end to end really

**[02:16]** scale of in it can use end to end really large scale. So that's where Geno comes

**[02:19]** large scale. So that's where Geno comes

**[02:19]** large scale. So that's where Geno comes in. We have different pieces. There's on

**[02:21]** in. We have different pieces. There's on

**[02:21]** in. We have different pieces. There's on the UI side which is the genux. Then

**[02:23]** the UI side which is the genux. Then

**[02:23]** the UI side which is the genux. Then there's orchestrator. That's basically

**[02:25]** there's orchestrator. That's basically

**[02:25]** there's orchestrator. That's basically the piece where different teams are

**[02:27]** the piece where different teams are

**[02:27]** the piece where different teams are working on different components,

**[02:28]** working on different components,

**[02:28]** working on different components, different pieces, different LM

**[02:30]** different pieces, different LM

**[02:30]** different pieces, different LM solutions. How do you find the right

**[02:31]** solutions. How do you find the right

**[02:31]** solutions. How do you find the right solution to answer the right question

**[02:33]** solution to answer the right question

**[02:33]** solution to answer the right question and uh into it calls the entire

**[02:36]** and uh into it calls the entire

**[02:36]** and uh into it calls the entire experience that we power through this

**[02:37]** experience that we power through this

**[02:38]** experience that we power through this into it assist. So I'm going to deep

**[02:41]** into it assist. So I'm going to deep

**[02:41]** into it assist. So I'm going to deep dive into specific pieces that our team

**[02:43]** dive into specific pieces that our team

**[02:43]** dive into specific pieces that our team used to build out uh the experience for

**[02:45]** used to build out uh the experience for

**[02:45]** used to build out uh the experience for Turboax.

**[02:52]** So as I said earlier right we have

**[02:52]** So as I said earlier right we have millions and millions of customers who

**[02:54]** millions and millions of customers who

**[02:54]** millions and millions of customers who are coming in. So we're trying to build

**[02:55]** are coming in. So we're trying to build

**[02:55]** are coming in. So we're trying to build a scalable solution that can work end to

**[02:57]** a scalable solution that can work end to

**[02:57]** a scalable solution that can work end to end. So on the slide here I'm basically

**[02:59]** end. So on the slide here I'm basically

**[02:59]** end. So on the slide here I'm basically going to talk about different pieces


### [03:00 - 04:00]

**[03:01]** going to talk about different pieces

**[03:01]** going to talk about different pieces that are powering the experience. Uh of

**[03:04]** that are powering the experience. Uh of

**[03:04]** that are powering the experience. Uh of course to begin with the first iteration

**[03:05]** course to begin with the first iteration

**[03:05]** course to begin with the first iteration was the prompt tooling uh basically a

**[03:08]** was the prompt tooling uh basically a

**[03:08]** was the prompt tooling uh basically a prompt based solution to try and go

**[03:10]** prompt based solution to try and go

**[03:10]** prompt based solution to try and go through what's your tax situation going

**[03:12]** through what's your tax situation going

**[03:12]** through what's your tax situation going on. Let's take example of what I was

**[03:14]** on. Let's take example of what I was

**[03:14]** on. Let's take example of what I was showing earlier which was your tax

**[03:15]** showing earlier which was your tax

**[03:15]** showing earlier which was your tax refund. So your tax refund has many

**[03:18]** refund. So your tax refund has many

**[03:18]** refund. So your tax refund has many constituents. These are your deductions.

**[03:20]** constituents. These are your deductions.

**[03:20]** constituents. These are your deductions. These are your credits, standard

**[03:22]** These are your credits, standard

**[03:22]** These are your credits, standard deduction, W2 withholding and so on. So

**[03:25]** deduction, W2 withholding and so on. So

**[03:25]** deduction, W2 withholding and so on. So we want to make sure that you understand

**[03:26]** we want to make sure that you understand

**[03:26]** we want to make sure that you understand all of that. So we built a prompt based

**[03:28]** all of that. So we built a prompt based

**[03:28]** all of that. So we built a prompt based solution around it and work from there.

**[03:31]** solution around it and work from there.

**[03:32]** solution around it and work from there. The production model that we went with

**[03:34]** The production model that we went with

**[03:34]** The production model that we went with is claude uh for this use case. Uh in is

**[03:38]** is claude uh for this use case. Uh in is

**[03:38]** is claude uh for this use case. Uh in is one of the uh biggest users of claude.

**[03:41]** one of the uh biggest users of claude.

**[03:41]** one of the uh biggest users of claude. Uh we had a multi-million dollar

**[03:42]** Uh we had a multi-million dollar

**[03:42]** Uh we had a multi-million dollar contract for this year as well. And uh

**[03:45]** contract for this year as well. And uh

**[03:45]** contract for this year as well. And uh you'll also see open eye over there. So

**[03:46]** you'll also see open eye over there. So

**[03:46]** you'll also see open eye over there. So open eye is where we used for other

**[03:49]** open eye is where we used for other

**[03:49]** open eye is where we used for other question and answering. So you'll see on

**[03:51]** question and answering. So you'll see on

**[03:51]** question and answering. So you'll see on the slide we're talking about static and

**[03:53]** the slide we're talking about static and

**[03:53]** the slide we're talking about static and dynamic type of queries. So uh static

**[03:56]** dynamic type of queries. So uh static

**[03:56]** dynamic type of queries. So uh static queries would be you know what I was

**[03:57]** queries would be you know what I was

**[03:57]** queries would be you know what I was showing earlier that we know you are


### [04:00 - 05:00]

**[04:00]** showing earlier that we know you are

**[04:00]** showing earlier that we know you are looking at your summary. You want to see

**[04:02]** looking at your summary. You want to see

**[04:02]** looking at your summary. You want to see what happened overall. So that would be

**[04:04]** what happened overall. So that would be

**[04:04]** what happened overall. So that would be a static prompt. Think of it like a

**[04:06]** a static prompt. Think of it like a

**[04:06]** a static prompt. Think of it like a prepared statement. Uh however the

**[04:09]** prepared statement. Uh however the

**[04:09]** prepared statement. Uh however the additional information that we're

**[04:10]** additional information that we're

**[04:10]** additional information that we're gathering is the tax info when the user

**[04:12]** gathering is the tax info when the user

**[04:12]** gathering is the tax info when the user comes in. Now uh dynamic query would be

**[04:15]** comes in. Now uh dynamic query would be

**[04:16]** comes in. Now uh dynamic query would be user have questions about the tax

**[04:17]** user have questions about the tax

**[04:17]** user have questions about the tax situation you know can I deduct my dog

**[04:20]** situation you know can I deduct my dog

**[04:20]** situation you know can I deduct my dog well you can't but you can try so things

**[04:23]** well you can't but you can try so things

**[04:23]** well you can't but you can try so things like that that's what we're trying to

**[04:25]** like that that's what we're trying to

**[04:25]** like that that's what we're trying to answer more dynamically u opens GP4 mini

**[04:29]** answer more dynamically u opens GP4 mini

**[04:29]** answer more dynamically u opens GP4 mini had been the model of choice for until a

**[04:31]** had been the model of choice for until a

**[04:31]** had been the model of choice for until a few months ago we're now iterating on

**[04:33]** few months ago we're now iterating on

**[04:33]** few months ago we're now iterating on the newer versions of course models

**[04:35]** the newer versions of course models

**[04:35]** the newer versions of course models change every year every month I should

**[04:37]** change every year every month I should

**[04:37]** change every year every month I should say uh so we're trying to focus on that

**[04:41]** say uh so we're trying to focus on that

**[04:41]** say uh so we're trying to focus on that u same for the dynamic piece Again

**[04:43]** u same for the dynamic piece Again

**[04:43]** u same for the dynamic piece Again another important aspect is you know tax

**[04:46]** another important aspect is you know tax

**[04:46]** another important aspect is you know tax information. IRS changes forms every

**[04:48]** information. IRS changes forms every

**[04:48]** information. IRS changes forms every year uh into it has proprietary tax uh

**[04:51]** year uh into it has proprietary tax uh

**[04:51]** year uh into it has proprietary tax uh information tax engines that we want to

**[04:53]** information tax engines that we want to

**[04:53]** information tax engines that we want to use. So we have rag based and of course

**[04:56]** use. So we have rag based and of course

**[04:56]** use. So we have rag based and of course graph rag based solutions around it as

**[04:58]** graph rag based solutions around it as

**[04:58]** graph rag based solutions around it as well. So they help us uh answer users


### [05:00 - 06:00]

**[05:01]** well. So they help us uh answer users

**[05:01]** well. So they help us uh answer users questions much better. And uh one thing

**[05:04]** questions much better. And uh one thing

**[05:04]** questions much better. And uh one thing that we also piloted recently was

**[05:06]** that we also piloted recently was

**[05:06]** that we also piloted recently was actually having a fine tuned LLM. So uh

**[05:10]** actually having a fine tuned LLM. So uh

**[05:10]** actually having a fine tuned LLM. So uh we went with cloud because that's the

**[05:11]** we went with cloud because that's the

**[05:12]** we went with cloud because that's the primary one we are using there and we

**[05:13]** primary one we are using there and we

**[05:13]** primary one we are using there and we stuck to static queries and we tested it

**[05:15]** stuck to static queries and we tested it

**[05:15]** stuck to static queries and we tested it out and uh it does well uh it definitely

**[05:19]** out and uh it does well uh it definitely

**[05:19]** out and uh it does well uh it definitely does well uh quality is there uh it

**[05:22]** does well uh quality is there uh it

**[05:22]** does well uh quality is there uh it takes effort to fine-tune the model uh

**[05:25]** takes effort to fine-tune the model uh

**[05:25]** takes effort to fine-tune the model uh however we found that was a little too

**[05:27]** however we found that was a little too

**[05:27]** however we found that was a little too specialized in the specific use case and

**[05:30]** specialized in the specific use case and

**[05:30]** specialized in the specific use case and uh one thing I want to highlight I'll

**[05:32]** uh one thing I want to highlight I'll

**[05:32]** uh one thing I want to highlight I'll deep dive further on is eval so you want

**[05:34]** deep dive further on is eval so you want

**[05:34]** deep dive further on is eval so you want to make sure that we evaluate everything

**[05:37]** to make sure that we evaluate everything

**[05:37]** to make sure that we evaluate everything we do um you want to make sure what's

**[05:39]** we do um you want to make sure what's

**[05:40]** we do um you want to make sure what's happening in production. You want to

**[05:41]** happening in production. You want to

**[05:41]** happening in production. You want to make sure in the development life cycle

**[05:43]** make sure in the development life cycle

**[05:43]** make sure in the development life cycle you're doing everything you need to do

**[05:44]** you're doing everything you need to do

**[05:44]** you're doing everything you need to do to make sure the you have the best

**[05:46]** to make sure the you have the best

**[05:46]** to make sure the you have the best bronze out there. Uh and with that

**[05:49]** bronze out there. Uh and with that

**[05:49]** bronze out there. Uh and with that moving on to the next slide.

**[05:52]** moving on to the next slide.

**[05:52]** moving on to the next slide. So to summarize a little bit you know

**[05:54]** So to summarize a little bit you know

**[05:54]** So to summarize a little bit you know these are the key pillars that we have.

**[05:56]** these are the key pillars that we have.

**[05:56]** these are the key pillars that we have. I already spoke about some of them

**[05:57]** I already spoke about some of them

**[05:57]** I already spoke about some of them before I want to highlight here that the


### [06:00 - 07:00]

**[06:00]** before I want to highlight here that the

**[06:00]** before I want to highlight here that the bottom part in this slide actually the

**[06:02]** bottom part in this slide actually the

**[06:02]** bottom part in this slide actually the human domain expert. So uh indeed has a

**[06:05]** human domain expert. So uh indeed has a

**[06:05]** human domain expert. So uh indeed has a lot of tax analysts that we work with of

**[06:08]** lot of tax analysts that we work with of

**[06:08]** lot of tax analysts that we work with of course that are on that work with us uh

**[06:10]** course that are on that work with us uh

**[06:10]** course that are on that work with us uh decoding IRS changes year-over-year

**[06:13]** decoding IRS changes year-over-year

**[06:13]** decoding IRS changes year-over-year making changes and so on. So they are

**[06:15]** making changes and so on. So they are

**[06:15]** making changes and so on. So they are the experts that provide us the

**[06:17]** the experts that provide us the

**[06:17]** the experts that provide us the information uh make sure the evaluations

**[06:20]** information uh make sure the evaluations

**[06:20]** information uh make sure the evaluations are correctly done. So we have a phased

**[06:22]** are correctly done. So we have a phased

**[06:22]** are correctly done. So we have a phased evaluation system. We have manual

**[06:24]** evaluation system. We have manual

**[06:24]** evaluation system. We have manual evaluations initially in the development

**[06:26]** evaluations initially in the development

**[06:26]** evaluations initially in the development life cycle. Um and another thing that we

**[06:29]** life cycle. Um and another thing that we

**[06:29]** life cycle. Um and another thing that we have done is actually using the tax

**[06:31]** have done is actually using the tax

**[06:31]** have done is actually using the tax analysts as the prompt engineers. So

**[06:33]** analysts as the prompt engineers. So

**[06:33]** analysts as the prompt engineers. So that allows us the folks in data science

**[06:35]** that allows us the folks in data science

**[06:35]** that allows us the folks in data science and ML world to actually focus on the

**[06:37]** and ML world to actually focus on the

**[06:37]** and ML world to actually focus on the quality defining the metrics uh making

**[06:40]** quality defining the metrics uh making

**[06:40]** quality defining the metrics uh making sure we have a nice data set that we can

**[06:42]** sure we have a nice data set that we can

**[06:42]** sure we have a nice data set that we can iterate on and test on. uh as we go

**[06:45]** iterate on and test on. uh as we go

**[06:45]** iterate on and test on. uh as we go along as I said models change we want to

**[06:47]** along as I said models change we want to

**[06:47]** along as I said models change we want to try out different models we want to see

**[06:50]** try out different models we want to see

**[06:50]** try out different models we want to see uh the laws change in the IRS say tax

**[06:53]** uh the laws change in the IRS say tax

**[06:53]** uh the laws change in the IRS say tax year 23 to 24 what happened uh so those

**[06:56]** year 23 to 24 what happened uh so those

**[06:56]** year 23 to 24 what happened uh so those changes so we focus on that uh and human


### [07:00 - 08:00]

**[07:00]** changes so we focus on that uh and human

**[07:00]** changes so we focus on that uh and human experts bring their expertise and are

**[07:02]** experts bring their expertise and are

**[07:02]** experts bring their expertise and are able to both help with prompt

**[07:04]** able to both help with prompt

**[07:04]** able to both help with prompt engineering and get the initial

**[07:06]** engineering and get the initial

**[07:06]** engineering and get the initial evaluations done that then becomes the

**[07:08]** evaluations done that then becomes the

**[07:08]** evaluations done that then becomes the basis for automated evaluations um LLM

**[07:11]** basis for automated evaluations um LLM

**[07:12]** basis for automated evaluations um LLM as a judge is what we use as

**[07:14]** as a judge is what we use as

**[07:14]** as a judge is what we use as uh I'm going to talk a little bit more

**[07:16]** uh I'm going to talk a little bit more

**[07:16]** uh I'm going to talk a little bit more about that. Uh I'm going to take uh

**[07:20]** about that. Uh I'm going to take uh

**[07:20]** about that. Uh I'm going to take uh going back then to what I was turning

**[07:22]** going back then to what I was turning

**[07:22]** going back then to what I was turning earlier about the claw3 highQ and

**[07:25]** earlier about the claw3 highQ and

**[07:25]** earlier about the claw3 highQ and fine-tuning. So uh fine-tuning

**[07:29]** fine-tuning. So uh fine-tuning

**[07:29]** fine-tuning. So uh fine-tuning as part of genos we built out a lot of

**[07:31]** as part of genos we built out a lot of

**[07:31]** as part of genos we built out a lot of tool sets. Uh one more thing that we

**[07:33]** tool sets. Uh one more thing that we

**[07:33]** tool sets. Uh one more thing that we want to do is support fine-tuning. So

**[07:35]** want to do is support fine-tuning. So

**[07:35]** want to do is support fine-tuning. So for our use case we actually stuck to

**[07:37]** for our use case we actually stuck to

**[07:37]** for our use case we actually stuck to just fine-tuning on claw 3 haiku powered

**[07:39]** just fine-tuning on claw 3 haiku powered

**[07:39]** just fine-tuning on claw 3 haiku powered by AWS bedrock. And the goal there was

**[07:42]** by AWS bedrock. And the goal there was

**[07:42]** by AWS bedrock. And the goal there was that we wanted to see if we can actually

**[07:44]** that we wanted to see if we can actually

**[07:44]** that we wanted to see if we can actually improve uh the quality of responses. Uh

**[07:47]** improve uh the quality of responses. Uh

**[07:47]** improve uh the quality of responses. Uh biggest driver of course is uh fewer

**[07:50]** biggest driver of course is uh fewer

**[07:50]** biggest driver of course is uh fewer instructions are needed once you have

**[07:53]** instructions are needed once you have

**[07:53]** instructions are needed once you have fine-tuned the model. We want to make uh

**[07:55]** fine-tuned the model. We want to make uh

**[07:55]** fine-tuned the model. We want to make uh latencies are a big concern. So we want

**[07:57]** latencies are a big concern. So we want

**[07:57]** latencies are a big concern. So we want to see if we can squeeze down the prompt

**[07:59]** to see if we can squeeze down the prompt

**[07:59]** to see if we can squeeze down the prompt size and at the same time keep the


### [08:00 - 09:00]

**[08:01]** size and at the same time keep the

**[08:01]** size and at the same time keep the quality uh that we need and keep going

**[08:03]** quality uh that we need and keep going

**[08:04]** quality uh that we need and keep going there. So this is roughly what it looks

**[08:06]** there. So this is roughly what it looks

**[08:06]** there. So this is roughly what it looks like. We build out uh we have different

**[08:09]** like. We build out uh we have different

**[08:09]** like. We build out uh we have different test AWS accounts, different

**[08:11]** test AWS accounts, different

**[08:11]** test AWS accounts, different environments uh that are provided by the

**[08:14]** environments uh that are provided by the

**[08:14]** environments uh that are provided by the uh platform teams that we work with. We

**[08:16]** uh platform teams that we work with. We

**[08:16]** uh platform teams that we work with. We look at the data and uh brief not to

**[08:20]** look at the data and uh brief not to

**[08:20]** look at the data and uh brief not to regulations uh 7 to six uh 16

**[08:22]** regulations uh 7 to six uh 16

**[08:22]** regulations uh 7 to six uh 16 regulations. So we only use consented

**[08:24]** regulations. So we only use consented

**[08:24]** regulations. So we only use consented data from users uh make sure uh we're on

**[08:27]** data from users uh make sure uh we're on

**[08:27]** data from users uh make sure uh we're on the right

**[08:29]** the right

**[08:29]** the right and uh just to double down on the

**[08:32]** and uh just to double down on the

**[08:32]** and uh just to double down on the evaluation part right you want to

**[08:34]** evaluation part right you want to

**[08:34]** evaluation part right you want to evaluate everything. So the key pillars

**[08:36]** evaluate everything. So the key pillars

**[08:36]** evaluate everything. So the key pillars are accuracy, relevancy and coherence.

**[08:38]** are accuracy, relevancy and coherence.

**[08:38]** are accuracy, relevancy and coherence. So we have both manual and automated

**[08:41]** So we have both manual and automated

**[08:41]** So we have both manual and automated systems. We also have broad monitoring

**[08:43]** systems. We also have broad monitoring

**[08:43]** systems. We also have broad monitoring uh automated systems basically look at

**[08:45]** uh automated systems basically look at

**[08:45]** uh automated systems basically look at sample data uh on what the LLM is

**[08:48]** sample data uh on what the LLM is

**[08:48]** sample data uh on what the LLM is basically giving real users in real

**[08:50]** basically giving real users in real

**[08:50]** basically giving real users in real time. And uh for this tooling that we've

**[08:54]** time. And uh for this tooling that we've

**[08:54]** time. And uh for this tooling that we've built out uh here LLM is a judge comes

**[08:57]** built out uh here LLM is a judge comes

**[08:57]** built out uh here LLM is a judge comes in in the auto side. We've also

**[08:59]** in in the auto side. We've also

**[08:59]** in in the auto side. We've also developed some tooling uh inhouse uh to


### [09:00 - 10:00]

**[09:02]** developed some tooling uh inhouse uh to

**[09:02]** developed some tooling uh inhouse uh to basically do some automated prompt

**[09:05]** basically do some automated prompt

**[09:05]** basically do some automated prompt changeing and that actually really helps

**[09:07]** changeing and that actually really helps

**[09:07]** changeing and that actually really helps to update our LLM as a judge. Basically

**[09:11]** to update our LLM as a judge. Basically

**[09:11]** to update our LLM as a judge. Basically LLM as a judge operates on top of a

**[09:13]** LLM as a judge operates on top of a

**[09:13]** LLM as a judge operates on top of a prompt. Uh it needs different

**[09:15]** prompt. Uh it needs different

**[09:15]** prompt. Uh it needs different information. It needs some manual

**[09:17]** information. It needs some manual

**[09:17]** information. It needs some manual samples which are the like golden data

**[09:19]** samples which are the like golden data

**[09:19]** samples which are the like golden data set. We use AWS ground truth for that.

**[09:22]** set. We use AWS ground truth for that.

**[09:22]** set. We use AWS ground truth for that. Uh and take on that. Uh one more thing

**[09:25]** Uh and take on that. Uh one more thing

**[09:25]** Uh and take on that. Uh one more thing that I want to highlight here is uh

**[09:27]** that I want to highlight here is uh

**[09:27]** that I want to highlight here is uh models. So we made the move from uh uh

**[09:31]** models. So we made the move from uh uh

**[09:31]** models. So we made the move from uh uh anthropic cloud instant to anthropic

**[09:33]** anthropic cloud instant to anthropic

**[09:33]** anthropic cloud instant to anthropic cloud haiku for the next year uh for uh

**[09:36]** cloud haiku for the next year uh for uh

**[09:36]** cloud haiku for the next year uh for uh taxia 24 and that takes some effort and

**[09:40]** taxia 24 and that takes some effort and

**[09:40]** taxia 24 and that takes some effort and the only way it's possible is because we

**[09:41]** the only way it's possible is because we

**[09:41]** the only way it's possible is because we have clear eval in place so that we can

**[09:44]** have clear eval in place so that we can

**[09:44]** have clear eval in place so that we can test out uh whatever we are changing and

**[09:47]** test out uh whatever we are changing and

**[09:47]** test out uh whatever we are changing and uh model changes are not uh as smooth as

**[09:49]** uh model changes are not uh as smooth as

**[09:49]** uh model changes are not uh as smooth as you would think.

**[09:56]** These are some more details on what

**[09:56]** These are some more details on what we're talking about on the automated

**[09:58]** we're talking about on the automated

**[09:58]** we're talking about on the automated evals. Uh


### [10:00 - 11:00]

**[10:01]** evals. Uh

**[10:01]** evals. Uh as you can see the key output is we want

**[10:03]** as you can see the key output is we want

**[10:03]** as you can see the key output is we want to make sure it's tax accurate. That's

**[10:04]** to make sure it's tax accurate. That's

**[10:04]** to make sure it's tax accurate. That's the main thing we want to aim for and

**[10:07]** the main thing we want to aim for and

**[10:07]** the main thing we want to aim for and focus on that. I'm going to move on

**[10:09]** focus on that. I'm going to move on

**[10:09]** focus on that. I'm going to move on here. So let's talk about some major

**[10:11]** here. So let's talk about some major

**[10:11]** here. So let's talk about some major learnings that we have. So uh the

**[10:14]** learnings that we have. So uh the

**[10:14]** learnings that we have. So uh the contracts are really expensive and the

**[10:16]** contracts are really expensive and the

**[10:16]** contracts are really expensive and the only way they are slightly cheaper if

**[10:18]** only way they are slightly cheaper if

**[10:18]** only way they are slightly cheaper if you have long-term contracts. So uh you

**[10:21]** you have long-term contracts. So uh you

**[10:21]** you have long-term contracts. So uh you are tied in to the vendor. So it helps

**[10:24]** are tied in to the vendor. So it helps

**[10:24]** are tied in to the vendor. So it helps to have strong partners on the vendor

**[10:27]** to have strong partners on the vendor

**[10:27]** to have strong partners on the vendor side who work with you uh to help

**[10:29]** side who work with you uh to help

**[10:29]** side who work with you uh to help iterate, help improve and uh I think I

**[10:32]** iterate, help improve and uh I think I

**[10:32]** iterate, help improve and uh I think I was in this conference last year and

**[10:34]** was in this conference last year and

**[10:34]** was in this conference last year and this was one thing called out then as

**[10:35]** this was one thing called out then as

**[10:35]** this was one thing called out then as well that uh essentially vendors are a

**[10:38]** well that uh essentially vendors are a

**[10:38]** well that uh essentially vendors are a form of lock in the prompts are a form

**[10:41]** form of lock in the prompts are a form

**[10:41]** form of lock in the prompts are a form of lock in. It's not easy and we found

**[10:43]** of lock in. It's not easy and we found

**[10:43]** of lock in. It's not easy and we found out it's not even easy to upgrade this

**[10:45]** out it's not even easy to upgrade this

**[10:45]** out it's not even easy to upgrade this model from the same vendor going into

**[10:47]** model from the same vendor going into

**[10:47]** model from the same vendor going into the next year. So we want to focus on

**[10:49]** the next year. So we want to focus on

**[10:49]** the next year. So we want to focus on that. Uh, another thing I really want to

**[10:52]** that. Uh, another thing I really want to

**[10:52]** that. Uh, another thing I really want to highlight here is the latency. So, uh,

**[10:55]** highlight here is the latency. So, uh,

**[10:55]** highlight here is the latency. So, uh, LLM models of course they don't have the

**[10:58]** LLM models of course they don't have the

**[10:58]** LLM models of course they don't have the SLAs of backend services. We're not


### [11:00 - 12:00]

**[11:01]** SLAs of backend services. We're not

**[11:01]** SLAs of backend services. We're not looking at, you know, 100 millisecond,

**[11:02]** looking at, you know, 100 millisecond,

**[11:02]** looking at, you know, 100 millisecond, 200 milliseconds. We're talking about 3

**[11:04]** 200 milliseconds. We're talking about 3

**[11:04]** 200 milliseconds. We're talking about 3 seconds, 5 seconds, 10 seconds. So as

**[11:08]** seconds, 5 seconds, 10 seconds. So as

**[11:08]** seconds, 5 seconds, 10 seconds. So as the user's tax info tax information

**[11:10]** the user's tax info tax information

**[11:10]** the user's tax info tax information comes in maybe they have a complicated

**[11:12]** comes in maybe they have a complicated

**[11:12]** comes in maybe they have a complicated situation like me that you know they own

**[11:14]** situation like me that you know they own

**[11:14]** situation like me that you know they own a home they have maybe something in

**[11:16]** a home they have maybe something in

**[11:16]** a home they have maybe something in stocks and they're trying to file they

**[11:18]** stocks and they're trying to file they

**[11:18]** stocks and they're trying to file they have their spouse have their jobs as

**[11:20]** have their spouse have their jobs as

**[11:20]** have their spouse have their jobs as well a lot of things going on so the

**[11:22]** well a lot of things going on so the

**[11:22]** well a lot of things going on so the prompts really balloon up uh if you're

**[11:25]** prompts really balloon up uh if you're

**[11:25]** prompts really balloon up uh if you're trying to figure out the outcome and uh

**[11:27]** trying to figure out the outcome and uh

**[11:27]** trying to figure out the outcome and uh as you go into you know tax day

**[11:29]** as you go into you know tax day

**[11:29]** as you go into you know tax day everybody's trying to file on tax day

**[11:31]** everybody's trying to file on tax day

**[11:31]** everybody's trying to file on tax day right April 15 so uh latency really is

**[11:36]** right April 15 so uh latency really is

**[11:36]** right April 15 so uh latency really is uh shooting through the roof. So we

**[11:38]** uh shooting through the roof. So we

**[11:38]** uh shooting through the roof. So we design a product around that. We want to

**[11:40]** design a product around that. We want to

**[11:40]** design a product around that. We want to make sure we have the right uh fallback

**[11:43]** make sure we have the right uh fallback

**[11:43]** make sure we have the right uh fallback mechanisms, the right uh user design uh

**[11:47]** mechanisms, the right uh user design uh

**[11:47]** mechanisms, the right uh user design uh product design to make sure that the

**[11:49]** product design to make sure that the

**[11:49]** product design to make sure that the user experience is seamless and uh

**[11:51]** user experience is seamless and uh

**[11:51]** user experience is seamless and uh useful. Uh we want to make sure that the

**[11:53]** useful. Uh we want to make sure that the

**[11:53]** useful. Uh we want to make sure that the explanations are helpful more than

**[11:54]** explanations are helpful more than

**[11:54]** explanations are helpful more than anything else. And uh I think I covered

**[11:58]** anything else. And uh I think I covered

**[11:58]** anything else. And uh I think I covered all the other places but once again I


### [12:00 - 13:00]

**[12:00]** all the other places but once again I

**[12:00]** all the other places but once again I cannot say that enough. Evals are a must

**[12:02]** cannot say that enough. Evals are a must

**[12:02]** cannot say that enough. Evals are a must to launch. Focus on evals. Make sure you

**[12:05]** to launch. Focus on evals. Make sure you

**[12:05]** to launch. Focus on evals. Make sure you have clear guidelines on what you're

**[12:06]** have clear guidelines on what you're

**[12:06]** have clear guidelines on what you're building. Uh have clear golden data set.

**[12:10]** building. Uh have clear golden data set.

**[12:10]** building. Uh have clear golden data set. I've heard that from other talks as

**[12:11]** I've heard that from other talks as

**[12:11]** I've heard that from other talks as well. That's really a key point.

**[12:17]** Uh that's all I'm going to pause here

**[12:17]** Uh that's all I'm going to pause here for questions.

**[12:20]** for questions.

**[12:20]** for questions. Uh if you're going to be asking

**[12:21]** Uh if you're going to be asking

**[12:21]** Uh if you're going to be asking questions, please come to one of the

**[12:22]** questions, please come to one of the

**[12:22]** questions, please come to one of the microphones so that we can capture the

**[12:24]** microphones so that we can capture the

**[12:24]** microphones so that we can capture the audio.

**[12:33]** Yeah. Hi. Um you said uh evaluate

**[12:33]** Yeah. Hi. Um you said uh evaluate everything, right? But uh with geni

**[12:36]** everything, right? But uh with geni

**[12:36]** everything, right? But uh with geni systems there could be you know very

**[12:37]** systems there could be you know very

**[12:37]** systems there could be you know very small changes right you make small

**[12:39]** small changes right you make small

**[12:39]** small changes right you make small change to a prompt and evaluations can

**[12:43]** change to a prompt and evaluations can

**[12:43]** change to a prompt and evaluations can get very expensive or slow down your

**[12:44]** get very expensive or slow down your

**[12:44]** get very expensive or slow down your whole sort of development process right

**[12:47]** whole sort of development process right

**[12:47]** whole sort of development process right so maybe could you dive a little bit

**[12:49]** so maybe could you dive a little bit

**[12:49]** so maybe could you dive a little bit deeper into like when do you bring in

**[12:51]** deeper into like when do you bring in

**[12:51]** deeper into like when do you bring in different types of evaluations? Are

**[12:53]** different types of evaluations? Are

**[12:53]** different types of evaluations? Are there are there anything that you just

**[12:55]** there are there anything that you just

**[12:55]** there are there anything that you just say uh we ran some aggression tests and

**[12:57]** say uh we ran some aggression tests and

**[12:57]** say uh we ran some aggression tests and it looks fine so you launch or do you

**[12:59]** it looks fine so you launch or do you

**[12:59]** it looks fine so you launch or do you always go kind of with the expert? Sure.


### [13:00 - 14:00]

**[13:02]** always go kind of with the expert? Sure.

**[13:02]** always go kind of with the expert? Sure. Uh thank you for the question. So just

**[13:05]** Uh thank you for the question. So just

**[13:05]** Uh thank you for the question. So just to reiterate so the evaluations are

**[13:07]** to reiterate so the evaluations are

**[13:07]** to reiterate so the evaluations are different types. I would say when we are

**[13:09]** different types. I would say when we are

**[13:09]** different types. I would say when we are in the initial phase of development we

**[13:10]** in the initial phase of development we

**[13:10]** in the initial phase of development we are looking more on the uh manual

**[13:13]** are looking more on the uh manual

**[13:13]** are looking more on the uh manual relations with tax experts so we can get

**[13:14]** relations with tax experts so we can get

**[13:14]** relations with tax experts so we can get a baseline in place. Then as we are

**[13:16]** a baseline in place. Then as we are

**[13:16]** a baseline in place. Then as we are tweaking different things in the prompts

**[13:18]** tweaking different things in the prompts

**[13:18]** tweaking different things in the prompts that's where auto evaluation comes in.

**[13:20]** that's where auto evaluation comes in.

**[13:20]** that's where auto evaluation comes in. So we basically take the input from the

**[13:23]** So we basically take the input from the

**[13:23]** So we basically take the input from the uh uh tax experts and use that to train

**[13:27]** uh uh tax experts and use that to train

**[13:27]** uh uh tax experts and use that to train a judge prompt for the LLM. So that LLM

**[13:30]** a judge prompt for the LLM. So that LLM

**[13:30]** a judge prompt for the LLM. So that LLM is once again expensive. Uh we go for

**[13:33]** is once again expensive. Uh we go for

**[13:33]** is once again expensive. Uh we go for the GPD4 series until recently on that

**[13:35]** the GPD4 series until recently on that

**[13:35]** the GPD4 series until recently on that one. And uh then minor iterations we can

**[13:39]** one. And uh then minor iterations we can

**[13:39]** one. And uh then minor iterations we can do with auto eval. So we have clear

**[13:41]** do with auto eval. So we have clear

**[13:41]** do with auto eval. So we have clear understanding with product we want to

**[13:42]** understanding with product we want to

**[13:42]** understanding with product we want to make sure that the quality is there. And

**[13:44]** make sure that the quality is there. And

**[13:44]** make sure that the quality is there. And maybe once we have major changes for

**[13:46]** maybe once we have major changes for

**[13:46]** maybe once we have major changes for example we went from tax year 23 to tax

**[13:48]** example we went from tax year 23 to tax

**[13:48]** example we went from tax year 23 to tax year 24 then we definitely reiterate if

**[13:51]** year 24 then we definitely reiterate if

**[13:51]** year 24 then we definitely reiterate if the prompt changes a lot we would uh go

**[13:54]** the prompt changes a lot we would uh go

**[13:54]** the prompt changes a lot we would uh go for manual evaluations.

**[13:57]** for manual evaluations.

**[13:57]** for manual evaluations. Um thank you for the technical deep

**[13:59]** Um thank you for the technical deep

**[13:59]** Um thank you for the technical deep dive. I was more interested in the


### [14:00 - 15:00]

**[14:01]** dive. I was more interested in the

**[14:01]** dive. I was more interested in the product side of it. Sure. We we also do

**[14:04]** product side of it. Sure. We we also do

**[14:04]** product side of it. Sure. We we also do taxes. So I was curious what are the

**[14:06]** taxes. So I was curious what are the

**[14:06]** taxes. So I was curious what are the kind of um LLM interactions that the

**[14:08]** kind of um LLM interactions that the

**[14:08]** kind of um LLM interactions that the users are having like what are the kind

**[14:10]** users are having like what are the kind

**[14:10]** users are having like what are the kind of questions they're asking? Is it is it

**[14:13]** of questions they're asking? Is it is it

**[14:13]** of questions they're asking? Is it is it more like critical parts of the workflow

**[14:15]** more like critical parts of the workflow

**[14:15]** more like critical parts of the workflow or more like um what? So uh we have

**[14:20]** or more like um what? So uh we have

**[14:20]** or more like um what? So uh we have question answering for all types of

**[14:21]** question answering for all types of

**[14:21]** question answering for all types of questions that includes both the product

**[14:23]** questions that includes both the product

**[14:23]** questions that includes both the product question as in you know how do I do this

**[14:25]** question as in you know how do I do this

**[14:25]** question as in you know how do I do this in turbo tax uh or also their tax

**[14:28]** in turbo tax uh or also their tax

**[14:28]** in turbo tax uh or also their tax situation. So for example uh I paid the

**[14:31]** situation. So for example uh I paid the

**[14:31]** situation. So for example uh I paid the tuition from my grandchild can I claim

**[14:34]** tuition from my grandchild can I claim

**[14:34]** tuition from my grandchild can I claim that on my taxes so things like that. So

**[14:37]** that on my taxes so things like that. So

**[14:37]** that on my taxes so things like that. So our goal is we have different teams

**[14:38]** our goal is we have different teams

**[14:38]** our goal is we have different teams going after different pieces. Our goal

**[14:40]** going after different pieces. Our goal

**[14:40]** going after different pieces. Our goal is we want to answer all of these

**[14:41]** is we want to answer all of these

**[14:41]** is we want to answer all of these questions and uh accordingly different

**[14:45]** questions and uh accordingly different

**[14:45]** questions and uh accordingly different types of questions need different

**[14:47]** types of questions need different

**[14:47]** types of questions need different solutions and that's where maybe I would

**[14:49]** solutions and that's where maybe I would

**[14:49]** solutions and that's where maybe I would reiterate go back to

**[14:52]** reiterate go back to

**[14:52]** reiterate go back to here


### [15:00 - 16:00]

**[15:01]** so right so this piece here planner so

**[15:01]** so right so this piece here planner so essentially this is where it comes in we

**[15:03]** essentially this is where it comes in we

**[15:03]** essentially this is where it comes in we want to make sure when the query comes

**[15:04]** want to make sure when the query comes

**[15:04]** want to make sure when the query comes in we understand what the user is trying

**[15:05]** in we understand what the user is trying

**[15:06]** in we understand what the user is trying to ask and then we have different kind

**[15:07]** to ask and then we have different kind

**[15:07]** to ask and then we have different kind of solutions for different kind of

**[15:09]** of solutions for different kind of

**[15:09]** of solutions for different kind of questions and go through that.

**[15:12]** questions and go through that.

**[15:12]** questions and go through that. Thank you.

**[15:14]** Thank you.

**[15:14]** Thank you. Yeah. Hi. So you mentioned about the

**[15:15]** Yeah. Hi. So you mentioned about the

**[15:16]** Yeah. Hi. So you mentioned about the evaluation. So one quick question like

**[15:17]** evaluation. So one quick question like

**[15:17]** evaluation. So one quick question like so Turboax I'm sure it involves a lot of

**[15:20]** so Turboax I'm sure it involves a lot of

**[15:20]** so Turboax I'm sure it involves a lot of numbers the answers. So how do you

**[15:22]** numbers the answers. So how do you

**[15:22]** numbers the answers. So how do you verify those numbers in terms of the

**[15:23]** verify those numbers in terms of the

**[15:23]** verify those numbers in terms of the evaluation? Let's say uh the actual tax

**[15:25]** evaluation? Let's say uh the actual tax

**[15:26]** evaluation? Let's say uh the actual tax number is 11,235

**[15:28]** number is 11,235

**[15:28]** number is 11,235 and if it's something like 11,100 so

**[15:30]** and if it's something like 11,100 so

**[15:30]** and if it's something like 11,100 so it's quite difficult to catch this with

**[15:32]** it's quite difficult to catch this with

**[15:32]** it's quite difficult to catch this with a manual evaluation or an yeah uh thank

**[15:35]** a manual evaluation or an yeah uh thank

**[15:35]** a manual evaluation or an yeah uh thank you for the question. So that's a key

**[15:37]** you for the question. So that's a key

**[15:37]** you for the question. So that's a key thing that we work on. So Turboax of

**[15:39]** thing that we work on. So Turboax of

**[15:39]** thing that we work on. So Turboax of course has a tax knowledge engine that

**[15:41]** course has a tax knowledge engine that

**[15:41]** course has a tax knowledge engine that we have built proprietary in house

**[15:43]** we have built proprietary in house

**[15:43]** we have built proprietary in house managed over the years built and

**[15:44]** managed over the years built and

**[15:44]** managed over the years built and developed and that's really what's

**[15:46]** developed and that's really what's

**[15:46]** developed and that's really what's providing these numbers. The tax profile

**[15:48]** providing these numbers. The tax profile

**[15:48]** providing these numbers. The tax profile information is all coming from these

**[15:49]** information is all coming from these

**[15:49]** information is all coming from these numbers. We are not having LLMs do the

**[15:52]** numbers. We are not having LLMs do the

**[15:52]** numbers. We are not having LLMs do the calculations at all. We're basically

**[15:54]** calculations at all. We're basically

**[15:54]** calculations at all. We're basically using the ground truth that is already

**[15:55]** using the ground truth that is already

**[15:55]** using the ground truth that is already existing in our systems as the numbers

**[15:58]** existing in our systems as the numbers

**[15:58]** existing in our systems as the numbers that we see. And we have safety guard


### [16:00 - 17:00]

**[16:00]** that we see. And we have safety guard

**[16:00]** that we see. And we have safety guard rails. Uh maybe this piece here I would

**[16:03]** rails. Uh maybe this piece here I would

**[16:03]** rails. Uh maybe this piece here I would probably call out. We have a lot of

**[16:05]** probably call out. We have a lot of

**[16:05]** probably call out. We have a lot of safety guardrails on what's the raw LLM

**[16:07]** safety guardrails on what's the raw LLM

**[16:07]** safety guardrails on what's the raw LLM response. Make sure you know we are not

**[16:10]** response. Make sure you know we are not

**[16:10]** response. Make sure you know we are not hallucinating numbers before we send to

**[16:12]** hallucinating numbers before we send to

**[16:12]** hallucinating numbers before we send to the user. Got it. So uh the data is

**[16:15]** the user. Got it. So uh the data is

**[16:15]** the user. Got it. So uh the data is coming from the tax engine itself. But

**[16:17]** coming from the tax engine itself. But

**[16:17]** coming from the tax engine itself. But when you formulate the final explanation

**[16:19]** when you formulate the final explanation

**[16:19]** when you formulate the final explanation the answer itself. So how do you make

**[16:21]** the answer itself. So how do you make

**[16:21]** the answer itself. So how do you make sure that the numbers that are actually

**[16:23]** sure that the numbers that are actually

**[16:23]** sure that the numbers that are actually in the final answer are you know that's

**[16:26]** in the final answer are you know that's

**[16:26]** in the final answer are you know that's coming from data. So basically we have

**[16:28]** coming from data. So basically we have

**[16:28]** coming from data. So basically we have ML models that are working under the

**[16:30]** ML models that are working under the

**[16:30]** ML models that are working under the hood as part of the uh security aspect

**[16:32]** hood as part of the uh security aspect

**[16:32]** hood as part of the uh security aspect that you see here that basically make

**[16:34]** that you see here that basically make

**[16:34]** that you see here that basically make sure we did not hallucinate any numbers

**[16:36]** sure we did not hallucinate any numbers

**[16:36]** sure we did not hallucinate any numbers that we built up. Got it. Yeah. Thank

**[16:37]** that we built up. Got it. Yeah. Thank

**[16:37]** that we built up. Got it. Yeah. Thank you.

**[16:47]** Um could you give an overview of how you

**[16:47]** Um could you give an overview of how you use both just a traditional rag and

**[16:49]** use both just a traditional rag and

**[16:50]** use both just a traditional rag and graph rag like an hybrid in your

**[16:51]** graph rag like an hybrid in your

**[16:51]** graph rag like an hybrid in your workflow? Sure. Sure. So uh and and

**[16:53]** workflow? Sure. Sure. So uh and and

**[16:53]** workflow? Sure. Sure. So uh and and sorry one more question is now with the

**[16:55]** sorry one more question is now with the

**[16:55]** sorry one more question is now with the new model cloud 4 coming out do you

**[16:57]** new model cloud 4 coming out do you

**[16:57]** new model cloud 4 coming out do you think the fine-tuning might be getting

**[16:59]** think the fine-tuning might be getting

**[16:59]** think the fine-tuning might be getting easier or needs needed? Uh I'll take the


### [17:00 - 18:00]

**[17:02]** easier or needs needed? Uh I'll take the

**[17:02]** easier or needs needed? Uh I'll take the first one. Uh so uh graph rack we've

**[17:05]** first one. Uh so uh graph rack we've

**[17:05]** first one. Uh so uh graph rack we've definitely seen better response uh

**[17:07]** definitely seen better response uh

**[17:07]** definitely seen better response uh better response quality with graph rack.

**[17:09]** better response quality with graph rack.

**[17:09]** better response quality with graph rack. Uh even more than that though I think

**[17:11]** Uh even more than that though I think

**[17:11]** Uh even more than that though I think for end user helpfulness getting

**[17:14]** for end user helpfulness getting

**[17:14]** for end user helpfulness getting personalized answer is the key piece. I

**[17:17]** personalized answer is the key piece. I

**[17:17]** personalized answer is the key piece. I would say graphic definitely outperforms

**[17:20]** would say graphic definitely outperforms

**[17:20]** would say graphic definitely outperforms uh well regular rack uh and what even

**[17:24]** uh well regular rack uh and what even

**[17:24]** uh well regular rack uh and what even more outperforms is personalizing the

**[17:26]** more outperforms is personalizing the

**[17:26]** more outperforms is personalizing the answers and to your second question uh

**[17:28]** answers and to your second question uh

**[17:28]** answers and to your second question uh we are constantly evaluating the models

**[17:31]** we are constantly evaluating the models

**[17:31]** we are constantly evaluating the models uh this is really the time that you know

**[17:33]** uh this is really the time that you know

**[17:33]** uh this is really the time that you know April is just behind us we are trying to

**[17:35]** April is just behind us we are trying to

**[17:35]** April is just behind us we are trying to look at what new things we can do we

**[17:36]** look at what new things we can do we

**[17:36]** look at what new things we can do we also have some uh in-house models that

**[17:38]** also have some uh in-house models that

**[17:38]** also have some uh in-house models that in it trains and develops so we are

**[17:41]** in it trains and develops so we are

**[17:41]** in it trains and develops so we are constantly evaluating and uh I don't

**[17:43]** constantly evaluating and uh I don't

**[17:43]** constantly evaluating and uh I don't have an answer now what we'll do for the

**[17:45]** have an answer now what we'll do for the

**[17:45]** have an answer now what we'll do for the next tax year but yes we keep working on

**[17:47]** next tax year but yes we keep working on

**[17:47]** next tax year but yes we keep working on that.

**[17:49]** that.

**[17:49]** that. Uh you mentioned uh you have different

**[17:51]** Uh you mentioned uh you have different

**[17:51]** Uh you mentioned uh you have different situations, tax stack situations and you

**[17:53]** situations, tax stack situations and you

**[17:53]** situations, tax stack situations and you come up with an answer. So if I describe

**[17:56]** come up with an answer. So if I describe

**[17:56]** come up with an answer. So if I describe my situation and it's complicated and it

**[17:59]** my situation and it's complicated and it

**[17:59]** my situation and it's complicated and it comes up with an answer, is that answer


### [18:00 - 19:00]

**[18:02]** comes up with an answer, is that answer

**[18:02]** comes up with an answer, is that answer being generated using the LLM or is it

**[18:05]** being generated using the LLM or is it

**[18:05]** being generated using the LLM or is it going back to the tax engine and how do

**[18:07]** going back to the tax engine and how do

**[18:07]** going back to the tax engine and how do you explain how you came up with that

**[18:10]** you explain how you came up with that

**[18:10]** you explain how you came up with that answer and I I assume there's going to

**[18:12]** answer and I I assume there's going to

**[18:12]** answer and I I assume there's going to be a lot of legal challenges to a wrong

**[18:15]** be a lot of legal challenges to a wrong

**[18:15]** be a lot of legal challenges to a wrong answer. Absolutely. I mean uh into it

**[18:18]** answer. Absolutely. I mean uh into it

**[18:18]** answer. Absolutely. I mean uh into it focuses heavily on legal legal and

**[18:20]** focuses heavily on legal legal and

**[18:20]** focuses heavily on legal legal and privacy uh controls. So the solution for

**[18:24]** privacy uh controls. So the solution for

**[18:24]** privacy uh controls. So the solution for this one right what we worked on here

**[18:26]** this one right what we worked on here

**[18:26]** this one right what we worked on here this is specific this is more of the

**[18:28]** this is specific this is more of the

**[18:28]** this is specific this is more of the static variety of questions. So once

**[18:30]** static variety of questions. So once

**[18:30]** static variety of questions. So once again what I was saying earlier the

**[18:32]** again what I was saying earlier the

**[18:32]** again what I was saying earlier the inherent numbers are coming in from tax

**[18:34]** inherent numbers are coming in from tax

**[18:34]** inherent numbers are coming in from tax knowledge engine and we have tax experts

**[18:37]** knowledge engine and we have tax experts

**[18:37]** knowledge engine and we have tax experts who actually crafted these prompts. So

**[18:39]** who actually crafted these prompts. So

**[18:39]** who actually crafted these prompts. So they are specifically tested for each

**[18:41]** they are specifically tested for each

**[18:41]** they are specifically tested for each piece that you see here. So that's

**[18:44]** piece that you see here. So that's

**[18:44]** piece that you see here. So that's basically when we do the evad, we make

**[18:45]** basically when we do the evad, we make

**[18:45]** basically when we do the evad, we make sure it doesn't happen what you're

**[18:47]** sure it doesn't happen what you're

**[18:47]** sure it doesn't happen what you're suggesting.

**[18:49]** suggesting.

**[18:49]** suggesting. Okay, great. Thanks. Thank you so much.

**[18:51]** Okay, great. Thanks. Thank you so much.

**[18:52]** Okay, great. Thanks. Thank you so much. What a great talk.


