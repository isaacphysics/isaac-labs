---
title: Using the Equation Editor for Word and LaTeX
author: James Sharkey
profile_picture: https://isaacphysics.org/api/any/api/images/content/general_pages/about_us/photos/js.png
about_stub: James is a physicist turned computer scientist, working both on physics and computing for Isaac
author_site: https://isaacphysics.org/about
---
We've put a lot of work into our Equation Editor to make it as usable as possible and whilst it's still very much a work in progress, we get asked from time to time if it can be used to do more than answer questions on Isaac. Can it be used instead of the equation editor in Microsoft Word and LibreOffice? Can it be used to generate LaTeX expressions for more advanced work?

It can actually do all of these things, and we have a page dedicated to making this process as easy as possible: <a href="https://isaacphysics.org/equality" target="_blank">isaacphysics.org/equality</a>.

We provide maths output in three formats: LaTeX, which is how maths is rendered on Isaac and written by professionals; Python, which is what we use to check answers; and MathML, a common standard for sharing maths equations (used for Word and LibreOffice). The chemistry editor provides output in only slightly different formats: LaTeX, which is just a wrapper for the second format; mhchem, a LaTeX package for displaying chemical equations; and MathML again.

 - **LaTeX**: To use the maths LaTeX result, just copy and paste the output into a LaTeX document. You shouldn't need to use any packages, but may find `amsmath` useful. The chemistry result uses the `\ce{...}` command, which is provided by the `mhchem` package. Just add `\usepackage{mhchem}` to the preamble of your document and copy-paste away! (Technically speaking the chemistry result does not actually require the $-signs around it).

 - **Python**: This one isn't technically pure Python, but it's the format we use when we check answers. It's based on Python, and we parse it using Python to check student answers to symbolic questions.

 - **mhchem**: This is basically the same output as the LaTeX result, but can be copied and pasted directly into existing formulae without having to remove the LaTeX command too.

 - **MathML**: This result can be copied and pasted into Word and LibreOffice documents to import the equation. In newer versions of Word, simply paste the output into the document and when the paste options icon appears, choose "Keep Text Only". As a keyboard sequence, this is `Ctrl-V`, `Ctrl`, `T`; or "Home" -> Paste" -> "Keep Text Only" in the menu. In recent versions of LibreOffice Writer, insert a formula ("Insert" -> "Object" -> "Formula") and then once the formula editor opens use "Tools" -> "Import MathML from Clipboard". You can then edit these equations as you would any other equation in Word or LibreOffice should you need to edit them later.

 This covers most of the ways you can use the result of the equation editor; if you know of another widely-used output type we don't support and would be useful to you or spot any mistakes in output - let us know!

 (Also, if you're wondering about the URL for the editor page, the internal name for the very first version of the equation editor was "Equality" and the URL has stuck with us since. If you want to know more, check out [Marking Maths, Part 1](/marking-equations.html) and [Entering Maths](/entering-maths.html)).