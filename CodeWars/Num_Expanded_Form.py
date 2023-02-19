def expanded_form(num):
    num_str = list(reversed(list(enumerate(reversed(str(num))))))
    exp_form_list = list((str(int(i[1]) * pow(10, i[0]))) for i in num_str if int(i[1]) != 0)
    return " + ".join(exp_form_list) 

input_num = expanded_form(4068)
print(input_num) 



def count_positives_sum_negatives(arr):
    counter = 0
    negative_sum = 0
    if arr == []:
        return []
    for i in arr:
        if i > 0:
            counter += 1
        elif i < 0:
            negative_sum += i
    return [counter, negative_sum]

result = count_positives_sum_negatives([1,2,3,-45,123,2,-1,4,12,-4,234,1,-132])
print(result)