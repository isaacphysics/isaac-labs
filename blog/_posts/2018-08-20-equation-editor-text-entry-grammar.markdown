---
title: Text Entry for Symbolic Questions, done right
description: Improving an old beta feature!
keywords: formal grammar, mathematics, maths, parser, nearley, javascript
author: Andrea Franceschini
profile_picture: https://isaacphysics.org/api/any/api/images/content/general_pages/about_us/photos/af2.png
about_stub: Andrea is a computer scientist on the Isaac Physics project, interested in human-computer interaction, education, and art.
author_site: https://isaacphysics.org/about
---
<a href="/equation-editor-text-entry.html">Earlier this year</a> we launched a new beta feature: the ability to type answers to our symbolic questions. The very first version of this feature worked well enough, but we were unsatisfied with the way it integrated with the site -- i.e., the text entry box and the equation editor box did not talk to each other. That meant that a user could type literally anything in the box, and submit it for checking, which opened the way for all sorts of errors that are difficult to detect and redress automatically[^1].

To fix that, and to provide a better experience, we developed a full text-based maths parser that interprets the users' input and turns it into the same language that the graphical editor speaks. In this way, we can ask the graphical editor to produce a version of the answer that is indistinguishable from the same answer entered via the graphical editor itself, and also safer for us to handle, because we can strictly control what is sent back for checking, eliminating the problem of users typing arbitrary and potentially dangerous code. Not only that, but we can also provide immediate feedback using the render box to show what mathematical expression corresponds to the typed expression, so students always know that they are typing what they mean.

<figure style="text-align:center;margin:15px auto 25px auto;">
    <img src="/images/eqn-text-entry-grammar/text-entry.gif" alt="A symbolic question, showing the new text-entry box underneath.">
</figure>

---

<b>For the enthusiasts:</b>
So, how do we do it? To parse and interpret linear-text mathematical expressions, we use a "[formal grammar](https://en.wikipedia.org/wiki/Formal_grammar)", which is a set of rules that describe what a "[formal language](formal language theory)" looks like. Formal languages are as fascinating as they are outside the scope of this post but, just to give you an idea, computer programming languages, such as Python or JavaScript, are considered excellent examples of formal languages, because they are flexible and expressive, but follow very strict rules of syntax, that is, what words can go where and what certain sequences of words mean when they are placed where they are.

A grammar takes the form of a series of "production rules", which are the rules that describe how to produce and interpret the "sentences" of a language. Imagine for example that you want to describe a language for screaming, where a scream is represented by the word `"argh"` with an arbitrary number of `"a"`s. A grammar to describe this "language" looks like this

```
S -> A "rgh"

A -> A "a"
   | "a"
```

The symbol `S` is where everything starts from. The first rule says that the grammar recognises a sequence of the symbol `A` and the symbol `"rgh"`. The symbol `A` is called a "non-terminal" because the grammar says that it can be substituted by a sequence of symbols containing a non-terminal -- in this case, itself. In fact, `S` is a non-terminal too, because it can be substituted by a sequence containing a non-terminal, `A`. The symbols in double quotes, `"a"` and `"rgh"` are called "terminals", because the grammar does not contain any rule that says that they can be substituted by any other symbol. Considering what we know so far, we can see that `A` recognises, or "produces", all the strings composed by an arbitrary number of `"a"`s: `a`, `aaa`, `aaaaaaa`, and so on. On the other hand, `S` recognises all the strings that contain `A` followed by `"rgh"`, therefore `argh`, `aaargh`, `aaaaaaargh`, and so on. If you feel pirate-y, try to modify the grammar to recognise the same language including an arbitrary number of `"r"`s!

We used a library called [nearley](https://nearley.js.org/) to "compile" the grammar into JavaScript code that can run in the browser. There is an [online playground](https://omrelli.ug/nearley-playground/) that you can use to play around with grammars, but be careful as it is very easy to write grammars that end up in infinite loops and crash your browser! If you know what you are doing, you can [download nearley](https://nearley.js.org/docs/getting-started#installation) onto your computer and play around with its various command-line tools, which make it easier to recover from infinite loops and other bugs.

---

As we can see from this very simple example, writing formal grammars is not an easy endeavour. If you are curious to see what a simple maths grammar looks like, [head over here](https://github.com/kach/nearley/blob/master/examples/calculator/arithmetic.ne), and bear in mind that [ours is even more complex](https://github.com/ucam-cl-dtg/isaac-app/blob/eqn-text-entry-with-grammar/app/js/lib/equation_editor/grammar.ne#L253) because it not only recognises maths, but also translates it into the language of the graphical equation editor.

As always, we welcome feedback on both the equation editor and the new text entry feature: <a href="https://isaacphysics.org/contact?subject=Beta%20Feature%20Feedback" target="_blank">drop us a message here</a>!

[^1]: If you want to know more about the perils of handling arbitrary user input, I highly recommend reading about [improper input validation](https://en.wikipedia.org/wiki/Improper_input_validation).