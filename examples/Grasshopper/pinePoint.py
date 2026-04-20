# requirements: pine
import pine
import ghpythonlib.treehelpers as th
import rhinoscriptsyntax as rs

def addPoint(coords):
    if (coords[0] and coords[1] and coords[2]):
        pt = rs.AddPoint( (coords[0],coords[1],coords[2]) )
    else:
        pt = None
    return pt

xlist = th.tree_to_list(x,None)
ylist = th.tree_to_list(y,None)
zlist = th.tree_to_list(z,None)

outlist = pine.resolve([xlist, ylist, zlist], addPoint)

pt = th.list_to_tree(outlist)