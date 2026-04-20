# requirements: pine
import pine
import ghpythonlib.treehelpers as th
import rhinoscriptsyntax as rs

def transformObject(inpts):
    if (inpts[0] and inpts[1]):
        obj = inpts[0]
        matrix = inpts[1]
        transobj = rs.CopyObject( obj )
        rs.TransformObject(transobj, matrix)
    else:
        transobj = None
    return transobj

objlist = th.tree_to_list(obj,None)
matrixlist = th.tree_to_list(matrix,None)

outlist = pine.resolve([objlist, matrixlist], transformObject)

obj = th.list_to_tree(outlist)