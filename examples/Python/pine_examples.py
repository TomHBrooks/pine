import pine

def multiply(nums):
    return nums[0]*nums[1]

def concat(strs):
    return strs[0] + strs[1]


a = ["a","b","c"]
b = ["x","y","z"]

print("inputs a = {} b = {}".format(a,b))

results = pine.resolve([a,b],concat)

print("a & b concatenated = {}".format(results))

a = ["a","b","c"]
b = ["x","y"]

print("inputs a = {} b = {}".format(a,b))

results = pine.resolve([a,b],concat)

print("a & b concatenated = {}".format(results))

a = [["a"],["b"],["c"]]
b = [["x","y","z"]]

print("inputs a = {} b = {}".format(a,b))

results = pine.resolve([a,b],concat)

print("a & b concatenated = {}".format(results))

a = [["a","b"],["c"]]
b = [["x"],["y","z"]]

print("inputs a = {} b = {}".format(a,b))

results = pine.resolve([a,b],concat)

print("a & b concatenated = {}".format(results))

a = [ ["a"]          ,["b",["c","d"]] ]
b = [ ["w",["x","y"]],"z"             ]

print("inputs a = {} b = {}".format(a,b))

results = pine.resolve([a,b],concat)

print("a & b concatenated = {}".format(results))

a = [[["a"]],[["b"],"c"]]
b = ["x","y","z"]

results = pine.resolve([a,b],concat)

print("a & b concatenated = {}".format(results))

a = [0,[1,2],[3,[4,5]]]
b = [[1],[2],[[3]]]

results = pine.resolve([a,b],multiply)
print(results)

#######################################

print("Example 1.")
data_tree_1 = ["a"]
data_tree_2 = ["x"]
results = pine.resolve([data_tree_1,data_tree_2],concat)
print("pine.resolve([{},{}],concat) = {}".format(data_tree_1,data_tree_2,results))
print('There are two data tree inputs, ["a"] and ["x"]; elements a and x are matched and concatenated together.\n')

print("Example 2.")
data_tree_1 = ["a","b","c"]
data_tree_2 = ["x","y","z"]
results = pine.resolve([data_tree_1,data_tree_2],concat)
print("pine.resolve([{},{}],concat) = {}".format(data_tree_1,data_tree_2,results))
print("Adding 2 elements to both inputs; since the inputs are the same length the elements of the inputs are matched by index.\n")

print("Example 3.")
data_tree_1 = ["a","b","c"]
data_tree_2 = ["x"]
results = pine.resolve([data_tree_1,data_tree_2],concat)
print("pine.resolve([{},{}],concat) = {}".format(data_tree_1,data_tree_2,results))
print("Reducing the second input to one element; a and x are matchen then, the last element in the smaller input, x, is distrobuted over b and c\n")

print("Example 4.")
data_tree_1 = [["a1","a2"],"b","c"]
data_tree_2 = ["x"]
results = pine.resolve([data_tree_1,data_tree_2],concat)
print("pine.resolve([{},{}],concat) = {}".format(data_tree_1,data_tree_2,results))
print('Replacing a with ["a1","a2"] in the first input; x is distrobuted over all of the elements - ')
print('the output data tree has the same structure as the first input.\n')

print("Example 5.")
data_tree_1 = [["a1","a2"],"b","c"]
data_tree_2 = [["x1","x2"]]
results = pine.resolve([data_tree_1,data_tree_2],concat)
print("pine.resolve([{},{}],concat) = {}".format(data_tree_1,data_tree_2,results))
print('Replacing x with ["x1","x2"] in the second input; a1 is matched with x1, a2 is matched with x2, then ["x1","x2"] is distrobuted over b and c.\n')
print('Resulting in a new, combined data tree structure.\n')

print("Example 6.")
data_tree_1 = [["a1","a2"],"b","c"]
data_tree_2 = [["x1","x2"],["y1","y2"]]
results = pine.resolve([data_tree_1,data_tree_2],concat)
print("pine.resolve([{},{}],concat) = {}".format(data_tree_1,data_tree_2,results))
print('Adding ["y1","y2"] to the second input; all the a\'s and x\'s are matched as before and ["y1","y2"] is distrobuted over "b" and "c".') 
print('Resulting in a new, combined data tree structure.\n')
