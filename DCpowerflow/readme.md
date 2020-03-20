# DC Power Flow

>Version: 0.0.1  
>Author: itaoxiaoran  
>E-mail: ta0ran@163.com  

## Contents

>[Introduction](#introduction)  
>[DC Power Flow Model](#dc-power-flow-model)  
>[Module Required](#module-required)  
>[How to Use this Code  ](#how-to-use-this-code)  
>[Example](#example)  

## Introduction

DC power flow model is a kind of imprecise power flow model, which is widely used in power system, especially in power system planning and contingency analysis. 

When you do not care the reactive power or voltage amplitude, the <u>DC Power Flow Model</u> will match your needs.

## DC Power Flow Model

​	In DC Power Flow Model, nonlinear model of the AC system is simplified to a linear form through these assumptions:  

• Line resistances (active power losses) are negligible i.e. $R<<X$ .  
• Voltage angle differences are assumed to be small i.e. $sin(\theta) = \theta$ and
$cos(\theta)=1$.  
• Magnitudes of bus voltages are set to 1.0 per unit (flat voltage profile).  
• Tap settings are ignored.   

​	Based on the above assumptions, voltage angles and active power injections are
the variables of DC Power Flow. Active power injections are known in advance. Therefore
for each bus $i$ in the system is converted to
$$
P_{i}=\sum_{j=1}^{N} B_{i j}\left(\theta_{i}-\theta_{j}\right)
$$
in which $B_{ij}$ is the reciprocal of the reactance between bus $i$ and bus $j$. As
mentioned earlier, $B_{ij}$ is the imaginary part of $Y_{ij}$.
	As a result, active power flow through transmission line $i$, between buses s and
$r$, can be calculated from.
$$
P_{L i}=\frac{1}{X_{L i}}\left(\theta_{s}-\theta_{r}\right)
$$
where $X_{Li}$ is the reactance of line $i$.

​	DC power flow equations in the matrix form and the corresponding matrix relation for flows through branches are represented as following:
$$
\begin{aligned}
&\theta=[\mathbf{B}]^{-1} \mathbf{P}\\
&\mathbf{P}_{\mathbf{I}}=(\mathbf{b} \times \mathbf{A}) \theta
\end{aligned}
$$
where

|                | Descriptions                                                 |
| -------------- | :----------------------------------------------------------- |
| $\mathbf{P}$   | $N \times 1$ vector of bus active power injections for buses $1, …, N$ |
| $\mathbf{B}$   | $N \times N$ admittance matrix with $R = 0$                  |
| $\theta$       | $N \times 1$ vector of bus voltage angles for buses $1, …, N$ |
| $\mathbf{P_L}$ | $M \times 1$ vector of branch flows ($M$ is the number of branches) |
| $\mathbf{b}$   | $M \times M$ matrix ($b_{kk}$ is equal to the susceptance of line $k$ and non-diagonal elements are zero) |
| $\mathbf{A}$   | $M \times N$ bus-branch incidence matrix                     |

​	Each diagonal element of $B$ (i.e. $B_{ii}$) is the sum of the reciprocal of the lines reactances connected to bus $i$. The off-diagonal element (i.e. $B_{ij}$) is the negative sum of the reciprocal of the lines reactances between bus $i$ and bus $j$. 

​	$\mathbf{A}$ is a connection matrix in which $a_{ij}$ is 1, if a line exists from bus $i$ to bus $j$; otherwise zero. Moreover, for the starting and the ending buses, the elements are 1 and -1, respectively.

Reference: More details read [this](https://link.springer.com/content/pdf/bbm%3A978-3-642-17989-1%2F1.pdf).(Actually, I just copy this PDF document.)

## Module Required

​	numpy, scipy, pandas


## How to Use this Code

## Examples