# DC Power Flow

>Version: 0.0.1
>Author: itaoxiaoran
>E-mail: ta0ran@163.com

## Contents

>[Introduction](##introduction)
>[DC Power Flow Model](##dc power flow model)
>[How to Use this Code](##how to use this code)
>[Example](##example)

## Introduction

DC power flow model is a kind of imprecise power flow model, which is widely used in power system, especially in power system planning and contingency analysis. 

When you do not care the reactive power or voltage amplitude, the <u>DC Power Flow Model</u> will match your needs.

## DC Power Flow Model

We can describe the transmission line as following:
In DC Power Flow Model, nonlinear model of the AC system is simplified to a linear form
through these assumptions:  
• Line resistances (active power losses) are negligible i.e.$R<<X$ .  
• Voltage angle differences are assumed to be small i.e. $sin(\theta) = \theta$ and
$cos(\theta)$ = 1.  
• Magnitudes of bus voltages are set to 1.0 per unit (flat voltage profile).
• Tap settings are ignored.  
Based on the above assumptions, voltage angles and active power injections are
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
Reference: More details read [this](https://link.springer.com/content/pdf/bbm%3A978-3-642-17989-1%2F1.pdf)




## How to Use this Code

## Example