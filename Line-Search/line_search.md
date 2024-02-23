- Topics: Line Search, Unconstrained Optimization
- Last Revised: Jan. 22, 2024

---

# Motivation

Why we have a "line" and what we are searching along this line? These questions may come to our mind when we first come to this topic. In optimization, one very general problem is to study the minimization of an objective function $f:\mathbb{R}^n\rightarrow\mathbb{R}$ without any constraint

$$\min_{x\in\mathbb{R}^n} f(x).\qquad(1)$$

The function $f$ does not need to be convex, so that the optimal point is generally a local minimum. In general, the function does not need to be smooth neither. However, it is usually assumed to be $C^1$ with Lipschitz continous gradient, which is adopted here.

One basic method to find an ultimate point that minizes the objective function is the iterative method, which is, we obtain a new data at each iteration that approaches closer to the optimal data. There are generally three ways to implement this

1. *Gradient-free optimzation*. You can simply use some random guess $p$ to try to minimize the problem step by step with $x_{(i+1)}=x_{(i)}+p$.
2. *First-order methods*. The first derivative called gradient $\nabla f(x_{(i)})$ is used to be the search direction. With a hyperparameter, usually called step size $\alpha_{(i)}$, a new data is obtained by $x_{(i+1)}=x+\alpha_{(i)}\nabla f(x_{(i)})$. Note that for a minimization problem, the function decreases in the negative of gradient direction. In orther words, $\alpha_{(i)}$ is negative.
3. *Second-order methods*. The Hessian is used $x_{(i+1)}=x_{(i)}+\alpha_{(i)}(\nabla^2f(x_{(i)}))^{-1}\nabla f(x_{(i)})$. Computing the Hessian is usually expensive. Some quasi-Newton methods are good approximates to reduce the complexity.

Anyway, we can see that all these three methods can be unified as $x_{(i+1)}=x_{(i)}+\alpha_{(i)}d_{(i)}$. Given a search direction $d_{(i)}$, no matter from first-order methods or second-order methods, we need to 

**find a feasible hyperparameter $\alpha_{(i)}$ such that $f(x_{(i)})>f(x_{(i)}+\alpha_{(i)}d_{(i)})$.**

It is the same as searching a good step size along a line, and this is where the name "line search" comes from. An alternative that approaches the optimal point by formulating update scheme differently from Eq. (1) is the class of *trust-region methods*. The trust-region methods are very powerful, but line search methods are conceptually simple and work well in practice for integrating with existing optimizer implementations.

# Generic Line Search Method

1. Pick an initial iterate $x_{(0)}$ by educated guess, set $k=0$.
2. Until converged
   1. Calculate a search direction $d_{(i)}$ from $x_{(i)}$, ensuring that this direction is a *descent direction*, that is if $\nabla f(x_{(i)})\neq0$
      $$(\nabla f(x_{(i)}))^Td_{(i)}<0$$
      so that for small enough steps away from $x_{(i)}$ in the direction $d_{(i)}$ the objective function will be reduced.
   2. Calculate a suitable *step size* $\alpha_{(i)}>0$ so that
      $$f(x_{(i)}+\alpha_{(i)}d_{(i)})<f(x_{(i)}).$$ 
      The computation of $\alpha_{(i)}$ is called *line search*, and this is usually an inner iterative loop.
   3. Set $x_{(i+1)}=x_{(i)}+\alpha_{(i)}d_{(i)}$.

Acutal methods differ from one another in how search direction and step size are computed.

# Exact and Inexact Line Search

One can obtain $\alpha_{(i)}$ by minimizing $f(x_{(i)}+\alpha_{(i)}d_{(i)})$ exactly or inexactly.

- *Exact line search* is done by computing $\partial f(x_{(i)}+\alpha_{(i)}d_{(i)})/\partial\alpha_{(i)}=0$. This approach can be inefficient in calculating the derivative, and sometimes becomes impossible.
- *Inexact line search (more common approach)* overcomes this disadvantage by approximating the optimal $\alpha_{(i)}$. Practically, an exact solution of $\alpha_{(i)}$ obtained by substantial computational or storage resources is not desired, because the current search direction is not always optimal neither. The iterative method iterates with step size and search direction, and what we want is to acquire a reasonable step size and then a reasonable new search direction based on the new data. In a word, the exactly optimal step size at one particular iteration doesn't provide better performance in terms of global complexity than a reasonably estimated one. One standard inexact search is called *[backtracking line search](backtracking_line_search.md)*.

  The phrases from Wikipedia illustrate very well the tradeoff between computing the step size and computing the search direction:

  > This is because the computing resources needed to find a more precise minimum along one particular direction could instead be employed to identify a better search direction. Once an improved starting point has been identified by the line search, another subsequent line search will ordinarily be performed in a new direction. The goal, then, is just to identify a value of α \alpha that provides a reasonable amount of improvement in the objective function, rather than to find the actual minimizing value of $\alpha$.
