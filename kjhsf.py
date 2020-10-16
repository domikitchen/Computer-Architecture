# ogarr = [
#   [8, [4]], 
#   [[90, 91], -1, 3], 
#   [9, 62], 
#   [[-7, -1, [-56, [-6]]]], 
#   [201], 
#   [[76, 0], 18],
# ]

# sum = 0

# def things(arr, newArr = [], newNewArr = []):
#     sum = 0
#     if len(newArr) == 0:
#         for a in arr:
#             if isinstance(a, int):
#                 newNewArr.append(a)
#             elif isinstance(a, list):
#                     things(arr, a)
#             else:
#                 print("hmmmm")
#     else:
#         min = 1902 * 1983
#         for a in newArr:
#             if isinstance(a, int):
#                 if a < min:
#                     min = a
#             elif isinstance(a, list):
#                     things(arr, a)
#             else:
#                 print("well heck")

#         if min != (1902 * 1983):
#             newNewArr.append(min)
        
#     for i in newNewArr:
#         sum += i

#     return sum

# print(things(ogarr))

# def rec_func(arr, storage=None):
#     if storage is None:
#         storage = list()
#     for a in arr:
#         temp_list = list()
#         for elem in a:
#             if type(elem) == list:
#                 rec_func([elem], storage)
#             else:
#                 temp_list.append(elem)
#         if len(temp_list) > 0:
#             storage.append(temp_list)
#         print(storage)
#     total = 0
#     for a in storage:
#         total += min(a)
#     return total
# print(rec_func(ogarr))


arr = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']

dic = {}

for a in arr:
    if (len(a) % 2) == 0:
        mid = int(len(a) / 2)
        dic[a] = a[mid]
    
    else:
        mid = int((len(a) / 2) + 0.5)
        dic[a] = a[mid]

arr = []

for a in dic:
    arr.append(dic[a])

arr = sorted(arr)

print(arr)
