l_1 = [1,11,14,5,8,9]

def under_ten(input_list):
    return [item for item in input_list if item < 10]
    
#     output_list = []
#     for item in input_list:
#         if item < 10:
#             output_list.append(item)
#     return output_list

print(under_ten(l_1))

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def merge_and_sort(input_list_1,input_list_2):
    output_list = input_list_1 + input_list_2
    output_list.sort()
    return output_list

print(merge_and_sort(l_1,l_2))
print(list(set(merge_and_sort(l_1,l_2))))