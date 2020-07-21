def square_digits(num):
    num_list = [(int(i)**2) for i in str(num)]
    return int(''.join(map(str, num_list)))
    pass
