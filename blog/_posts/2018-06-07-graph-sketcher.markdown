---
title: Graph Sketcher
description: First version implementation of the graph sketcher.
author: Ben Hanson
profile_picture: https://isaacphysics.org/api/any/api/images/content/general_pages/about_us/photos/bh.png
about_stub: Ben is a physicist working both on physics and computing for Isaac.
author_site: https://isaacphysics.org/about
---
Our current method of asking graph sketching questions is to either ask for users to type in co-ordinates of key features or to pose a quick question and simply reveal the answer. These methods have their drawbacks, with co-ordinate entry not ensuring users have attempted to draw a curve, i.e. they could simply calculate the values from the equation. Quick questions simply have no way of ensuring the question is attempted, and don't allow us to award marks. 

Our solution, a graph sketching app, allowing users to draw graphs freehand with a mouse, trackpad or even touchscreen! Once drawn, the curve can be customised by dragging it's maxima and minima, along with stretching and translating it. We currently can't mark the answers provided but more on that later. 

<figure style="text-align:center;margin:15px auto 25px auto;width:90%;">
    <img src="/images/graph-sketcher/sketcher.PNG" alt="A graph sketcher example showing a blue curve and and orange straight line.">
    <figcaption>Users can draw multiple lines per solution, in different colours and specify straight or curved lines, allowing for more complex questions to be posed.</figcaption>
</figure>

The axes aren't scaled, allowing users to focus on the shape of the curve without worrying too much about going through exact points. Labels can be dragged and anchored to special points (turning/crossing points) to select answers to certain questions.

<figure style="text-align:center;margin:15px auto 25px auto;width:90%;">
    <img src="/images/graph-sketcher/graph_sketcher.gif" alt="A gif showing how to simply draw and edit a curve">
    <figcaption>Once you've sketched out a curve you can simply click and drag certain points to edit it.</figcaption>
</figure>

At the moment only the ability to sketch curves exists, we're working on implementing marking and making it fully functional. With users all entering slightly differing curves as answers to the same question (given the lack of a scale) it's going to take a bit of time to develop a robust graph checker!

If you'd like to have a go with the current graph sketching implementation, the test page can be found <a href="https://isaacphysics.org/questions/graph_sketcher_test" target="_blank">here</a>, or <a href="https://isaacphysics.org/contact?subject=Graph%20Sketcher" target="_blank">get in touch with any questions here</a>!
