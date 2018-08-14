# Operations-Research
### Building a tool for visualization of Critical Path in Critical Path Method for Operations Research.

### :warning: Code is buggy :warning:

### Introduction
This project is in the process of being developed for the effective visualization of Critical Path, Best Starting time and Lagging time.

#### This code has not been fully developed. Some portions of it are still incomplete. Suggestions for improving the code are always appreciated.

#### Terminologies
1. <strong>Nodes:</strong> Symbolize the start or end (sometimes both), of events. A node can be the starting (or terminating) point of one or more events.
2. <strong>Event:</strong> The sequence of actions in between two nodes.

### Functioning
- Program requests for the number of nodes involved in the network.
- Building upon the network of nodes, the relations between the different nodes are assigned (Check the Build Log for a list of assignments that are currently possible.)
- Following up on the previous relations, the program then assigns the absolute times of the events in between the different nodes.
- The [graph](https://github.com/SarthakJShetty/ORM/blob/master/Results/Hello.csv.pdf) is generated using Graphviz for visual representation of the process and the network.

### Usage:

1. Clone this repository:

	```git clone https://github.com/SarthakJShetty/ORM```

2. First

### Graphviz Representation:

<img src="https://raw.githubusercontent.com/SarthakJShetty/ORM/master/Results/Graph_Image.jpg" height="75%" width="75%" align="middle" title="Representation of Graph">
<caption><strong>Fig 1.</strong> Simple network with forward pass times</caption>

<img src="https://raw.githubusercontent.com/SarthakJShetty/ORM/master/Results/Hello/Hello_Graph_Image.png" height="75%" width="75%" align="middle" title="Complex Graph">
<caption><strong>Fig 2.</strong> Complex network with forward pass times</caption>

#### Build-log:

Check out the <a href="https://github.com/SarthakJShetty/ORM/blob/master/build-log.md">build-log</a> for a more detailed progress report.