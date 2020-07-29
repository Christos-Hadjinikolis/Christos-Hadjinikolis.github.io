---
title: AWS ML Certification 
author: Christos Hadjinikolis
layout: post
---
I recently took the [AWS Certified Machine Learning - Specialty](https://aws.amazon.com/certification/certified-machine-learning-specialty/). 
I went through a lot of work in order to adequately prepare for this exam and I can tell you that it is indeed one of 
the hardest AWS certifications. Nevertheless, with proper preparation and a bit of dedication you should be fine.

<span class="image center"><img src="{{ 'assets/images/2020-07-29-AWS-Cert.png' | relative_url }}" alt="" /></span>

## How long do I need to study for this?
Well it depends; if you are an experienced Data Scientist and have been applying Data Science for about 3+ years then an hour per day for a month should be enough. This also holds if you are an engineer already exposed to the AWS infrastructure and services but are not familiar with Data Science topics. 

You see, this certification is labelled as hard simply because it is not just about AWS services. 50% of it is concerned with purely Data Science topics; the other 50% is about AWS services that support Data Science and ML activities. If you are neither exposed to Data Science nor to the AWS services then at least 2 months of studying is recommended.    

## What does the exam cover?
Data Engineering covers 20% of the exam, then Exploratory Data Analysis concerns another 24%, modelling is 36% and Machine Learning Implementation and Operations is 20%.  

I put together a list below, in an attempt to summarise the content:
* **Data Concepts**: Deals with data preparation routines; things like: Feature selection and feature engineering, PCA, dealing with missing data or unbalanced datasets, labels and one-hot encoding as well as splitting and randomisation of data.
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
    * Simple Storage Services - S3
    * Glue
    * Athena
    * Amazon Quicksight
    * Kinesis, Streams, Firehose, Video & Analytics (S.O.S. this one ;) ) 
    * EMR with Spark
    * EC2 for ML
    * Lambda Functions
    * Step Functions
* **Amazon Serverless ML Services**: These are out-of-the-box ML solutions offered by AWS.
    * Rekognition (image/video)
    * Amazon Poly (Text-to-Speech)
    * Amazon Transcribe (Speech-to-Text)
    * Amazon Translate
    * Amazon Comprehend (Text Analysis Service)
    * Amazon Lex (Conversation Interface Service - Chatbots)
    * Amazon Service Chaining with AWS Step Functions
* **Sagemaker**: A service that you really need to spend time with!
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

Ideally I would recommend spending some time with `Sagemaker` and try to interact with services like `lambda` functions and `step-functions` as well as `Kinesis`, `Glue` and `Athena`. 
However, that would take a while to do plus, using these resources does not come for free.     

The Linux Academy Course has a number of labs that will help you develop an adequate understanding of these services. You can worry about honing your skills and knowledge at a later point. 

## How long does the exam last?
The exam consists of 65 multiple-choice, multi-selection questions. It is 3 hours long, which I think is more than enough 
to answer all questions and then review your responses (...or take a nap while waiting for your colleagues to finish; I do have a colleague who actually did this&ndash;myself I can never relax that much when it comes to exams). 

In general, AWS exams are taken at authorised exam centers. Due to the COVID-19 lockdown, this was adjusted to satisfy the high demand in exam takers and
people can take the test from home. However, the process is equally strict:
* You need to provide information about the room you will be sitting in;
* Room needs to be completely quite during the exam session;
* You need to be alone in the room;
* You need to provide pictures of your surroundings to show you have no notes or anything suspicious close to you;
* A proctor will login at the time of the exam and will ask to inspect the space around you (he asked me to show him the back of my wall prior beginning and doing so with my iMac was quite a challenge... so if you have an option go for laptop).
* The exam session will be recorded. 

Note that, as one would expect, looking away from the screen for more than a couple of seconds might prompt the proctor to give you a notice. To be honest, as soon as the exam began it was quite easy to just focus on the screen. It took me 
less than an hour to cover all questions and then used all the remaining time reviewing my responses. I received a positive notification that I passed on exam completion, but it was subject to a committee review. I guess that examiners inspect the video of 
yourself taking the exam to identify if you tried cheating or something. In no more than 3 days I got the official certification. 

## Any tips? Advice?
Well, tip number one is: "If you don't know which is the right answer, then just go for the AWS solution in the list of options". At large, this exam tests whether you are familiar with what is available to you through the AWS platform 
If a client wants to use ML for image moderation and you recommend anything other than `Rekognition` then you clearly don't know how `Rekognition` is used! This has generally worked for me as a way of filtering in and out options.  

I would definitely recommend covering the Sagemalker [FAQs](https://aws.amazon.com/sagemaker/faqs/) which I see as a wonderful source for exam material. 

Do cover the official AWS practice exam; it is just 20 questions, but it is enough to give you an idea about what you are up against. 

Finally, I have put together this [Cheat-sheet](https://github.com/Christos-Hadjinikolis/AWS-ML-cheatsheet/blob/master/README.md). It was quite useful to me and I hope that it will be to you too. Feel free to fork this repo, enrich it with additional material and issue a PR to include your changes. 

That's it! I really wish that this article will help you get started with your learning journey and I hope that soon enough you will be joining the [AWS Certified Global Community](https://www.linkedin.com/groups/6814264/) to share your badge with everyone. 

Cheers!

<blockquote class="twitter-tweet" data-theme="light"><p lang="en" dir="ltr">I successfully took the AWS Machine Learning Specialty Certification during the COVID-19 lockdown! <br><br>Here are my thoughts: <a href="https://t.co/WejGBrmDvy">https://t.co/WejGBrmDvy</a></p>&mdash; Christos Hadjinikoli (@chatzinikolis) <a href="https://twitter.com/chatzinikolis/status/1288507051824549888?ref_src=twsrc%5Etfw">July 29, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

