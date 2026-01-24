# The Billable Hour is Dead; Long Live the Billable Hour — Kevin Madura + Mo Bhasin, Alix Partners

**Video URL:** https://www.youtube.com/watch?v=Wv1tAxKYLeE

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** I'm Mo. Uh I'm director of AI products

**[00:18]** I'm Mo. Uh I'm director of AI products at Alex Partners. Prior to this, I was a

**[00:20]** at Alex Partners. Prior to this, I was a

**[00:20]** at Alex Partners. Prior to this, I was a co-founder of an anomaly detection

**[00:22]** co-founder of an anomaly detection

**[00:22]** co-founder of an anomaly detection anomaly detection startup and prior to

**[00:24]** anomaly detection startup and prior to

**[00:24]** anomaly detection startup and prior to that I was a data scientist at Google.

**[00:26]** that I was a data scientist at Google.

**[00:26]** that I was a data scientist at Google. uh together we co-lead the development

**[00:28]** uh together we co-lead the development

**[00:28]** uh together we co-lead the development of a internal Genai platform. We've been

**[00:31]** of a internal Genai platform. We've been

**[00:31]** of a internal Genai platform. We've been working it for the last two years. Uh we

**[00:33]** working it for the last two years. Uh we

**[00:33]** working it for the last two years. Uh we have 20 engineers. We've scaled it to 50

**[00:35]** have 20 engineers. We've scaled it to 50

**[00:35]** have 20 engineers. We've scaled it to 50 deployments uh and hundreds of users and

**[00:37]** deployments uh and hundreds of users and

**[00:37]** deployments uh and hundreds of users and we're excited to tell you everything

**[00:38]** we're excited to tell you everything

**[00:38]** we're excited to tell you everything we've learned on that journey. Great.

**[00:40]** we've learned on that journey. Great.

**[00:40]** we've learned on that journey. Great. And I'm Kevin Madura. I help companies,

**[00:42]** And I'm Kevin Madura. I help companies,

**[00:42]** And I'm Kevin Madura. I help companies, courts, and regulators understand new

**[00:44]** courts, and regulators understand new

**[00:44]** courts, and regulators understand new technologies like AI and LLMs. As Mo

**[00:47]** technologies like AI and LLMs. As Mo

**[00:47]** technologies like AI and LLMs. As Mo mentioned, both of us work at a company

**[00:49]** mentioned, both of us work at a company

**[00:49]** mentioned, both of us work at a company called Alex Partners. It's a global

**[00:51]** called Alex Partners. It's a global

**[00:51]** called Alex Partners. It's a global management consulting firm. I realize

**[00:53]** management consulting firm. I realize

**[00:53]** management consulting firm. I realize lots of you in this room might be

**[00:54]** lots of you in this room might be

**[00:54]** lots of you in this room might be rolling your eyes at that, rightfully

**[00:55]** rolling your eyes at that, rightfully

**[00:55]** rolling your eyes at that, rightfully so, but I like to think our firm does a

**[00:57]** so, but I like to think our firm does a

**[00:57]** so, but I like to think our firm does a little bit more than deliver

**[00:58]** little bit more than deliver

**[00:58]** little bit more than deliver PowerPoints. We actually roll up our

**[00:59]** PowerPoints. We actually roll up our

**[00:59]** PowerPoints. We actually roll up our sleeves and and solve problems, whether


### [01:00 - 02:00]

**[01:01]** sleeves and and solve problems, whether

**[01:01]** sleeves and and solve problems, whether that's coding or or actually uh getting

**[01:03]** that's coding or or actually uh getting

**[01:03]** that's coding or or actually uh getting into the weeds of things. So, we're here

**[01:05]** into the weeds of things. So, we're here

**[01:05]** into the weeds of things. So, we're here to talk to you today about really three

**[01:06]** to talk to you today about really three

**[01:06]** to talk to you today about really three different things. One is how we see AI

**[01:09]** different things. One is how we see AI

**[01:09]** different things. One is how we see AI reshaping knowledge work as we see it

**[01:11]** reshaping knowledge work as we see it

**[01:11]** reshaping knowledge work as we see it today. So, a lot of how it's impacting

**[01:12]** today. So, a lot of how it's impacting

**[01:12]** today. So, a lot of how it's impacting professional services, advisory

**[01:14]** professional services, advisory

**[01:14]** professional services, advisory services, that sort of thing. We'll

**[01:16]** services, that sort of thing. We'll

**[01:16]** services, that sort of thing. We'll bring three real life use cases uh that

**[01:18]** bring three real life use cases uh that

**[01:18]** bring three real life use cases uh that we'll walk through in terms of how we've

**[01:19]** we'll walk through in terms of how we've

**[01:19]** we'll walk through in terms of how we've actually deployed it realistically,

**[01:21]** actually deployed it realistically,

**[01:21]** actually deployed it realistically, concretely within the way that we work

**[01:23]** concretely within the way that we work

**[01:23]** concretely within the way that we work in our business and then wrap up with

**[01:25]** in our business and then wrap up with

**[01:25]** in our business and then wrap up with what doesn't work and where we see

**[01:26]** what doesn't work and where we see

**[01:26]** what doesn't work and where we see things going.

**[01:28]** things going.

**[01:28]** things going. So, some of you here might recognize

**[01:29]** So, some of you here might recognize

**[01:29]** So, some of you here might recognize this chart from an organization called

**[01:31]** this chart from an organization called

**[01:31]** this chart from an organization called Meter, which evaluates the ability for

**[01:34]** Meter, which evaluates the ability for

**[01:34]** Meter, which evaluates the ability for LLMs to complete a a certain set of

**[01:37]** LLMs to complete a a certain set of

**[01:37]** LLMs to complete a a certain set of tasks, and it very specifically measures

**[01:39]** tasks, and it very specifically measures

**[01:39]** tasks, and it very specifically measures the length of task that LMS can

**[01:41]** the length of task that LMS can

**[01:41]** the length of task that LMS can complete, at least with 50% um success

**[01:44]** complete, at least with 50% um success

**[01:44]** complete, at least with 50% um success rate. And so, the takeoff rate is pretty

**[01:47]** rate. And so, the takeoff rate is pretty

**[01:47]** rate. And so, the takeoff rate is pretty significant here. Um now, we think

**[01:50]** significant here. Um now, we think

**[01:50]** significant here. Um now, we think that's mostly because it's a verifiable

**[01:52]** that's mostly because it's a verifiable

**[01:52]** that's mostly because it's a verifiable domain and as we all know, model

**[01:53]** domain and as we all know, model

**[01:53]** domain and as we all know, model capabilities are a little bit jagged. So

**[01:55]** capabilities are a little bit jagged. So

**[01:55]** capabilities are a little bit jagged. So they perform very very well in software

**[01:57]** they perform very very well in software

**[01:57]** they perform very very well in software development maybe not so well in uh


### [02:00 - 03:00]

**[02:00]** development maybe not so well in uh

**[02:00]** development maybe not so well in uh non-verifiable or or more messy domains

**[02:03]** non-verifiable or or more messy domains

**[02:03]** non-verifiable or or more messy domains like knowledge work. So we think it's a

**[02:04]** like knowledge work. So we think it's a

**[02:04]** like knowledge work. So we think it's a it's a rough proxy for the coming

**[02:06]** it's a rough proxy for the coming

**[02:06]** it's a rough proxy for the coming disruption for professional services and

**[02:09]** disruption for professional services and

**[02:09]** disruption for professional services and and knowledge work more broadly. Do we

**[02:11]** and knowledge work more broadly. Do we

**[02:11]** and knowledge work more broadly. Do we think the takeoff will be as steep as

**[02:13]** think the takeoff will be as steep as

**[02:13]** think the takeoff will be as steep as software engineering? Probably not just

**[02:15]** software engineering? Probably not just

**[02:15]** software engineering? Probably not just because of the messiness of of the real

**[02:16]** because of the messiness of of the real

**[02:16]** because of the messiness of of the real world if you will. Um and for those of

**[02:19]** world if you will. Um and for those of

**[02:19]** world if you will. Um and for those of you not familiar there there's typically

**[02:21]** you not familiar there there's typically

**[02:21]** you not familiar there there's typically two main models for professional

**[02:23]** two main models for professional

**[02:23]** two main models for professional services. One is the junior le model.

**[02:25]** services. One is the junior le model.

**[02:25]** services. One is the junior le model. This is where you have very senior

**[02:27]** This is where you have very senior

**[02:27]** This is where you have very senior individuals and uh more junior

**[02:29]** individuals and uh more junior

**[02:29]** individuals and uh more junior individuals provide that leverage. So

**[02:30]** individuals provide that leverage. So

**[02:30]** individuals provide that leverage. So it's a lot of directing. Okay, do this

**[02:32]** it's a lot of directing. Okay, do this

**[02:32]** it's a lot of directing. Okay, do this and you throw 50 people at a problem and

**[02:34]** and you throw 50 people at a problem and

**[02:34]** and you throw 50 people at a problem and they kind of figure it out and probably

**[02:36]** they kind of figure it out and probably

**[02:36]** they kind of figure it out and probably waste some time in doing so. There's

**[02:38]** waste some time in doing so. There's

**[02:38]** waste some time in doing so. There's also the senior le model which is more

**[02:40]** also the senior le model which is more

**[02:40]** also the senior le model which is more senior folks who have 15 20 years of

**[02:42]** senior folks who have 15 20 years of

**[02:42]** senior folks who have 15 20 years of experience. They're much more involved

**[02:45]** experience. They're much more involved

**[02:45]** experience. They're much more involved in the day-to-day. They're actually

**[02:46]** in the day-to-day. They're actually

**[02:46]** in the day-to-day. They're actually doing the work, delivering the work.

**[02:47]** doing the work, delivering the work.

**[02:47]** doing the work, delivering the work. This is the Alex Partners model uh where

**[02:49]** This is the Alex Partners model uh where

**[02:49]** This is the Alex Partners model uh where it's a little bit less leverage um but

**[02:51]** it's a little bit less leverage um but

**[02:51]** it's a little bit less leverage um but we you know can can deliver results uh a

**[02:54]** we you know can can deliver results uh a

**[02:54]** we you know can can deliver results uh a lot faster and more more impactfully

**[02:55]** lot faster and more more impactfully

**[02:55]** lot faster and more more impactfully because it's the senior le uh folks. We

**[02:58]** because it's the senior le uh folks. We

**[02:58]** because it's the senior le uh folks. We think the future is probably somewhat of


### [03:00 - 04:00]

**[03:00]** think the future is probably somewhat of

**[03:00]** think the future is probably somewhat of a hybrid but we think because of model

**[03:03]** a hybrid but we think because of model

**[03:03]** a hybrid but we think because of model capabilities and how quickly they're

**[03:04]** capabilities and how quickly they're

**[03:04]** capabilities and how quickly they're advancing it really provides that those

**[03:07]** advancing it really provides that those

**[03:07]** advancing it really provides that those more experienced folks. people have been

**[03:09]** more experienced folks. people have been

**[03:09]** more experienced folks. people have been in a particular domain or industry for

**[03:11]** in a particular domain or industry for

**[03:11]** in a particular domain or industry for 15 20 years. Um if you've listened to

**[03:14]** 15 20 years. Um if you've listened to

**[03:14]** 15 20 years. Um if you've listened to Dwaresh Patel and his podcast, fantastic

**[03:17]** Dwaresh Patel and his podcast, fantastic

**[03:17]** Dwaresh Patel and his podcast, fantastic podcast, he has this concept of an AI

**[03:19]** podcast, he has this concept of an AI

**[03:19]** podcast, he has this concept of an AI first firm where you can basically take

**[03:21]** first firm where you can basically take

**[03:21]** first firm where you can basically take the knowledge and start to replicate

**[03:22]** the knowledge and start to replicate

**[03:22]** the knowledge and start to replicate that out. So you can have 50 copies of

**[03:24]** that out. So you can have 50 copies of

**[03:24]** that out. So you can have 50 copies of the CEO as an example. We think the

**[03:26]** the CEO as an example. We think the

**[03:26]** the CEO as an example. We think the future is something like that where you

**[03:27]** future is something like that where you

**[03:28]** future is something like that where you have you're basically replicating the

**[03:30]** have you're basically replicating the

**[03:30]** have you're basically replicating the knowledge experience of more senior

**[03:32]** knowledge experience of more senior

**[03:32]** knowledge experience of more senior individuals and you provide and you

**[03:34]** individuals and you provide and you

**[03:34]** individuals and you provide and you scale out that leverage below using AI

**[03:36]** scale out that leverage below using AI

**[03:36]** scale out that leverage below using AI to do so.

**[03:38]** to do so.

**[03:38]** to do so. And so the way we think about typical

**[03:40]** And so the way we think about typical

**[03:40]** And so the way we think about typical engagements, um it's really it roughly

**[03:43]** engagements, um it's really it roughly

**[03:43]** engagements, um it's really it roughly falls into these three different

**[03:44]** falls into these three different

**[03:44]** falls into these three different buckets. Not always, but for just for

**[03:45]** buckets. Not always, but for just for

**[03:46]** buckets. Not always, but for just for demonstration purposes, there's a lot of

**[03:47]** demonstration purposes, there's a lot of

**[03:48]** demonstration purposes, there's a lot of upfront work initially. Um whether it's

**[03:50]** upfront work initially. Um whether it's

**[03:50]** upfront work initially. Um whether it's an M&A transaction, a corporate

**[03:52]** an M&A transaction, a corporate

**[03:52]** an M&A transaction, a corporate investigation, some type of due

**[03:54]** investigation, some type of due

**[03:54]** investigation, some type of due diligence. Oftentimes, you're left with

**[03:56]** diligence. Oftentimes, you're left with

**[03:56]** diligence. Oftentimes, you're left with a bunch of PDFs, databases, Excels,

**[03:59]** a bunch of PDFs, databases, Excels,

**[03:59]** a bunch of PDFs, databases, Excels, whatever it might be. There's just a lot


### [04:00 - 05:00]

**[04:00]** whatever it might be. There's just a lot

**[04:00]** whatever it might be. There's just a lot of upfront work to just understand what

**[04:03]** of upfront work to just understand what

**[04:03]** of upfront work to just understand what you've got, right? just ingest the data,

**[04:06]** you've got, right? just ingest the data,

**[04:06]** you've got, right? just ingest the data, normalize it, categorize things, put it

**[04:08]** normalize it, categorize things, put it

**[04:08]** normalize it, categorize things, put it into a framework that you can then use

**[04:11]** into a framework that you can then use

**[04:11]** into a framework that you can then use to do what you do best, which what

**[04:13]** to do what you do best, which what

**[04:13]** to do what you do best, which what whatever that might be. If you're a

**[04:14]** whatever that might be. If you're a

**[04:14]** whatever that might be. If you're a private equity equity expert or

**[04:16]** private equity equity expert or

**[04:16]** private equity equity expert or investigator, whatever it is, you

**[04:18]** investigator, whatever it is, you

**[04:18]** investigator, whatever it is, you typically have some type of playbook,

**[04:20]** typically have some type of playbook,

**[04:20]** typically have some type of playbook, and that's phase phase two, which is the

**[04:22]** and that's phase phase two, which is the

**[04:22]** and that's phase phase two, which is the black part, which is the analysis, the

**[04:24]** black part, which is the analysis, the

**[04:24]** black part, which is the analysis, the hypothesis generation. You're basically

**[04:26]** hypothesis generation. You're basically

**[04:26]** hypothesis generation. You're basically getting all that data into a format that

**[04:28]** getting all that data into a format that

**[04:28]** getting all that data into a format that then you can you can take and use um and

**[04:31]** then you can you can take and use um and

**[04:31]** then you can you can take and use um and derive some type of insights from. And

**[04:33]** derive some type of insights from. And

**[04:33]** derive some type of insights from. And all of that, of course, is in support of

**[04:35]** all of that, of course, is in support of

**[04:35]** all of that, of course, is in support of the the last piece, which is really what

**[04:37]** the the last piece, which is really what

**[04:37]** the the last piece, which is really what what clients actually care about, which

**[04:39]** what clients actually care about, which

**[04:39]** what clients actually care about, which is you solving their business problem.

**[04:41]** is you solving their business problem.

**[04:41]** is you solving their business problem. That's the recommendation, the

**[04:43]** That's the recommendation, the

**[04:43]** That's the recommendation, the deliverable, the output, whatever that

**[04:45]** deliverable, the output, whatever that

**[04:45]** deliverable, the output, whatever that might be that that's the reason that

**[04:46]** might be that that's the reason that

**[04:46]** might be that that's the reason that they've hired you in the first place.

**[04:48]** they've hired you in the first place.

**[04:48]** they've hired you in the first place. We're seeing AI today just significantly

**[04:51]** We're seeing AI today just significantly

**[04:51]** We're seeing AI today just significantly compressing at at minimum the that first

**[04:53]** compressing at at minimum the that first

**[04:53]** compressing at at minimum the that first part. So if if it was 50%, maybe it's 10

**[04:57]** part. So if if it was 50%, maybe it's 10

**[04:57]** part. So if if it was 50%, maybe it's 10 to to 20% today in terms of what's

**[04:59]** to to 20% today in terms of what's

**[04:59]** to to 20% today in terms of what's required from a human perspective just


### [05:00 - 06:00]

**[05:02]** required from a human perspective just

**[05:02]** required from a human perspective just to get up to speed about understanding

**[05:03]** to get up to speed about understanding

**[05:03]** to get up to speed about understanding the contents of a data room or whatever

**[05:05]** the contents of a data room or whatever

**[05:05]** the contents of a data room or whatever it might be.

**[05:07]** it might be.

**[05:07]** it might be. And it's not only that because to the to

**[05:10]** And it's not only that because to the to

**[05:10]** And it's not only that because to the to date you're largely limited by the

**[05:12]** date you're largely limited by the

**[05:12]** date you're largely limited by the throughput of human beings. So you think

**[05:13]** throughput of human beings. So you think

**[05:14]** throughput of human beings. So you think of Doc Review as an example. If you have

**[05:16]** of Doc Review as an example. If you have

**[05:16]** of Doc Review as an example. If you have 5,000 different contracts, Box is a

**[05:19]** 5,000 different contracts, Box is a

**[05:19]** 5,000 different contracts, Box is a perfect um um precursor to this talk

**[05:21]** perfect um um precursor to this talk

**[05:21]** perfect um um precursor to this talk because that's exactly what they do. Um,

**[05:24]** because that's exactly what they do. Um,

**[05:24]** because that's exactly what they do. Um, if you have 5,000 contracts, think of

**[05:26]** if you have 5,000 contracts, think of

**[05:26]** if you have 5,000 contracts, think of how many people it would take if it

**[05:28]** how many people it would take if it

**[05:28]** how many people it would take if it takes 30 minutes to review each and

**[05:30]** takes 30 minutes to review each and

**[05:30]** takes 30 minutes to review each and every contract. You have 5,000 of them,

**[05:32]** every contract. You have 5,000 of them,

**[05:32]** every contract. You have 5,000 of them, you want to extract some type of

**[05:33]** you want to extract some type of

**[05:33]** you want to extract some type of information from it. You're inher

**[05:35]** information from it. You're inher

**[05:35]** information from it. You're inher inherently limited by either time or

**[05:37]** inherently limited by either time or

**[05:37]** inherently limited by either time or cost. And so, inevitably, there's some

**[05:39]** cost. And so, inevitably, there's some

**[05:39]** cost. And so, inevitably, there's some type of prioritization that occurs.

**[05:41]** type of prioritization that occurs.

**[05:41]** type of prioritization that occurs. You're only focusing on kind of the top

**[05:43]** You're only focusing on kind of the top

**[05:43]** You're only focusing on kind of the top 20% or whatever it might be, the most

**[05:45]** 20% or whatever it might be, the most

**[05:45]** 20% or whatever it might be, the most valuable um pieces of the data. With AI,

**[05:48]** valuable um pieces of the data. With AI,

**[05:48]** valuable um pieces of the data. With AI, that's completely changed, right? You

**[05:50]** that's completely changed, right? You

**[05:50]** that's completely changed, right? You can now look at 100% of the corpus of

**[05:52]** can now look at 100% of the corpus of

**[05:52]** can now look at 100% of the corpus of data, whatever that might be, and you

**[05:54]** data, whatever that might be, and you

**[05:54]** data, whatever that might be, and you can start to derive insights. You can

**[05:56]** can start to derive insights. You can

**[05:56]** can start to derive insights. You can apply your same methodology, your

**[05:58]** apply your same methodology, your

**[05:58]** apply your same methodology, your analysis, your insights to all of the


### [06:00 - 07:00]

**[06:00]** analysis, your insights to all of the

**[06:00]** analysis, your insights to all of the data. Now, because you're able to

**[06:02]** data. Now, because you're able to

**[06:02]** data. Now, because you're able to extract that information from across

**[06:04]** extract that information from across

**[06:04]** extract that information from across 100% of the data set. So now you can

**[06:06]** 100% of the data set. So now you can

**[06:06]** 100% of the data set. So now you can look at 100% of the vendor contracts,

**[06:08]** look at 100% of the vendor contracts,

**[06:08]** look at 100% of the vendor contracts, 100% of the customer base. You can start

**[06:11]** 100% of the customer base. You can start

**[06:11]** 100% of the customer base. You can start to derive those insights to identify

**[06:13]** to derive those insights to identify

**[06:13]** to derive those insights to identify savings opportunities, free up time to

**[06:15]** savings opportunities, free up time to

**[06:15]** savings opportunities, free up time to do more interviews, whatever it might

**[06:17]** do more interviews, whatever it might

**[06:17]** do more interviews, whatever it might be. you're freed up to do much more

**[06:19]** be. you're freed up to do much more

**[06:19]** be. you're freed up to do much more highv value work and the value is that

**[06:21]** highv value work and the value is that

**[06:21]** highv value work and the value is that because it's done across 100% of the

**[06:24]** because it's done across 100% of the

**[06:24]** because it's done across 100% of the data instead of just the first 20 or so

**[06:26]** data instead of just the first 20 or so

**[06:26]** data instead of just the first 20 or so percent the output is just that much

**[06:27]** percent the output is just that much

**[06:27]** percent the output is just that much better so to bring to life a little bit

**[06:29]** better so to bring to life a little bit

**[06:29]** better so to bring to life a little bit I'll turn it over to Mo to talk through

**[06:31]** I'll turn it over to Mo to talk through

**[06:31]** I'll turn it over to Mo to talk through some real life examples thanks Kevin

**[06:38]** so to motivate the use cases that we

**[06:38]** so to motivate the use cases that we have I want to start with the paradox

**[06:40]** have I want to start with the paradox

**[06:40]** have I want to start with the paradox that we face um everyone's investing in

**[06:42]** that we face um everyone's investing in

**[06:42]** that we face um everyone's investing in AI 89% of CEOs said that uh they're

**[06:45]** AI 89% of CEOs said that uh they're

**[06:45]** AI 89% of CEOs said that uh they're imple planning to implement agent

**[06:47]** imple planning to implement agent

**[06:47]** imple planning to implement agent authentic AI according to deote but we

**[06:50]** authentic AI according to deote but we

**[06:50]** authentic AI according to deote but we find ourselves in this paradox where uh

**[06:52]** find ourselves in this paradox where uh

**[06:52]** find ourselves in this paradox where uh national bureau of economic research

**[06:54]** national bureau of economic research

**[06:54]** national bureau of economic research says that there's been no significant

**[06:55]** says that there's been no significant

**[06:55]** says that there's been no significant impact on earnings or recorded hours

**[06:58]** impact on earnings or recorded hours

**[06:58]** impact on earnings or recorded hours BCG says that threequarters of company


### [07:00 - 08:00]

**[07:01]** BCG says that threequarters of company

**[07:01]** BCG says that threequarters of company failed to struggle and achieve and scale

**[07:02]** failed to struggle and achieve and scale

**[07:02]** failed to struggle and achieve and scale value with their geni initiatives and

**[07:05]** value with their geni initiatives and

**[07:05]** value with their geni initiatives and then finally S&P global said that almost

**[07:08]** then finally S&P global said that almost

**[07:08]** then finally S&P global said that almost half the uh companies were abandoning

**[07:10]** half the uh companies were abandoning

**[07:10]** half the uh companies were abandoning their AI initiatives this year so how is

**[07:13]** their AI initiatives this year so how is

**[07:13]** their AI initiatives this year so how is it that everyone's spending but no one's

**[07:15]** it that everyone's spending but no one's

**[07:15]** it that everyone's spending but no one's seeing the you. We think there's a

**[07:17]** seeing the you. We think there's a

**[07:18]** seeing the you. We think there's a difference between employee productivity

**[07:19]** difference between employee productivity

**[07:19]** difference between employee productivity and enterprise productivity. And so we

**[07:21]** and enterprise productivity. And so we

**[07:21]** and enterprise productivity. And so we want to talk about the use cases that we

**[07:22]** want to talk about the use cases that we

**[07:22]** want to talk about the use cases that we found that help drive enterprise

**[07:24]** found that help drive enterprise

**[07:24]** found that help drive enterprise productivity.

**[07:27]** productivity.

**[07:27]** productivity. So the first example I want to start

**[07:29]** So the first example I want to start

**[07:29]** So the first example I want to start with is categorization.

**[07:31]** with is categorization.

**[07:31]** with is categorization. Maybe trying to put a square peg in a

**[07:33]** Maybe trying to put a square peg in a

**[07:33]** Maybe trying to put a square peg in a round hole. How does this show up for

**[07:36]** round hole. How does this show up for

**[07:36]** round hole. How does this show up for us? Um think if you have IT support

**[07:39]** us? Um think if you have IT support

**[07:39]** us? Um think if you have IT support tickets, you laptop keeps restarting and

**[07:41]** tickets, you laptop keeps restarting and

**[07:41]** tickets, you laptop keeps restarting and that needs to be triaged to the hardware

**[07:43]** that needs to be triaged to the hardware

**[07:43]** that needs to be triaged to the hardware department. um you need to categorize

**[07:45]** department. um you need to categorize

**[07:45]** department. um you need to categorize those tickets accordingly. Something

**[07:47]** those tickets accordingly. Something

**[07:47]** those tickets accordingly. Something closer to home uh is we analyze

**[07:50]** closer to home uh is we analyze

**[07:50]** closer to home uh is we analyze companies a lot and so we want to look

**[07:51]** companies a lot and so we want to look

**[07:52]** companies a lot and so we want to look at accounts payables or spend data

**[07:54]** at accounts payables or spend data

**[07:54]** at accounts payables or spend data across companies and we need to say what

**[07:56]** across companies and we need to say what

**[07:56]** across companies and we need to say what is United Airlines if it's under travel.

**[07:59]** is United Airlines if it's under travel.


### [08:00 - 09:00]

**[08:00]** is United Airlines if it's under travel. How was this done before?

**[08:02]** How was this done before?

**[08:02]** How was this done before? Does anyone remember word clouds? You'd

**[08:04]** Does anyone remember word clouds? You'd

**[08:04]** Does anyone remember word clouds? You'd have to build a machine learning model.

**[08:06]** have to build a machine learning model.

**[08:06]** have to build a machine learning model. You'd have to stem your data, remove

**[08:09]** You'd have to stem your data, remove

**[08:09]** You'd have to stem your data, remove stop words, um, build a classifier,

**[08:12]** stop words, um, build a classifier,

**[08:12]** stop words, um, build a classifier, support vector machines, naive bays.

**[08:14]** support vector machines, naive bays.

**[08:14]** support vector machines, naive bays. It's a lot of work.

**[08:17]** It's a lot of work.

**[08:17]** It's a lot of work. Enter the new way, structured outputs.

**[08:20]** Enter the new way, structured outputs.

**[08:20]** Enter the new way, structured outputs. So with structured outputs, you can get

**[08:22]** So with structured outputs, you can get

**[08:22]** So with structured outputs, you can get the answer a lot easier. This is

**[08:23]** the answer a lot easier. This is

**[08:23]** the answer a lot easier. This is unsupervised learning. Uh, this is

**[08:25]** unsupervised learning. Uh, this is

**[08:25]** unsupervised learning. Uh, this is literally what that would look like. Say

**[08:27]** literally what that would look like. Say

**[08:27]** literally what that would look like. Say you have a list of companies, JD

**[08:29]** you have a list of companies, JD

**[08:29]** you have a list of companies, JD factors, and you have to categorize it

**[08:30]** factors, and you have to categorize it

**[08:30]** factors, and you have to categorize it into a taxonomy. Here the taxonomy would

**[08:33]** into a taxonomy. Here the taxonomy would

**[08:33]** into a taxonomy. Here the taxonomy would be the North American industry

**[08:34]** be the North American industry

**[08:34]** be the North American industry classification system. The NICS codes

**[08:37]** classification system. The NICS codes

**[08:37]** classification system. The NICS codes each code has a description. Uh and in

**[08:39]** each code has a description. Uh and in

**[08:39]** each code has a description. Uh and in this case it would be other cache

**[08:41]** this case it would be other cache

**[08:41]** this case it would be other cache management. For instance, uh typically

**[08:44]** management. For instance, uh typically

**[08:44]** management. For instance, uh typically JD factors is probably not part of the

**[08:46]** JD factors is probably not part of the

**[08:46]** JD factors is probably not part of the foundational model's knowledge. So how

**[08:48]** foundational model's knowledge. So how

**[08:48]** foundational model's knowledge. So how do we ensure that the classification

**[08:50]** do we ensure that the classification

**[08:50]** do we ensure that the classification works? Well, enter tool call. You can

**[08:53]** works? Well, enter tool call. You can

**[08:53]** works? Well, enter tool call. You can run a web query to append information to

**[08:56]** run a web query to append information to

**[08:56]** run a web query to append information to each of these pieces of uh to each of

**[08:57]** each of these pieces of uh to each of

**[08:57]** each of these pieces of uh to each of these companies and then categorize

**[08:59]** these companies and then categorize

**[08:59]** these companies and then categorize enormous volumes. Uh so this is what


### [09:00 - 10:00]

**[09:02]** enormous volumes. Uh so this is what

**[09:02]** enormous volumes. Uh so this is what we've been doing and we found that we've

**[09:04]** we've been doing and we found that we've

**[09:04]** we've been doing and we found that we've had huge wins from this. So uh what this

**[09:08]** had huge wins from this. So uh what this

**[09:08]** had huge wins from this. So uh what this has done is this democratized access to

**[09:09]** has done is this democratized access to

**[09:10]** has done is this democratized access to text classification for us.

**[09:13]** text classification for us.

**[09:13]** text classification for us. I want to talk about the the learnings

**[09:15]** I want to talk about the the learnings

**[09:15]** I want to talk about the the learnings that we've had from uh deploying this

**[09:17]** that we've had from uh deploying this

**[09:17]** that we've had from uh deploying this surgically at our company. Enomous wins

**[09:20]** surgically at our company. Enomous wins

**[09:20]** surgically at our company. Enomous wins in speed and accuracy those accuracy

**[09:22]** in speed and accuracy those accuracy

**[09:22]** in speed and accuracy those accuracy gains have not come cheaply. Uh this

**[09:25]** gains have not come cheaply. Uh this

**[09:25]** gains have not come cheaply. Uh this might be unsupervised learning but it's

**[09:27]** might be unsupervised learning but it's

**[09:27]** might be unsupervised learning but it's not unchecked. We've had to have the

**[09:29]** not unchecked. We've had to have the

**[09:29]** not unchecked. We've had to have the right relationships with the business

**[09:30]** right relationships with the business

**[09:30]** right relationships with the business partners who've worked handinhand with

**[09:32]** partners who've worked handinhand with

**[09:32]** partners who've worked handinhand with us to ensure that we get to the accuracy

**[09:33]** us to ensure that we get to the accuracy

**[09:33]** us to ensure that we get to the accuracy that we wanted. What this does is

**[09:36]** that we wanted. What this does is

**[09:36]** that we wanted. What this does is converts skeptics into champions. We

**[09:38]** converts skeptics into champions. We

**[09:38]** converts skeptics into champions. We don't become snake oil salesmen pushing

**[09:40]** don't become snake oil salesmen pushing

**[09:40]** don't become snake oil salesmen pushing and peddling AI. It becomes a pull from

**[09:43]** and peddling AI. It becomes a pull from

**[09:43]** and peddling AI. It becomes a pull from the firm that's asking us, hey, can you

**[09:44]** the firm that's asking us, hey, can you

**[09:44]** the firm that's asking us, hey, can you use this or can you apply Gen AI for us

**[09:47]** use this or can you apply Gen AI for us

**[09:47]** use this or can you apply Gen AI for us in these other initiatives, which is

**[09:48]** in these other initiatives, which is

**[09:48]** in these other initiatives, which is really powerful. Um, it's important to

**[09:51]** really powerful. Um, it's important to

**[09:51]** really powerful. Um, it's important to have business context that gets embedded

**[09:53]** have business context that gets embedded

**[09:53]** have business context that gets embedded for us in those taxonomies which are

**[09:54]** for us in those taxonomies which are

**[09:54]** for us in those taxonomies which are being used for classification.

**[09:56]** being used for classification.

**[09:56]** being used for classification. Uh, everyone's talking about agents.

**[09:59]** Uh, everyone's talking about agents.

**[09:59]** Uh, everyone's talking about agents. Well, you need to get the individual


### [10:00 - 11:00]

**[10:01]** Well, you need to get the individual

**[10:01]** Well, you need to get the individual steps right correctly. And what this

**[10:02]** steps right correctly. And what this

**[10:02]** steps right correctly. And what this does is it builds that individual step

**[10:04]** does is it builds that individual step

**[10:04]** does is it builds that individual step to a high level of robustness and

**[10:06]** to a high level of robustness and

**[10:06]** to a high level of robustness and accuracy that we can daisy chain into

**[10:07]** accuracy that we can daisy chain into

**[10:08]** accuracy that we can daisy chain into the agentic workflows that we want. And

**[10:10]** the agentic workflows that we want. And

**[10:10]** the agentic workflows that we want. And finally, you know, a call out is that

**[10:12]** finally, you know, a call out is that

**[10:12]** finally, you know, a call out is that these results are stoastic and not

**[10:13]** these results are stoastic and not

**[10:13]** these results are stoastic and not necessarily uh deterministic. That comes

**[10:16]** necessarily uh deterministic. That comes

**[10:16]** necessarily uh deterministic. That comes with some risks. Kevin will talk more

**[10:18]** with some risks. Kevin will talk more

**[10:18]** with some risks. Kevin will talk more about those.

**[10:20]** about those.

**[10:20]** about those. Punch line here. We've we've been able

**[10:21]** Punch line here. We've we've been able

**[10:21]** Punch line here. We've we've been able to achieve 95% accuracy across 10,000

**[10:24]** to achieve 95% accuracy across 10,000

**[10:24]** to achieve 95% accuracy across 10,000 categorizing 10,000 vendors. Uh doing in

**[10:27]** categorizing 10,000 vendors. Uh doing in

**[10:27]** categorizing 10,000 vendors. Uh doing in minutes what would have taken days at an

**[10:29]** minutes what would have taken days at an

**[10:29]** minutes what would have taken days at an order of magnitude less cost.

**[10:32]** order of magnitude less cost.

**[10:32]** order of magnitude less cost. All right, next use case. Uh this

**[10:34]** All right, next use case. Uh this

**[10:34]** All right, next use case. Uh this wouldn't be an AI conference if we

**[10:35]** wouldn't be an AI conference if we

**[10:35]** wouldn't be an AI conference if we didn't talk about rag. So what do we how

**[10:38]** didn't talk about rag. So what do we how

**[10:38]** didn't talk about rag. So what do we how do we how do we uh see rag at our firm?

**[10:41]** do we how do we uh see rag at our firm?

**[10:41]** do we how do we uh see rag at our firm? You get dumped with a bunch of data.

**[10:43]** You get dumped with a bunch of data.

**[10:43]** You get dumped with a bunch of data. Here's 80 gigs of internal documents.

**[10:45]** Here's 80 gigs of internal documents.

**[10:45]** Here's 80 gigs of internal documents. What did Acme release in 2020? Uh let's

**[10:47]** What did Acme release in 2020? Uh let's

**[10:47]** What did Acme release in 2020? Uh let's say you got a court filing that you have

**[10:49]** say you got a court filing that you have

**[10:50]** say you got a court filing that you have to submit on Monday and it's Friday. You

**[10:52]** to submit on Monday and it's Friday. You

**[10:52]** to submit on Monday and it's Friday. You know, you might get asked a question,

**[10:53]** know, you might get asked a question,

**[10:53]** know, you might get asked a question, what is Acme's escalation procedures for

**[10:55]** what is Acme's escalation procedures for

**[10:55]** what is Acme's escalation procedures for reporting safety violations?

**[10:57]** reporting safety violations?

**[10:57]** reporting safety violations? How do we do this? In the past, you'd

**[10:58]** How do we do this? In the past, you'd

**[10:58]** How do we do this? In the past, you'd have an index, a literal index. Someone


### [11:00 - 12:00]

**[11:01]** have an index, a literal index. Someone

**[11:01]** have an index, a literal index. Someone would say in an Excel file, what

**[11:02]** would say in an Excel file, what

**[11:02]** would say in an Excel file, what documents have been received? What

**[11:04]** documents have been received? What

**[11:04]** documents have been received? What documents haven't been received? And

**[11:05]** documents haven't been received? And

**[11:05]** documents haven't been received? And where are they? Uh or uh hope not, but

**[11:08]** where are they? Uh or uh hope not, but

**[11:08]** where are they? Uh or uh hope not, but maybe you'd use search and you have

**[11:10]** maybe you'd use search and you have

**[11:10]** maybe you'd use search and you have SharePoint search or something like that

**[11:12]** SharePoint search or something like that

**[11:12]** SharePoint search or something like that that uh probably wouldn't find you what

**[11:14]** that uh probably wouldn't find you what

**[11:14]** that uh probably wouldn't find you what you're looking for. Well, what do we do

**[11:16]** you're looking for. Well, what do we do

**[11:16]** you're looking for. Well, what do we do now? We have an enterprise scale rag

**[11:17]** now? We have an enterprise scale rag

**[11:18]** now? We have an enterprise scale rag app. It has to handle hundreds of

**[11:19]** app. It has to handle hundreds of

**[11:19]** app. It has to handle hundreds of gigabytes of data uh powerpoints,

**[11:22]** gigabytes of data uh powerpoints,

**[11:22]** gigabytes of data uh powerpoints, documents, Excel, CSVs, all sorts of

**[11:24]** documents, Excel, CSVs, all sorts of

**[11:24]** documents, Excel, CSVs, all sorts of formats, uh and and huge volumes. What

**[11:28]** formats, uh and and huge volumes. What

**[11:28]** formats, uh and and huge volumes. What can you append to that? You can append

**[11:29]** can you append to that? You can append

**[11:29]** can you append to that? You can append tool calls to third party proprietary

**[11:31]** tool calls to third party proprietary

**[11:31]** tool calls to third party proprietary databases. Let let me talk about that

**[11:33]** databases. Let let me talk about that

**[11:33]** databases. Let let me talk about that for a second. What are the trade-offs

**[11:35]** for a second. What are the trade-offs

**[11:35]** for a second. What are the trade-offs that we've had? Sorry, I'm going really

**[11:37]** that we've had? Sorry, I'm going really

**[11:37]** that we've had? Sorry, I'm going really fast, short on time. Um the the wins and

**[11:40]** fast, short on time. Um the the wins and

**[11:40]** fast, short on time. Um the the wins and the losses. So it's been rag is

**[11:43]** the losses. So it's been rag is

**[11:43]** the losses. So it's been rag is invaluable at at consulting companies

**[11:45]** invaluable at at consulting companies

**[11:45]** invaluable at at consulting companies because you get dumped on a project

**[11:46]** because you get dumped on a project

**[11:46]** because you get dumped on a project really quick and you have to get up to

**[11:47]** really quick and you have to get up to

**[11:47]** really quick and you have to get up to speed. So uh ends up being really

**[11:49]** speed. So uh ends up being really

**[11:49]** speed. So uh ends up being really valuable. Uh but I want to call out the

**[11:52]** valuable. Uh but I want to call out the

**[11:52]** valuable. Uh but I want to call out the teaching LLM APIs part. Um typically

**[11:55]** teaching LLM APIs part. Um typically

**[11:55]** teaching LLM APIs part. Um typically certain data sources would be siloed

**[11:58]** certain data sources would be siloed

**[11:58]** certain data sources would be siloed behind organizations that had licenses


### [12:00 - 13:00]

**[12:00]** behind organizations that had licenses

**[12:00]** behind organizations that had licenses that would have to pull information from

**[12:02]** that would have to pull information from

**[12:02]** that would have to pull information from a web UI that would then be emailed to a

**[12:04]** a web UI that would then be emailed to a

**[12:04]** a web UI that would then be emailed to a certain to a certain team and then that

**[12:06]** certain to a certain team and then that

**[12:06]** certain to a certain team and then that team would analyze the Excel. Well, what

**[12:08]** team would analyze the Excel. Well, what

**[12:08]** team would analyze the Excel. Well, what we did was we took the API spec,

**[12:10]** we did was we took the API spec,

**[12:10]** we did was we took the API spec, embedded it, and taught the LLM how to

**[12:12]** embedded it, and taught the LLM how to

**[12:12]** embedded it, and taught the LLM how to call an API. We have democratized access

**[12:14]** call an API. We have democratized access

**[12:14]** call an API. We have democratized access to information that would otherwise have

**[12:15]** to information that would otherwise have

**[12:15]** to information that would otherwise have taken days for people to use. Really

**[12:17]** taken days for people to use. Really

**[12:17]** taken days for people to use. Really condensing the time as Kevin said before

**[12:19]** condensing the time as Kevin said before

**[12:19]** condensing the time as Kevin said before in some of the projects on the highv

**[12:21]** in some of the projects on the highv

**[12:21]** in some of the projects on the highv value work. Uh the last thing to call

**[12:22]** value work. Uh the last thing to call

**[12:22]** value work. Uh the last thing to call out about rag is that it serves as a

**[12:25]** out about rag is that it serves as a

**[12:25]** out about rag is that it serves as a substrate on which you can tack on a a

**[12:27]** substrate on which you can tack on a a

**[12:27]** substrate on which you can tack on a a number of geni features that's proven

**[12:28]** number of geni features that's proven

**[12:28]** number of geni features that's proven really valuable for us at our firm. Uh

**[12:31]** really valuable for us at our firm. Uh

**[12:31]** really valuable for us at our firm. Uh number of call outs, you know, people

**[12:32]** number of call outs, you know, people

**[12:32]** number of call outs, you know, people have high expectations on what they what

**[12:34]** have high expectations on what they what

**[12:34]** have high expectations on what they what they want to receive from a a prompt

**[12:36]** they want to receive from a a prompt

**[12:36]** they want to receive from a a prompt box. If you say reason across all

**[12:37]** box. If you say reason across all

**[12:38]** box. If you say reason across all documents, that's just not how Rag

**[12:39]** documents, that's just not how Rag

**[12:39]** documents, that's just not how Rag works. So we have to build those

**[12:41]** works. So we have to build those

**[12:41]** works. So we have to build those solutions step by step and it's a long

**[12:42]** solutions step by step and it's a long

**[12:42]** solutions step by step and it's a long journey that we have to go on and we're

**[12:44]** journey that we have to go on and we're

**[12:44]** journey that we have to go on and we're excited to be on it. With that, over to

**[12:46]** excited to be on it. With that, over to

**[12:46]** excited to be on it. With that, over to Kevin in the third use case. Yeah. Oh,

**[12:48]** Kevin in the third use case. Yeah. Oh,

**[12:48]** Kevin in the third use case. Yeah. Oh, thanks. Um, so it's a good thing Box

**[12:50]** thanks. Um, so it's a good thing Box

**[12:50]** thanks. Um, so it's a good thing Box went before us because they covered a

**[12:52]** went before us because they covered a

**[12:52]** went before us because they covered a lot of the advantages of the the ability

**[12:54]** lot of the advantages of the the ability

**[12:54]** lot of the advantages of the the ability fundamentally to take unstructured data

**[12:57]** fundamentally to take unstructured data

**[12:57]** fundamentally to take unstructured data and create structure from that. It it is

**[12:59]** and create structure from that. It it is

**[12:59]** and create structure from that. It it is an unbelievably powerful concept. It's


### [13:00 - 14:00]

**[13:01]** an unbelievably powerful concept. It's

**[13:01]** an unbelievably powerful concept. It's it's very simple on its face, but it is

**[13:03]** it's very simple on its face, but it is

**[13:03]** it's very simple on its face, but it is incredibly powerful in an enterprise

**[13:04]** incredibly powerful in an enterprise

**[13:04]** incredibly powerful in an enterprise context because you can take something

**[13:06]** context because you can take something

**[13:06]** context because you can take something like this credit agreement. It's 50 or

**[13:08]** like this credit agreement. It's 50 or

**[13:08]** like this credit agreement. It's 50 or so pages long in terms of a PDF and you

**[13:11]** so pages long in terms of a PDF and you

**[13:11]** so pages long in terms of a PDF and you can very quickly extract information

**[13:13]** can very quickly extract information

**[13:13]** can very quickly extract information that's useful like contract parties,

**[13:15]** that's useful like contract parties,

**[13:15]** that's useful like contract parties, maturity date, senior lenders, whoever

**[13:17]** maturity date, senior lenders, whoever

**[13:17]** maturity date, senior lenders, whoever that might be. Um, and so you see folks

**[13:20]** that might be. Um, and so you see folks

**[13:20]** that might be. Um, and so you see folks like Jason Lou, Pinantic is all you

**[13:22]** like Jason Lou, Pinantic is all you

**[13:22]** like Jason Lou, Pinantic is all you need. It is still true. It is still all

**[13:24]** need. It is still true. It is still all

**[13:24]** need. It is still true. It is still all you need. Um, and fundamentally what

**[13:26]** you need. Um, and fundamentally what

**[13:26]** you need. Um, and fundamentally what this looks like, I box went through a

**[13:28]** this looks like, I box went through a

**[13:28]** this looks like, I box went through a lot of it, but it's combining a document

**[13:30]** lot of it, but it's combining a document

**[13:30]** lot of it, but it's combining a document with a schema with an LLM with some

**[13:33]** with a schema with an LLM with some

**[13:33]** with a schema with an LLM with some validation and scaffolding around it to

**[13:34]** validation and scaffolding around it to

**[13:34]** validation and scaffolding around it to make sure that you're pulling out the

**[13:35]** make sure that you're pulling out the

**[13:36]** make sure that you're pulling out the the values that you uh that you need.

**[13:38]** the values that you uh that you need.

**[13:38]** the values that you uh that you need. And the business value really is in the

**[13:40]** And the business value really is in the

**[13:40]** And the business value really is in the schema of what you're actually what

**[13:42]** schema of what you're actually what

**[13:42]** schema of what you're actually what you're extracting and why you're

**[13:43]** you're extracting and why you're

**[13:43]** you're extracting and why you're extracting that information. It's the

**[13:45]** extracting that information. It's the

**[13:45]** extracting that information. It's the flexibility um that is really powerful

**[13:47]** flexibility um that is really powerful

**[13:47]** flexibility um that is really powerful here because you can start to reapply it

**[13:49]** here because you can start to reapply it

**[13:49]** here because you can start to reapply it across different types of engagements.

**[13:51]** across different types of engagements.

**[13:51]** across different types of engagements. investigations might be looking at

**[13:53]** investigations might be looking at

**[13:53]** investigations might be looking at something entirely different than an M&A

**[13:55]** something entirely different than an M&A

**[13:55]** something entirely different than an M&A transaction. This fundamental capability

**[13:57]** transaction. This fundamental capability

**[13:57]** transaction. This fundamental capability can can span across all those and the

**[13:59]** can can span across all those and the

**[13:59]** can can span across all those and the power is there at the bottom where you


### [14:00 - 15:00]

**[14:01]** power is there at the bottom where you

**[14:01]** power is there at the bottom where you can do this type of thing repeatedly

**[14:03]** can do this type of thing repeatedly

**[14:03]** can do this type of thing repeatedly across multiple documents up thousands,

**[14:06]** across multiple documents up thousands,

**[14:06]** across multiple documents up thousands, tens of thousands, hundreds of thousands

**[14:07]** tens of thousands, hundreds of thousands

**[14:07]** tens of thousands, hundreds of thousands of documents where doing a human review

**[14:09]** of documents where doing a human review

**[14:09]** of documents where doing a human review might take days or weeks. Using an LLM,

**[14:12]** might take days or weeks. Using an LLM,

**[14:12]** might take days or weeks. Using an LLM, you can get it down to minutes. It's

**[14:13]** you can get it down to minutes. It's

**[14:13]** you can get it down to minutes. It's incredibly powerful. Um in terms of user

**[14:16]** incredibly powerful. Um in terms of user

**[14:16]** incredibly powerful. Um in terms of user trust, we um not only are using external

**[14:19]** trust, we um not only are using external

**[14:19]** trust, we um not only are using external sources like Box and others as well, but

**[14:21]** sources like Box and others as well, but

**[14:21]** sources like Box and others as well, but we've we've rolled our own uh internally

**[14:24]** we've we've rolled our own uh internally

**[14:24]** we've we've rolled our own uh internally as well. And so um in terms of just

**[14:27]** as well. And so um in terms of just

**[14:27]** as well. And so um in terms of just exposing some of the model internals to

**[14:29]** exposing some of the model internals to

**[14:29]** exposing some of the model internals to users to have somewhat of an off-ramp

**[14:31]** users to have somewhat of an off-ramp

**[14:31]** users to have somewhat of an off-ramp for them to understand um where the

**[14:33]** for them to understand um where the

**[14:33]** for them to understand um where the model is more or less confident, we use

**[14:35]** model is more or less confident, we use

**[14:35]** model is more or less confident, we use the log probs that's returned from the

**[14:37]** the log probs that's returned from the

**[14:37]** the log probs that's returned from the OpenAI API and we align that with the

**[14:40]** OpenAI API and we align that with the

**[14:40]** OpenAI API and we align that with the output schema from structured outputs.

**[14:42]** output schema from structured outputs.

**[14:42]** output schema from structured outputs. So we ignore all the JSON data. We

**[14:44]** So we ignore all the JSON data. We

**[14:44]** So we ignore all the JSON data. We ignore the field names themselves. We

**[14:46]** ignore the field names themselves. We

**[14:46]** ignore the field names themselves. We just home in on the values themselves.

**[14:49]** just home in on the values themselves.

**[14:49]** just home in on the values themselves. So in this case, the green box above the

**[14:51]** So in this case, the green box above the

**[14:51]** So in this case, the green box above the interest rate of LIBOR plus 1% peranom.

**[14:54]** interest rate of LIBOR plus 1% peranom.

**[14:54]** interest rate of LIBOR plus 1% peranom. That's the field that we want. We u

**[14:56]** That's the field that we want. We u

**[14:56]** That's the field that we want. We u basically take the geometric mean of the

**[14:58]** basically take the geometric mean of the

**[14:58]** basically take the geometric mean of the log props associated with those tokens


### [15:00 - 16:00]

**[15:00]** log props associated with those tokens

**[15:00]** log props associated with those tokens in particular and use that as a rough

**[15:03]** in particular and use that as a rough

**[15:03]** in particular and use that as a rough proxy of the model's confidence in

**[15:05]** proxy of the model's confidence in

**[15:05]** proxy of the model's confidence in producing that output. So the um the

**[15:08]** producing that output. So the um the

**[15:08]** producing that output. So the um the boxes way at the beginning that you saw

**[15:09]** boxes way at the beginning that you saw

**[15:09]** boxes way at the beginning that you saw in terms of green and and uh and yellow

**[15:11]** in terms of green and and uh and yellow

**[15:12]** in terms of green and and uh and yellow is a direct reflection of the confidence

**[15:13]** is a direct reflection of the confidence

**[15:13]** is a direct reflection of the confidence level. So it's a really relatively

**[15:15]** level. So it's a really relatively

**[15:15]** level. So it's a really relatively intuitive way for users to get an

**[15:17]** intuitive way for users to get an

**[15:17]** intuitive way for users to get an understanding of the model's confidence

**[15:19]** understanding of the model's confidence

**[15:19]** understanding of the model's confidence again for for human review to the extent

**[15:21]** again for for human review to the extent

**[15:21]** again for for human review to the extent that's needed. Uh I won't go through all

**[15:23]** that's needed. Uh I won't go through all

**[15:23]** that's needed. Uh I won't go through all these but fundamentally like I said it

**[15:25]** these but fundamentally like I said it

**[15:25]** these but fundamentally like I said it is magic when it works and it works at

**[15:27]** is magic when it works and it works at

**[15:27]** is magic when it works and it works at scale. It is a total unlock particularly

**[15:29]** scale. It is a total unlock particularly

**[15:29]** scale. It is a total unlock particularly for non-technical folks who are not up

**[15:31]** for non-technical folks who are not up

**[15:31]** for non-technical folks who are not up to speed with the capabilities of LLM.

**[15:33]** to speed with the capabilities of LLM.

**[15:33]** to speed with the capabilities of LLM. to be able to do this is is a light

**[15:35]** to be able to do this is is a light

**[15:35]** to be able to do this is is a light switch light bulb moment for them. Um,

**[15:37]** switch light bulb moment for them. Um,

**[15:37]** switch light bulb moment for them. Um, and it really is a gamecher. Now, uh,

**[15:39]** and it really is a gamecher. Now, uh,

**[15:39]** and it really is a gamecher. Now, uh, that being said, there's a lot of work

**[15:41]** that being said, there's a lot of work

**[15:41]** that being said, there's a lot of work to be done in terms of validation. You

**[15:43]** to be done in terms of validation. You

**[15:43]** to be done in terms of validation. You saw all the work that Box and others

**[15:44]** saw all the work that Box and others

**[15:44]** saw all the work that Box and others have done in terms of getting it to a

**[15:46]** have done in terms of getting it to a

**[15:46]** have done in terms of getting it to a level of rigor that you could that users

**[15:48]** level of rigor that you could that users

**[15:48]** level of rigor that you could that users can trust. U, and so that's really a key

**[15:51]** can trust. U, and so that's really a key

**[15:51]** can trust. U, and so that's really a key tenant for all this. And so, finally,

**[15:53]** tenant for all this. And so, finally,

**[15:53]** tenant for all this. And so, finally, uh, I'll turn it to Mo for the must

**[15:55]** uh, I'll turn it to Mo for the must

**[15:55]** uh, I'll turn it to Mo for the must haves. Ju, so just a couple quick

**[15:57]** haves. Ju, so just a couple quick

**[15:57]** haves. Ju, so just a couple quick callouts. Uh I know this is a tech

**[15:59]** callouts. Uh I know this is a tech

**[15:59]** callouts. Uh I know this is a tech conference but a lot of this to get to


### [16:00 - 17:00]

**[16:01]** conference but a lot of this to get to

**[16:01]** conference but a lot of this to get to work at the enterprise requires people

**[16:03]** work at the enterprise requires people

**[16:03]** work at the enterprise requires people skills and working closely with the

**[16:04]** skills and working closely with the

**[16:04]** skills and working closely with the organization. There are a couple things

**[16:05]** organization. There are a couple things

**[16:05]** organization. There are a couple things I want to call out that have been really

**[16:07]** I want to call out that have been really

**[16:07]** I want to call out that have been really important for us to scale our gen

**[16:08]** important for us to scale our gen

**[16:08]** important for us to scale our gen initiatives at our firm. The first one

**[16:10]** initiatives at our firm. The first one

**[16:10]** initiatives at our firm. The first one is uh demos. We we build in Streamlip

**[16:13]** is uh demos. We we build in Streamlip

**[16:13]** is uh demos. We we build in Streamlip but we uh we we prototype in Streamlip

**[16:16]** but we uh we we prototype in Streamlip

**[16:16]** but we uh we we prototype in Streamlip but we build in React. And so we have a

**[16:18]** but we build in React. And so we have a

**[16:18]** but we build in React. And so we have a constant cadence once a month that we

**[16:20]** constant cadence once a month that we

**[16:20]** constant cadence once a month that we show the latest and greatest of what

**[16:21]** show the latest and greatest of what

**[16:21]** show the latest and greatest of what we're building. This inspires the firm

**[16:23]** we're building. This inspires the firm

**[16:23]** we're building. This inspires the firm and what we're able to build and

**[16:24]** and what we're able to build and

**[16:24]** and what we're able to build and continue to invest in our uh

**[16:25]** continue to invest in our uh

**[16:25]** continue to invest in our uh initiatives. Uh and then the second

**[16:27]** initiatives. Uh and then the second

**[16:27]** initiatives. Uh and then the second thing is you know there's always the

**[16:29]** thing is you know there's always the

**[16:29]** thing is you know there's always the next shiny thing agents MCP uh the

**[16:33]** next shiny thing agents MCP uh the

**[16:33]** next shiny thing agents MCP uh the latest model uh NPS is our our metric

**[16:37]** latest model uh NPS is our our metric

**[16:37]** latest model uh NPS is our our metric ROI is our metric and that is one

**[16:39]** ROI is our metric and that is one

**[16:39]** ROI is our metric and that is one hardearned one bug fix at a time uh I'll

**[16:42]** hardearned one bug fix at a time uh I'll

**[16:42]** hardearned one bug fix at a time uh I'll skip the other one you know partnerships

**[16:43]** skip the other one you know partnerships

**[16:43]** skip the other one you know partnerships are really important it's a shared

**[16:45]** are really important it's a shared

**[16:45]** are really important it's a shared journey so and I think we're out of time

**[16:47]** journey so and I think we're out of time

**[16:47]** journey so and I think we're out of time but uh I'll leave you with this once

**[16:49]** but uh I'll leave you with this once

**[16:49]** but uh I'll leave you with this once Excel powered uh LLMs actually work we

**[16:52]** Excel powered uh LLMs actually work we

**[16:52]** Excel powered uh LLMs actually work we will be at AGI so I'm looking forward to

**[16:54]** will be at AGI so I'm looking forward to

**[16:54]** will be at AGI so I'm looking forward to that next talk thank Thank you. Thank

**[16:56]** that next talk thank Thank you. Thank

**[16:56]** that next talk thank Thank you. Thank you.


