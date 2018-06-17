
# Operations-Research
### Building a tool for visualization of Critical Path in Critical Path Method for Operations Research.

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

### Graphviz Representation:

<img src="https://raw.githubusercontent.com/SarthakJShetty/ORM/master/Results/Graph_Image.jpg" height="75%" width="75%" align="middle">

### Build Log:

#### 12/30/2017
- Build has not (yet) been configured to handle multiple events leading to a single node.

#### 12/31/2017 (Happy New Year!)
- Incorporated the last node concept.
- Can now calculate Critical Path in the forward direction.
- Need to obtain the Critical Path in the reverse direction to confirm the Critical Path.
- Working on theory to obtain the Reverse Start Times.

### 06/14/2018
- Integrating graphviz for visualization.
- Fixing Explainer code.

### 06/15/2018
- Graphviz has been integrated.
- Functions 'graph_builder' & 'graph_plotter' have also been included.
- Error encountered when graph of the same name already exists in the same directory.


### 06/16/2018
- Graphviz has been integrated.
- Attribute 'shape' of node 0 has been changed to 'doublecircle' to ensure that starting node can be comfortably identified.
- Interpreter now asks the name to be assigned to the graph.
- Trying to integrate labels for edges, allignment issues persist.
- Graph now has labels!
- Graph_Image.jpg has also been added.