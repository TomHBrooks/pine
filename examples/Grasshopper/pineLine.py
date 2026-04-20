# requirements: pine
import pine
import ghpythonlib.treehelpers as th
import rhinoscriptsyntax as rs

def addLine2Pt(pts):
    if (pts[0] and pts[1]):
        pt = rs.AddLine( pts[0],pts[1] )
    else:
        pt = None
    return pt

Alist = th.tree_to_list(A,None)
Blist = th.tree_to_list(B,None)

outlist = pine.resolve([Alist, Blist], addLine2Pt)

line = th.list_to_tree(outlist)