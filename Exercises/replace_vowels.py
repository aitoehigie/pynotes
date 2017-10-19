# Replacing vowels with whitespaces


def replace_vowels(text):
    """ Return the text after replacing the vowels in it with whitespaces.
    
    >>> replace_vowels("This Is fun.")
    >>> 'Th s  s f n.'
    """

    # your code here
    x = list(text)
    for item in x:
        if item in ["a", "e", "i", "o", "u"]:
            x[x.index(item)] = " "
        else:
            continue
    return "".join(x)

        
        
