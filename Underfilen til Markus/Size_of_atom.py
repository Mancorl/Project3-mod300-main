import numpy as np
def Get_dim_and_size_of_atom():
    """
    Reads 'dna_coords.txt' and replaces atom symbols with their atomic radius.

    Each line in the file should be formatted as:
        <AtomType> <x> <y> <z>

    Returns
    -------
    list of list of str
        Each inner list contains [radius, x, y, z] as strings.

    Raises
    ------
    FileNotFoundError
        If 'dna_coords.txt' is missing.
    """
    return_list_H = []
    return_list_O = []
    return_list_P = []
    return_list_C = []
    return_list_N = []
    atom_radius = {
        "H": "1.2",   
        "C": "1.7",
        "N": "1.55",
        "O": "1.52",
        "P": "1.8"
    }

    try:
        with open("dna_coords.txt") as txt:
            for line in txt:
                new_line = line.strip()
                #print(new_list)

                if new_line[0] == "H":
                    for i in new_line:
                        if i in atom_radius:
                            new_line = new_line.replace(i, atom_radius[i])
                    new_list = new_line.split()
                    new_list = [float(item) for item in new_list]
                    return_list_H.append(new_list)

                if new_line[0] == "O":
                    for i in new_line:
                        if i in atom_radius:
                            new_line = new_line.replace(i, atom_radius[i])
                    new_list = new_line.split()
                    new_list = [float(item) for item in new_list]
                    return_list_O.append(new_list)

                if new_line[0] == "P":
                    for i in new_line:
                        if i in atom_radius:
                            new_line = new_line.replace(i, atom_radius[i])
                    new_list = new_line.split()
                    new_list = [float(item) for item in new_list]
                    return_list_P.append(new_list)

                if new_line[0] == "C":
                    for i in new_line:
                        if i in atom_radius:
                            new_line = new_line.replace(i, atom_radius[i])
                    new_list = new_line.split()
                    new_list = [float(item) for item in new_list]
                    return_list_C.append(new_list)

                if new_line[0] == "N":
                    for i in new_line:
                        if i in atom_radius:
                            new_line = new_line.replace(i, atom_radius[i])
                    new_list = new_line.split()
                    new_list = [float(item) for item in new_list]
                    return_list_N.append(new_list)

    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    dna_list = return_list_H + return_list_O + return_list_P + return_list_C + return_list_N
    return np.array(return_list_H),np.array(return_list_O),np.array(return_list_P),np.array(return_list_C),np.array(return_list_N), np.array(dna_list)

