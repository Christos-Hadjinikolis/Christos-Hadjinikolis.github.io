---
title: AWS ML Certification 
title_html: "<span class='blog-title-accent blog-title-accent--aws'>AWS</span> ML Certification"
author: Christos Hadjinikolis
layout: post
og_image: assets/images/posts/2020/aws-ml-certification/2020-07-29-AWS-Cert.png
description: "A practical guide to the AWS Machine Learning Specialty exam, including difficulty, study scope, and how long preparation usually takes."
seo_keywords: ["AWS certification", "AWS machine learning specialty", "exam preparation", "machine learning certification", "cloud ML"]
tldr_why_read: "Useful if you are deciding whether the <span class=\"blog-highlight blog-highlight--aws\">AWS</span> <span class=\"blog-highlight blog-highlight--ml\">ML</span> Specialty is worth the effort and how to prepare for it."
tldr_persona: "Data scientists, <span class=\"blog-highlight blog-highlight--ml\">ML</span> engineers, and cloud practitioners deciding whether to invest in the <span class=\"blog-highlight blog-highlight--aws\">AWS</span> <span class=\"blog-highlight blog-highlight--ml\">ML</span> Specialty exam."
tldr_learn: "How hard the exam really is, how its topics are split, and what kind of study timeline makes sense."
tldr_takeaways: ["The exam is broad, not just <span class=\"blog-highlight blog-highlight--aws\">AWS</span> services", "Preparation time depends heavily on your background", "A structured study plan matters more than cramming"]
---
I recently took the [AWS Certified Machine Learning - Specialty](https://aws.amazon.com/certification/certified-machine-learning-specialty/), which remains one of the most demanding <span class="blog-highlight blog-highlight--aws">AWS</span> certifications. 
I went through a lot of work in order to adequately prepare for this exam and I can tell you that it is indeed one of 
the hardest <span class="blog-highlight blog-highlight--aws">AWS certifications</span>. Nevertheless, with proper preparation and a bit of dedication you should be fine.

<span class="image center"><img src="{{ 'assets/images/posts/2020/aws-ml-certification/2020-07-29-AWS-Cert.png' | relative_url }}" alt="" /></span>

## How long do I need to study for this?
Well it depends; if you are an experienced Data Scientist and have been applying Data Science for about 3+ years then an hour per day for a month should be enough. This also holds if you are an engineer already exposed to the <span class="blog-highlight blog-highlight--aws">AWS</span> infrastructure and services but are not familiar with Data Science topics. 

You see, this certification is labelled as hard simply because it is not just about <span class="blog-highlight blog-highlight--aws">AWS</span> services. 50% of it is concerned with purely Data Science topics; the other 50% is about <span class="blog-highlight blog-highlight--aws">AWS</span> services that support Data Science and <span class="blog-highlight blog-highlight--ml">ML</span> activities. If you are neither exposed to Data Science nor to the <span class="blog-highlight blog-highlight--aws">AWS</span> services then at least 2 months of studying is recommended.    

## What does the exam cover?
Data Engineering covers 20% of the exam, then Exploratory Data Analysis concerns another 24%, modelling is 36% and Machine Learning Implementation and Operations is 20%.  

I put together a list below, in an attempt to summarise the content:
* **Data Concepts**: 
    * Deals with data preparation routines; things like: 
        * Feature selection and; 
        * Feature engineering
        * PCA, 
        * dealing with missing data or unbalanced datasets, 
        * labels and one-hot encoding as well as;
        * splitting and randomisation of data.
* **ML Concepts**: Covers:
    * Classical ML Categories of Algorithms
    * Deep Learning
    * The ML-Life-cycle
    * Optimisation: Gradient Descent
    * Regularisation
    * Hyperparameter Tuning
    * Cross-Validation
    * Record I/O
* **ML Algorithms**: A list of algorithms you should be familiar with:
    * Logistic Regression
    * Linear Regression
    * Support Vector Machine
    * Decision Trees
    * Random Forests
    * K-Means
    * K-Nearest Neighbours
    * Latent Dirichlet Allocation (LDA) Algorithm
* **Deep Learning**:
    * Cover Neural Networks in a general sense
    * Convolutional Neural Networks: High-level understanding
    * Recurrent Neural Networks: High-level understanding
* **Model Optimisation**:
    * Confusion Matrix
    * Sensitivity and Specificity
    * Accuracy & Precision
    * ROC/AUC
    * Gini Impurity
    * F1-Score
* **ML Tools & Frameworks**: Cover basic ML tools (know what they do and what they are used for)
    * Jupyter Notebooks
    * Pytorch
    * MXNet
    * TensorFlow
    * Keras
    * Scikit-learn
* **Amazon Serverless Services**: Not everything; think about the things that a Data Scientist of ML engineer would need to do.
    * `Simple Storage Services - S3`
    * `Glue`
    * `Athena`
    * `Amazon Quicksight`
    * `Kinesis`, Streams, Firehose, Video & Analytics (S.O.S. this one ;) ) 
    * `EMR` with Spark
    * `EC2` for ML
    * `Lambda Functions`
    * `Step Functions`
* **Amazon Serverless ML Services**: These are out-of-the-box ML solutions offered by AWS.
    * `Rekognition` (image/video)
    * `Amazon Poly` (Text-to-Speech)
    * `Amazon Transcribe` (Speech-to-Text)
    * `Amazon Translate`
    * `Amazon Comprehend` (Text Analysis Service)
    * `Amazon Lex` (Conversation Interface Service - Chatbots)
    * `Amazon Service Chaining` with `AWS Step Functions`
* **<span class="blog-highlight blog-highlight--aws">SageMaker</span>**: A service that you really need to spend time with!
    * What is it exactly?
    * Benefits? Advantages?
    * Supported Algorithms (huge list; learn most popular ones)
    * Building and Pre-processing / Ground Truth 
    * Training and Data sourcing
    * Hyper-parameter Tuning
    * Model Servicing (Https endpoints)
    * Elastic inference
    * Batch Transform 
    
This is by no means an exhaustive list, but you will at least get an idea about what is generally involved.

## How should I prepare?
There are many ways to prepare. Myself, I covered [the relative course on Linux academy](https://linuxacademy.com/cp/modules/view/id/340), which I highly recommend. 

Ideally I would recommend spending some time with <span class="blog-highlight blog-highlight--aws">`SageMaker`</span> and try to interact with services like `lambda` functions and `step-functions` as well as `Kinesis`, `Glue` and `Athena`. 
However, that would take a while to do plus, using these resources does not come for free.     

The Linux Academy Course has a number of labs that will help you develop an adequate understanding of these services. You can worry about honing your skills and knowledge at a later point. 

## How long does the exam last?
The exam consists of 65 multiple-choice, multi-selection questions. It is 3 hours long, which I think is more than enough 
to answer all questions and then review your responses (...or take a nap while waiting for your colleagues to finish; I do have a colleague who actually did this&ndash;myself I can never relax that much when it comes to exams). 

In general, AWS exams are taken at authorised exam centers. Due to the COVID-19 lockdown, this was adjusted to satisfy the high demand in exam takers and
people can take the test from home. However, the process is equally strict:
* You need to provide information about the room you will be sitting in;
* Room needs to be completely quiet during the exam session;
* You need to be alone in the room;
* You need to provide pictures of your surroundings to show you have no notes or anything suspicious close to you;
* A proctor will login at the time of the exam and will ask to inspect the space around you (he asked me to show him the back of my computer prior beginning and doing so with my iMac was quite a challenge... so if you have an option go for laptop).
* The exam session will be recorded. 

Note that, as one would expect, looking away from the screen for more than a couple of seconds might prompt the proctor to give you a notice. To be honest, as soon as the exam began it was quite easy to just focus on the screen. It took me 
less than an hour to cover all questions and then used all the remaining time reviewing my responses. I received a positive notification that I passed on exam completion, but it was subject to a committee review. I guess that examiners inspect the video of 
yourself taking the exam to identify if you tried cheating or something. In no more than 3 days I got the official certification. 

## Any tips? Advice?
Well, tip number one is: *"If you don't know which is the right answer, then just go for the <span class="blog-highlight blog-highlight--aws">AWS</span> solution in the list of options".* At large, this exam tests whether you are familiar with what is available to you through the <span class="blog-highlight blog-highlight--aws">AWS</span> platform. If a client wants to use <span class="blog-highlight blog-highlight--ml">ML</span> for image moderation and you recommend anything other than `Rekognition` then you clearly don't know how `Rekognition` is used! This has generally worked for me as a way of filtering in and out options.  

I would definitely recommend covering the <span class="blog-highlight blog-highlight--aws">SageMaker</span> [FAQs](https://aws.amazon.com/sagemaker/faqs/) which I see as a wonderful source for exam material. 

Do cover the official AWS practice exam; it is just 20 questions, but it is enough to give you an idea about what you are up against. 

That's it! I really wish that this article will help you get started with your learning journey and I hope that soon enough you will be joining the [AWS Certified Global Community](https://www.linkedin.com/groups/6814264/) to share your badge with everyone. 

Remember to like my post and re-share it (if you really liked it)!

See you soon! 

<p><a href="http://feeds.feedburner.com/MlAffairs" rel="alternate" type="application/rss+xml"><img src="//feedburner.google.com/fb/images/pub/feed-icon32x32.png" alt="" style="vertical-align:middle;border:0"/></a>&nbsp;<a href="http://feeds.feedburner.com/MlAffairs" rel="alternate" type="application/rss+xml">Register to the ML-Affairs RSS Feed</a></p>
