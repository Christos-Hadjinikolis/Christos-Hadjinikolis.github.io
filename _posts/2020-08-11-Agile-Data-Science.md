---
title: Agile Data Science
author: Christos Hadjinikolis
layout: post
---
<head>
<meta property="og:image" content="assets/images/iunera-logo-shadow.png" />
</head>
Re-posting from [https://www.iunera.com/](https://www.iunera.com/kraken/big-data-science-strategy/the-agile-approach-in-data-science-explained-by-an-ml-expert/)
Around two weeks ago I was approached by [Dr. Tim Frey](https://www.linkedin.com/in/dr-tim-frey-7b28171/), General Manager at Iunera GmbH & Co. KG. I was quite surprised to read his message:

> Hi Christos, 
> We met at the mind mastering machines conference in London.
> We operate a company blog (https://iunera.com/kraken ) and one of our writers wrote about agile in Data Science. 
> I liked your talk two years ago and I thought she can approach you to ask a few questions like kind of an in-article 
> interview with an expert. 
> Hope that is fine with you. Would be super glad to get your insights.

I must admit this was a first for me! Then again, that talk in 2018 was quite an interesting one for me too. 

## It's story time... 
You see, 3 years ago I was asked to join an exceptional team over at UBS to help with a graph analytics project. If you asked me then I would 
proudly tell you that "...I am a Data Scientist"; that is how I saw myself. However, that was bound to change forever. 

The first three months were amazing. I worked with a vast amount of data and revealed some very interesting insights. 
So, inevitably, my project manager approached me and asked "...how about we take this work of yours into production"!

<span class="image center"><img src="{{ 'assets/images/2020-08-11-agile-ds-01.png' | relative_url }}" alt="Agile Data Science" /></span>

I didn't have a clue about what that meant in reality, but I was about to find out. He said: "Well, don't worry, we will pair 
you with an engineer and you both can get started on it". So we did! 

This is basically the story about how I was exposed to software engineering and the Agile way of working&ndash;about how i was converrted into 
a ML Engineer. Two years later I decided to take my learnings from this experience and share it with my community, and so I did at mcubed London in 2018:

<iframe width="560" height="315" src="https://www.youtube.com/embed/nRsqFrutfSg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

That's where I also met Tim. Turns out that a year and half later a colleague of Tim's ([Dhanhyaashri Mahendran](https://www.linkedin.com/in/dhanhyaashri-mahendran/)) was doing a bit iof research on 
"Doing Data Science the Agile way" and Tim suggested that she gets in touch with me to ask me some questions, which I welcomed.       
                                               
## Some very interesting questions were thrown my way...
I really liked the questions that Dhanhyaashri had prepared. She had obviously done her research. I did my best to respond and two weeks later 
the interview was published on the Iunera blog. You can read it [here](https://www.iunera.com/kraken/big-data-science-strategy/the-agile-approach-in-data-science-explained-by-an-ml-expert/) 
but I also felt like re-posting the interview on my personal blog too.


**Besides the cutting of time-consuming planning and quicker turnaround of projects, what other benefits are there in applying the Agile approach in data science?**
> For the community, I would say that that would be the emergence of new Data-Science-oriented practices that will drive the application of Agile in the research domain.

> The problem with applying Agile in Data Science is that, traditionally, Agile is practiced in software development projects where experimentation, testing and tuning are minimum (usually dealt as spikes). The focus there is about delivering business requirements, in the form of features and products, fast in a volatile, constantly evolving environment. To support this, a number of underpinning practices have been developed, covering areas like modelling and design, coding and testing, risk handling and quality assurance. But all these, focus primarily on feature delivery (backlogs, user-stories, CI/CD, TDD or BDD to name a few). Some of these underpinning practices can directly be transferred in the Data Science world (e.g. user stories and backlogs, timeboxing and retrospectives) but others, not so much; for instance, how can TDD be useful when experimenting with what is the optimal k with which to cluster customer datasets? So, a clear benefit of trying to apply Agile in Data Science is that gradually, similar Data Science-specific underpinning practices will eventually be developed and these will, of course, be based on the same Agile drives: adaptive planning, evolutionary development, early delivery and continual improvement, and more generally, flexible responses to change.

> For the Data Scientists I would say it is mostly about adjusting to the requirement of working in a way to deliver business value from their experimentation.

> The feature-oriented focus that Agile is characterised by in the software development world is not so familiar to data scientists and researchers. What’s more is that "value"—business value—is perceived in very different ways across these two worlds as well. Have you ever discussed the “value” of an experiment with a project manager? Not an easy task I assure you! My experience tells me that most of the time this comes down to project managers fearing that no tangible outputs will be produced through experimentation. This is completely wrong, but only as long as experiments are well-structured and well-thought. To me, Agile Data science is all about iterative hypothesis testing. Proving or disproving a hypothesis is always useful; it minimises the risk of failure and increases decision awareness when choosing what needs to be prioritised! But these outcomes can only be achieved when Data Scientists know exactly what they are trying to prove, discover or disprove and how that would be valuable to their team’s objective. Gradually, Data Scientists become better at it and this benefits both themselves as well as their teams.   

**What are the downsides of Agile in data science? What can we do about these downsides?**
> Agile is a set of values and principles; as such, I can’t really say that there is something wrong with it. What is surely wrong is to assume that Agile is the only way that a team can work and be productive—it’s not. Ever since Agile emerged—in the concrete form that we know it today through the Agile manifesto—many hurried to undermine the effectiveness of other development models, e.g. Waterfall. 

> There is nothing wrong with the Waterfall model either; the real question is whether these practices or models are fit for purpose! There are surely research projects as well as business requirements around the delivery of software that could potentially be delivered through the Waterfall approach or maybe through a combination of the two. What project managers and teams should strive for is increasing their effectiveness and efficiency. If that can be done by building on top of the Agile values then great; if not, then maybe they will need to try and come up with a different formula. 

> Project managers focusing too much on what Agile is and what is not—if it needs to be Scrum or Kanban or if too much documentation or too much time spent in design is not Agile—are bound to make mistakes. 

**Do you think that the imposition of Agile on teams (the Agile Industrial Complex) is defeating the purpose of Agile in finding what works best for teams in working adaptively?**
> In similar spirit to my previous response, I do! Once more, I can’t stress enough how there is no single perfect development model. Project managers need to always assess what is fit for purpose. Primarily though, they should focus on the underpinning values and principles that Agile or other development models are characterised by. When they do, a recurrent mistake that I have experienced through my consulting career is the oversimplification of Agile as an anti-methodology, anti-documentation and anti-planning development model. I appreciate that this makes understanding Agile much easier, but at the same time it is a very unfair representation of what Agile is! Imposing it on this basis is surely wrong. Equally, practicing Agile is definitely not something that comes through imposition.

> I was exposed to the Agile methodology through a passionate software engineer who was an evangelist of Xtreme Programming. To him, the way he worked was a way of seeing the software engineering world and was supported by many more things than just sprints and Jira tickets and user-stories. Knowledge transferring and evolution through an unparallel team spirit and an overall culture to do things in a way that will help everyone grow (people and software) in a fast-paced and fast-evolving world. Empathy was found at the centre of everything he did and his ability to convey this passion was extreme! 

> This is because Agile is, above all, a culture—a way of thinking; a way of caring about the impact and consequences of every individual’s contribution to a team goal. When it is collectively addressed as such, then only good things can come out of it.

**Is there a possible reason for many data scientists to not be aware of the Agile manifesto?**
> I can’t be too sure about this but I if I was to point at anything, that would be how Data Science has, until recently (5 years ago), been so disjoint from the delivery of production-ready solutions. It was more focussed on research and discovery to aid decision making. Lately, the evolution and growth of ML as well as of cost-effective services to support it, necessitates the interaction of the two worlds. 

> Never before has it been so much the case that ML models are such an integral component of software. Before, Data Scientists did not need to worry about the operationalisation and maintenance of their model. Concepts like versioning, robustness, code-coverage and testing where not so much imposed or needed, let alone challenges related to things like dealing with technical debt and refactoring. The traditional work environment would be a Jupyter notebook with access to a database! So, Data Scientists did not need to be exposed to so many practices to govern how they would work to deliver new insights.       

**What kind of challenges stand in the way of operational production level DS solutions?**
> This mostly has to do with bridging the gap between software engineers and data scientists. Software engineers not exposed to data science can’t really do this because they fail to appreciate how exactly to maintain ML-pipelines. Note that in contrast to traditional software pipelines, there are many more issues that need to be addressed; I would refer your readers to the 2014, NIPS seminal paper on the “Hidden Technical Debt in Machine Learning Systems”. Equally, Data Scientists don’t appreciate the complexity of developing and maintaining code-bases and software solutions in a flexible and robust way to allow for things like CI/CD to be supported. This gap is now partially addressed through the emergence of a new paradigm: the ML engineer, a hybrid data scientist and software engineer, equipped with the knowledge to deal with challenges from both worlds. However, that is not enough to account for everything. What is also necessary is the emergence of appropriate tooling to support the development and maintenance of ML pipelines. A good example is Apache KubeFlow, AWS Sagemaker and the less mature but fast evolving Google AI platform.

> What is surely not helpful is the bad practice of finding ways to schedule and run python notebooks in production, and I purposely changed paragraphs to highlight this! I can’t stress enough how many times I have dealt with this in my career! Python notebooks are not made to be run as part of production pipelines—yet so many companies just do so!

> This is a plea to every project manager running an ML project out there: **This is madness! Please stop it!**
> <div class="tenor-gif-embed" data-postid="3413789" data-share-method="host" data-width="100%" data-aspect-ratio="2.4174757281553396"><a href="https://tenor.com/view/300-action-drama-gerard-butler-madness-gif-3413789">This. Is. Sparta! GIF</a> from <a href="https://tenor.com/search/300-gifs">300 GIFs</a></div><script type="text/javascript" async src="https://tenor.com/embed.js"></script>

**In your opinion, what is the most important factor in making ML-Ops agile?**
> I think that the answer to this question is “culture”. ML-Ops are here to help cultivate collaboration between data scientists and engineers to support the ML-lifecycle. They are a manifestation of Agile for Data Science in a way! What’s needed is for this mentality towards the development of production level ML solutions to be supported by practitioners, project managers and stakeholders the same. Everyone needs to take risks and own responsibility. Data Scientists need to develop the courage of supporting their experiments even if they may appear to delay production; they need to help stakeholders and project managers appreciate the actual value of experimentation. This will often prove to be very challenging; loss aversion will eventually kick in and when it does people will be more reluctant to change, and they will want to stick to what they know. But this is to be expected! It is natural human behaviour, and this is what we, as a community, are up against.

> At the end of the day, we need to remember that it is almost impossible to find the right balance or get it perfectly right. There is no formula for it. Nevertheless, value will come simply from trying to get it right, and that is more than enough!

Many thanks again to both Tim and Dhanhyaashri for their time and effort!

Remember to like my post and re-share (if you really liked it)!

See you soon! 

<p><a href="http://feeds.feedburner.com/MlAffairs" rel="alternate" type="application/rss+xml"><img src="//feedburner.google.com/fb/images/pub/feed-icon32x32.png" alt="" style="vertical-align:middle;border:0"/></a>&nbsp;<a href="http://feeds.feedburner.com/MlAffairs" rel="alternate" type="application/rss+xml">Register to the ML-Affairs RSS Feed</a></p>

<blockquote class="twitter-tweet" data-theme="light"><p lang="en" dir="ltr">I was recently interviewed by <a href="https://t.co/t4PaVxz4Y2">https://t.co/t4PaVxz4Y2</a> on &quot;doing data science the agile way&quot;. You can read their blog here: <a href="https://t.co/zkI9zNoEAR">https://t.co/zkI9zNoEAR</a></p>&mdash; Christos Hadjinikoli (@chatzinikolis) <a href="https://twitter.com/chatzinikolis/status/1293217047472734213?ref_src=twsrc%5Etfw">August 11, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


         
