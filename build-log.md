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
- Graph now has labels! (haven't been aligned yet though).

### 06/25/2018
- Will be integrating a file handling system that converts .pdf into .jpeg.
- Trying to fix ```backward_time()``` function
- Implementing a ```graph_checker()``` function to check the continuity of the graph.

### 01/07/2018
- Fixed the ```rel_events()``` and ```abs_events()``` time calculator.
- Still working on the continuity issue.

### 09/07/2018
- Fixed the ```leaderNode``` issue. Works great now.
- Still working on the continuity.