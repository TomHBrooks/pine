# requirements: pine
import pine
import ghpythonlib.treehelpers as th
import rhinoscriptsyntax as rs

def addCircle(inpts):
    print(inpts)
    if (inpts[0] and inpts[1]):
        circ = rs.AddCircle( inpts[0], inpts[1] )
    else:
        circ = None
    return circ

centrelist = th.tree_to_list(centre,None)
radiuslist = th.tree_to_list(radius,None)

outlist = pine.resolve([centrelist, radiuslist], addCircle)

circ = th.list_to_tree(outlist)