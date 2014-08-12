#This algorithm ensures that nagrams are dealt differently during hashing.
#This is done, by weighing the ordinal value by the char's position.
#(i+1) because Python's indexing starts from 0.


def str_ana_check(inp, table):
    sum = 0
    for i in range(len(inp)):
        sum += (ord(inp[i]))*(i+1)

    return sum%table

print str_ana_check("cat", 11)
