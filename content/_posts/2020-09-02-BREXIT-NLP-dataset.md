---
title: A BREXIT NLP Dataset! 
title_html: "A <span class='blog-title-accent blog-title-accent--eu'>BREXIT</span> NLP Dataset!"
author: Christos Hadjinikolis
layout: post
og_image: assets/images/posts/2020/brexit-nlp-dataset/eu-brexit-classifier.png
description: "How I built a BREXIT-related NLP dataset and why real-world labeling and collection choices matter in applied NLP."
seo_keywords: ["BREXIT NLP", "NLP dataset", "text classification", "twitter data", "applied machine learning"]
tldr_why_read: "Useful if you care about how topical <span class=\"blog-highlight blog-highlight--nlp\">NLP</span> datasets get assembled outside clean benchmark settings."
tldr_persona: "Practitioners building applied <span class=\"blog-highlight blog-highlight--nlp\">NLP</span> datasets from messy real-world sources rather than benchmark-ready corpora."
tldr_learn: "How the dataset idea emerged, why labeling is the hard part, and what makes a practical <span class=\"blog-highlight blog-highlight--nlp\">NLP</span> dataset usable."
tldr_takeaways: ["Real data collection is messy", "Labeling strategy determines downstream value", "Applied <span class=\"blog-highlight blog-highlight--nlp\">NLP</span> starts with better datasets, not just models"]
---
So here is the thing... I love discussing politics; I think that everyone should, at least occasionally, bother 
themselves with what is happening in their country's political scenery. 

<span class="image center"><img src="{{ 'assets/images/posts/2020/brexit-nlp-dataset/eu-brexit-classifier.png' | relative_url }}" alt="BREXIT 2016" /></span>
 
Regardless of whether you are into politics or not, it would be practically impossible to escape debating <span class="blog-highlight blog-highlight--eu">BREXIT</span> back 
in the summer of 2016. At the time, I had just been hired by Data Reply UK and the company's annual XChange conference was
around the corner.

My boss at the time, wanted to us to come up with something interesting and eye catching for our demo pod at the conference. 
So, being that BREXIT was a trending and highly debated topic, I thought that maybe I can come up with a way to predict 
peoples' political stance by means of their social activity.

## The idea
The idea was simple:
> Provided one's twitter @handle, try to infer their political views on <span class="blog-highlight blog-highlight--eu">BREXIT</span>.

The original approach was to:

1. Collect people's tweets through the twitter API;
2. Label tweets related to <span class="blog-highlight blog-highlight--eu">BREXIT</span> as either PRO or CON;
3. Calculate a ratio between the 2 and produce a number that would represent their political stance.

After experimenting a bit, I figured out that using one's own tweets would not be enough. Many twitter users don't 
tweet that often and when they do, they are not really concerned with the EU or BREXIT. So I thought that maybe we can
use the tweets of the people that one follows. This draws from social science and ideas behind tribalism:
> "...you are likely to be ideologically aligned with the positions of your peers [or of those you follow on twitter ;)]!"

## The dataset
In order to be able to label tweets, I had to develop an <span class="blog-highlight blog-highlight--nlp">NLP</span> <span class="blog-highlight blog-highlight--ml">ML</span> model. To do so, I needed a relatively 
big corpus of labelled tweets. 

I turned to an [article by BBC](https://www.bbc.com/news/uk-politics-eu-referendum-35616946) 
at the time, which categorised MPs according to the public stance on BREXIT. Using a twitter list that had the twitter 
handles of 449 MPs at the time and using the twitter API, I accumulated a corpus of 60,941 tweets from 449 UK 
MPs (at the time). Tweets had one or more of the following keywords:                                                             
```python
key_words = ['European union', 'European Union', 'european union', 'EUROPEAN UNION',
    'Brexit', 'brexit', 'BREXIT',
    'euref', 'EUREF', 'euRef', 'eu_ref', 'EUref',
    'leaveeu', 'leave_eu', 'leaveEU', 'leaveEu',
    'borisvsdave', 'BorisVsDave',
    'StrongerI', 'strongerI', 'strongeri', 'strongerI',
    'votestay', 'vote_stay', 'voteStay',
    'votein', 'voteout', 'voteIn', 'voteOut', 'vote_In', 'vote_Out',
    'referendum', 'Referendum', 'REFERENDUM']
```
and were automatically labelled based on the views of the MP who tweeted them.     

You can find more details on how I worked to generate the ML model and how the demo solution worked if you follow this
 [github repository](https://github.com/Christos-Hadjinikolis/eu_tweet_classifier).

## Dataset now available on Kaggle
It took me some time to publish it, but the dataset is now available to everyone to use on Kaggle. You can find it 
if you follow this [link](https://www.kaggle.com/chadjinik/labelledbrexittweets). 

I hope that the ML community will make good use of it. It's 4 years after the referendum but BREXIT is yet to really 
happen and unfortunately it remains a concerning issue. So, who knows, maybe someone wants to use this dataset in some 
other equally interesting way.         

Remember to like my post and re-share it (if you really liked it)!

See you soon! 

<p><a href="http://feeds.feedburner.com/MlAffairs" rel="alternate" type="application/rss+xml"><img src="//feedburner.google.com/fb/images/pub/feed-icon32x32.png" alt="" style="vertical-align:middle;border:0"/></a>&nbsp;<a href="http://feeds.feedburner.com/MlAffairs" rel="alternate" type="application/rss+xml">Register to the ML-Affairs RSS Feed</a></p>

  
