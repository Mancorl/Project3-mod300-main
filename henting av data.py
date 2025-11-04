import numpy as np

def Get_dim_and_size_of_atom():
    """
    Reads 'dna_coords.txt' and replaces atom symbols with their atomic radius.

    Each line in the file should be formatted as:
        <AtomType> <x> <y> <z>

    Returns
    -------
    np.ndarray
        Each row contains [radius, x, y, z] as floats.
    """
    atom_radius = {
        "H": 1.2,
        "O": 1.52,
        "P": 1.8,
        "C": 1.7,
        "N": 1.55,
    }

    return_list = []

    try:
        with open("dna_coords.txt", "r") as txt:
            for line in txt:
                parts = line.strip().split()
                if len(parts) != 4:
                    print(f"Skipping malformed line: {line.strip()}")
                    continue

                atom, x, y, z = parts
                if atom not in atom_radius:
                    print(f"Unknown atom type: {atom}")
                    continue

                radius = atom_radius[atom]
                return_list.append([radius, float(x), float(y), float(z)])

        return np.array(return_list)

    except FileNotFoundError:
        raise FileNotFoundError("Error: The file 'dna_coords.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return np.array([])


if __name__ == "__main__":
    print(Get_dim_and_size_of_atom())
