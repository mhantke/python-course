def distance2(a, b):
    if a == b:
        print("Warning! The coordinates are the same!")
    else:
        ab0 = (a[0] - b[0])**2
        ab1 = (a[1] - b[1])**2
        d = (ab0 + ab1)**0.5
        return d