# Optimization Solvers

## A Summary

Available packages in different programming languages are listed on the [website](https://web.stanford.edu/~boyd/software.html) of Prof. Boyd (from Stanford):

| Languages | Name of Packages | Main Contributors |
| :-------: | :---:            | :---: |
| R         | [CVXR](https://cvxr.rbind.io/) | Stanford University Convex Optimization Group |
| Matlab    | [cvx](http://cvxr.com/) | 
| Python    | [CVXPY](https://www.cvxpy.org/) |


## [Open Source] OSQP Solver

[OSQP](https://osqp.org/docs/index.html), the **O**perator **S**plitting **Q**uadratic **P**rogram solver, is a numerical optimization package for solving problems related to quadratic program.

## [Open Source] SCS Solver by Stanford University Convex Optimization Group

[SCS](https://www.cvxgrp.org/scs/) stands for splitting conic solver, a numerical method for solving large-scale convex cone problems.

## [Open Source] ECOS Solver by Embotech AG

[ECOS](https://github.com/embotech/ecos), **E**mbedded **C**onic **S**olver, is a numerical software for solving convex second-order cone programs.

## [Open Source] DCCP Solver by Stanford University Convex Optimization Group

DCCP, disciplined convex-concave programming, is another package provided by the Stanford University. DCCP is built on top of CVXPY. In the other words, it is an extension of CVXPY. It tries to solve nonconvex problems where every function in the objective and the constraints has any known curvature according to the rules of disciplined convex programming (DCP).

## [Commercial] MOSEK 

MOSEK is not a solver but a commercial software with the capacity of solving a variety of optimization problems such as linear programming, quadratic programming. 

