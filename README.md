# pine

A data tree traversal library for Python, inspired by Grasshopper's 
data tree logic (Rhino3D).

pine allows you to write functions that operate on nested list structures 
(data trees). The traversal and input matching is handled recursively by 
pine.resolve().

## Install

pip install pine

## How It Works

pine takes data from nested lists (data trees) and a specially formatted function 
as input, and handles the combination and distrobution of that data into the
function; matching branches and leaves, and sending them to the function for
processing. It outputs the results in a new data tree, maintaining the inputs
structure.

pine does this in its "resolve" function which takes the longest input list 
and trys to match each of its elements with elements of the shorter lists,
first by index, then by repeating the last element of the shorter lists if
it has run out of elements to match. It starts at the root of each data tree 
and works up through the branches until each leaf is matched.

If one or more of the matched elements is a list then all of the elements are 
recusively passed back to the resolve function for further matching.

When all the lists have been resolved into list items and matchhed they are sent 
to the function for processing.

```
Example 1.
pine.resolve([['a'],['x']],concat) = ['ax']
There are two data tree inputs, ["a"] and ["x"]; elements a and x are matched and concatenated together.

Example 2.
pine.resolve([['a', 'b', 'c'],['x', 'y', 'z']],concat) = ['ax', 'by', 'cz']
Adding 2 elements to both inputs; since the inputs are the same length the elements of the inputs are matched by index.

Example 3.
pine.resolve([['a', 'b', 'c'],['x']],concat) = ['ax', 'bx', 'cx']
Reducing the second input to one element; a and x are matched, then the last element in the smaller input, x, is distrobuted over b and c

Example 4.
pine.resolve([[['a1', 'a2'], 'b', 'c'],['x']],concat) = [['a1x', 'a2x'], 'bx', 'cx']
Replacing a with ["a1","a2"] in the first input; x is distrobuted over all of the elements. The output data tree has the same structure as the first input.

Example 5.
pine.resolve([[['a1', 'a2'], 'b', 'c'],[['x1', 'x2']]],concat) = [['a1x1', 'a2x2'], ['bx1', 'bx2'], ['cx1', 'cx2']]
Replacing x with ["x1","x2"] in the second input; a1 is matched with x1, a2 is matched with x2, then ["x1","x2"] is distrobuted over b and c.
Resulting in a new, combined data tree structure.

Example 6.
pine.resolve([[['a1', 'a2'], 'b', 'c'],[['x1', 'x2'], ['y1', 'y2']]],concat) = [['a1x1', 'a2x2'], ['by1', 'by2'], ['cy1', 'cy2']]
Adding ["y1","y2"] to the second input; all the a's and x's are matched as before and ["y1","y2"] is distrobuted over "b" and "c".
```

## Writing a pine-compatible function

A function passed to pine.resolve() receives a flat list of matched 
inputs — one value per input — and returns a single output value.

```python
def add(inputs):
    return inputs[0] + inputs[1]

result = pine.resolve([[1, 2, 3], [10, 20]], add)
# result: [11, 22, 23]  — last element of shorter list repeats
```

The function only needs to handle a single set of scalar inputs. 
pine handles the iteration and nesting.

## Using pine in Grasshopper

1. Import the pine python library (use ```# requirements: pine``` to automatically download the library from PyPI first).
1. Create a python component. Set it's inputs to "tree access", and set the input(s) and output(s) type hints.
2. Convert your inputs to a list with ghpythonlib.treehelpers.tree_to_list().
3. Create a function which takes a list of inputs as it's only argument.
4. Process your inputs by nesting them into an array, and passing this, and your function to pine.resolve()
5. Store the output and convert it to a grasshopper tree with ghpythonlib.treehelpers.tree_to_list(), pass this to your nodes output.

[<img src="Examples/Images/pine_Grasshopper_node.png">]

```python
# requirements: pine
import pine
import ghpythonlib.treehelpers as th

def add(inputs):
    return inputs[0] + inputs[1]

xlist = th.tree_to_list(x, None)
ylist = th.tree_to_list(y, None)

result = pine.resolve([xlist, ylist], add)
a = th.list_to_tree(result)
```

## Grasshopper Plugin

To try the nodes in examples see [Grasshopper Plugin]("/grasshopper/pine.Components.gha")

## Status

Core resolve algorithm complete and published to PyPI. 
Grasshopper plugin in development.

## Why pine?

pine provides an intuitive way of working with data trees in python and grasshopper.

pine used in Grasshopper allows for automatic branch matching, which can improve node graph
logic.

[<img src="Examples/Images/Pine_Example_01.png">]