def Binary_search(alist, item):

    first = 0
    last = len(alist) - 1
    found = False
    
    while not found and (first<last):
        mid = (first+last)//2

        if alist[mid] == item:
            found = True

        else:
            if item > alist[mid]:
                first = mid+1
            if item < alist[mid]:
                last = mid

    return found            
