print ('''1. Hello World!!
  This is a multiline string.
    Here's the end
    ''')

#
#   Parameters
#
age = 63
name = 'Chip'

print ('2. {0} is {1} years old when he entered this tiny Python program'.format(name, age))
print ('Why is {0} playing with Python?'.format(name))

#
#   Using named parameters in format method
#
print ('''
3. {name} is {age} years old when he entered this tiny Python program. 
           Again with named parameters to format method!'''.format(name=name, age=age))

#
#   Printing using f-strings
#
print (f'{name} is {age} years old whe he wrote this tiny program using f-strings')
print ("")
#
# More format method argumentation
#
print ("4. Printing functionality")
print ('Precision of 1/3 is {0:.3f}'.format(1.0 / 3))
print ('{0:_^11}'.format('hello'))
print ('{name} wrote this program named {filename}'.format(name='Chip', filename="Helloworld"))
print ('a', end=' ')
print ('b', end=' ')
print ('c')