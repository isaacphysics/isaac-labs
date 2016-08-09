---
title: Visualising Related Concepts
author: James Sharkey
profile_picture: https://isaacphysics.org/api/any/api/images/content/general_pages/about_us/photos/js.png
about_stub: James works on both the Physics and Computing sides of the Isaac Physics project, having previously worked on the Dynamics and Maths questions.
author_site: https://isaacphysics.org/about
---
Isaac has about 75 concept pages that go alongside the questions and cover key material in physics and maths. They aren’t designed to replace a textbook, more as a reminder of important points and key areas. One of the neat, but under-used, features of Isaac is the “Related Content” boxes at the bottom of questions and concept pages. They list questions that use the same skills, or concepts that are relevant to the current page.

<a href="/images/isaacMechanics.svg" target="_blank"><img src="/images/isaacMechanics.png" style="width:50%;float:left;margin-right:20px;"></a>
Visually showing the links between concepts could be useful when revising or when answering questions. For those who like maths terms, all the related question/concept information on Isaac forms a big directed graph.

Unfortunately, there are far too many questions on Isaac to make this usable on the whole site - just drawing the graph for related questions in our Mechanics section gives the spidery mess in the image above!

Trying again just for concept pages produces something more manageable. In fact; with Graphviz, some Javascript and a decent browser you can make a basic but reasonably interactive way to explore the concept pages on Isaac. It works on desktop: try scrolling the mouse wheel to zoom in and out (don't use the browser's zoom), and use the arrow keys to move about (dragging won't work). Mobile devices and small screens will still load the page and be able to pan and zoom, but the highlighting of linked concepts won’t work!

<a href="https://cdn.isaacphysics.org/isaac/labs/isaacConceptPages.html" class="capsule" target="_blank" style="margin:15px auto 15px auto;text-align: center;display: block;width: 33%;">Explore it here</a>

There are almost certainly links between concepts missing and the data is now very much out of date. Maybe the whole thing ought to be a symmetric directed graph (arrows both ways for all links)! We’re not really sure how useful such a tool is, or how we’d actually use it on Isaac - but it was a fun afternoon’s work all the same!