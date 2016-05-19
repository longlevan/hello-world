__author__ = 'Louis Le'
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

"Pyplot tutorial"
# matplotlib.pyplot is a collection of command style functions that make matplotlib work like Matlab
plt.figure(1)
plt.plot([1,2,3,4])
plt.ylabel('some numbers')

# plot() is a versatile command, and will take an arbitrary number of arguments
plt.figure(2)
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.axis([0,6,0,20])

t = np.arange(0.,5.,0.2)
plt.figure(3)
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

"Controlling line properties"
# Lines have many attributes that you can set: linewidth, dash style, antialiased, etc; see matplotlib.lines.Line2D. There are several ways to set line properties
# Use keywords args:
# plt.plot(x,y,linewidth=2.0)

lines = plt.plot([1,2,3])
plt.setp(lines)
"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

"Working with multiple figures and axes"
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1 = np.arange(0.0,5.0,0.1)
t2 = np.arange(0.0,5.0,0.02)

plt.figure(4)
plt.subplot(211)
plt.plot(t1,f(t1),'bo',t2,f(t2),'k')

plt.subplot(212)
plt.plot(t2,np.cos(2*np.pi*t2),'r--')
# The figure() command here is optional because figure(1) will be created by default, just as a subplot(111) will be created by default if you don't manually specify an axes
# The subplot() command specifies numrows, numcols, fignum where fignum ranges from 1 to numrows*numcols

plt.figure(5)
plt.subplot(211)
plt.plot([1,2,3])
plt.subplot(212)
plt.plot([4,5,6])

plt.figure(6)
plt.plot([4,5,6])

plt.figure(5)
plt.subplot(211)
plt.title('Easy as 1,2,3')
"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

"Working with text"
mu, sigma = 100, 15
x = mu+sigma*np.random.randn(1000)

# the histogram of the data
"The normed=True in histogram does not mean that the sum of the value at each bar will be unity, but rather than the integral over the bars is unity"
plt.figure(7)
n, bins, patches = plt.hist(x,50,normed=1,facecolor='g',alpha=0.75)
plt.xlabel('Smarts', fontsize=14, color='red')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60,.025,r'$\mu=100,\ \sigma=15$')
plt.axis([40,160,0,0.03])
plt.grid(True)
"Using mathematical expression in text"
# matplotlib accepts TeX equations in any text expression.
plt.title(r'$\sigma_i=15$')
# The r preceding the title is important -  It signifies that the string i a raw string and not to treat backslashes as python escapes
"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

plt.figure(8)
ax = plt.subplot(111)
t = np.arange(0.0,5.0,0.01)
s = np.cos(2*np.pi*t)
line,=plt.plot(t,s,lw=2)
plt.annotate('local max',xy =(2,1),xytext=(3,1.5),arrowprops=dict(facecolor='black',shrink=0.05),)
plt.ylim(-2,2)
"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
plt.figure()
ax1 = plt.subplot()
t_a = np.arange(0.01,10.0,0.01)
s1 = np.exp(t_a)
ax1.plot(t_a,s1,'b-',label='Curve 1')
ax1.legend(loc=1)
ax1.set_xlabel('time (s)')
# Make the y-axis label and tick labels match the line color
ax1.set_ylabel('exp', color='b')
for t1 in ax1.get_yticklabels():
    t1.set_color('b')

ax2 = ax1.twinx()
t_b = np.arange(0.01,10.5,0.01)
s2 = np.sin(2*np.pi*t_b)
ax2.plot(t_b,s2,'r.', label='Curve 2')
ax2.legend(loc=2)
ax2.set_ylabel('sin',color='r')

for t1 in ax2.get_yticklabels():
    t1.set_color('r')

plt.show()