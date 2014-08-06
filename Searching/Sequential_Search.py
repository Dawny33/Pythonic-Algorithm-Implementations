def sequential_search(alist,item):
    pos = 0
    found = False

    while(pos<len(alist)) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1

    return found        


alist2 = [1,24,56,25,16,2]

print sequential_search(alist2, 5)
        
