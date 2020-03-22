#  Power System Optimization
> Version：0.0.1  
> Author：itaoxiaoran  
> E-mail：ta0ran@163.com <br>


> **About me** : Hello, My name is **ran**. I'm a student researching on power system optimization and deep reinforcement learing. I would like to share some works (theories, codes, etc.) in my usual study through this project. This repository is named "power system optimization" mainly to distinguish it from other fields of power system, such as stability analysis, power electronics, etc. I believe that you can see some methods or algorithm in literature reading, but you didn't know how to use the program to achieve them. I will share what I have achieved in the form of "detailed descriptions + codes" to you, so as to avoid to reinvent wheels repeatedly.  

​	                                                   **Welcome to discuss with me~** :smile:

## Contents

- [x] [Transferring Matpower Case File to CSV format](#transferring-matpower-case-file-to-csv-format)
- [x] [DC Power Flow](#dc-power-flow)
- [ ] [AC Power Flow](ac-power-flow)
- [ ] [DC Optimal Power Flow](#dc-optimal-power-flow)
- [ ] [AC Optimal Power Flow](#ac-optimal-power-flow)
- [ ] [Multi-Objective Optimal Power Flow](#multi-objective-optimal-power-flow)
- [ ] [Small Amount of Real Active Load Data](#small-amount-of-real-active-load-data)
- [ ] [Load Forecasting](#load-forecasting)
- [ ] [Uniform Pricing Market Clearance](#uniform-pricing-market-clearance)
- [ ] [Nodal Pricing Market Clearance](#nodal-pricing-market-clearance)
- [ ] [Joint Energy and Reserve Market Clearance](#joint-energy-and-reserve-market-clearance)
- [ ] [Quick start Power System Optimization by Pyomo](#quick-start-power-system-optimization-by-pyomo)
- [ ] [Some Useful Tools](#some-useful-tools)

## This is an ABSOLUTE  preview !

The following functions have been developed and are waiting to be sorted out and summarized .  
Functions | Programming Language or File Format | Expected Release Time | Actual Release Time 
-|-|-|-
DC power flow | Python | 04/2020 | 03/23 2020 
AC power flow| Python | 04/2020 |
DC optimal power flow| Python | 12/2020 |
AC optimal power flow| Python | 12/2020               |
Multi-objective optimal power flow | Python | 05/2020 |
Transferring Matpower case file to CSV format | CSV Format, Python, MATLAB | 04/2020 |03/22 2020
Small amount of real active load data | CSV Format      | 06/2020 |
Load forecasting | Python, CSV Format | 12/2020 |
Uniform pricing market clearance | Python             | 08/2020 |
 Nodal pricing market clearance | Python             | 08/2020 |
Joint energy and reserve market clearance | Python             | 08/2020 |
Quick start Power System Optimization by Pyomo | Python | 10/2020 |
Some Useful Tools | Python | 12/2020 |
 My first Blog for this project | ——                 | May be blew you off |

If you have any other demands or suggestions, you can [**pull the Issues**](https://github.com/itaoxiaoran/power-system-optimization/issues) or email me. 

## Before use and read most pages in this repository.

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



## Transferring Matpower case file to CSV format

**HAVE BEEN DONE: 03/22 2020**

the **Transferring Matpower Case File to CSV Foramt** can help you use the Matpower case file in Python.

> **getDataFrame.py** for getting the power system data in Python  
> **write2csv.m** for transferring the case file to CSV format file  
> **Required**: numpy, pandas, sys, MATLAB, Matpower    

Start directly: [click here](https://github.com/itaoxiaoran/transfer-matpower-case-file)

## DC Power Flow

**HAVE BEEN DONE: 03/23 2020**

the DC Power Flow can help you to calculate the DC power flow in Python.

> **getDataFrame.py** for getting the power system data in Python  
> **dcpf.m** for calculating the DC power flow in Python  
> **Required**: numpy, pandas, sys, prettytable(optional)  

Start directly: [click here](https://github.com/itaoxiaoran/dc-power-flow)

## AC Power Flow

waiting...

Start directly: [click here](https://github.com/itaoxiaoran/ac-power-flow)

## DC Optimal Power Flow

waiting...

Start directly: [click here](https://github.com/itaoxiaoran/dc-optimal-power-flow)

## AC Optimal Power Flow

waiting...

Start directly: [click here](https://github.com/itaoxiaoran/ac-optimal-power-flow)

## Multi-objective Optimal Power Flow

waiting...

Start directly: [click here](https://github.com/itaoxiaoran/multi-objective-power-flow)

## Small Amount of Real Active Load Data

waiting...

Start directly: [click here](https://github.com/itaoxiaoran/real-load-data)

## Load Forecasting

waiting...

Start directly: [click here](https://github.com/itaoxiaoran/load-forecasting)

## Uniform pricing market clearance

waiting...

Start directly: [click here](https://github.com/itaoxiaoran/uniform-pricing-electricity-market)

## Nodal pricing market clearance

waiting...

Start directly: [click here](https://github.com/itaoxiaoran/nodal-pricing-electricity-market)

## Joint energy and reserve market clearance

waiting...

Start directly: [click here](https://github.com/itaoxiaoran/joint-energy-and-reserve-electricity-market)

## Quick start Power System Optimization by Pyomo

waiting...

Start directly: [click here](https://github.com/itaoxiaoran/quick-start-power-system-optimization-by-Pyomo)

## Some Useful Tools

waiting...

Start directly: [click here](https://github.com/itaoxiaoran/useful-tools-for-power-system)









