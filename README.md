#  Power System Optimization
## This is a notice
> Version：0.0.1  
> Author：itaoxiaoran  
> E-mail：ta0ran@163.com  

 >About me : Hello, my name is itaoxiaoran. I am just an ordinary student researching on power system optimization.
 I wish to share with you some contents (theories, codes, etc.) in my usual study through this project. This project is named "power system optimization" mainly to distinguish it from other fields of power system, such as stability analysis, power electronics, etc. I believe that you can see some seemingly common methods in normal literature reading, but you don't know how to use the program to realize them. I will share what I have realized in the form of "detailed description + code" to you, so as to avoid you from making wheels repeatedly.
 Welcome to discuss, exchange and improve the project with me~ 

The following functions have been developed and are waiting to be sorted out and summarized   
Function | Programming language or file format| Expected release time | Actual release time 
-|-|-|-
DC power flow | Python | 2020.5 | 
AC power flow| Python | 2020.5 |
Multi-Obj optimal power flow | Python | 2020.5 |
Transferring Matpower case to .csv | .csv               | 2020.4|
A small amount of real active load data | .csv               | 2020.6 |
Clearing uniform pricing market | Python             | 2020.8 |
 Clearing nodal pricing market | Python             | 2020.8 |
Clearing joint energy and reserve market | Python             | 2020.8 |
 My first Blog for this project | ——                 | May be blew your off |

If you have other demands, you can **pull the Issues** or email me. Maybe I wrote them, but they haven't been sorted out, I will upload them~

## Before use and read most page in this repository.

If you cannot see the formula as following
$$
\left[\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 n} \\
a_{21} & a_{22} & \cdots & a_{2 n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m 1} & a_{m 2} & \cdots & a_{m n}
\end{array}\right]
$$
You'd better install the Chrome plugin:[MathJax Plugin for Github](https://chrome.google.com/webstore/detail/mathjax-plugin-for-github/ioemnmodlmafdkllaclgeombjnmnbima/related) to view the Latex formula normally.

and, the code of this repository require the special module:

1. [pyomo-the Pyomo optimization modeling software](https://github.com/Pyomo/pyomo)

   `pip install pyomo`

2. [geatpy-Evolutionary algorithm toolbox and framework with high performance for Python](https://github.com/geatpy-dev/geatpy)

   `pip install geatpy`

3. **Any Solvers** supported by Pyomo for solving LP problems, i.e. glpk, gurobi, cplex, etc.