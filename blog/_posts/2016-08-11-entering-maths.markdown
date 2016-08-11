---
title: Entering Maths
author: Andrea Franceschini
profile_picture: https://isaacphysics.org/api/any/api/images/content/general_pages/about_us/photos/af2.png
about_stub: Andrea is a computer scientist on the Isaac Physics project, interested in human-computer interaction, education, and art.
author_site: https://isaacphysics.org/about
---
Our [previous formulae editor]({% post_url 2016-04-20-marking-equations %}) was working, but sometimes a bit hard to use. Users could position symbols on the canvas freely, and that resulted in certain edge cases that were much more ambiguous than we expected. Being able to freely build formulae is nice, but being able to do so with limited headaches is much nicer, so we took a step back and realised that we were giving users too much freedom.

There are only so many meaningful places where you can place mathematical symbols relatively to each other, and these places are well known -- think about exponents, subscripts, left- and right-hand sides, and so on -- so we added constraints, and made them explicit to users.

<figure style="text-align:center;margin:15px auto 25px auto;">
	<img src="/images/entering-maths-docking-points.png" alt="Classic E=mc^2 formula in the new editor, showing docking points.">
	<figcaption>Blue circles are points where you can "dock" other symbols to.</figcaption>
</figure>

Those blue circles around symbols are called "docking points", and they are the places where you drop other symbols on to give them a particular meaning. Sometimes an image is worth a thousand words, so here are several in rapid succession.

<figure style="text-align:center;margin:15px auto 25px auto;">
	<img src="/images/entering-maths-formula.gif" alt="Euler's identity.">
	<figcaption>Euler's identity being built.</figcaption>
</figure>

Docking points offer an unambiguous way of placing symbols exactly where you want them. However, no design is perfect, and we are currently dealing with a number of glitches, for example complex formulae where docking points are likely to overlap and become difficult to reach.

<figure style="text-align:center;margin:15px auto 25px auto;">
	<img src="/images/entering-maths-complex-formula.png" alt="A complex formula with lots of difficult to reach docking points.">
	<figcaption>Not that anyone will ever want to create anything like that, right?</figcaption>
</figure>

## Technical bits

Unlike the previous version of the editor, this one is based on [p5.js](http://p5js.org/), that is a Javascript implementation of the [Processing](https://processing.org) environment.

Processing is a "creative coding" environment aimed at electronic and new media artists, and often used to teach the basics of programming. It is however a very powerful tool to create highly interactive and "free form" user interfaces, such as the one we wanted for our formulae editor, and p5.js brings all this to the web through the [`canvas` element](https://www.w3.org/TR/html5/scripting-1.html#the-canvas-element) introduced in HTML 5.

Complex, highly interactive UIs are often easier to model using a class-based, object oriented approach. However, Javascript's approach to classes and objects is peculiar to say the least. For this reason, we chose to write the editor using [TypeScript](https://www.typescriptlang.org/), a strict superset of Javascript that adds optional static typing and classes, and that gets [transpiled](https://en.wikipedia.org/wiki/Source-to-source_compiler) to Javascript before being deployed and executed.

## Try it

You can try the editor by answering some of the <a class="capsule" href="https://isaacphysics.org/gameboards#eqn_editor_beta">symbolic questions</a> on Isaac Physics, or you can try the [big and scary version](https://isaacphysics.org/equality) we use to create new formulae whenever we need them!
