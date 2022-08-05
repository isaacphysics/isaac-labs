---
title: Visualising Data in New Ways
author: James Sharkey
profile_picture: https://isaacphysics.org/api/any/api/images/content/general_pages/about_us/photos/js.png
about_stub: James is a physicist turned computer scientist, working both on physics and computing for Isaac
author_site: https://isaacphysics.org/about
---
Isaac has seen nearly 7.1 million question attempts over the last 2 years, and as a research-oriented platform we collect data about these attempts. One incidental piece of information we have is a rough idea of where in the world people are attempting our questions from. We can't use this data for research, because it's not very reliable; it's based on IP address, and doesn't necessarily reflect where a user really is.

But we don't need an accurate location to have fun visualising it - just a rough idea will do!

Enter Google's [WebGL Globe](https://www.chromeexperiments.com/globe), a Chrome Experiment for visualising geographic data in a novel way; the taller the spike on the map, the more "stuff" has happened at that location. What would happen if we made a heat-map like plot of where people answered questions on Isaac from?

<figure style="text-align:center;margin:15px auto 25px auto;">
	<img src="{{ '/images/visualising-data-globe/question-attempts-globe.png' | relative_url }}" alt="A screenshot of the WebGL globe, showing question attempts. There's a huge spike in London and lots of activity in the UK but less elsewhere.">
	<figcaption>This is what happens! The enormous spike corresponds to central London, which is probably because many UK ISPs are registered there, and the grid-like pattern is simply an artfact of the location resolution not in the data itself per se.</figcaption>
</figure>

We can also look at the locations of schools in the UK and Ireland which have students and teachers registered at. We have postcode and Eircode information for these schools, and can show an indication of how many users are active at each. Of course, many students haven't told us their school, and so the data is necessarily incomplete. But as a quick way of visualising where Isaac is being used, it's quite cool!

<figure style="text-align:center;margin:15px auto 25px auto;">
	<img src="{{ '/images/visualising-data-globe/schools-uk-ireland-globe.png' | relative_url }}" alt="A screenshot of the WebGL globe, showing how many users at schools across the Britsh Isles.">
	<figcaption>The peaks give an indication of the number of students and teachers using Isaac at schools we know about. Note that the scale is radically different on this plot!</figcaption>
</figure>

You can <a class="capsule" href="https://cdn.isaacphysics.org/isaac/labs/webgl-globe/index.html">explore the globes yourself here</a>, though they may not work if you're not using Chrome.