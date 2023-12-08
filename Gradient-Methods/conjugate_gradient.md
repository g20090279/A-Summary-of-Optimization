- Topics: Conjugate Gradient Descent Method
- Last Revised: Dec. 7, 2023 

---

The deepest descent method iterates along the gradient, which is the fastest decrease (if not mentioned specifically, we consider a convex minimization problem). It is interesting to see that feastest decrease at each step does not necessarily result in fastest path on the whole, where the fastness is measured by the number of iterations until the iterative algorithm ends. In fact, convergence of steepest descent is fast if the condition number of $A$ is small (Shewchuk, 1994, Fig. 17). On the contrary, a large condition number of $A$ can be bad for convergence (not necessary, there will be higher chance for slow convergence in the case of large condition number. However, we one can chose the starting point to lie on or very closely on one of the eigenvectors of $A$, the convergence can also be very fast, e.g. just one step. More detail are given in (Shewchuk, 1994, §6.2)).

# Review of Linear Gradient Descent

Initially, the gradient descent methods are discovered to solve the system of linear equations, which is $Ax=b$ and $x=[x_1,x_2,\cdots,x_n]^T\in\mathbb{R}^n$. From the point of view of optimization theory, solving $Ax=b$ is equivalent to obtain the optimum of the following optimization problem

$$\min_{x\in\mathbb{R}^n}f(x)=\frac{1}{2}x^TAx-b^T+c,\qquad(1)$$

where $A$ is assumed to be positive-definite matrix, with which the optimization problem becomes convex. $A$ is further assumed to be symmetric, where exactly $n$ orthogonal vectors exist and form an orthogonal basis. The symmetricity of $A$ guarantees the equivalence as well, since the derivative of $f$ is $\nabla f(x)=f^\prime(x)=\left[\frac{\partial f}{\partial x_1},\frac{\partial f}{\partial x_2},\cdots,\frac{\partial f}{\partial x_n}\right]^T=Ax-b$, resulting in $Ax-b=0$ at the optimal point. $\nabla f(x)$ is also called *gradient*, the direction of greatest increase of $f(x)$ for a given $x$. The greatest decrease heads opposite to $\nabla f(x)$, i.e., $r=-\nabla f(x)=b-Ax$, at point $x$. The iterative approach can be formed to approach the optimum value step by step with

$$x_{(i+1)}=x_{(i)}+\alpha_{(i)}r_{(i)}.\qquad(2)$$

Note that the subscript with parentheses donotes the index the iteration. We can see that the search direction of the steepest descent method is the residual, which is the negative of the gradient. The iterative method of form in Eq. (2) has another name called *line search method*. This name comes from that finding the optimal $\alpha_{(i)}$ is to search an optimal point along a line. 

## Determine the Optimal Step Size: Line-Searching Algorithm

The step size $\alpha_{(i)}$ can be found both exactly and inexactly. In this quadratic-objective optimization problem, the step size can be found exactly, which is to let the derivative of $f(x_{(i+1)})$ w.r.t. $\alpha_{(i)}$ be zero, resulting in $\alpha_{(i)}=r^{T}_{(i)}r_{(i)}/(r^{T}_{(i)}Ar_{(i)})$.

The inexact line search can be considered if it is difficult to obtain an analytical equation for $\alpha_{(i)}$ from Eq. (3). One example is the *backtracking line search* method.

## The Adjacent Residuals (Search Directions in Steepest Descent) Are Orthogonal

The interesting thing is that the procedure reveals the fact that the two adjacent residules, $r_{(i+1)}$ and $r_{(i)}$, are *orthogonal* to each other. This can be proved by calculating the derivative of $f(x_{(i+1)})$ with the chain rule, which is

$$\frac{\partial f(x_{(i+1)})}{\partial\alpha_{(i)}}=\nabla f(x_{(i+1)})\frac{\partial}{\partial\alpha_{(i)}}x_{(i+1)}=-r_{(i+1)}r_{(i)}=0.\qquad(3)$$

## The Steepest Descent Method

The steepest descent method can be summarized as

||Steepest Descent Method|
|:---|:---|
|1|$r_{(i)}=b-Ax_{(i)}$|
|2|$\alpha_{(i)}=\frac{r^{T}_{(i)}r_{(i)}}{r^{T}_{(i)}Ar_{(i)}}$|
|3|$x_{(i+1)}=x_{(i)}+\alpha_{(i)}r_{(i)}$|

The above algorithm requires two matrix-vector multiplications per iteration, which are $Ax_{(i)}$ at Step 1 and $Ar_{(i)}$ at Step 2. Actually, the residual can also be updated iteratively by $r_{(i+1)}=r_{(i)}-\alpha_{(i)}Ar_{(i)}$ instead of calculating at Step 1, resulting from multiplying Eq. (2) by $-A$ and adding $b$. As a result, only one matrix-vector multiplication, $Ar_{(i)}$ is required.

## The Speed of Convergence of Steepest Descent

We can see that the matrix $A$ plays a very important role since all the steps of the algorithm involve $A$. The *error*, defined by $e_{(i)}=x_{(i)}-x^{\text{opt}}$ where $x^{\text{opt}}$ is the optimal point, will give a clear picture how the relation between $A$ and $x$ affects the speed of convergence. By subtracting $x^{\text{opt}}$ from both sides of Eq. (2), we can see the error iterates as $e_{(i+1)}=e_{(i)}+\alpha_{(i)}r_{(i)}$. Note that the error at each iteration is unknown during the algorithm, because the knowledge of optimal solution indicates the end of the algorithm.

Consider one example that if the error at the $i$-th iteration lies on one of the eigenvectors of $A$. The search direction coincides with the direction of $e_{(i)}$ due to $r_{(i+1)}=-Ae_{(i)}=-\lambda_ee_{(i)}$. The error at the next iteration is

$$e_{(i+1)}=e_{(i)}+\alpha_{(i)}r_{(i)}=e_{(i)}+\frac{r^{T}_{(i)}r_{(i)}}{\lambda_er^T_{(i)}r_{(i)}}(-\lambda_ee_{(i)})=0.$$

The new error becomes zero. On the other words, if the error is one of the eigenvectors of $A$, the algorithm will produce the optimal at the next iteration. This example can give a first impression that the closer the error to one of the eigenvectors of $A$ is, the faster the algorithm can converge.

***<TO DO: convergence in general case>***

## Summary of Notations

Consider the optimization problem in Eq. (1).

| Notation | Expression | Notes |
|:---:|:---:|:---:|
|Gradient|$\nabla f(x)=Ax-b$|The gradient is the direction of *greatest* increase of $f(x)$|
|Residual|$r_{(i)}=-\nabla f(x_{(i)})=b-Ax_{(i)}$|Is the negative direction of gradient. The residual measures how close $Ax$ approaches $b$. Since the optimum is obtained if $Ax-b=0$, we would like have the residual as small as possible. |
|Residual Update|$r_{(i+1)}=r_{(i)}-\alpha_{(i)}Ar_{(i)}$|Multiply Eq. (2) by $-A$ and adding $b$.|
|Error|$e_{(i)}=x_{(i)}-x^{\text{opt}}$|It measures the distance between the current $x$ and the optimal $x$.|
|Error Update in Steepest Descent|$e_{(i+1)}=e_{(i)}+\alpha_{(i)}r_{(i)}$|Subtracting $x^{\text{opt}}$ from Eq. (2).|
|Residual-Error Relation|$r_{(i)}=-Ae_{(i)}$|The residual (and also the gradient) is the linear transform of $x_{(i)}$ with matrix $A$.|

# From Steepest Direction to Conjugate Direction

The steepest descent method may be slow in some cases, suce as if $A$ is ill-conditioned.

# References

- Shewchuk, J. R. (1994). *An introduction to the conjugate gradient method without the agonizing pain*. Carnegie Mellon University.
