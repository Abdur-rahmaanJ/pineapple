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
'''
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