import numpy
proton_number={'C': 6, 'N': 7, 'O' : 8, 'S' :16}
def read_pdb(filename='1PRE.pdb'):
    X=[]
    Y=[]
    Z=[]
    A=[]
    with open('1PRE.pdb','r') as file_handle:
        lines=file_handle.readlines()
        for line in lines:
            if line[17:20] == "CYS":
                x=float(line[31:38])
                y=float(line[39:47])
                z=float(line[47:55])
                prot=line[77:78]
                a=proton_number[prot]
                X.append(x)
                Y.append(y)
                Z.append(z)
                A.append(a)
    X = numpy.array(X)
    Y = numpy.array(Y)
    Z = numpy.array(Z)
    A = numpy.array(A)
    return (X, Y, Z, A)