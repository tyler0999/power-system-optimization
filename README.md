#  Power System Optimization
## This is a notice
> Version：0.0.1  
> Author：itaoxiaoran  
> E-mail：ta0ran@163.com  

 >About me : Hello, my name is itaoxiaoran. I am just an ordinary student researching on power system optimization.
 I wish to share with you some contents (theories, codes, etc.) in my usual study through this project. This project is named "power system optimization" mainly to distinguish it from other fields of power system, such as stability analysis, power electronics, etc. I believe that you can see some seemingly common methods in normal literature reading, but you don't know how to use the program to realize them. I will share what I have realized in the form of "detailed description + code" to you, so as to avoid you from making wheels repeatedly.
 Welcome to discuss, exchange and improve the project with me~ 

The following functions have been developed and are waiting to be sorted out and summarized .  
Function | Programming language or file format| Expected release time | Actual release time 
-|-|-|-
DC power flow | Python | 2020.5 | 
AC power flow| Python | 2020.5 |
Multi-Obj optimal power flow | Python | 2020.5 |
Transferring Matpower case file to .csv | .csv               | 2020.4|
A small amount of real active load data | .csv               | 2020.6 |
Uniform pricing market clearance | Python             | 2020.8 |
 Nodal pricing market clearance | Python             | 2020.8 |
Joint energy and reserve market clearance | Python             | 2020.8 |
 My first Blog for this project | ——                 | May be blew you off |

If you have other demands, you can **pull the Issues** or email me. Maybe I wrote them, but they haven't been sorted out, I will upload them~

## Before use and read most page in this repository.

If you cannot see the formula normally as following:
$$
\begin{aligned}
P_{i j}+\mathrm{j} Q_{i j} &=\dot{V}_{i} \hat{I}_{i j}=\dot{V}_{i}\left(\hat{I}^{\prime}++\hat{I}^{\prime \prime}\right) \\
&=\dot{V}_{i}\left[\hat{V}_{i}\left(G_{i 0}-\mathrm{j} B_{i 0}\right)+\left(\hat{V}_{i}-\hat{V}_{j}\right)\left(G_{i j}-j B_{i j}\right)\right] \\
&=\dot{V}_{i}\left(\hat{V}_{i} G_{i 0}-\mathrm{j} \hat{V}_{i} B_{i 0}+\hat{V}_{i} G_{i j}-j \hat{V}_{i} B_{i j}-\hat{V}_{j} G_{i j}+j \hat{V}_{j} B_{i j}\right)
\end{aligned}
$$


You'd better install the Chrome plugin:[MathJax Plugin for Github](https://chrome.google.com/webstore/detail/mathjax-plugin-for-github/ioemnmodlmafdkllaclgeombjnmnbima/related) to view the Latex formula normally.

and, the code of this repository require the special module:

1. [pyomo-the Pyomo optimization modeling software](https://github.com/Pyomo/pyomo)

   `pip install pyomo`

2. [geatpy-Evolutionary algorithm toolbox and framework with high performance for Python](https://github.com/geatpy-dev/geatpy)

   `pip install geatpy`

3. **Any Solvers** supported by Pyomo for solving LP problems, i.e. glpk, gurobi, cplex, etc.

## Contents

Transferring Matpower case file to .csv

[DC Power Flow](https://github.com/itaoxiaoran/power-system-optimization/tree/master/DCpowerflow)

[AC Power Flow](https://github.com/itaoxiaoran/power-system-optimization/tree/master/ACpowerflow)

[Multi-Object Optimal Power Flow](https://github.com/itaoxiaoran/power-system-optimization/tree/master/MultiObjPowerFlow)

[A Small Amount of  Real Active Load Data](https://github.com/itaoxiaoran/power-system-optimization/tree/master/RealActiveLoadData)

[Uniform Pricing Market Clearance](https://github.com/itaoxiaoran/power-system-optimization/tree/master/ClearingUniformPricingMarket)

[Nodal Pricing Market Clearance](https://github.com/itaoxiaoran/power-system-optimization/tree/master/ClearingNodalPricingMarket)

[Joint Energy and Reserve Market Clearance](https://github.com/itaoxiaoran/power-system-optimization/tree/master/ClearingJointEnergyandReserveMarket)





