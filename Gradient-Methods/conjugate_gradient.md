- **Topics**: Conjugate Gradient Descent Method
- **Last Revised**: Dec. 27, 2023 
- **Author**: Zekai Liang (zekai.liang [at] hotmail [dot] com)

---

The deepest descent method iterates along the gradient, which is the fastest decrease (if not mentioned specifically, we consider a convex minimization problem). It is interesting to see that feastest decrease at each step does not necessarily result in fastest path on the whole, where the fastness is measured by the number of iterations until the iterative algorithm ends. In fact, convergence of steepest descent is fast if the condition number of $A$ is small (Shewchuk, 1994, Fig. 17). On the contrary, a large condition number of $A$ can be bad for convergence (not necessary, there will be higher chance for slow convergence in the case of large condition number. However, we one can chose the starting point to lie on or very closely on one of the eigenvectors of $A$, the convergence can also be very fast, e.g. just one step. More detail are given in (Shewchuk, 1994, §6.2)).

# Review of Linear Gradient Descent

Initially, the gradient descent methods are discovered to solve the system of linear equations, which is $Ax=b$ and $x=[x_1,x_2,\cdots,x_n]^T\in\mathbb{R}^n$. From the point of view of optimization theory, solving $Ax=b$ is equivalent to obtain the optimum of the following optimization problem

$$\min_{x\in\mathbb{R}^n}f(x)=\frac{1}{2}x^TAx-b^T+c,\qquad(1)$$

where $A$ is assumed to be positive-definite matrix, with which the optimization problem becomes convex. $A$ is further assumed to be symmetric, where exactly $n$ orthogonal vectors exist and form an orthogonal basis. With the symmetricity of $A$, the derivative of $f$ is $\nabla f(x)=f^\prime(x)=\left[\frac{\partial f}{\partial x_1},\frac{\partial f}{\partial x_2},\cdots,\frac{\partial f}{\partial x_n}\right]^T=Ax-b$, resulting in $Ax-b=0$ at the optimal point. $\nabla f(x)$ is also called *gradient*, the direction of greatest increase of $f(x)$ for a given $x$. The greatest decrease heads opposite to $\nabla f(x)$. Now, we define the residual at i-th iteration $r_{(i)}=-\nabla f(x_{(i)})=b-Ax_{(i)}=-\nabla f(x_{(i)})$ at point $x$. The iterative approach can be formed to approach the optimum value step by step as

$$x_{(i+1)}=x_{(i)}+\alpha_{(i)}r_{(i)}.\qquad(2)$$

Note that the subscript with parentheses donotes the index of the iteration. We can see that the search direction of the steepest descent method is the residual, which is the negative of the gradient. The iterative method of form in Eq. (2) has another name called *line search method*. This name comes from that finding the optimal $\alpha_{(i)}$ is to search an optimal point along a line. 

## Determine the Optimal Step Size: Line-Searching Algorithm

The step size $\alpha_{(i)}$ can be found both exactly and inexactly. In this quadratic-objective optimization problem, the step size can be found exactly, which is to let the derivative of $f(x_{(i+1)})$ w.r.t. $\alpha_{(i)}$ be zero, resulting in $\alpha_{(i)}=r^{T}_{(i)}r_{(i)}/(r^{T}_{(i)}Ar_{(i)})$.

The inexact line search can be considered if it is difficult to obtain an analytical equation for $\alpha_{(i)}$ from Eq. (3). One example is the *backtracking line search* method.

## The Adjacent Residuals (Search Directions in Steepest Descent) Are Orthogonal

The interesting thing is that the procedure reveals the fact that the two adjacent residules, $r_{(i+1)}$ and $r_{(i)}$, are *orthogonal* to each other. This can be proved by calculating the derivative of $f(x_{(i+1)})$ with the chain rule, which is

$$\frac{\partial f(x_{(i+1)})}{\partial\alpha_{(i)}}=\nabla^Tf(x_{(i+1)})\frac{\partial}{\partial\alpha_{(i)}}x_{(i+1)}=-r_{(i+1)}^Tr_{(i)}=0.\qquad(3)$$

Furthermore, the error at (i+1)-th iteration is orthogonal to the residual (remind that the residual is the same as the search direction), which is $-r_{(i)}^Tr_{(i)}=(Ae_{(i+1)})^Tr_{(i)}=e_{(i+1)}^TAr_{(i)}$.

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

The steepest descent method may be slow in some cases, such as if $A$ is ill-conditioned. Remind that the optimality of exact search of step size ensures the adjacents search directions are orthogonal. It results in the fact that the algorithm may step into the same search direction many times. Why not just adjust the search directions and the corresponding optimal step size, make sure that only one search is done in the same search direction. This is the basic idea of conjugate descent method. If $x\in\mathbb{R}^{n}$, the conjugate descent guarantees that the optimal point is reached at most n iterations.

Let's denote the search direction at $i$-th iteration as $d_{(i)}$. Similar to the steepest descent method, the point will be updated at each iteration with a specific step size at a specific direction. Describing it mathematically, we have

$$x_{(i+1)}=x_{(i)}+\alpha_{(i)}d_{(i)}.\qquad(4)$$

From this update scheme, it remains to define the N search directions and the corresponding step sizes. From the intuition, we should impose some constraints on the search directions, so that any vector in $\mathbb{R}^n$, say $e_{(i)}$, can be represented by n different search directions.

## Possibility 1 (Not Feasible): Search Directions Are Orthogonal

Consider an initial point $x_{(0)}$ and the optimal point $x^{\text{opt}}$. An error vector $e_{(0)}=x_{(0)}-x^{\text{opt}}$ is in the Euclidean space $\mathbb{R}^n$ as well. One intuition is to find an orthogonal basis to represent the initial error at that basis. With that basis, we only need to find the weights of the n orthogonal vectors, and use it as the step sizes. Then we can attain the optimal point in maximum n steps. In conclusion, the search directions in conjugate descent method are constrained to be orthogonal to each other, while in the steepest descent method are only the two adjacent search directions orthogonal to each other.

An interesting observation is that the updated remaining error $e_{(i+1)}$ is always orthogonal to all the previous search directions $d_{(0)},d_{(1)},\cdots,d_{(i)}$, so that the same search direction would not be used again. The step size $\alpha_{(i)}$ can be obtain from $d_{(i)}^{T}e_{(i+1)}=0$, since $d_{(i)}^{T}(e_{(i)}+\alpha_{(i)}d_{(i)})=0$ results in $\alpha_{(i)}=-d_{(i)}^Te_{(i)}/(d_{(i)}^Td_{(i)})$.

However, we don't have any information about $e_{(i)}$ until we solve the problem to know $x^{\text{opt}}$. Therefore, we have no chance to calculate the step size if we use the orthogonal basis as the search directions.

## Possibility 2 (Feasible): Search Directions Are A-Orthogonal (Conjugate)

Two vectors (search directions) $d_{(i)}$ and $d_{(j)}$ are *A-orthogonal* or *conjugate* if

$$d_{(i)}^{T}Ad_{(j)}=0.$$

Similarly, the error $e_{(i+1)}$ is required to be A-orthogonal instead of orthogonal to $d_{(i)}$, which is $d_{(i)}^TAe_{(i+1)}=0$. In other words, this requirement says that the gradient should be orthogonal to the previous search direction. Let's have a look if it is feasible to compute the step size. The step size can be obtained by reranging $d_{(i)}^TA(e_{(i)}+\alpha_{(i)}d_{(i)})=0$

$$\alpha_{(i)}=-\frac{d_{(i)}^TAe_{(i)}}{d_{(i)}^TAd_{(i)}}=\frac{d_{(i)}^Tr_{(i)}}{d_{(i)}^TAd_{(i)}},\qquad(5)$$

where the residual $r_{(i)}$ can be computed iteratively as well, which will be illustrated later.

### Common Stretegy for Optimal Step Size between Steepest Descent and Conjugate Descent

One common point between conjugate descent with A-orthogonality constraint and steepest descent is that the step sizes are found by minimizing the function along the search direction $d_{(i)}$, since according to the definition of residual and Eq. (4), we have

$$\frac{\partial}{\partial\alpha_{(i)}}f(x_{(i+1)})=\nabla^Tf(x_{(i+1)})\frac{\partial}{\partial\alpha}x_{(i+1)}=-r_{(i+1)}^{T}d_{(i)}=d_{(i)}^TAe_{(i+1)}=0.$$

If the search direction $d_{(i)}$ is same as residual, the conjugate descent method is same as the steepest descent. Hence, these two descent methods differ only in the selection (or constraints) of the search directions. 

### Prove that n A-Orthogonal Vectors Can Form A Basis

It remains to prove that every vector in $\mathbb{R}^n$, say the initial error vector $e_{(0)}$, can be represented by n A-orthogonal vectors, so that the error can be eliminated at most n steps. From every step further, that A-orthogonal vector component will be removed. Let's assume n search directions, $d_{(0)}$, $d_{(1)}$, ..., $d_{(n-1)}$, are A-orthogonal to each other, i.e., $d_{(i)}Ad_{(j)}=0$. The initial error must be able to have form $e_{(0)}=\sum_{j=0}^{n-1}\delta_{(j)}d_{(j)}$. If we can find feasible coefficients $\delta_{(j)}$, we can assert that A-orthogonal vectors can form a basis. Since A-orthogonal, only the same search direction component remains if $e_{(0)}$ is multiplied by $d_{(i)}^TA$, which is $d_{(i)}^TAe_{(0)}=\delta_{(i)}d_{(i)}^TAd_{(i)}$. Rearrange the equation, we have $\delta_{(i)}=d_{(i)}^TAe_{(0)}/(d_{(i)}^TAd_{(i)})$. With the A-orthogonal properties, we can change $e_{(0)}$ to any $e_{(i)}$. However, it is interesting to see that

$$\delta_{(i)}=\frac{d_{(i)}^TAe_{(i)}}{d_{(i)}^TAd_{(i)}}=-\frac{d_{(i)}^Tr_{(i)}}{d_{(i)}^TAd_{(i)}}=-\alpha_{(i)}.$$

It reveals the fact that the error update scheme $e_{(i+1)}=e_{(i)}+\alpha_{(i)}d_{(i)}$ indicates that the error on the A-orthogonal search direction will be gradually removed, as $e_{(i+1)}=e_{(i)}-\alpha_{(i)}d_{(i)}$. Since contribution of one search direction will be eliminated at every step, the current error comprises the contribution only from the current and the remaining search directions

$$e_{(i)}=\sum_{j=i}^{n-1}\delta_{(j)}d_{(j)}.$$

### The Name "Conjugate Descent"

To this point, it is clear that the word "conjugate" in the name of "conjugate descent method" comes from the introduced constraint on the search directions. The search directions are conjugate (A-orthogonal). In other words, the search directions are orthogonal in a stretched space (stretched by A).

# The Conjugate Method: Continue the Possibility 2

So far we have already known how to obtain the optimal step size. From Eq. (5), we still need to obtain two things, the search directions and the residuals.

## Find Search Directions: Gram-Schmidt Conjugation

### Review of Gram-Schmidt Orthogonalization

Consider the Euclidean space $\mathbb{R}^n$ equipped with standard inner product $\langle u,v\rangle=u^Tv$. This is the mostly practical space in the reality. The Gram-Schmidt process is to transform a set of independent vectors to a set of independent and orthogonal vectors. Take two vectors $u$ and $v$ as a simple and initial example. The idea to orthogonalize these two vectors is based on the fact that any vector in $\mathbb{R}^n$, say $u$, can be decomposed to the two parts with respect to another vector, say $v$, one parallel to $v$ and on orthogonal to $v$, as $u=u_{\|v}+u_{\perp v}$. The component of $u$ parallel to $v$ is also called the *projection* of $u$ on $v$.

The inner product of $u$ and $v$ equals $\langle u,v\rangle=\|u\|\|v\|\cos\theta$ as well, where $\theta$ is the angle between $u$ and $v$. From this on, we can write the projection of $u$ on $v$ as

$$\text{proj}_u(v)=\frac{\langle u,v\rangle}{\langle v,v\rangle}v.$$

Once $\text{proj}_u(v)$ is subtracted from $u$, the remaining part is perpendicular (orthogonal) to the reference vector $v$. Similarly, if we have multiple vectors, to obtain a vector that orthogonal to the others, what we can do is to subtract the projections on the other vector from this vector, and we are done. We can conclude now the Gram-Schmidt orthogonalization can be described as follows

|Algorithm|Gram-Schmidt Orthogonalization Process|
|:---|:---|
||Given n linearly independent vectors $u_1,u_2,\cdots,u_n$|
|1|$v_1=u_1$|
|2|$v_2=u_2-\text{proj}_{v_1}(u_2)$|
|3|$v_3=u_3-\text{proj}_{v_1}(u_3)-\text{proj}_{v_2}(u_3)$|
|$\vdots$|$\vdots$|
|n|$v_n=u_n-\text{proj}_{v_1}(u_n)-\cdots-\text{proj}_{v_{n-1}}(u_n)$|

### The Gram-Schmidt Conjugation Process

With the experience from Gram-Schmidt Orthogonalization, we should be able to deal with multiple vectors. Suppose we have $n$ linearly independent vectors $u_1,u_2,\cdots,u_n$. Similar to the orthogonalization process, to construct the A-orthogonal search direction $d_{(i)}$, we can subtract any components that are not A-orthogonal to the previous search directions from $u_i$. In other words, we define

$$d_{(i)}=u_i+\sum_{k=1}^{i-1}\beta_{ik}d_{(k)},$$

where $i>k$. To obtain $\beta_{ik}$, we use the A-orthogonalitty between $d_{(i)}$ and any previous vector $d_{(j)}$ where $j<i$

$$d_{(i)}^TAd_{(j)}=u_i^TAd_{(j)}+\sum_{k=1}^{i-1}\beta_{ik}d_{(k)}^TAd_{(j)}=u_i^TAd_{(j)}+\beta_{ij}d^T_{(j)}Ad_{(j)}=0,$$

resulting in

$$\beta_{ij}=-\frac{u_i^TAd_{(j)}}{d^T_{(j)}Ad_{(j)}}.$$

|Algorithm|Gram-Schmidt Conjugation Process|
|:---|:---|
||Given n linearly independent vectors $u_1,u_2,\cdots,u_n$|
|1|$d_{(1)}=u_1$|
|2|$d_{(2)}=u_2+\beta_{21}d_{(1)}$, where $\beta_{21}=-\frac{u_2^TAd_{(1)}}{d_{(1)}^TAd_{(1)}}$|
|3|$d_{(3)}=u_3+\beta_{31}d_{(1)}+\beta_{32}d_{(2)}$, where $\beta_{31}=-\frac{u_3^TAd_{(1)}}{d_{(1)}^TAd_{(1)}}$ and $\beta_{32}=-\frac{u_3^TAd_{(2)}}{d_{(2)}^TAd_{(2)}}$|
|$\vdots$|$\vdots$|
|n|$d_{(n)}=u_n+\sum_{k=1}^{n-1}\beta_{nk}d_{(k)}$, where $\beta_{nk}=-\frac{u_i^TAd_{(k)}}{d^T_{(k)}Ad_{(k)}}$|

## Find the Residuals: Similar Update Scheme As Steepest Descent

Remind that the error $e_{(i)}$ is A-orthogonal to all its previous search directions $d_{(j)}$ where $j=0,1,\cdots,i-1$. The residual $r_{(i)}=-Ae_{(i)}$ is *orthogonal* (NOT A-orthogonal) to the previous search directions. Put the error update scheme in this property, we have the residual update scheme

$$r_{(i+1)}=r_{(i)}-\alpha_{(i)}Ad_{(i)},\qquad(6)$$

where $\alpha_{(i)}$ is obtained from Eq. (5) and the search directions are obtained by the Gram-Schmidt Conjugate procedure.

### Use Residuals as Initial Vectors in Gram-Schmidt Conjugation Process

Besides, the residuals $r_{(0)},r_{(1)},\cdots,r_{(n-1)}$ can be used as the initial set of $n$ independent vectors. It requires the residuals are linearly independent. It is true under the requirement in conjugate descent method that the error is A-orthogonal to previous search directions. With Eq. (5) and Eq. (6), we can prove that $r_{(i)}^Tr_{(j)}=0$ for $i\neq j$. Therefore, there are two facts for the residual, (1) the residuals are orthogonal to all previous search directions, (2) the residuals are orthogonal to all previous residuals. Due to the orthogonality, the residuals are linearly independent, and can be used as the initial vectors for Gram-Schmidt Conjugation process.

The search vector is linear transformation of the current and previous residuals according to the Gram-Schmidt Conjugation process. The implication of choosing residuals as the initial vectors tells that the subspace $\text{span}\{r_{(0)},r_{(1)},\cdots,r_{(i-1)}\}$ is the subspace $\mathcal{D}_i$ spanned by $d_{(0)},d_{(1)},\cdots,d_{(i-1)}$. This implication leads to another interesting finding based on Eq. (6). We can see the new residual $r_{(i+1)}$ is the linear combination of the previous residual $r_{(i)}$ and the previous search direction $Ad_{(i)}$. The new subpace $\mathcal{D}_{i+1}$ is then the union of $\mathcal{D}_i$ and $A\mathcal{D}_i$. We know $r_{(i+1)}$ is orthogonal to $\mathcal{D}_{i+1}$, it is also orthogonal to $\mathcal{D}_i$ and $A\mathcal{D}_i$, which means that it is A-orthogonal to $\mathcal{D}_i$.

The Gram-Schmidt constant becomes $\beta_{ij}=-\frac{r_{(i)}^TAd_{(j)}}{d_{(j)}^TAd_{(j)}}$ by replacing $u_i$ with $r_{(i)}$. Normally, to compute the new search direction $d_{(i)}$, we need to store and use the all previous search directions $j=0,1,\cdots,i-1$, and the coeffients are different for any $i$ and $j$. As the residuals being the base sequence in Gram-Schmidt Conjugate process, we can exploit the properties of residuals (a residual is orthogonal to all previous search directions, is orthogonal to all previous residuals, and is A-orthogonal to the space spanned by all the search directions up to the second previous residual.). We observe that only the numerator of $\beta_{ij}$ includes the residual. We can try to apply the orthogonal property to see what we can derive. Say, put the update scheme of $r_{(j+1)}$ into $r_{(i)}^Tr_{(j)}$, we got $r_{(i)}^Tr_{(j+1)}=r_{(i)}^Tr_{(j)}-\alpha_{(j)}r_{(i)}^TAd_{(j)}$. After rearranging the both sides, we can obtain an equivalence of the numerator of $\beta_{ij}$, which is $\alpha_{(i)}^Tr_{(i)}^TAd_{(j)}=r_{(j)}^Tr_{(j)}-r_{(i)}^Tr_{(j+1)}$. Considering the right-hand side of the equality, if $i=j$, the second term $r_{(i)}^Tr_{(j+1)}=0$. If $i=j+1$, the first term $r_{(i)}^Tr_{(j)}=0$. In other cases, both terms are zero. Note that the definition of $\beta_{ij}$ constrains that the maximum $j$ is $i-1$. Therefore, if $j=i-1$, $r_{(i)}^TAd_{(j)}=-r_{(i)}^Tr_{(i)}/\alpha_{(j)}$. Otherwise, $r_{(i)}^TAd_{(j)}=0$. In conclusion,

$$\beta_{ij}=\begin{cases}\frac{1}{\alpha_{(i-1)}}\frac{r^T_{(i)}r_{(i)}}{d_{(i-1)}^TAd_{(i-1)}},&i=j+1,\\0,&i>j+1.\end{cases}$$

This means for some fixed $i$, only one $j$ index, $j=i-1$, results in non-zero $\beta_{ij}$. For simplicity, we can leave out any non-zero items, and write $\beta_{(i)}=\beta_{i,i-1}$ as

$$\beta_{(i)}=\frac{r_{(i)}^Tr_{(i)}}{d_{(i-1)}^Tr_{(i-1)}}=\frac{r_{(i)}^Tr_{(i)}}{r^T_{(i-1)}r_{(i-1)}}.$$

The first equality is obtained by using optimal step size $\alpha_{(i)}$ in Eq. (5). The second equality results from $d^T_{(i)}r_{(j)}=r_{(i)}^Tr_{(j)}+\sum_{k=0}^{i-1}\beta_{ik}d_{(k)}^Tr_{(j)}$, and $0=r_{(i)}^Tr_{(j)}$ for $i<j$ while $d_{(i)}^Tr_{(i)}=r_{(i)}^Tr_{(i)}$ for $i=j$.

## The Method Of Conjugate Gradients

|Algorithm|(Linear) Conjugate Gradients|
|:---|:---|
|1. initial search direction & residuals [Note-1]|$d_{(0)}=r_{(0)}=b-Ax_{(0)}$|
|2. step size|$\alpha_{(i)}=\frac{r_{(i)}^Tr_{(i)}}{d_{(i)}^TAd_{(i)}}$|
|3. update data|$x_{(i+1)}=x_{(i)}+\alpha_{(i)}d_{(i)}$|
|4. update residual|$r_{(i+1)}=r_{(i)}-\alpha_{(i)}Ad_{(i)}$|
|5. update Gram-Schmidt constant|$\beta_{(i+1)}=\frac{r_{(i+1)}^Tr_{(i+1)}}{r_{(i)}^Tr_{(i)}}$|
|6. find new search direction by Gram-Schmidt process|$d_{(i+1)}=r_{(i+1)}+\beta_{(i+1)}d_{(i)}$|
|(CG is complete after n iterations)||

Note-1: If a rough estimation of x is avaialbe, use it as the initial x. If not, set $x_{(0)}=0$.

# Nonlinear Conjugate Gradient Method

Conjugate Gradient method can find the minimum of not only a quadratic form, but also any continuous function. Without the linear form of gradient (quadratic form of objective function), many equivalent expressions in the linear case are no longer true in the nonlinear case. Above all, let's have a look at the nonlinear Conjugate Gradient method

|Algorithm|(Nonlinear) Conjugate Gradients|
|:---|:---|
|1. initial search direction & residual|$d_{(0)}=r_{(0)}=-f^\prime(x_{(0)})$|
|2. step size|Find $\alpha_{(i)}$ that minimizes $f(x_{(i)}+\alpha_{(i)}d_{(i)})$|
|3. update data|$x_{(i+1)}=x_{(i)}+\alpha_{(i)}d_{(i)}$|
|4. update residual|$r_{(i+1)}=-f^\prime(x_{(i+1)})$|
|5. update Gram-Schmidt constant|Choose one of the update schemes|
|6. find new search direction by Gram-Schmidt process|$d_{(i+1)}=r_{(i+1)}+\beta_{(i+1)}d_{(i)}$|
|(CG is complete after n iterations)||

The algorithm structures are the same in linear and nonlinear conjugate gradient methods. Some changes are done due to the nonlinearity. First, some terms lose their intrinsic meaning. For example, 'residual' is used to refer the remaining from $Ax$ to $b$, which equals the negative of the gradient. Because of the nonlinearity, the residual doesn't represent such difference and can be considered to be defined as the negative of the gradient.

Second, due to the nonlinearity, some parameters become more difficult to be obtained. One is the step size $\alpha_{(i)}$. $r_{(i)}\neq-Ae_{(i)}$ results in that $\alpha_{(i)}$ can not be computed as Eq. (5). The line search becomes more difficult in the nonlinear case. Another example is the Gram-Schmidt constant $\beta_{(i)}$. There are many other equalities resulting from the linearity are no longer valid, which are not listed one by one here.

||Linear CG|Nonlinear CG|Comment|
|:---|:---|:---|:---|
|Objective Function|$f(x)=\frac{1}{2}x^TAx-b^T+c$|any countinuous function $f(x)$||
|Griadient|$f^\prime(x)=Ax-b$|$f^\prime(x)$||
|Residual|$r(x_{(i)})=b-Ax_{(i)}=-f^\prime(x_{(i)})$|$r(x_{(i)})=-f^\prime(x_{(i)})$||
|Search Direction|$d_{(i)}$, A-orthogonal to each other, generated by Gram-Schmidt conjugation process with residuals as base sequence|same||
|Requirement of Conjugation|Equivalent expressions: (1) Gradient is orthogonal to the previous search direction $d^T_{(i)}f^\prime(x_{(i+1)})=0$. (2) $d_{(i)}^TAe_{(i+1)}=0$ (3) $r_{(i+1)}^Td_{(i)}=0$. |Gradient is orthogonal to the previous search direction $\left[f^\prime(x_{(i)}+\alpha_{(i)}d_{(i)})\right]^Td_{(i)}$||
|Update Data|$x_{(i+1)}=x_{(i)}+\alpha_{(i)}r_{(i)}$|$x_{(i+1)}=x_{(i)}+\alpha_{(i)}d_{(i)}$||
|Update Gram-Schmidt Constant|Several equivalent expressions, one is $\beta_{(i+1)}=\frac{r_{(i+1)}^Tr_{(i+1)}}{r_{(i)}^Tr_{(i)}}$|(1) Fletcher-Reeves formula (Fletcher, 1964) $\beta_{(i+1)}^{\text{FR}}=\frac{r_{(i+1)}^Tr_{(i+1)}}{r_{(i)}^Tr_{(i)}}$. (2) Polak-Ribière formula (Polak, 1969) $\beta_{(i+1)}^{\text{PR}}=\frac{r_{(i+1)}^T(r_{(i+1)}-r_{(i)})}{r_{(i)}^Tr_{(i)}}$||

# References

- Fletcher, R.; Reeves, C. M. (1964). "Function minimization by conjugate gradients". The Computer Journal. 7 (2): 149–154. doi:10.1093/comjnl/7.2.149
- Polak, E.; Ribière, G. (1969). "Note sur la convergence de méthodes de directions conjuguées". Revue Française d'Automatique, Informatique, Recherche Opérationnelle. 3 (1): 35–43. 
- Shewchuk, J. R. (1994). *An introduction to the conjugate gradient method without the agonizing pain*. Carnegie Mellon University.
