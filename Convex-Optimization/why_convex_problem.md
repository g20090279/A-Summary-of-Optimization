- Local maximum is global maximum
- For strictly convex, if an optimal point exists, it is unique
- Feasible points that satisfy the first-order conditions of the problem are optimal points of the function
- There are a variety of algorithms that solve convex optimization problem efficiently and reliably. No matter what algorithms are they, the efficiency from solving the convex optimization problem comes from that these algorithm can verify that a point satisfies the first-order conditions before returning it as a solution. Nelder-Mead, Genetic Algorithms, Simulated Annealing algorithms do not have this property, and therefore they are comparatively slow for convex problems.

# Why Convex Problems are "Easy" to Solve

If you are located in some point of the objective function, to solve this optimization problem at this point is that where you should head for the next step. The convexity give you sufficient information about the neighbourhood of the current guess. This is actually the key concept of "locally optimal" and *greedy algorithm*, where each step is determined by its current best choice. The best thing of convex optimization is that the local optimal is also the global one.
