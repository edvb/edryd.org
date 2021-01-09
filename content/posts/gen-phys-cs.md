---
title: "General Physics Cheatsheet"
date: 2017-06-02
tags: phys cheatsheet
categories: phys
math: true
---

$ \newcommand{\e}[1]{ \times 10^{#1}} $

## constants

$m_e = 9.11\e{-31} kg = .511 \frac{MeV}{c^2} = 5.4858\e{-4} u$

$m_p = 1.673\e{-27} kg = 938 \frac{MeV}{c^2} = 1.007276 u$

$m_n = 1.675\e{-27} kg = 940 \frac{MeV}{c^2} = 1.008665 u$

$u = 1.6605\e{-27} kg = 931.5 \frac{MeV}{c^2}$

$e = 1.6012\e{-19} C$

$\mu_0 = 4\pi\e{-7}$

$k = 8.988\e9 \frac{Nm^2}{C^2}$

$\varepsilon_0 = 8.854\e{-12} \frac{F}{m}$

$c = 2.998\e8 \frac{m}{s}$

$h = 6.626\e{-34} Js = 4.136\e{-15} eVs$

$T = 1.6\e{-19}$

$E_1 = -13.6 eV$

$r_0 = 1.2\e{-15} m$

## equations

$\varepsilon_0 = \frac1{4\pi k} = \frac1{\mu_0c^2}$

### electric fields

$E = \frac{\sigma}{\varepsilon_0}$

$\Phi_E = \vec E \cdot \vec A = EA\cos \theta = \frac{q_A}{\varepsilon_0}$

$\vec F_E = \frac{kqQ}{r^2} = Q \vec E$

$W = \vec F \Delta x \cos \theta$

$\Delta U = -\Delta E_k = -W$

$\Delta V = \frac{\Delta U}{q_0} = -\vec E \Delta x$

$V = \frac{kQ}r$

### capacitance

$V = Ed$

$Q = \sigma A$

$C = \frac{Q}V = kC_0$

$U = \frac{CV^2}2$

### electric currents

$V = IR$

$P = IV$

$I = \frac{\Delta Q}{\Delta t}$

$I = v_DAnq$

$I_{rms} = \frac{I_0}{\sqrt2}$

$R = \frac{\rho \ell}A$

### dc circuits

$\tau = RC$

$V_0 = \frac{Q_0}C$

$I_0 = \frac{V_0}R$

$Q_{max} = CV_B$

$\sum I_{in} = \sum I_{out}$

$\sum V_{loop} = 0$

#### series

$\sum Q = Q_1 = Q_2 = \cdots = Q_n$

$\frac1{\sum C} = \frac1{C_1} + \frac1{C_2} + \cdots + \frac1{C_n}$

$\sum U = \frac{Q_1^2}{2C_1} + \frac{Q_2^2}{2C_2} + \cdots + \frac{Q_n^2}{2C_n}$

$\sum R = R_1 + R_2 + \cdots + R_n$

#### parallel

$\sum V = V_1 = V_2 = \cdots + R_n$

$\sum C = C_1 + C_2 + \cdots + C_n$

$\sum U = \frac{Q_1}{2C_1} + \frac{Q_2}{2C_2} + \cdots + \frac{Q_n}{2C_n}$

$\frac1{\sum R} = \frac1{R_1} + \frac1{R_2} + \cdots + \frac1{R_n}$

### rc circuits

$i = I_0 e^{\frac{-t}\tau}$

$V_R = I_0 R e^{\frac{-t}\tau}$

$U = \frac{q^2}{2C}$

$P = i^2 R$

#### charging

$q = Q_{max} \left(1 - e^{\frac{-t}\tau}\right)$

$V_C = V_B \left(1 - e^{\frac{-t}\tau}\right)$

#### discharging

$q = Q_{max} e^{\frac{-t}\tau}$

$V_C = V_B e^{\frac{-t}\tau}$

### magnetism

$\vec F_B = q \vec v \cdot \vec B = qvB\sin\theta$

$F_B = \frac{mv^2}{R} = qvB$

$\frac{F_M}{\ell} = BI\sin\theta$

$B = \frac{\mu_0 I}{2 \pi r} = \frac{\mu_0 I N}{\ell}$

$\frac{F_{21}}{\Delta \ell} = \frac{\mu_0 I_1 I_2}{2 \pi d}$

### electromagnetic induction

$\mathcal{E} = \left\|\frac{\Delta \Phi_B}{\Delta t}\right\| = -vBL = NBAq$

$I_{avg} = \frac{\left\|\mathcal{E}\right\|}R$

$\Delta \Phi_B = B \Delta A = \Delta B A$

$U = \frac{LI^2}2 = \frac{B^2V_{ol}}{2\mu_0}= \frac{B^2\pi r^2\ell}{2\mu_0}$

$\tau = \vec \mu \cdot \vec B$

$P = \vec F \cdot \vec v = \frac{\left(B \ell v\right)^2}R$

$\frac{N_P}{N_S} = \frac{V_P}{V_S} = \frac{I_S}{V_P}$

### electromagnetic waves

$v = f\lambda$

$\vec{S} = \frac{EB}{2\mu_0} = \frac{P}A$

$E = \frac{I}{A\mathcal{E}_0} = cB$

$\sum U = U_E + U_B = \mathcal{E}_0E^2$

$U_E = \frac{\mathcal{E}_oE^2}2$

$U_B = \frac{B^2}{2\mu_0}$

$S = \frac{CB^2}{\mu_0} = \frac{\Delta U}{A\Delta t}$

### optics

$\frac1{d_0} + \frac1{d_i} = \frac1{f} = \frac2{r}$

$\frac1{f} = (n-1)\left(\frac1{R_1}-\frac1{R_2}\right)$

$M = \frac{-d_i}{d_0} = \frac{h_i}{h_0}$

$n_1\sin\theta_1 = n_2\sin\theta_2$

$\lambda_m = \frac{\lambda_v}n$

### special theory of relativity

$\Delta t = \gamma \Delta t_0$

$L = \frac{L_0}{\gamma}$

$\gamma = \frac1{\sqrt{1-\frac{v^2}{c^2}}}$

$v = c \sqrt{1-\frac1{\gamma^2}}$

### quantum mechanics

$\hbar = \frac{h}{2\pi}$

$\Delta x \Delta p \gtrsim \hbar$

$\Delta E \Delta t \gtrsim \hbar$

$E_n = \frac{Z^2}{n^2}(-13.6eV)$

### nuclear physics

$r = r_0 A^{1/3}$

$N = N_0e^{-\lambda t}$

$A = \lambda N$

## info

### prefixes

| name  | prefix | power      |
| ----  | ------ | ---------- |
| exa   | E      | $10^{18}$  |
| peta  | P      | $10^{15}$  |
| tera  | T      | $10^{12}$  |
| giga  | G      | $10^9$     |
| mega  | M      | $10^6$     |
| kilo  | k      | $10^3$     |
| hecto | h      | $10^2$     |
| deca  | da     | $10^1$     |
| -     | -      | -          |
| deci  | d      | $10^{-1}$  |
| centi | c      | $10^{-2}$  |
| milli | m      | $10^{-3}$  |
| mirco | μ      | $10^{-6}$  |
| nano  | n      | $10^{-9}$  |
| pico  | p      | $10^{-12}$ |
| femto | f      | $10^{-15}$ |
| atto  | a      | $10^{-18}$ |

### right hand rules

| hand    | vector          |
| ------- | --------------- |
| fingers | $\vec v$ or $I$ |
| palm    | $\vec B$        |
| thumb   | $\vec F$        |

### quantum numbers

| (n, ℓ, m, s)    |
| --------------- |
| n = 1, 2, 3 … ∞ |
| ℓ = 0 … n-1     |
| m = -ℓ … +ℓ     |
| s = ±½          |
