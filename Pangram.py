import string


def is_pangram(s):
    alphabet = string.ascii_lowercase
    list_alph = [x for x in alphabet]
    for i in s.lower():
        if i.isalpha():
            if i in list_alph:
                list_alph.remove(i)
            else:
                continue
        else:
            continue
    if list_alph == []:
        return True
    else:
        return False