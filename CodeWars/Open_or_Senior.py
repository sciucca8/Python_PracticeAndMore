def open_or_senior(data):
    output = []
    while len(data) > 0:
        if data[0][0] >= 55 and data[0][1] > 7:
            output.append('Senior')
        else:
            output.append('Open')
        data.pop(0)
    return output

open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)])