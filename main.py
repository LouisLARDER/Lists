# list items are enclosed in square brackets
# lists are in order 
# lists are mutable
# lists elementrs do not nee to be unique
# lists can be differnt data

# list = []
# list = [1,2,3], 
# list = ['orange', 'apple', 'pear', 'banana']
# list = [1, 'hello', 5.0]

# print (list)

'''
list indexing
''' 
# fruits = ['orange', 'apple', 'pear', 'banana']
# print (fruits[0])

# fruits = ['orange', 'apple', [ 'pear', 'banana']]
# print (fruits[2][1]) 




'''
how to slice
'''
# fruits = ['orange', 'apple', 'pear', 'banana']

# # print(fruits [0:3])
# # print(fruits[:-2])
# # print(fruits[::2])
# print(fruits[:])
# print(fruits[2:5])
# print(fruits[:-2]) 
# print(fruits[:2]) 
# print(fruits[::2])
# print(fruits[::-1])

'''
add elements to a list
'''
# fruits = ['orange', 'apple', 'pear', 'banana']

# # fruits[0] = 'berries'
# # print (fruits)

# # fruits[1:3] = ['mandarins','peaches','plums']
# # print (fruits)

# fruits.append('limes')
# print(fruits)


'''
remove or delete list items
'''

# fruits = ['orange', 'apple', 'pear', 'banana']

# del fruits[0]
# print(fruits)

# del fruits[0:2]
# print(fruits)

# del fruits
# print(fruits)



''''
pythonlist methods
'''
# print(dir(list))
# print(help(list.count))
# fruits = ['orange', 'apple', 'pear', 'banana','banana']
# # fruits.append('cashew', 'tomato')# can only give one argument

# # print(fruits)
# #============

# # fruits.insert(0, ' tomato')
# # print(fruits)

# #=============
# # fruits.clear()
# # print (fruits)

# #==================

# # fruits.pop(1)
# # print (fruits)

# pos = fruits.index('banana')
# fruits.pop(pos)
# print(fruits)

#=======================================

# print(fruits.count('banana'))

# result = {}
# for x in fruits:
#    result[x] = fruits.count(x)

# print (result)

# from collections import Counter

# print(Counter(fruits))

#====================================

'''
list membership test
'''
# fruits = ['orange', 'apple', 'pear', 'banana','banana']

# print('orange' not in fruits)