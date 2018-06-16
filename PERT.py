#Building tools to calculate critical path for PERT applications
#Basic Terminologies:
#Node: Indicates the start or the conlcusion of the event(s)
#Event: Indicates the period between two consecutive nodes

#Build log:
#30/12/2017
#Build has not been configured (yet) to handle nodes with multiple events leading upto it

#31/12/2017-New Year's Eve
#Incorporated the last node concept
#Yet to incorporate reverse times

#Importing required libraries over here
import numpy as np
import matplotlib.pyplot as plt
import os
from graphviz import Digraph

#Declaring the graph here from Graphviz
def graph_define():
	nameOfGraph=input("[INFO] Provide a name for the graph: ")
	g=Digraph('G',filename=nameOfGraph+'.csv',engine='sfdp')
	g.attr('node',shape='circle')
	return g

#Function to determine the number of nodes
def number_of_nodes():
	n=int(input("\n[DATA] Enter the number of nodes involved in the network: "))
	return n

#Function to determine the number of events between the nodes
def number_of_events(a,n):
	print("[INFO] The number of events between the nodes is a total of %d"%n)
	return (n-1)

#Assigns the preceeding activity
def relation(a,n):
	print("[INFO] The first node is considered the starting event with node index 0\n")
	#Assigning first node to -1 to indicate start of the network
	a[0][0]=0
	print("[INFO] The event with index %d is the last event"%(n-1))
	for i in range(1,n):
		a[i][0]=int(input("\n[DATA] Enter the preceding node for %d node: "%(i)))

#Explains the relation between the nodes
def explainer(a,n):
	print("[INFO] Node: 1 is the starting node")
	for i in range(1,n):
		print("[INFO] Node: %d follows Node: %d"%(i+1,int(a[i][0])+1))

#Defining the event time between the nodes, relative in nature
def rel_events(a,n):
	for i in range(1,n):
		a[i][1]=input("[DATA] Enter the relative time for %d and %d event to take place:"%(i,a[i][0]))

#Calculating the absolute time between with respect to the starting point
def abs_events(a,n):
	for i in range(1,n):
		j=int(a[i][0])
		a[i][2]=a[i][1]+a[j][2]

#To find the last node in the network
def last_node(a,n):
	j=0
	for i in range(0,n):
		if(a[i][2]>a[j][2]):
			j=i
	print("[INFO] The last node in the network is: %d"%(j))
	return j

#To find the back time
def back_time(a,n,j):
	k=0
	a[j][3]=a[j][2]
	a[0][3]=a[0][2]
	for i in range(n):
		k=int(a[j][0])

#We'll be using graphviz to build the graph
def graph_builder(a,g,n):
	#Changing the attributes of the 'node' 0, to ensure that starting node is marked by double-circle
	g.attr('node',shape='doublecircle')
	g.node('0')
	g.attr('node',shape='circle')
	for i in range(1,len(a)):
		g.edge(str(int(i)),str(int(a[i][0])),label=str(a[i][2]),labeltooltip="Time taken for event"+str(a[i][2]))

#This function uses 
def graph_plotter(g):
	g.view()

#n is a variable to store the number of nodes involved in the network
n=0
n=number_of_nodes()
print("\n")

#Declaring the numpy array here for entering the nodes
a=np.zeros((n,4))

#Defines the relation of connectivity of the nodes
relation(a,n)
print("\n")

#Explains the relations between the nodes for verification
explainer(a,n)
print("\n")

#Function provides the number of events between nodes, in total
number_of_events(a,n)
print("\n")

#Function to enter the time elapsed in carrying out the events
rel_events(a,n)
print("\n")

#Function to evaluate the absolute time in execution of the events
abs_events(a,n)
print("\n")

#Prints the last node in the network
j=0
j=last_node(a,n)
print("\n")

#Provide a name for the graph that will be generated.
g=graph_define()

#Builds the graph. Graph is then sent for viewing
graph_builder(a,g,n)

#Plots the graph
graph_plotter(g)


#Printing the final matrix obtained
print("[INFO] First row provides the node leading upto respective node.\n")
print("[INFO] Second row provides relative time elapsed between said node and node in first row.\n")
print("[INFO] Third row provides the absolute time taken for event completion.\n")
print(a)