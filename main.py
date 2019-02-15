'''
multiline comment

#print(1)
# single line


# print(1, 2, 3, 4, sep='&', end='_')
x = 1
y = 1.2


name = 'waliid durgahed'
length_name = len(name)
print(length_name)
# start:end:step
print(name[0:9])


names = ['rashid', 'walid', 'ali', 'zubeir']

for x in names:
    print(x)
    

#numbers = [1, 2, 3, 4, 5]

for x in range(1000):
    print(x)'''

width = 50
length = 100
area = width * length

#print(area)

width2 = 119
length2 = 234
area2 = width2 * length2

#print(area2)


'''
def area_rect(width, length):
    print(width*length)


area_rect(20, 40)
area_rect(40, 40)

def area_rect(width, length):
    return width*length

area_of_yard = area_rect(30, 100)
area_of_house = area_rect(40, 200)
area_of_property = area_of_yard + area_of_house

print(area_of_property)
# for x in range(10):
#    area_rect(x, 40)

def print_square():
    print('------')
    print('|    |')
    print('|    |')
    print('|    |')
    print('------')

for i in range(5):
    print_square()

my_number = 53

if my_number % 2 == 0:
    print('even')
else:
    print('odd')


nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for x in nums:
    if x < 5:
        print(x)



num = 64

for x in range(1, num+1):
    #print(x)
    if num % x == 0:
        print(x)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for element in b:
    if element in a:
        print(element)



word = 'dad'

if word == word[::-1]:
    print('palindrome')
else:
    print('not palindrome')
'''
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(
    [i for i in a if i%2==0]
    )