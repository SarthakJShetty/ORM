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

#Checkout the repository README for a more detailed log.

#Importing required libraries over here
import numpy as np
import matplotlib.pyplot as plt
import os
from graphviz import Digraph

#Declaring the graph here from Graphviz
def graph_define():
	nameOfGraph=input("[INFO] Provide a name for the graph: ")
	#Stores the nameOfGraph.pdf, nameOfGraph.csv files in the nameOfGraph folder under Results.
	path='Results/'+nameOfGraph
	processGraph=Digraph('G',filename=os.path.join(path,nameOfGraph+'.csv'),engine='sfdp')
	processGraph.attr('node',shape='circle')
	return processGraph

#Function to determine the number of nodes
def number_of_nodes():
	try:
		numberOfNodes=int(input("\n[DATA] Enter the number of nodes involved in the network: "))
	except ValueError:
		numberOfNodes=int(input("\n[DATA] Enter a valid number of nodes involved in the network: "))
	return numberOfNodes

#Function to determine the number of events between the nodes
def number_of_events(tableOfEvents,numberOfNodes):
	#Prints the serial number of events on the extreme left.
	for node in range(0,numberOfNodes):
		tableOfEvents[node][0]=node
	print("[INFO] The number of events between the nodes is a total of %d"%numberOfNodes)
	return (numberOfNodes-1)

#Assigns the preceeding activity
def event_relation(tableOfEvents,numberOfNodes):
	print("[INFO] The first node is considered the starting node with node index 0")
	#Assigning first node to -1 to indicate start of the network
	tableOfEvents[0][0]=0
	print("[INFO] The event with index %d is the last event\n"%(numberOfNodes-1))
	for node in range(0,numberOfNodes):
		if(node!=0):
			tableOfEvents[node][1]=int(input("[DATA] Enter the preceding node index (from 0->%d) for %d node: "%(numberOfNodes-1,node)))
			if(tableOfEvents[node][1]>numberOfNodes):
				tableOfEvents[node][1]=int(input("[DATA] Enter a valid preceding node index (from 0->%d) for %d node: "%(numberOfNodes-1,node)))

#This function checks if the graph has conitnuity
def graph_continuity(tableOfEvents,numberOfNodes):
	for node in range(0,(numberOfNodes)):
		tableOfEvents[int(tableOfEvents[node][2])][3]=1

#Explains the relation between the nodes
def graph_explainer(tableOfEvents,numberOfNodes):
	print("[INFO] Node: 1 is the starting node")
	for node in range(1,numberOfNodes):
		print("[INFO] Node: %d follows Node: %d"%(node,int(tableOfEvents[node][1])+1))

#Defining the event time between the nodes, relative in nature
def rel_events(tableOfEvents,numberOfNodes):
	for node in range(1,numberOfNodes):
		tableOfEvents[node][2]=input("[DATA] Enter the relative time for %d and %d event to take place:"%(node,tableOfEvents[node][1]))

#Calculating the absolute time between with respect to the starting point
def abs_events(tableOfEvents,numberOfNodes):
	for current_node in range(1,numberOfNodes):
		#Here, the leader node is node leading upto the current node.
		'''The abs_time will be the relative time between current_node and the leader_node
		and the abs_time of the leader_node
		'''
		leader_node=int(tableOfEvents[leader_node][1])
		tableOfEvents[current_node][3]=tableOfEvents[current_node][2]+tableOfEvents[leader_node][3]

#To find the last node in the network
def last_node(tableOfEvents,numberOfNodes):
	for node in range(0,numberOfNodes):
		referenceNode=0
		if(tableOfEvents[node][3]>tableOfEvents[referenceNode][3]):
			referenceNode=node
	print("[INFO] The last node in the network is: %d"%(referenceNode))
	return referenceNode

#We'll be using graphviz to build the graph
def graph_builder(tableOfEvents,processGraph,numberOfNodes):
	#Changing the attributes of the 'node' 0, to ensure that starting node is marked by double-circle
	processGraph.attr('node',shape='doublecircle')
	processGraph.node('0')
	processGraph.attr('node',shape='circle')
	for node in range(1,len(tableOfEvents)):
		processGraph.edge(str(int(tableOfEvents[node][1])),str(int(node)),label=("Forward Pass Time: "+str(int(tableOfEvents[node][2]))))
		
		#Backward time not yet implemented
		#g.edge(str(int(node)),str(int(a[node][0])),label="Backward Pass Time: "+str(a[node][3]))

#This function uses the processGraph and plots the graph for visualization.
def graph_plotter(processGraph):
	processGraph.view()
	print('\n')

#Analyzes the nodes in reverse to detwemine backward-pass time.
'''def backward_pass(a,g,n):
	for events_1 in range(0,len(a)):
		b=np.zeros(n,1)
		for events_2 in range(1,len(a)):
			if(a[events_2][0]==a[events_1][0]):
				b.append(a[events_1])
		a[events_1][3]=np.amax(b)
	print(b)'''

#n is a variable to store the number of nodes involved in the network.
numberOfNodes=number_of_nodes()
print("\n")

#Declaring the numpy array here for entering the nodes.
tableOfEvents=np.zeros((numberOfNodes,5))

#Defines the relation of connectivity of the nodes.
event_relation(tableOfEvents,numberOfNodes)
print("\n")

#Checking the continuity of the graph here.
graph_continuity(tableOfEvents,numberOfNodes)

#Explains the relations between the nodes for verification.
graph_explainer(tableOfEvents,numberOfNodes)
print("\n")

#Function provides the number of events between nodes, in total.
number_of_events(tableOfEvents,numberOfNodes)
print("\n")

#Function to enter the time elapsed in carrying out the events.
rel_events(tableOfEvents,numberOfNodes)

#Function to evaluate the absolute time in execution of the events.
abs_events(tableOfEvents,numberOfNodes)
print("\n")

#Prints the last node in the network.
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
print("[INFO] First row provides a serial reference for the events")
print("[INFO] Second row provides the node leading upto respective node.")
print("[INFO] Third row provides relative time elapsed.")
print("[INFO] Fourth row provides the absolute time taken for event completion.\n")
print(tableOfEvents)