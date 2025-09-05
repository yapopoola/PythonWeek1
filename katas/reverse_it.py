def reverse_it(data):
    if type(data) == str:
        return data[::-1]
    elif type(data) == int:
        data = str(data)
        data = data[::-1]
        return int(data)
    elif type(data) == float:
        data = str(data)
        data = data[::-1]
        return float(data)
    else:
        return data
