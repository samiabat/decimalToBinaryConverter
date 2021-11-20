def decimalToBinaryConverter(n):
    temp = 0
    string = ""
    fra = n - int(n)
    m = int(n)
    while m != 0:
        if m%2 == 0:
            string = string + "0"
        else:
            string = string + "1"
        m = m//2
    fin = string[::-1]
    if fra != 0.0:
        fin = fin + "."
        for i in range(10):
            if (fra != 1.0) or (fra != 0.0):
                temp = 2*fra
                if temp < 1:
                    fin = fin + "0"
                else:
                    fin = fin + "1"
                fra = temp - int(temp)

    rev = fin[::-1]
    loc = rev.find("1")
    re = rev[loc:]
    string = re[::-1]
    return string
