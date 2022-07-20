def segundos(d,h,m,s):
    d *= 24
    d *= 60
    d *= 60
    h *= 60
    h *= 60
    m *= 60
    s += d+h+m
    print(s)