# import matplotlib
# In this section, we first import the necessary matplotlib tools

import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey
# We now build a Sankey with an input flow and an output flow of 1. The flows are specified with the flows argument, while labels are provided using labels

sankey = Sankey()
sankey.add(flows=[1,-1],
           labels=['input','output'])
sankey.finish()

# There are others arguments that can be specified. For instance, one can change the orientation of the diagram using the rotation argument
sankey = Sankey()
sankey.add(flows=[1,-1],
           labels=['input','ouput'],
           orientations=[0,0])
sankey.finish()

# Let's go a step further by providing a third flow to our diagram. To do this, we need to specify an orientations argument. In the previous diagram
# we had only tow flows, so by default the Sankey module assumes those to be input and output. Now, we need to specify how the flows align with the diagram
# using a list of orientations. Here, putting an orientation of 1 means it come from the side
sankey=Sankey()
sankey.add(flows=[2,-1,1],
           orientations=[0,0,-1],
           labels=['input','output','second input'],
           rotation=-90)
sankey.finish()

sankey=Sankey()
sankey.add(flows=[1,0.25,-0.25,-0.15,-0.1,-0.1,-0.3,-0.1],
           orientations=[0,1,1,1,1, 1, 0,-1], pathlengths=[1,0.25,0.25,0.15,0.1,0.1,0.3,0.1],
           labels=['Gross input','Recovered','','Recovered heat','Available heat','', '', ''],
           facecolor='red',
           patchlabel='patch label')
sankey.finish()

sankey.add(flows=[-0.25,0.25],
           orientations=[1,1],
           labels=['2',''],
           facecolor='red',
           prior=0,
           connect=(1,0))
sankey.finish()




# Connecting diagram together
sankey=Sankey()
# first diagram, indexed by prior =0
sankey.add(flows=[1,-1],
           labels=['input','output'])
#second diagram indexed by prior =1
sankey.add(flows=[1,-1],
           labels=['input2','output2'],
           prior=0,
           connect=(1,0))
sankey.finish()

"""
# Example 1 -- Mostly defaults
# This demonstrates how to create a simple diagram by implicity calling the Sankey.add() method and by appending finish() to the call to the class
Sankey(flows=[0.25, 0.15, 0.6, -0.2, -0.15,0.05,-0.5, -0.1],
       labels=['', '','', 'First', 'Second', 'Third', 'Fourth', 'Fifth'],
       orientations=[-1, 1, 0, 1, 1, 1,  0, -1]).finish()
plt.title("The default settings produce a diagram like this")
fig=plt.figure()
"""
plt.show()
"""
ax = fig.add_subplot(1,1,1,xticks=[],ysticks=[],
                     title="Flow diagram of a widget")

"""