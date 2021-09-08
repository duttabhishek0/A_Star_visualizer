# A Star Visualizer
This is a visualizer to visualize the A star algorithm, used in finding the shortest path using a heuristic. A heuristic is used to guess the  minimal cost of a node to the target. So when choosing a node, we don't only analyze the cost from the start to this node but also the probable cost from the node to the target. This allows us to ignore paths that would lead to wrong direction.
<br>
In any path finding problem, there are always two things given:
<ol>
  <li> Starting Node</li>
  <li> Goal Node</li>
</ol>
The objective is to move from the Start Node to the Goal node, and for that a shortest path has to be selected.

The formula used to calculate the path :
```
  f(n) = g(n) + h(n)
  
  f(n) => Resultant cost if we visit the node n by taking that path.
  g(n) => Cost of the current node from the start node.
  h(n) => Cost of the current node, when we move from that particular node to the end node or the goal node..
```
In the above formula, the cost is calculated, then at the next iteration, it is checked whether the path previously taken is optimal or not.

# The Visualizer
This project goes with modular approach to build the visualiser by separating the following into individual modules
- Algorithm  (The core of this visualizer)
- Drawing facilities  (Added support for pointing )
- Nodes   
- Colors Used

I have used the [gruvbox color scheme](https://github.com/morhetz/gruvbox). 

I have added all the requirements in the [requirements.txt](https://github.com/duttabhishek0/A_Star_visualizer/blob/main/requirements.txt) file
