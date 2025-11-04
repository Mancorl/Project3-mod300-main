
"""
This file contains the function that reads the txt file and gives sizes to all of the atoms
"""
import numpy as np
def Get_dim_and_size_of_atom():
    """
    Reads 'dna_coords.txt' and replaces atom symbols with their atomic radius.

    Each line in the file should be formatted as:
        AtomType x y z

    Returns
    -------
    list of list of str
        Each inner list contains [radius, x, y, z] as strings.

    Raises
    ------
    FileNotFoundError
        If 'dna_coords.txt' is missing.
    """
    atom_radius = {
        "H": 1.2,
        "O": 1.52,
        "P": 1.8,
        "C": 1.7,
        "N": 1.55,
    }

    atoms = {
    "H": [],
    "O": [],
    "P": [],
    "C": [],
    "N": []
    }


    try:
        with open("dna_coords.txt") as txt:
            for line in txt:
                parts = line.strip().split()

                assert len(parts) == 4, "Line in dna_coords.txt does not have 4 values"

                atom = parts[0]

                assert atom in atom_radius, "Unknown atom type found"

                x = float(parts[1])
                y = float(parts[2])
                z = float(parts[3])
                r = atom_radius[atom]

                atoms[atom].append([r, x, y, z])

    except FileNotFoundError:
        print("Error: 'dna_coords.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    
    H = np.array(atoms["H"])
    O = np.array(atoms["O"])
    P = np.array(atoms["P"])
    C = np.array(atoms["C"])
    N = np.array(atoms["N"])

    
    dna_list = []
    for i in [H, O, P, C, N]:
        if len(i) > 0:
            for atom in i:
                dna_list.append(atom)

    dna_list = np.array(dna_list)

    return H, O, P, C, N, dna_list

if __name__ == "__main__":
    Get_dim_and_size_of_atom()
