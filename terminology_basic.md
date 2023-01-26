This introduction is mainly based on Boyd's book "Convex Optimization".

Consider a optimization problem written mathematically as

$$\begin{aligned}
  (P1)\quad\mathrm{minimize}\quad & f_0(x)\\
  \text{subject to}\quad & f_i(x)\leq0,\quad i=1,\cdots,m
  & h_i(x)=0,\quad i=1,\cdots,p.
\end{aligned}$$

This form of an optimization problem is called ***standard form***, where the righthand side of the inequality and equality constraints are zero.

We name the following variables:
- ***optimization variable***: $x\in\mathbb{R}^n$
- ***objective function*** / ***cost function***: $f_0:\mathbb{R}^n\rightarrow\mathbb{R}$
- ***inequality constraints***: $f_i(x)\leq0,\quad i=1,\cdots,m$
- ***inequality constraint functions***: $f_i:\mathbb{R}^n\rightarrow\mathbb{R},\quad i=1,\cdots,m$
- ***equality constraints***: $h_i(x)=0,\quad i=1,\cdots,p$
- ***equality constraint functions***: $h_i:\mathbb{R}^n\rightarrow\mathbb{R},\quad i=1,\cdots,p$
- ***unconstraint*** if $m=p=0$

Each function $f_i$ or $h_i$ has different domain on $x$. The intersection of the domains of all functions becomes the ***domain*** of the optimization problem:

$$\mathcal{D}=\bigcap_{i=0}^{m}\bold{dom}f_i\cap\bigcap_{i=0}^{p}h_i.$$


