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

#Definung the necessary functions here

#Function to determine the number of nodes
def number_of_nodes():
	n=int(input("Enter the number of nodes involved in the network: "))
	return n

#Function to determine the number of events between the nodes
def number_of_events(a,n):
	print("The number of events between the nodes is a total of %d"%(n-1))
	return (n-1)

#Assigns the preceeding activity
def relation(a,n):
	print("Note: The first node is considered the starting event with node index 0\n")
	#Assigning first node to -1 to indicate start of the network
	a[0][0]=-1
	print("Note: The event with index %d is considered the last event with node index %d\n"%(n,n))
	for i in range(1,n):
		a[i][0]=int(input("Enter the preceding node for %d node: "%(i+1)))

#Explains the relation between the nodes
def explainer(a,n):
	print("Node: 1 is the starting node")
	for i in range(1,n):
		print("Node: %d follows Node: %d"%(1+i,int(a[i][0])+1))

#Defining the event time between the nodes, relative in nature
def rel_events(a,n):
	for i in range(1,n):
		a[i][1]=input("Enter the relative time for %d and %d event to take place:"%(i+1,a[i][0]))

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
	print("The last node in the network is: %d"%(j))
	return j

#To find the back time
def back_time(a,n,j):
	k=0
	a[j][3]=a[j][2]
	a[0][3]=a[0][2]
	for i in range(n):
		k=int(a[j][0])



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



#Printing the final matrix obtained
print("First row provides the node leading upto respective node.\nSecond row provides relative time elapsed between said node and node in first row.\nThird row provides the absolute time taken for event completion.\n")
print(a)