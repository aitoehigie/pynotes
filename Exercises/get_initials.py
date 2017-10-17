# Write a program that takes a full name, prints the initials of the first,
# middle, and last name. If the middle name is “NA”, then the program
# should print only the initials of the first and the last name.


def get_initials(name):
    """ Return initials of first, last and middle name.
    If the middle name is 'NA', return only the initials of the first and the last name.
    
    >>> get_initials("Alfred E. Newman")
    >>> 'A.E.N.'
    >>> get_initials("John NA Smith")
    >>> 'J.S.'
    """

    # your code here
    result = ""
    if name.split()[1] == "NA":
        for item in name.split():
            result.join(item[0])+"."
        return result
    else:
        for item in name.split():
            result.join(item[0])+"."
	return result

