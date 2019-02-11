def addBinary(a, b):
    result = ""
    plus = 0
    length_a = len(a)
    length_b = len(b)
    a = list (a)
    b = list (b)
    for i in range(length_a):
        a[i] = int (a[i])
    for i in range(length_b):
        b[i] = int (b[i])
    while length_a > 0 and length_b > 0:
        a[length_a - 1] += plus
        if a[length_a - 1] == 2:
            a[length_a - 1] -= 2
            plus = 1
        else:
            plus = 0
        a[length_a - 1] += b[length_b - 1]
        if a[length_a - 1] == 2:
            a[length_a - 1] -= 2
            plus = 1
        length_a -= 1
        length_b -= 1
    while length_a > 0:
        a[length_a - 1] += plus
        if a[length_a - 1] == 2:
            a[length_a - 1] -= 2
            plus = 1
        else:
            plus = 0
        length_a -= 1
    while length_b > 0:
        b[length_b - 1] += plus
        if b[length_b - 1] == 2:
            b[length_b - 1] -= 2
            plus = 1
        else:
            plus = 0
        a.insert(0,b[length_b - 1])
        length_b -= 1
    if plus == 1:
        a.insert(0,plus)

    for i in range (len (a)):
        a[i] = str(a[i])
    return "".join (a)

a = "11"
b = "1"
print (type (addBinary(a,b)))
print (addBinary(a,b))


