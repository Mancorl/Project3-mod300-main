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
    return_list = []
    atom_radius = {
        "H": "1.2",
        "O": "1.52",
        "P": "1.8",
        "C": "1.7",
        "N": "1.55",
    }

    try:
        with open("dna_coords.txt") as txt:
            for line in txt:
                new_line = line.strip()
                for i in new_line:
                    if i in atom_radius:
                        new_line = new_line.replace(i, atom_radius[i])
                new_list = new_line.split()
                print(new_list)
                return_list.append(new_list)

    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return return_list


Get_dim_and_size_of_atom()


