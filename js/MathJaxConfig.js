// Allow inline maths with single $s, define Isaac macros:
MathJax.Hub.Config({

    config: ["TeX-AMS_HTML.js"],

    tex2jax: {
        inlineMath: [ ['$','$'], ["\\(","\\)"] ],
        displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
        processEscapes: true,
        preview: ["---"],
    },
    TeX: {
        Macros: {
            // See http://docs.mathjax.org/en/latest/tex.html#defining-tex-macros
            "quantity": ["{#1}\\,{\\rm{#2}}",2],
            "valuedef": ["{#1}={\\quantity{#2}{#3}}",3],
            "vtr": ["{\\underline{\\boldsymbol{#1}}}",1],
            "d": "\\mathrm{d}",
            "vari": ["#1",1],
            "s": ["_{\\sf{#1}}", 1],
            "half": ["\\frac{1}{2}",0],
            "third": ["\\frac{1}{3}",0],
            "quarter": ["\\frac{1}{4}",0],
            "eighth": ["\\frac{1}{8}",0],
            "e": ["\\textrm{e}",0],
            "units": ["\\rm{#1}",1],
            // Chemistry:
            "standardstate": ["\\mathbin{\u29B5}",0],
            // Boolean Algebra (mathematical syntax):
            "true": "\\boldsymbol{\\rm{T}}",
            "false": "\\boldsymbol{\\rm{F}}",
            "and": ["{#1} \\wedge {#2}", 2],
            "or": ["{#1} \\lor {#2}", 2],
            "not": ["\\lnot{#1}", 1],
            "bracketnot": ["\\lnot{(#1)}", 1],
            "xor": ["{#1} \\veebar {#2}", 2],
            "equivalent": "\\equiv"
        },
        extensions: ["mhchem.js"],
    },
  "HTML-CSS": {
    availableFonts: [], 
    preferredFont: null, // force Web fonts
    webFont: "STIX-Web"
  },

    "AssistiveMML": {
    disabled: false,
    styles: {
      ".MJX_Assistive_MathML": {
        position:"absolute!important",
        clip: (MathJax.Hub.Browser.isMSIE && (document.documentMode||0) < 8 ?
               "rect(1px 1px 1px 1px)" : "rect(1px, 1px, 1px, 1px)"),
        padding: "1px 0 0 0!important",
        border: "0!important",
        height: "1px!important",
        width: "1px!important",
        overflow: "hidden!important",
        display:"block!important"
      }
    }
  },

// Fix font issues in Chrome 32
// https://groups.google.com/forum/#!msg/mathjax-users/S5x-RQDPJrI/p4nmRXJvoskJ
  extensions: ["MatchWebFonts.js", "AssistiveMML.js"],
});


if (MathJax.Hub.Browser.isChrome) {
    MathJax.Hub.Register.StartupHook(
        "HTML-CSS Jax Config",
        function () {MathJax.OutputJax["HTML-CSS"].FontFaceBug = true}
    );
}

// Signal that we're done configuring MathJax.
MathJax.Hub.Configured();

// FIXME: We could easily use the user's preferences to change the definitions:
if (false) {
    // Boolean Algebra (engineering syntax):
    MathJax.Hub.config.TeX.Macros.and = ["{#1} \\cdot {#2}", 2];
    MathJax.Hub.config.TeX.Macros.or = ["{#1} + {#2}", 2];
    MathJax.Hub.config.TeX.Macros.not = ["\\overline{#1}", 1];
    MathJax.Hub.config.TeX.Macros.bracketnot = MathJax.Hub.config.TeX.Macros.not; // Don't do anything special for engineering syntax!
    MathJax.Hub.config.TeX.Macros.xor = ["{#1} \\oplus {#2}", 2];
    MathJax.Hub.config.TeX.Macros.true = "1";
    MathJax.Hub.config.TeX.Macros.false = "0";
    MathJax.Hub.config.TeX.Macros.equivalent = "=";
}