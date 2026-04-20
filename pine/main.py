def isArray(x):
    if type(x) in (tuple, list):
        return True
    else:
        return False

def resolve(inputs, func):
    
    #The length of each input
    iLen=[]
    #Largest length
    maxLen=0

    #Calculate and store input lengths. Handle non-array inputs
    for i in inputs:
        l = len(i) if isArray(i) else 1
        maxLen = l if l > maxLen else maxLen
        iLen.append(l - 1)
    
    #Output array
    out = []

    #Iterate over the maximum input elements
    for i in range( 0, maxLen ):

        #Passed to the function if an item (non-array), recusively passed to back to resolve if it's an array
        inp = []
        toResolve = False
        empty = False
        
        #iterate over the inputs
        for j in range(0, len(inputs)):
                
            #If the jth input is an array recusively resolve it's ith element (or the last element if iLen[j] < i)
            #If it's a item (non-array) pass it straight to the input.
            if isArray(inputs[j]):
                if len(inputs[j]) > 0:
                    r = inputs[j][min(i,iLen[j])]
                else:
                    empty = True
            else:
                if inputs[j] is not None:
                    r = inputs[j]
                else:
                    empty = True

            #Handle empty input
            if empty == True:
                r = []
            
            #Flag array elements
            if isArray(r):
                toResolve = True

            inp.append(r)
        
        if not empty:
            if toResolve:
                out.append( resolve(inp,func) )
            else:
                out.append( func(inp) )
            
    return out