def UFO(N, data, octal):
    result = []
    if octal == True:
        for i in range(N):
            degree = len(str(data[i])) - 1
            e_bit = 0
            for j in(str(data[i])):
                e_bit = e_bit + (int(j) * (8 ** degree))
                degree = degree - 1
            result.append(e_bit)
    else:
        for i in range(N):
            degree = len(str(data[i])) - 1
            s_bit = 0
            for j in(str(data[i])):
                s_bit = s_bit + (int(j) * (16 ** degree))
                degree = degree - 1
            result.append(s_bit)
    return result