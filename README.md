#  Power System Optimization
> Version：0.0.1  
> Author：itaoxiaoran  
> E-mail：ta0ran@163.com <br>


> **About me** : Hello, My name is **ran**. I'm a student researching on power system optimization and deep reinforcement learing. I would like to share some works (theories, codes, etc.) in my usual study through this project. This repository is named "power system optimization" mainly to distinguish it from other fields of power system, such as stability analysis, power electronics, etc. I believe that you can see some methods or algorithm in literature reading, but you didn't know how to use the program to achieve them. I will share what I have achieved in the form of "detailed descriptions + codes" to you, so as to avoid to reinvent wheels repeatedly.  

​	                                                   **Welcome to discuss with me~** :smile:

## Contents

- [x] [Transferring Matpower Case File to .csv](https://github.com/itaoxiaoran/power-system-optimization/tree/master/Casefile)
- [ ] [DC Power Flow](https://github.com/itaoxiaoran/power-system-optimization/tree/master/DCpowerflow)
- [ ] [AC Power Flow](https://github.com/itaoxiaoran/power-system-optimization/tree/master/ACpowerflow)
- [ ] [Multi-Object Optimal Power Flow](https://github.com/itaoxiaoran/power-system-optimization/tree/master/MultiObjPowerFlow)

- [ ] [A Small Amount of  Real Active Load Data](https://github.com/itaoxiaoran/power-system-optimization/tree/master/RealActiveLoadData)

- [ ] [Uniform Pricing Market Clearance](https://github.com/itaoxiaoran/power-system-optimization/tree/master/ClearingUniformPricingMarket)

- [ ] [Nodal Pricing Market Clearance](https://github.com/itaoxiaoran/power-system-optimization/tree/master/ClearingNodalPricingMarket)
- [ ] [Joint Energy and Reserve Market Clearance](https://github.com/itaoxiaoran/power-system-optimization/tree/master/ClearingJointEnergyandReserveMarket)

## This is  an ABSOLUTE  preview !

The following functions have been developed and are waiting to be sorted out and summarized .  
Functions | Programming Language or File Format | Expected Release Time | Actual Release Time 
-|-|-|-
DC power flow | Python | 2020.5 | 
AC power flow| Python | 2020.5 |
Multi-Obj optimal power flow | Python | 2020.5 |
Transferring Matpower case file to .csv | .csv               | 2020.4|2020.3.21
A small amount of real active load data | .csv               | 2020.6 |
Uniform pricing market clearance | Python             | 2020.8 |
 Nodal pricing market clearance | Python             | 2020.8 |
Joint energy and reserve market clearance | Python             | 2020.8 |
 My first Blog for this project | ——                 | May be blew you off |

​	

​	If you have any other demands or suggestions, you can [**pull the Issues**](https://github.com/itaoxiaoran/power-system-optimization/issues) or email me. 

## Before use and read most page in this repository.

​	If you cannot see the formula normally as following:
$$
\frac{d c}{d x}+\mu \frac{d h}{d x}=0
$$


​	You'd better install the Chrome plugin:[MathJax Plugin for Github](https://chrome.google.com/webstore/detail/mathjax-plugin-for-github/ioemnmodlmafdkllaclgeombjnmnbima/related) to view the Latex formula normally.

​	And, the code of this repository require these **special** module:

1. [pyomo-the Pyomo optimization modeling software](https://github.com/Pyomo/pyomo)

   `pip install pyomo`

2. [geatpy-Evolutionary algorithm toolbox and framework with high performance for Python](https://github.com/geatpy-dev/geatpy)

   `pip install geatpy`

3. **Any Solvers** supported by Pyomo for solving LP problems, i.e. glpk, gurobi, cplex, etc.







