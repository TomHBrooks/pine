# requirements: pine
import pine
import ghpythonlib.treehelpers as th
import rhinoscriptsyntax as rs

def concat(strs):
    out = ""
    for s in strs:
        if s is not None: 
            out = out + s
        else:
            out = out + ""
            break
    return out

xlist = th.tree_to_list(x,None)
ylist = th.tree_to_list(y,None)

outlist = pine.resolve([xlist, ylist], concat)

string = th.list_to_tree(outlist)