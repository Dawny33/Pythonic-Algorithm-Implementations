from timeit import default_timer

def list1():
    start = default_timer()
    l = []
    for i in range(1000):
        l = l + [i]
    duration = default_timer() - start
    return duration

def list2():
    start = default_timer()
    l = []
    for i in range(1000):
        l.append(i)
    duration = default_timer() - start
    return duration

def list3():
    start = default_timer()
    l = [i for i in range(1000)]
    duration = default_timer() - start
    return duration

def list4():
    start = default_timer()
    l = list(range(1000))
    duration = default_timer() - start
    return duration


print list1()
print list2()
print list3()
print list4()

'''Running Time Analysis:
list1 > list2 > list3 > list4
'''
#Popping from an end of the list takes O(1); while anywhere in the middle, it in O(n), as the list needs to re-size