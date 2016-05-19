__author__ = 'Louis Le'
"pycse: Python Computation in Science and Engineering"

"1. Basic math" \
"The most basic mathematical operations: addition, subtraction, multiplication, division and exponentation" \
"We use the print to get the output" \
"integers and float numbers"
print (2+4)
print (8.1 - 5)
print (5*4)
print (3.1*2)
print (4.0/2.0)
print (1.0/3.1)
print (4/2)
print (1/3)
print (3.**2)
print (3**2)
print (2**0.5)
"Other types of mathematical operations require us to import functionality from python libraries"
"2. Advanced mathematical operators"
"The primary library we will consider is numpy, which provides many mathematical functions, statistics as well as support for linear algebra" \
"For a complete listing of the functions available see: "
import numpy as np
print(np.exp(1))
print(np.sqrt(2))
"There are two logarithmic functions commonly used, the natural log function numpy.log and the base 10 logarithm numpy.log10"
print(np.log(10))
print(np.log10(10))

"3. Creating your own functions" \
"We can combine operations to evaluate complex equations. Consider the value of equation x^3 - log(x) for the value x = 4.1"
x = 3
print(x**3-np.log(x))

def f(x):
    return x**3 - np.log(x)

print(f(3))
print(f(5.1))

"4. Defining functions in python"
def f(x):
    "return the inverse square of x"
    return 1.0/x**2



"Note that functions are not automatically vectorized. That is why we see the error"
def f(x):
    "return the inverse square of x"
    x = np.array(x)
    return 1.0/x**2

x = np.array([4,5])
print(x)

print(f([4,5]))

def func(x,y):
    "return product of x and y"
    return x*y

print(func(2,3))

print(func(np.array([2,3]),np.array([3,4])))
"You can define lambda functions, which are also known as inline or anonymous functions." \
"The syntax is lambda var:f(var). "
from scipy.integrate import quad
print (quad(lambda x:x**3,0,2))

def wrapper(x):
    a = 4
    def func(x,a):
        return a*x

    return func(x,a)

print(wrapper(4))

def func(x,a):
    return a*x

def wrapper(x):
    a=4
    return func(x,a)

print(wrapper(4))

"last example, defining a function for an ode"
from scipy.integrate import odeint
import matplotlib.pyplot as plt

k = 2.2
def myode(y,t):
    "ode defining exponential growth"
    return k*y

y0=3

tspan = np.linspace(0,1)
y = odeint(myode,y0,tspan)

plt.plot(tspan,y)
plt.xlabel('Time')
plt.ylabel('y')
plt.savefig('funcs-ode.png')

"Advanced function creation"
"Python has some nice features in creating functions. You can create default values for variables, have optional variables" \
"and optional keyword variables. In this function f(a,b), a and b are called positional arguments, and they are required," \
"and must be provided in the same order as the functions defines"
def func(a,n=2):
    "compute the nth power of a"
    return a**n
# three different ways to call the function
print(func(2))
print(func(2,3))
print(func(2,n=4))
"in the first call to the function, we only define the argument a, which is a mandatory, positional argument."

"It is occasinally useful to allow an arbitrary number of argument"
def func(*args):
    sum = 0
    for arg in args:
        sum +=arg
    return sum

print(func(1,2,3,4))


def func(**kwargs):
     for kw in kwargs:
         print('{0}={1}'.format(kw, kwargs[kw]))

func(t1=6,color='blue')


def myplot(x,y,fname = None, **kwargs):
    plt.plot(x,y,**kwargs)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('My plot')
    if fname:
        plt.savefig(fname)
    else:
        plt.show()


x = [1,3,4,5]
y = [3,6,9,12]

myplot(x,y,'myfig.png',color = 'orange',marker='s')

from sympy.solvers import solve
from sympy import Symbol
x = Symbol('x')
print(solve(x**2-5*x+6,x))

def f(x): return x**2

print(f(8))

g = lambda x: x**2

print(g(8))

def make_incrementor(n): return lambda x: x+n

f = make_incrementor(2)
g = make_incrementor(6)

print(f(42),g(42))



#!/usr/bin/env python3
# -*- coding: utf-8-unix -*-

import datetime
import gantt

# Change font default
gantt.define_font_attributes(fill='black',
                             stroke='black',
                             stroke_width=0,
                             font_family="Verdana")

# Add vacations for everyone
gantt.add_vacations(datetime.date(2014, 12, 25))
gantt.add_vacations(datetime.date(2015, 1, 1))
gantt.add_vacations(datetime.date(2015, 1, 13))

# Create two resources
rANO = gantt.Resource('ANO')
rJLS = gantt.Resource('JLS')

# Add vacations for one lucky resource
rANO.add_vacations(
    dfrom=datetime.date(2014, 12, 29),
    dto=datetime.date(2015, 1, 4)
    )
rANO.add_vacations(
    dfrom=datetime.date(2015, 1, 6),
    dto=datetime.date(2015, 1, 8)
    )

# Test if this resource is  avalaible for some dates
print(rANO.is_available(datetime.date(2015, 1, 5)))
print(rANO.is_available(datetime.date(2015, 1, 8)))
print(rANO.is_available(datetime.date(2015, 1, 6)))
print(rANO.is_available(datetime.date(2015, 1, 2)))
print(rANO.is_available(datetime.date(2015, 1, 1)))


# Create some tasks
t1 = gantt.Task(name='tache1',
                start=datetime.date(2014, 12, 25),
                duration=4,
                percent_done=44,
                resources=[rANO],
                color="#FF8080")
t2 = gantt.Task(name='tache2',
                start=datetime.date(2014, 12, 28),
                duration=6,
                resources=[rJLS])
t7 = gantt.Task(name='tache7',
                start=datetime.date(2014, 12, 28),
                duration=5,
                percent_done=50)
t3 = gantt.Task(name='tache3',
                start=datetime.date(2014, 12, 25),
                duration=4,
                depends_of=[t1, t7, t2],
                resources=[rJLS])
t4 = gantt.Task(name='tache4',
                start=datetime.date(2015,1,1),
                duration=4,
                depends_of=t1,
                resources=[rJLS])
t5 = gantt.Task(name='tache5',
                start=datetime.date(2014, 12, 23),
                duration=3)
t6 = gantt.Task(name='tache6',
                start=datetime.date(2014, 12, 25),
                duration=4,
                depends_of=t7,
                resources=[rANO])
t8 = gantt.Task(name='tache8',
                start=datetime.date(2014, 12, 25),
                duration=4,
                depends_of=t7,
                resources=[rANO, rJLS])


# Create a project
p1 = gantt.Project(name='Projet 1')

# Add tasks to this project
p1.add_task(t1)
p1.add_task(t7)
p1.add_task(t2)
p1.add_task(t3)
p1.add_task(t5)
p1.add_task(t8)



# Create another project
p2 = gantt.Project(name='Projet 2', color='#FFFF40')

# Add tasks to this project
p2.add_task(t2)
p2.add_task(t4)


# Create another project
p = gantt.Project(name='Gantt')
# wich contains the first two projects
# and a single task
p.add_task(p1)
p.add_task(p2)
p.add_task(t6)



# Test cases for milestones
# Create another project
ptcm = gantt.Project(name='Test case for milestones')

tcm11 = gantt.Task(name='tcm11',
                   start=datetime.date(2014, 12, 25),
                   duration=4)
tcm12 = gantt.Task(name='tcm12',
                   start=datetime.date(2014, 12, 26),
                   duration=5)
ms1 = gantt.Milestone(name=' ',
                      depends_of=[tcm11, tcm12])
tcm21 = gantt.Task(name='tcm21',
                   start=datetime.date(2014, 12, 30),
                   duration=4,
                   depends_of=[ms1])
tcm22 = gantt.Task(name='tcm22',
                   start=datetime.date(2014, 12, 30),
                   duration=6,
                   depends_of=[ms1])
ms2 = gantt.Milestone(name='MS2',
                      depends_of=[ms1, tcm21, tcm22])
tcm31 = gantt.Task(name='tcm31',
                   start=datetime.date(2014, 12, 30),
                   duration=6,
                   depends_of=[ms2])
ms3 = gantt.Milestone(name='MS3', depends_of=[ms1])


ptcm.add_task(tcm11)
ptcm.add_task(tcm12)
ptcm.add_task(ms1)
ptcm.add_task(tcm21)
ptcm.add_task(tcm22)
ptcm.add_task(ms2)
ptcm.add_task(tcm31)
ptcm.add_task(ms3)


p.add_task(ptcm)

##########################$ MAKE DRAW ###############
p.make_svg_for_tasks(filename='test_full.svg',
                     today=datetime.date(2014, 12, 31),
                     start=datetime.date(2014,8, 22),
                     end=datetime.date(2015, 1, 14))
p.make_svg_for_tasks(filename='test_full2.svg',
                     today=datetime.date(2014, 12, 31))
p.make_svg_for_tasks(filename='test.svg',
                     today=datetime.date(2014, 12, 31),
                     start=datetime.date(2015, 1, 3),
                     end=datetime.date(2015, 1, 6))
p1.make_svg_for_tasks(filename='test_p1.svg',
                      today=datetime.date(2014, 12, 31))
p2.make_svg_for_tasks(filename='test_p2.svg',
                      today=datetime.date(2014, 12, 31))
p.make_svg_for_resources(filename='test_resources.svg',
                         today=datetime.date(2014, 12, 31),
                         resources=[rANO, rJLS])
p.make_svg_for_tasks(filename='test_weekly.svg',
                     today=datetime.date(2014, 12, 31),
                     scale=gantt.DRAW_WITH_WEEKLY_SCALE)
##########################$ /MAKE DRAW ###############



