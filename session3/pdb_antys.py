def read_pdb(filename):
    if filename.endswith(".pdb"):
        with open(filename,'r') as file_handle:
            list_of_strings = file_handle.readlines()
            for string in list_of_strings:
                if string.startswith("ATOM"):
                    x=float(string[30:38])
                    y=float(string[38:46])
                    z=float(string[46:54])
                    atom=string[77:78]
                    if atom=="H":
                        atom=1
                    if atom=="C":
                        atom=6
                    if atom=="N":
                        atom=7
                    if atom=="O":
                        atom=8
                    if atom=="S":
                        atom=16
                    print(f"{numpy.array([x, y, z, atom])}")