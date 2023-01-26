[Projected Gradient Descent]

# Prerequisite

- basic knowledge of convex optimization, especially gradient descent method

# Introduction

Projected gradient descent is a gradient descent method deals with more general optimization problem. More exactly, gradient descent method is used in unconstrained convex optimization problem with continuous and differentiable objective function, while projected gradient descent is applied to the **constrained optimization**.

## Constrained Problem

Consider the following constrained minimization problem

$$\min_{\boldsymbol{x}\in\mathcal{Q}}f(\boldsymbol{x}),$$

where the set $\mathcal{Q}\subset\mathbb{R}^{n}$. Now, $\boldsymbol{x}$ is not in $\mathbb{R}^{n}$, but constrained in a subset of real number set. Hence, not any $\boldsymbol{x}$ can be a solution. The feasible solution has to be inside the set $\mathcal{Q}$. Here we are talking about the convex optimization, and therefore $\mathcal{Q}$ is assumed to be a **closed convex** set.

One example of such a constrained problem is the minimization with an equality constrained, e.g.

$$\begin{aligned}
\min_{\boldsymbol{x}}\quad&f(\boldsymbol{x})\\
\text{s. t.}\quad&\mathbf{A}\boldsymbol{x}=\boldsymbol{b}
\end{aligned}$$

The equality constraint defines a convex set $\mathcal{Q:\{\boldsymbol{x}|\mathbf{A}\boldsymbol{x}=\boldsymbol{b}\}}$.

With constraint, the normal gradient descent can not be applied in this problem, because the updated solution of a new iteration can be outside the constraint set.

## Project the outside point onto the constraint set



# Examples

## Example 1

Let function $f:\mathbb{R}^2\rightarrow\mathbb{R}$ be defined as

$$f(\boldsymbol{x})=x_1+x_1x_2+(1+x_2)^2,$$

where $\boldsymbol{x}=[x_1,x_2]^T$. Considering the feasible set

$$\mathcal{Q}=\{\boldsymbol{x}\in\mathbb{R}^2|0\leq x_1\leq1,1\leq x_2\leq2\},$$

apply the first step of Projected Gradient Descent on

$$\min_{\boldsymbol{x}\in\mathcal{Q}}f(\boldsymbol{x}),$$

starting from $\boldsymbol{x}^{(0)}=[1,0]^T$ and step $\alpha=0.1$. $\square$

**Solution**. There are two sub-steps:

1. Apply normal gradient descent. The derivative of $f$ is
   
   $$\nabla f(\boldsymbol{x})=\begin{bmatrix}
     \frac{\partial f}{\partial x_1}\\
     \frac{\partial f}{\partial x_2} 
   \end{bmatrix}=\begin{bmatrix}
     1+x_2\\
     x_1+2(1+x_2)
   \end{bmatrix}.$$

   With this gradient, the update at the first iteration is
   
   $$\begin{aligned}
   \tilde{\boldsymbol{x}}^{(1)}&=\boldsymbol{x}^{(0)}-\alpha\nabla f(\boldsymbol{x}^{(0)})\\
   &=\begin{bmatrix}
     1\\0 
   \end{bmatrix}-0.1\cdot\begin{bmatrix}
     1\\ 3
   \end{bmatrix}=\begin{bmatrix}
     0.9\\-0.3 
   \end{bmatrix}.
   \end{aligned}$$

   The solution above is not in the set $\mathcal{Q}$. THerefore, we need to map the point $\tilde{\boldsymbol{x}}^{(1)}$ onto $\mathcal{Q}$, i.e. find the close point in $\mathcal{Q}$.

2. Find the close point.
   
   $$\begin{aligned}
    \boldsymbol{x}^{(1)}&=\argmin_{\boldsymbol{y}\in\mathcal{Q}}\left\|\boldsymbol{y}-\tilde{\boldsymbol{x}}^{(1)}\right\|_2^2\\
    &=\argmin_{\boldsymbol{y}\in\mathcal{Q}}\quad\left(y_1-\tilde{x}_1^{(1)}\right)^2+\left(y_2-\tilde{x}_2^{(1)}\right)^2.
   \end{aligned}$$

   We can see that the optimization of $y_1$ and $y_2$ is independent. We can decompose the above optimization problem into two problems P1 and P2:

   $$\begin{aligned}
    (P1)\quad&x_1^{(1)}=\argmin_{y_1}\quad\left(y_1-\tilde{x}_1^{(1)}\right)^2\\
    \text{s. t.}\quad&0\leq y_1\leq1,
   \end{aligned}$$

   and

   $$\begin{aligned}
    (P2)\quad&x_2^{(1)}=\argmin_{y_2}\quad\left(y_2-\tilde{x}_2^{(1)}\right)^2\\
    \text{s. t.}\quad&1\leq y_2\leq2.
   \end{aligned}$$

   These are very simple optimization problems. The projected final update of $\boldsymbol{x}$ at the first iteration is

   $$\boldsymbol{x}^{(1)}=\begin{bmatrix}
     0.9\\1 
   \end{bmatrix}.$$ 
