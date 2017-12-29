#Building tools to calculate critical path for PERT applications
#Basic Terminologies:
#Node: Indicates the start of the event
#Event: Indicates the period between two consecutive nodes

#Importing required libraries over here
import numpy as np
import matplotlib.pyplot as plt

#Definung the necessary functions here

#Assigns the preceeding activity
def relation(a,n):
	print("Note: The first is considered the starting event with node index 0\n")
	#Assigning first node to -1 to indicate start of the network
	a[0][0]=-1
	print("Note: The event with index %d is considered the last event with node index %d\n"%(n,n))
	for i in range(1,n):
		a[i][0]=int(input("Enter the preceding node for %d node: "%(i+1)))

#Explains the relation betweem the nodes
def explainer(a,n):
	print("Node: 1 is the starting node")
	for i in range(1,n):
		print("Node: %d follows Node: %d"%(1+i,int(a[i][0])+1))

#Defining the events between the nodes
def events(a,n):
	for i in range(a,n):
		

#Enteriing the number of nodes in the given scheduling problem
n=int(input("Enter the number of nodes:"))
print("\n")
#Declaring the numpy array here for entering the nodes
a=np.zeros((n,3))

relation(a,n)
print("\n")
explainer(a,n)

#print(a)