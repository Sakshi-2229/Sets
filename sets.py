# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 22:33:21 2023

@author: sai
"""

'''
#creating a set
1. dont allow duplicates
2. enclosed in curly braces
3. unordered.
'''
"""
"""
basket={'apple','orange','apple','pear','orange','banana'}
print(basket)

#when will run this code it will print apple and orange only once.

#accessing elements in the set 
for item in basket:
    print(item)

#adding item to sets
basket={'apple','orange','apple','pear','orange','banana'}
basket.add('apricot')
print(basket)

#if you want to add more than one item to a set you can use the update
#when you want to update in sets you need to pass elements in the form of list
basket={'apple','orange','apple','pear','orange','banana'}
basket.update(['apricote','mango','grape'])
print(basket)

#obtaining the length of a set
basket={'apple','orange','apple','pear','orange','banana'}
len(basket)


#obtaining the max and min values in a set
basket2={1,2,3,4,5}
print(min(basket2))
print(max(basket2))


#removing an item
basket={'apple','orange','apple','pear','orange','banana'}
print(basket)
basket.remove('apple')
basket.discard('apricot')
print(basket)


#set operations
s1={'apple','orange','banana'}
s2={'grapefruit','lime','banana'}
print('Union:', s1 | s2)
print('Intersection:', s1 & s2)
print('Difference:', s1 - s2)
