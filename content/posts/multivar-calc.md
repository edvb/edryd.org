---
title: "Multivariable Calculus Cheatsheet"
date: 2017-11-14
tags: math calculus cheatsheet
categories: math
math: true
---

# trig identities

$$\sin^2 \theta + \cos^2 \theta = 1$$

$$1+ \tan^2 \theta = \sec^2 \theta$$

$$1+ \cot^2 \theta = \csc^2 \theta$$

$$\sin(a \pm b) = \sin(a)\cos(b) \pm \cos(a)\sin(b)$$

$$\cos(a \pm b) = \cos(a)\cos(b) \pm \sin(a)\sin(b)$$

$$\sin(-\theta) = -\sin \theta$$

$$\cos(-\theta) = \cos \theta$$

$$\tan(-\theta) = -\tan \theta$$

# derivatives

$$\frac{dy}{dx} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}}$$

$$\frac{d^2y}{dx^2} = \frac{\frac{d}{dt}\frac{dy}{dx}}{\frac{dx}{dt}}$$

$$\frac{d}{d\theta}\sin \theta = \cos \theta$$

$$\frac{d}{d\theta}\cos \theta = -\sin \theta$$

$$\frac{d}{d\theta}\tan \theta = \sec^2 \theta$$

$$\frac{d}{d\theta}\cot \theta = -\csc^2 \theta$$

$$\frac{d}{d\theta}\sec \theta = \sec \theta \tan \theta$$

$$\frac{d}{d\theta}\csc \theta = -\csc \theta \cot \theta$$

$$\frac{d}{dx}\sin^{-1} x = \frac1{\sqrt{1-x^2}}, x \in [-1,1]$$

$$\frac{d}{dx}\cos^{-1} x = \frac{-1}{\sqrt{1-x^2}}, x \in [-1,1]$$

$$\frac{d}{dx}\tan^{-1} x = \frac1{1+x^2}, x \in [\frac{-\pi}2, \frac{\pi}2]$$

$$\frac{d}{dx}\sec^{-1} x = \frac1{|x|\sqrt{x^2-1}}, |x| > 1$$

# integrals

$$\int{udv} = uv - \int{vdu}$$

$$\int_a^b{f(x)dx} = \lim_{n \to \infty} \sum_{i=1}^n f(x_i)\Delta x$$

$$\iint_R{f(x,y)dA} = \lim_{\substack{n \to \infty \\ m \to \infty}} \sum_{i=1}^n \sum_{j=1}^m f(x_i,y_i)\Delta x\Delta y$$

# vectors

$$\vec a \cdot \vec b = |\vec a||\vec b| \cos \theta$$

$$|\vec a \times \vec b| = |\vec a||\vec b| \sin \theta$$

$$\mathrm{proj}_{\vec b} \vec a = \frac{\vec a \cdot \vec b}{|\vec b|}\frac{\vec b}{|\vec b|}$$

$$\cos \theta = \frac{n_1n_2}{|n_1||n_2|}$$

$$D = \frac{|d_1-d_2|}{\sqrt{a^2+b^2+c^2}} = \frac{|ax_1+by_1+cz_1+d|}{\sqrt{a^2+b^2+c^2}}$$

$$A = \int_\alpha^\beta g(t)f'(t)dt$$

$$L = \int_\alpha^\beta\sqrt{\left(\frac{dx}{dt}\right)^2+\left(\frac{dy}{dt}\right)^2}$$

$$a_T(t) = \frac{r'(t) \cdot r'(t)'}{|r'(t)|}$$

$$a_N(t) = \frac{|r'(t) \times r'(t)'|}{|r'(t)|}$$

# surfaces

| name                    | equation                                                   |
| ----------------------- | ---------------------------------------------------------- |
| ellipsoid               | $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$  |
| elliptical paraboloid   | $\frac{x^2}{a^2} + \frac{y^2}{b^2} = \frac{z}{c}$          |
| hyperbolic paraboloid   | $\frac{x^2}{a^2} - \frac{y^2}{b^2} = \frac{z}{c}$          |
| cone                    | $\frac{x^2}{a^2} + \frac{y^2}{b^2} = \frac{z^2}{c^2}$      |
| hyperboloid of 1 sheet  | $\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c^2} = 1$  |
| hyperboloid of 2 sheets | $-\frac{x^2}{a^2} - \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$ |

# polar coordinates

$$x = r \cos \theta$$

$$y = r \sin \theta$$

$$r = \sqrt{x^2+y^2}$$

$$\tan \theta = \frac{y}{x}$$

# curvature

$$\vec T(t) = \frac{\vec r'{t}}{|r'(t)|}$$

$$\vec N(t) = \frac{\vec T'{t}}{|T'(t)|}$$

$$\vec B(t) = \vec T(t) \times \vec N(t)\$$

$$\kappa(t) = \left| \frac{d\vec T}{ds} \right| = \frac{|\vec T(t)|}{|\vec r(t)|} = \frac{|r'(t) \times r''(t)|}{|r'(t)|^3} = \frac{|f''(x)|}{(1+f'(x)^2)^{\frac{3}{2}}}$$

# partial derivatives

$$z - z_0 = \frac{\partial z}{\partial x}(x-a) + \frac{\partial z}{\partial y}(y-b)$$

$$dz = \frac{\partial z}{\partial x}dx + \frac{\partial z}{\partial y}dy$$

$$D(a,b) = f_{xx}(a,b)f_{yy}(a,b)-f_{xy}(a,b)^2$$
