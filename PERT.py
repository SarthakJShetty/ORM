#Building tools to calculate critical path for PERT applications
#Basic Terminologies:
#Node: Indicates the start or the conlcusion of the event(s).
#Event: Indicates the period between two consecutive nodes.

#Build log:
#30/12/2017
#Build has not been configured (yet) to handle nodes with multiple events leading upto it.

#31/12/2017-New Year's Eve.
#Incorporated the last node concept.
#Yet to incorporate reverse times.

#Checkout the repository README for detailed log.

#Importing required libraries over here
import numpy as np
import matplotlib.pyplot as plt
import os
from graphviz import Digraph

#Declaring the graph here from Graphviz
def graph_define():
	nameOfGraph=input("[INFO] Provide a name for the graph: ")
	path='Results'
	processGraph=Digraph('G',filename=os.path.join(path,nameOfGraph+'.csv'),engine='sfdp')
	processGraph.attr('node',shape='circle')
	return processGraph

#Function to determine the number of nodes
def number_of_nodes():
	numberOfNodes=int(input("\n[DATA] Enter the number of nodes involved in the network: "))
	return numberOfNodes

#Function to determine the number of events between the nodes
def number_of_events(tableOfEvents,numberOfNodes):
	print("[INFO] The number of events between the nodes is a total of %d"%numberOfNodes)
	return (numberOfNodes-1)

#Assigns the preceeding activity
def event_relation(tableOfEvents,numberOfNodes):
	print("[INFO] The first node is considered the starting event with node index 0\n")
	#Assigning first node to -1 to indicate start of the network
	tableOfEvents[0][0]=0
	print("[INFO] The event with index %d is the last event"%(numberOfNodes-1))
	for i in range(1,numberOfNodes):
		tableOfEvents[i][0]=int(input("\n[DATA] Enter the preceding node for %d node: "%(i)))

#Explains the relation between the nodes
def graph_explainer(tableOfEvents,numberOfNodes):
	print("[INFO] Node: 1 is the starting node")
	for i in range(1,numberOfNodes):
		print("[INFO] Node: %d follows Node: %d"%(i+1,int(tableOfEvents[i][0])+1))

#Defining the event time between the nodes, relative in nature
def rel_events(a,numberOfNodes):
	for i in range(1,numberOfNodes):
		tableOfEvents[i][1]=input("[DATA] Enter the relative time for %d and %d event to take place:"%(i,tableOfEvents[i][0]))

#Calculating the absolute time between with respect to the starting point
def abs_events(tableOfEvents,numberOfNodes):
	for i in range(1,numberOfNodes):
		j=int(tableOfEvents[i][0])
		tableOfEvents[i][2]=tableOfEvents[i][1]+tableOfEvents[j][2]

#To find the last node in the network
def last_node(tableOfEvents,numberOfNodes):
	j=0
	for i in range(0,numberOfNodes):
		if(tableOfEvents[i][2]>tableOfEvents[j][2]):
			j=i
	print("[INFO] The last node in the network is: %d"%(j))
	return j

#We'll be using graphviz to build the graph
def graph_builder(tableOfEvents,processGraph,numberOfNodes):
	#Changing the attributes of the 'node' 0, to ensure that starting node is marked by double-circle
	processGraph.attr('node',shape='doublecircle')
	processGraph.node('0')
	processGraph.attr('node',shape='circle')
	for i in range(1,len(tableOfEvents)):
		processGraph.edge(str(int(tableOfEvents[i][0])),str(int(i)),label=("Forward Pass Time: "+str(int(tableOfEvents[i][2]))))
		
		#Backward time not yet implemented
		#g.edge(str(int(i)),str(int(a[i][0])),label="Backward Pass Time: "+str(a[i][3]))

#This function uses 
def graph_plotter(processGraph):
	processGraph.view()

#Analyzes the nodes in reverse to detwemine backward-pass time.
'''def backward_pass(a,g,n):
	for events_1 in range(0,len(a)):
		b=np.zeros(n,1)
		for events_2 in range(1,len(a)):
			if(a[events_2][0]==a[events_1][0]):
				b.append(a[events_1])
		a[events_1][3]=np.amax(b)
	print(b)'''



#n is a variable to store the number of nodes involved in the network
numberOfNodes=0
numberOfNodes=number_of_nodes()
print("\n")

#Declaring the numpy array here for entering the nodes
tableOfEvents=np.zeros((numberOfNodes,4))

#Defines the relation of connectivity of the nodes
event_relation(tableOfEvents,numberOfNodes)
print("\n")

#Explains the relations between the nodes for verification
graph_explainer(tableOfEvents,numberOfNodes)
print("\n")

#Function provides the number of events between nodes, in total
number_of_events(tableOfEvents,numberOfNodes)
print("\n")

#Function to enter the time elapsed in carrying out the events
rel_events(tableOfEvents,numberOfNodes)
print("\n")

#Function to evaluate the absolute time in execution of the events
abs_events(tableOfEvents,numberOfNodes)
print("\n")

#Prints the last node in the network
j=0
j=last_node(tableOfEvents,numberOfNodes)
print("\n")

#Provide a name for the graph that will be generated
processGraph=graph_define()

#Inserting backward-pass function here
#backward_pass(a,g,n)

#Builds the graph. Graph is then sent for viewing
graph_builder(tableOfEvents,processGraph,numberOfNodes)

#Plots the graph
graph_plotter(processGraph)


#Printing the final matrix obtained
print("[INFO] First row provides the node leading upto respective node.\n")
print("[INFO] Second row provides relative time elapsed between said node and node in first row.\n")
print("[INFO] Third row provides the absolute time taken for event completion.\n")
print(tableOfEvents)