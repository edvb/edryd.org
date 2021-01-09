---
title: "Proof of Derivative Properties"
date: 2017-10-04
tags: math calculus proof notes
categories: math
math: true
---

## derivation of the quotient rule

The quotient rule is used to take the derivative of a function with divided
expressions:

$$
\left(\frac{u}{v}\right)' = \frac{vu' - uv'}{v^2}
$$

It is possible to prove this rule by utilizing the definition of the
derivative; however, this is not nearly as elegant as the following simple
proofs which use other derivative properties instead.

### product rule

$$\begin{align}
 y & = \frac{u}{v} \\
   & = uv^{-1} \\
y' & = v^{-1}u' + u(-v^{-2}v') \\
   & = \frac{u'}{v} - \frac{uv'}{v^2} \\
   & = \frac{v}{v}\cdot\frac{u'}{v} - \frac{uv'}{v^2} \\
   & = \frac{vu'}{v^2} - \frac{uv'}{v^2} \\
   & = \frac{vu' - uv'}{v^2} \\
\end{align}$$

### logarithm

$$\begin{align}
            y & = \frac{u}{v} \\
\mathrm{ln} y & = \mathrm{ln} \frac{u}{v} \\
              & = \mathrm{ln} u - \mathrm{ln} v \\
 \frac{y'}{y} & = \frac{u'}{u} - \frac{v'}{v} \\
              & = \frac{v}{v}\frac{u'}{u} - \frac{u}{u}\frac{v'}{v} \\
              & = \frac{vu' - uv'}{uv} \\
           y' & = y\frac{vu' - uv'}{uv} \\
              & = \frac{u}{v}\frac{vu' - uv'}{uv} \\
              & = \frac{vu' - uv'}{v^2} \\
\end{align}$$

## logarithmic proofs

As well as being used in the proof of the quotient rule, logarithms can also be
used to prove a couple of other derivative rules.

### power rule

$$\begin{align}
            y & = x^n \\
\mathrm{ln} y & = \mathrm{ln} x^n \\
              & = n \mathrm{ln} x \\
 \frac{y'}{y} & = n \frac{1}{x} \\
           y' & = yn \frac{1}{x} \\
              & = n x^n x^{-1} \\
              & = nx^{n-1}\\
\end{align}$$

### product rule

$$\begin{align}
            y & = uv \\
\mathrm{ln} y & = \mathrm{ln} uv \\
              & = \mathrm{ln} u + \mathrm{ln} v \\
 \frac{y'}{y} & = \frac{u'}{u} + \frac{v'}{v} \\
           y' & = y \frac{u'}{u} + \frac{v'}{v} \\
              & = uv \left(\frac{u'}{u} + \frac{v'}{v}\right) \\
              & = vu' + uv' \\
\end{align}$$
