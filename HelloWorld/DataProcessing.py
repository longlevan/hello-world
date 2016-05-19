__author__ = 'Louis Le'
"importing"
import numpy as np
import matplotlib.pyplot as plt
import math
"take 100 values between 0 and 2*pi"
x=np.linspace(0,4*math.pi,100)
y = np.sin(x)
plt.plot(x,y,'*',color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.figure(num=1,dpi=600)
plt.savefig('SineCurve')
"Making a histogram with normal data"
N = np.random.randn(100)
plt.figure(num=2,dpi=600,facecolor='green')
plt.hist(N,bins=10,color='red')
plt.show()
plt.savefig('histogram')
"importing data, manipulating lists, and using numpy"
"we are going to use the csv library to start off since it's relatively transparent with what is happening"
import csv as csv
'We begin by using csv command reader to read the csv file and change it into a more python-friendly format. We need to use and open(file) command inside of the reader command to have it read our file'

readdata=csv.reader(open('pop_change.csv','r'))

print(readdata)
"well that's certainly not what we wanted. The idea here is that to print out or save this data we need to iterate over it"
"for row in readdata:"

"this should give you all of the rows of the dataset. Great, neat. But that's not exactly what we want because that only prints the data. We can't do a whole lot of " \
"manipulate; feel free to delete this for statement and the print statement. we're going to do a little trick to keep all this data in a list. We're going to initialize a " \
"blank list called data by using the command data=[]. We'll then append each row to the list, making a list of rows. It's almost the same as the print statement above, and goes" \
"a little something like this "
data=[]
for row in readdata:
    data.append(row)

print(data)
"Now try to print the list data. You should see all of the rows; The rows will be in the form of a list, and they'll contain a state name, the polulation in 1910, and th population in 2010" \
"the first row, data[0] fives you the headings. For reasons that will become apparent in a second, we're going to want to make a list which is just our data and onother list which is just" \
"our headings"
Header = data[0]
data.pop(0)

print(data)
"as we noted the headings are at data[0]. The .pop[0] command tells us to take the list data and remove the 0-th element (the header element, in this case) " \
"after popping off that element, the list data will only contain the data without headers"
"displaying our beautiful data" \
"you might be anxious to see this data in a pretty table format. You could try a bunch with print statements and so forth, but it takes a lot of work and creativity to make a nice " \
"table format. at this point, we need to import pandas" \
"pandas is a sweet data analysis toll that we'll use much more later but, for now, it's useful as a way to make a pretty table for our data"
import pandas as pd

"but wait, I want to edit this data...!" \
"so the data that we've been using is real data. it tells us the population of a state in 1910 and 2010"
"we want to append a bit to the header. let's append the element Difference which will stand for the difference column"
Header.append("Difference")
for i in range(len(data)):
    diff = int(data[i][2])-int(data[i][1])
    data[i].append(diff)

print(pd.DataFrame(data,columns=Header))



