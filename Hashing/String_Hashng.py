def hash_string(inp, table):
    sum = 0
    for i in range(len(inp)):
        sum += ord(inp[i])
    return sum%table


print hash_string("cat", 11)
