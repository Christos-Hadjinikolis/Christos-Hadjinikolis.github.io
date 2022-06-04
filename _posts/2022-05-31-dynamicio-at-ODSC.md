---
title: Dynamic(i/o) Why you should start your ML-Ops journey with wrapping your I/O
author: Christos Hadjinikolis
layout: post
---
<head>
    <meta property="og:image" content="assets/images/2022-06-01-dynamicio.png" />
</head>

If you call yourself an ML-Engineer then you 've been there--you 've seen this before. To productionise your ml-pipeline; well, that’s surely a challenge.

<span class="image center"><img src="{{ 'assets/images/2022-06-01-dynamicio.png' | relative_url }}" alt="dynamic(i/o)" /></span>

I have worked for many years as a Data Science consultant, and I can surely confirm the statement that [“...more that 87% of Data Science projects never make it to production”](https://venturebeat.com/2019/07/19/why-do-87-of-data-science-projects-never-make-it-into-production/).
There is a reason why the first rule of doing Machine Learning is to really be sure you need to do ML! Surely, many reasons play into this challenge: 

* lack of the right leadership; 
* no or limited access to data in siloed organisations;
* lack of the necessary tooling or infrastructure support, and even;
* lack of a research-driven culture. 

But there is one more beast to be tamed out there; the gap between Data Science and ML-Engineering. And this is a gap you can perceive both in terms of the two practitioners in each 
field of work--data scientists and SWE--but also in terms of literally getting from a prototype to a production ready ML pipeline. 

<span class="image center"><img src="{{ 'assets/images/xkcd-data-answers.png' | relative_url }}" alt="xkcd - data answers" /></span>

Simply put, to put a model into production is one thing; but to maintain that model, properly monitor it to identify possible drifts and streamline the process of re-training it or updating it in a robust and 
reproducible way, supported by a clean CI/CD process, is daunting task! If anything, I 'd dare say that  ML-Engineering, as a domain, fully encapsulates SWE in addition to many more 
challenges (highly recommend reading [Hidden Technical Debt in Machine Learning Systems](https://proceedings.neurips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf)), for some of which we 
are still trying to standardise how we work in terms of best tooling or practices. 

In many cases, organisations are forced to come up with their own ways of working to accommodate the unique challenges of their custom use-cases. Then again, it all comes down to the requirements of a project. 
[Netflix has streamlined the process of putting python notebooks into production using papermil](https://netflixtechblog.com/scheduling-notebooks-348e6c14cfd6). 
Others, go as far as to standardise the whole ML-Engineering process using tools like Airflow or Kubeflow, relying on AI pipelines (on GCP) or SageMaker (on AWS), etc.

## So what do we do...?
At Vortexa, we are heavy users of Airflow and have recently embarked into a journey to include Kubeflow into our tech stack. 
As an ML-Engineer, my job usually concerns receiving a successful prototype of a model and implementing a complete end-to-end ML pipeline out of it; one that can be easily maintained
and reused. In many ways, this process is very common to a traditional SWE project, only more complex, since ML projects come with more requirements and a strong dependency on data.
Hence, it easily follows that everything one cares to implement for a SWE project needs to also be implemented for an ML-Engineering (MLE) project; and more. 

But let's start simple... 

## Here is my notebook! I am done; your turn now!  
<span class="image center"><img src="{{ 'assets/images/xkcd-data-pipelines.png' | relative_url }}" alt="xkcd - data pipelines" /></span>

So you are handed a notebook, and you inspect it; you spend time with the Data Scientist and understand all crucial aspects in the procedural logic, and you start splitting the 
process into various tasks. You, usually, end up with something like this:
<span class="image center"><img src="{{ 'assets/images/data-pipeline.png' | relative_url }}" alt="xkcd - data pipelines" /></span>

You think about the structure of your codebase, about how everything will be deployed, how you want to decouple orchestration from the logic of your ML-pipeline, and then you start thinking 
about domain driven development (DDD). You start thinking about abstractions and encapsulation, about testing and data validation. That's when it hits you&ndash;testing; you can unit test 
most things and build a robust pipeline, but you also want fast feedback for when you introduce changes and improvements to your pipeline (shifting to the left)! What if you wanted to run a 
local regression test? With all data being read from external resources (databases, object storage service) you 'll have to mock all these calls (doable, but takes time) and replace actual 
data with sample input. And, finally, what about schema and data validations? How do you guarantee after data ingestion that all your expectations on the input are respected? 

You have a look at the code again. Filled with various I/O operations. Sometimes it's `csv`, others `parquet`, and others it's `json`, sometimes you read from a database and others
from an object storage service (`s3` or `gcp`). Different libraries used to facilitate all these: `gcsfs`, `s3fs` and `fsspec`, `boto3` `sql-alchemy`, `tables`; and `pandas`, of course, sits at the core
of this process. As if that's not enough, each file comes with a series of peculiar set of requirements supported through the use of `kwargs`; in your python code: orientation of `json`
files, row-group-sizes for `parquet` files, coercions on certain timestamp columns&ndash;the list keeps going... This won't be the last time you need to do this either! 

It's just too many details&ndash;way too many details&ndash;for you to worry about. A clear violation of the dependency inversion principle:

> Business logic (high level code) should not be implemented in a way that "depends" on technical details (low level code, e.g., I/O in our case); instead both should be managed through abstractions!

You need abstractions to facilitate the flexibility to easily introduce changes. More often than not, business needs will require high-level modules to be modified. Low level code, on the 
other hand, is usually more cumbersome and difficult to change. The two should be independent; a database migration or a switch to an object storage service should have no impact on your
work to generate a new valuable feature for your model, and vice-versa. Abstracting both of these using distinct layers can achieve this! 

As David Wheeler said:
> All problems in computer science can be solved by adding a layer of indirection.

## What is `dynamicio` then?
Wouldn't it be great if you could:
* have an abstraction that encapsulates all I/O logic;
* be able to seamlessly handle reading or writing from and to different resource types or data types;
* have an interface that is easy to understand and use with minimum configuration; 
* respect your expectations on schema types and data quality;
* automatically generate metrics that would be used to leverage further insights, and more importantly;
* be able to seamlessly switch between `local`, `dev`, `staging` and `prod` environments, performing dynamic I/O against different datasets and effectively supporting development, testing and qa use cases?     

Well, `dynamic(i/o)` is exactly that; a layer of indirection for pandas I/O operations. 

If you want to find out more about it then [register to attend this year's `ODSC`](https://odsc.com/europe/) and [attend the presentation by myself and my colleague Tyler Ferguson on `dynamic(i/o)`](https://odsc.com/speakers/dynamicio-a-pandas-i-o-wrapper-why-you-should-start-your-ml-ops-journey-with-wrapping-your-i-o/). 
Come and learn about how its implementation and adoption has helped us go beyond just achieving consistency across our ML repos, effectively dealing with glue code and keeping our code-bases DRY, but also acting as an interface between different teams.

Remember to like my post and re-share it (if you really liked it)!

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Excited to be presenting at this year&#39;s <a href="https://twitter.com/hashtag/ODSCEurope?src=hash&amp;ref_src=twsrc%5Etfw">#ODSCEurope</a> on dynamicio, a brand new pandas I/O wrapper, which we intend to open source soon. read my latest blog to find out more: <a href="https://t.co/ynRvpGFVxJ">https://t.co/ynRvpGFVxJ</a> <a href="https://t.co/IkOQVC55dh">pic.twitter.com/IkOQVC55dh</a></p>&mdash; Christos Hadjinikoli (@chatzinikolis) <a href="https://twitter.com/chatzinikolis/status/1533033285433053184?ref_src=twsrc%5Etfw">June 4, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

See you soon!

<p><a href="http://feeds.feedburner.com/MlAffairs" rel="alternate" type="application/rss+xml"><img src="//feedburner.google.com/fb/images/pub/feed-icon32x32.png" alt="" style="vertical-align:middle;border:0"/></a>&nbsp;<a href="http://feeds.feedburner.com/MlAffairs" rel="alternate" type="application/rss+xml">Register to the ML-Affairs RSS Feed</a></p>   
