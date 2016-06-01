---
title: Marking Nuclear and Chemical Equations
author: James Sharkey
draft: true
profile_picture: https://isaacphysics.org/api/any/api/images/content/general_pages/about_us/photos/js.png
about_stub: James works on both the Physics and Computing sides of the Isaac Physics project, having previously worked on the Dynamics and Maths questions.
author_site: https://isaacphysics.org/about
---
Whilst adding the Thermodynamics questions to the site we ran into an issue: how do we mark non-mathematical equations? There are questions in the <a href="https://isaacphysics.org" target="_blank">Mastering Physics book</a> which require nuclear equations as answers, too. We currently have 3 main types of question on Isaac Physics, alongside one experimental one. Quick questions are simple show/hide boxes, designed to make students think but allowing us to tell them the answer. Multiple choice questions and numeric questions are pretty straightforward too (except for significant figures).

We have some new questions that can have answers provided in symbolic form; these are currently checked using <a href="http://www.sympy.org/en/index.html" target="_blank">SymPy</a>, a specialised Python library designed for symbolic computation. However SymPy isn’t designed to support chemistry, or the nuclear physics we need. We want to be able to give a student feedback when they type an equation with a mistake in it:

<table>
  <tr>
    <th>Student Answer</th>
    <th>Expected Answer</th>
  </tr>
  <tr>
    <td>$$\ce{CH4 + O2 -> H2O + CO2}$$</td>
    <td>$$\ce{CH4 + 2O2 -> 2H2O + CO2}$$</td>
  </tr>
</table>

Wouldn’t it be good if the computer could recognise that the equation the student has entered is the right one, but just isn’t balanced correctly? Without having to list all possible wrong answers first!

<img src="/images/simple_syntax_tree.svg" style="width:33%;float:right;margin-left:15px;">

So we built a parser, a program that takes a chemical equation in text form and gives us back a more useful representation of it, using JFlex and CUP in Java. We can then turn the text `NH3` into a tree-like structure on our server (see the figure, which looks vaguely like a Java class diagram). Now we know, for instance, that there are 3 Hydrogen atoms in $\ce{NH3}$ - and we can compare that to what we expect. We could also check if the “molecule” in each “term” of the above equation matched, but that the numbers did not.

For those who’ve met LaTeX, it uses much the same syntax as the mhchem package does; but for the rest of us, it’s usually what you expect. So `NH3` becomes $\ce{NH3}$ easily enough, and `CH4 + 2O2 -> 2H2O + CO2` is understood to be the equation above too. The parser can be tried out in the demo at the bottom, but we hope to have a graphical user interface for it before we get students to use it to answer questions.

It can’t balance equations all on its own (there are plenty of sites that will do that already, like <a href="https://www.wolframalpha.com/" target="_blank">Wolfram\|Alpha</a> or <a href="http://cs.mcgill.ca/~npaun/projects/chemlogic" target="_blank">Chemlogic</a>), but it can compare expressions to the answers expected and it can also check if the atoms and charges balance in an equation. It still treats charges relatively naively though: it has no idea what ionic bonding is right now, for instance. It works for what we need it to – and we’ll be refining it as we go.

This complicated looking redox reaction demonstrates all of the syntax required to try it out below (there’s even a representation of the tree this equation gets turned into <a href="/images/complex_syntax_tree.svg" target="_blank">here</a>)!

So

<code style="font-size: 1rem;display:block;text-align:center;">3CH3(CH2)2OH(l) + Cr2O7^{2-}(aq) + 8H^{+} -> 3CH3CH2CHO(l) + 2Cr^{3+}(aq) + 7H2O(g)</code>

becomes

$$\ce{3CH3(CH2)2OH(l) + Cr2O7^{2-}(aq) + 8H^{+} -> 3CH3CH2CHO(l) + 2Cr^{3+}(aq) + 7H2O(g)}$$

---
**Try it here**:
<form action="/container/labs-chemistry-checker/parse" method="post" target="result-frame" style="margin-bottom:5px;">
	<input name="test" type="text" value="2H2 + O2 -> 2H2O">
	<input type="submit">
</form>
<iframe name="result-frame" style="height:15em;"> </iframe>
---
Nuclear equations are more complicated: $\ce{_{92}^{238}U}$ isn’t straightforward to type and there are lots of ways to write beta decay and notations for beta particles. Watch this space!