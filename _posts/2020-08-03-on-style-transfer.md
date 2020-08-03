---
title: Style Transfer in Heraklion
author: Christos Hadjinikolis
layout: post
---
<head><meta property="og:image" content="assets/images/2020-08-03-style-transfer-koules.png" /></head>
I am currently in Crete for my annual get away. Crete is an amazing island with many beautiful places to visit and a vast 
history that goes all the way back to the Minoans in 2700 BC.  

<span class="image center"><img src="{{ 'assets/images/2020-08-03-style-transfer-koules.png' | relative_url }}" alt="" /></span>
One of the things I love doing whenever I am here is strolling around the city of Heraklion and taking pictures of the many hidden alleys, 
which reveal an amazing graffiti culture! I felt strongly about writing about it in my blog and I thought that maybe I can do so 
by using some amazing images I gathered just last week in a style-transfer post. So this is it: **"Style Transfer in Heraklion"**

## A bit of history: A Neural Algorithm of Artistic Style
Neural Style Transfer (NST) is a class of algorithms that process images to adopt the visual style of another image. A seminal paper 
that introduced this concept was ["A Neural Algorithm of Artistic Style"](https://arxiv.org/abs/1508.06576) by Leon A. Gatys, Alexander 
S. Ecker and Matthias Bethge. In their work, the authors emphasize that 
>"...representations of content and style in Neural Networks are 
seperable".   

This is the foundation of this work, since if these two notions are indeed separable then provided two images you can get the style 
of the first, the content of the second and merge them together. So, how is this done exactly? 

## Delving into the details
<span class="image center"><img src="{{ 'assets/images/2020-08-03-style-transfer-paper-01.png' | relative_url }}" alt="" /></span>

The first figure in the paper shows the original setup and how the VGG19 netowrk was modified to do NST. At the top left 
you see ["The Starry Night"](https://artsandculture.google.com/asset/the-starry-night/bgEuwDxel93-Pg?hl=en-GB&avm=2) by Vincent van Gogh
and below it is just a random content image. Note that here, the authors are using a pre-trained NN, referred to as VGG19. 
What we are interested in is how this network will repond to the inputs.

### Retrieving content
Provided both an input (style) image and a content image each neuron and respectively each layer in the NN will either activate or it won't.
Each image is processed, or better yet filtered, in a different way (by nature of the activation or not of different neurons). Looking at 
how the content image is gradually filtered in the below image you will notice that the first layer leaves the image seemingly intact. 
But you look all the way to the last filtered output you will see that this is not the case at all; shapes are there but the inside is not so much the same.
This is because of how the resulting high level features are generated on earlier abstractions of the same image produced by previous layers. 
This is the intended behaviour to retrieve the content.   
 
  










 
Remember to like my post and re-share (if you really liked it)!

See you soon! 

<p><a href="http://feeds.feedburner.com/MlAffairs" rel="alternate" type="application/rss+xml"><img src="//feedburner.google.com/fb/images/pub/feed-icon32x32.png" alt="" style="vertical-align:middle;border:0"/></a>&nbsp;<a href="http://feeds.feedburner.com/MlAffairs" rel="alternate" type="application/rss+xml">Register to the ML-Affairs RSS Feed</a></p>

<blockquote class="twitter-tweet" data-theme="light"><p lang="en" dir="ltr">I successfully took the AWS Machine Learning Specialty Certification during the COVID-19 lockdown! <br><br>Here are my thoughts: <a href="https://t.co/WejGBrmDvy">https://t.co/WejGBrmDvy</a></p>&mdash; Christos Hadjinikoli (@chatzinikolis) <a href="https://twitter.com/chatzinikolis/status/1288507051824549888?ref_src=twsrc%5Etfw">July 29, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

         
