# requirements: pine
import pine
import ghpythonlib.treehelpers as th
import rhinoscriptsyntax as rs

def add(nums):
	print(nums)
	out = 0
	for n in nums:
		if n is not None: 
		    out = out + n
		else:
			out = None
			break
	return out

xlist = th.tree_to_list(x,None)
ylist = th.tree_to_list(y,None)

outlist = pine.resolve([xlist, ylist], add)

num = th.list_to_tree(outlist)