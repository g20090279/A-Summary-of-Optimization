- Topics: Conjugate Gradient Descent Method
- Last Revised: Nov. 23, 2023

---

The deepest descent method iterates along the gradient, which is the fastest decrease (if not mentioned specifically, we consider a convex minimization problem). It is interesting to see that feastest decrease at each step does not necessarily result in fastest path on the whole, where the fastness is measured by the number of iterations until the iterative algorithm ends. In fact, convergence of steepest descent is fast if the condition number of $A$ is small (Shewchuk, 1994, Fig. 17). More exactly, the more ill-conditioned the matrix $A$, the slower the convergence of steepest descent.

# Review of Linear Gradient Descent

Initially, the gradient descent methods are discovered to solve the system of linear equations, which is $Ax=b$ and $x=[x_1,x_2,\cdots,x_n]^T\in\mathbb{R}^n$. From the point of view of optimization theory, solving $Ax=b$ is equivalent to obtain the optimum of the following optimization problem

$$\min_{x\in\mathbb{R}^n}f(x)=\frac{1}{2}x^TAx-b^T+c,$$

where $A$ is assumed to be positive-definite matrix, with which the optimization problem becomes convex. $A$ is further assumed to be symmetric, where exactly $n$ orthogonal vectors exist and form an orthogonal basis. The symmetricity of $A$ guarantees the equivalence as well, since the derivative of $f$ is $\nabla_xf=f^\prime(x)=\left[\frac{\partial f}{\partial x_1},\frac{\partial f}{\partial x_2},\cdots,\frac{\partial f}{\partial x_n}\right]^T=Ax-b$, resulting in $Ax-b=0$ at the optimal point. $\nabla_xf$ is also called gradient, the direction of greatest increase of $f(x)$ for a given $x$. The greatest decrease heads opposite to $\nabla_xf$, i.e., $r=-\nabla_xf=b-Ax$, at point $x$. The iterative approach can be formed to approach the optimum value step by step with

$$x_{(k+1)}=x_{(k)}+\alpha_{(k)}r_{(k)}.$$

Note that the subscript with parentheses donotes the index the iteration.

# References

- Shewchuk, J. R. (1994). *An introduction to the conjugate gradient method without the agonizing pain*. Carnegie Mellon University.
