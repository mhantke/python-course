def pdbatoms(file1, file2):
    filein=open(file1, "r")
    fileout=open(file2, "w")
    for line in filein:
        if line[0:4] == "ATOM":
            x = line[31:38]
            y = line[40:46]
            z = line[48:54]
            e = line[77:78]
            coord = f'{x}, {y}, {z}, {e}\n'
            print(coord)
            fileout.write(coord)