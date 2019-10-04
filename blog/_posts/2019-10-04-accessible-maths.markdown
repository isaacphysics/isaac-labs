---
title: Accessible Maths
description: Making maths accessible on Isaac
author: James Sharkey
profile_picture: https://isaacphysics.org/api/any/api/images/content/general_pages/about_us/photos/js.png
about_stub: James is a physicist turned computer scientist, working both on physics and computing for Isaac.
author_site: https://isaacphysics.org/about
---
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/katex.min.css" integrity="sha384-zB1R0rpPzHqg7Kpt0Aljp8JPLqbXI3bhnPWROx27a9N0Ll6ZP/+DiW/UqRcLbRjq" crossorigin="anonymous">

On Isaac Physics, we use MathJax (version 2) to render mathematical equations and expressions, but on our sister project <a href="https://isaaccomputerscience.org" rel="noopener">Isaac Computer Science</a> we're trying out KaTeX. Both support rendering equations to MathML, which is a badly-supported internet standard for equations. MathJax has several accessibility options which we have tried to make available to users, but they are not immediately intuitive. Browser support for MathML is also poor, and exploring mathematical equations with a screenreader is difficult. For Isaac Computer Science we've taken an accessibility library developed by Khan Academy to make KaTeX equations friendlier to screenreaders and updated it to suit the types of equations you see in school computer science and physics. We can make the way equations are read out slightly simpler, at the expense of making the library less general-purpose.

Below is a table presenting the different styles of rendering, using the five SUVAT equations as examples. The MathJax is that used currently on Isaac Physics, then there's KaTeX's default rendering, and finally the customised version of KaTeX we're testing on Isaac Computer Science.


<table>
   <thead>
      <tr>
        <th>MathJax</th>
        <th>KaTeX (default)</th>
        <th>KaTeX (customised)</th>
      </tr>
   </thead>
   <tbody>
      <tr>
        <td style="text-align: center;">
            $v = u + at$
        </td>
        <td style="text-align: center;">
            <span class="katex">
               <span class="katex-mathml">
                  <math xmlns="http://www.w3.org/1998/Math/MathML">
                     <semantics>
                        <mrow>
                           <mi>v</mi>
                           <mo>=</mo>
                           <mrow>
                              <mrow>
                                 <mi>u</mi>
                                 <mo>+</mo>
                                 <mi>a</mi>
                                 <mi>t</mi>
                              </mrow>
                              <mtext>&thinsp;</mtext>
                              <mrow></mrow>
                           </mrow>
                        </mrow>
                        <annotation encoding="application/x-tex">\valuedef{v}{u + at}{}</annotation>
                     </semantics>
                  </math>
               </span>
               <span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.43056em;vertical-align:0em;"></span><span class="mord"><span class="mord mathdefault" style="margin-right:0.03588em;">v</span></span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.69841em;vertical-align:-0.08333em;"></span><span class="mord"><span class="mord"><span class="mord mathdefault">u</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mord mathdefault">a</span><span class="mord mathdefault">t</span></span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord"><span class="mord"><span class="mord"></span></span></span></span></span></span>
            </span>
        </td>
        <td style="text-align: center;"><span class="katex"><span class="sr-only">v, equals, u, plus, a, t,</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.43056em;vertical-align:0em;"></span><span class="mord"><span class="mord mathdefault" style="margin-right:0.03588em;">v</span></span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.69841em;vertical-align:-0.08333em;"></span><span class="mord"><span class="mord"><span class="mord mathdefault">u</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mord mathdefault">a</span><span class="mord mathdefault">t</span></span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord"><span class="mord"><span class="mord"></span></span></span></span></span></span></span></td>
      </tr>
      <tr>
        <td style="text-align: center;">
            $s = ut + \frac{1}{2}at^{2}$
        </td>
        <td style="text-align: center;">
            <span class="katex">
               <span class="katex-mathml">
                  <math xmlns="http://www.w3.org/1998/Math/MathML">
                     <semantics>
                        <mrow>
                           <mi>s</mi>
                           <mo>=</mo>
                           <mrow>
                              <mrow>
                                 <mi>u</mi>
                                 <mi>t</mi>
                                 <mo>+</mo>
                                 <mfrac>
                                    <mn>1</mn>
                                    <mn>2</mn>
                                 </mfrac>
                                 <mi>a</mi>
                                 <msup>
                                    <mi>t</mi>
                                    <mn>2</mn>
                                 </msup>
                              </mrow>
                              <mtext>&thinsp;</mtext>
                              <mrow></mrow>
                           </mrow>
                        </mrow>
                        <annotation encoding="application/x-tex">\valuedef{s}{ut + \half at^2}{}</annotation>
                     </semantics>
                  </math>
               </span>
               <span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.43056em;vertical-align:0em;"></span><span class="mord"><span class="mord mathdefault">s</span></span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:1.190108em;vertical-align:-0.345em;"></span><span class="mord"><span class="mord"><span class="mord mathdefault">u</span><span class="mord mathdefault">t</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.845108em;"><span style="top:-2.6550000000000002em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">2</span></span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.394em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">1</span></span></span></span></span><span class="vlist-s">&#8203;</span></span><span class="vlist-r"><span class="vlist" style="height:0.345em;"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mord mathdefault">a</span><span class="mord"><span class="mord mathdefault">t</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord"><span class="mord"><span class="mord"></span></span></span></span></span></span>
            </span>
        </td>
        <td style="text-align: center;"><span class="katex"><span class="sr-only">s, equals, u, t, plus, one half, a, t, squared,</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.43056em;vertical-align:0em;"></span><span class="mord"><span class="mord mathdefault">s</span></span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:1.190108em;vertical-align:-0.345em;"></span><span class="mord"><span class="mord"><span class="mord mathdefault">u</span><span class="mord mathdefault">t</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.845108em;"><span style="top:-2.6550000000000002em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">2</span></span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.394em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">1</span></span></span></span></span><span class="vlist-s">&#8203;</span></span><span class="vlist-r"><span class="vlist" style="height:0.345em;"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mord mathdefault">a</span><span class="mord"><span class="mord mathdefault">t</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord"><span class="mord"><span class="mord"></span></span></span></span></span></span></span></td>
      </tr>
      <tr>
        <td style="text-align: center;">
            $s = vt - \frac{1}{2}at^{2}$
        </td>
        <td style="text-align: center;">
            <span class="katex">
               <span class="katex-mathml">
                  <math xmlns="http://www.w3.org/1998/Math/MathML">
                     <semantics>
                        <mrow>
                           <mi>s</mi>
                           <mo>=</mo>
                           <mrow>
                              <mrow>
                                 <mi>v</mi>
                                 <mi>t</mi>
                                 <mo>−</mo>
                                 <mfrac>
                                    <mn>1</mn>
                                    <mn>2</mn>
                                 </mfrac>
                                 <mi>a</mi>
                                 <msup>
                                    <mi>t</mi>
                                    <mn>2</mn>
                                 </msup>
                              </mrow>
                              <mtext>&thinsp;</mtext>
                              <mrow></mrow>
                           </mrow>
                        </mrow>
                        <annotation encoding="application/x-tex">\valuedef{s}{vt - \half at^2}{}</annotation>
                     </semantics>
                  </math>
               </span>
               <span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.43056em;vertical-align:0em;"></span><span class="mord"><span class="mord mathdefault">s</span></span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:1.190108em;vertical-align:-0.345em;"></span><span class="mord"><span class="mord"><span class="mord mathdefault" style="margin-right:0.03588em;">v</span><span class="mord mathdefault">t</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">−</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.845108em;"><span style="top:-2.6550000000000002em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">2</span></span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.394em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">1</span></span></span></span></span><span class="vlist-s">&#8203;</span></span><span class="vlist-r"><span class="vlist" style="height:0.345em;"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mord mathdefault">a</span><span class="mord"><span class="mord mathdefault">t</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord"><span class="mord"><span class="mord"></span></span></span></span></span></span>
            </span>
        </td>
        <td style="text-align: center;"><span class="katex"><span class="sr-only">s, equals, v, t, minus, one half, a, t, squared,</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.43056em;vertical-align:0em;"></span><span class="mord"><span class="mord mathdefault">s</span></span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:1.190108em;vertical-align:-0.345em;"></span><span class="mord"><span class="mord"><span class="mord mathdefault" style="margin-right:0.03588em;">v</span><span class="mord mathdefault">t</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">−</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.845108em;"><span style="top:-2.6550000000000002em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">2</span></span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.394em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">1</span></span></span></span></span><span class="vlist-s">&#8203;</span></span><span class="vlist-r"><span class="vlist" style="height:0.345em;"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mord mathdefault">a</span><span class="mord"><span class="mord mathdefault">t</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord"><span class="mord"><span class="mord"></span></span></span></span></span></span></span></td>
      </tr>
      <tr>
        <td style="text-align: center;">
            $s = \frac{1}{2}\left(u + v\right)t$
        </td>
        <td style="text-align: center;">
            <span class="katex">
               <span class="katex-mathml">
                  <math xmlns="http://www.w3.org/1998/Math/MathML">
                     <semantics>
                        <mrow>
                           <mi>s</mi>
                           <mo>=</mo>
                           <mrow>
                              <mrow>
                                 <mfrac>
                                    <mn>1</mn>
                                    <mn>2</mn>
                                 </mfrac>
                                 <mo stretchy="false">(</mo>
                                 <mi>u</mi>
                                 <mo>+</mo>
                                 <mi>v</mi>
                                 <mo stretchy="false">)</mo>
                                 <mi>t</mi>
                              </mrow>
                              <mtext>&thinsp;</mtext>
                              <mrow></mrow>
                           </mrow>
                        </mrow>
                        <annotation encoding="application/x-tex">\valuedef{s}{\half (u+v) t}{}</annotation>
                     </semantics>
                  </math>
               </span>
               <span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.43056em;vertical-align:0em;"></span><span class="mord"><span class="mord mathdefault">s</span></span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:1.190108em;vertical-align:-0.345em;"></span><span class="mord"><span class="mord"><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.845108em;"><span style="top:-2.6550000000000002em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">2</span></span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.394em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">1</span></span></span></span></span><span class="vlist-s">&#8203;</span></span><span class="vlist-r"><span class="vlist" style="height:0.345em;"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mopen">(</span><span class="mord mathdefault">u</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mord mathdefault" style="margin-right:0.03588em;">v</span><span class="mclose">)</span><span class="mord mathdefault">t</span></span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord"><span class="mord"><span class="mord"></span></span></span></span></span></span>
            </span>
        </td>
        <td style="text-align: center;"><span class="katex"><span class="sr-only">s, equals, one half, left bracket, u, plus, v, right bracket, t,</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.43056em;vertical-align:0em;"></span><span class="mord"><span class="mord mathdefault">s</span></span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:1.190108em;vertical-align:-0.345em;"></span><span class="mord"><span class="mord"><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.845108em;"><span style="top:-2.6550000000000002em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">2</span></span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.394em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">1</span></span></span></span></span><span class="vlist-s">&#8203;</span></span><span class="vlist-r"><span class="vlist" style="height:0.345em;"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mopen">(</span><span class="mord mathdefault">u</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mord mathdefault" style="margin-right:0.03588em;">v</span><span class="mclose">)</span><span class="mord mathdefault">t</span></span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord"><span class="mord"><span class="mord"></span></span></span></span></span></span></span></td>
      </tr>
      <tr>         
        <td style="text-align: center;">
            $v^{2} = u^{2} + 2as$
        </td>
        <td style="text-align: center;">
            <span class="katex">
               <span class="katex-mathml">
                  <math xmlns="http://www.w3.org/1998/Math/MathML">
                     <semantics>
                        <mrow>
                           <msup>
                              <mi>v</mi>
                              <mn>2</mn>
                           </msup>
                           <mo>=</mo>
                           <mrow>
                              <mrow>
                                 <msup>
                                    <mi>u</mi>
                                    <mn>2</mn>
                                 </msup>
                                 <mo>+</mo>
                                 <mn>2</mn>
                                 <mi>a</mi>
                                 <mi>s</mi>
                              </mrow>
                              <mtext>&thinsp;</mtext>
                              <mrow></mrow>
                           </mrow>
                        </mrow>
                        <annotation encoding="application/x-tex">\valuedef{v^2}{u^2 + 2as}{}</annotation>
                     </semantics>
                  </math>
               </span>
               <span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8141079999999999em;vertical-align:0em;"></span><span class="mord"><span class="mord"><span class="mord mathdefault" style="margin-right:0.03588em;">v</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.897438em;vertical-align:-0.08333em;"></span><span class="mord"><span class="mord"><span class="mord"><span class="mord mathdefault">u</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mord">2</span><span class="mord mathdefault">a</span><span class="mord mathdefault">s</span></span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord"><span class="mord"><span class="mord"></span></span></span></span></span></span>
            </span>
        </td>
        <td style="text-align: center;"><span class="katex"><span class="sr-only">v, squared, equals, u, squared, plus, 2, a, s,</span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8141079999999999em;vertical-align:0em;"></span><span class="mord"><span class="mord"><span class="mord mathdefault" style="margin-right:0.03588em;">v</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.897438em;vertical-align:-0.08333em;"></span><span class="mord"><span class="mord"><span class="mord"><span class="mord mathdefault">u</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mord">2</span><span class="mord mathdefault">a</span><span class="mord mathdefault">s</span></span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord"><span class="mord"><span class="mord"></span></span></span></span></span></span></span></td>
      </tr>
   </tbody>
</table>

If you're a screenreader user, we'd be interested to know which of the versions is easiest to understand. We'd also appreciate any feedback on how we could improve things. You can <a href="https://isaacphysics.org/contact?subject=Accessible%20Maths" target="_blank">send us any feedback you have via Isaac Physics</a>.
