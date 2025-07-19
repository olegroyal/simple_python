colors = ['red', 'blue', 'green'] + [1,2,3,4]
print(colors[0])    ## red
print(colors[5])    ## green
print(len(colors))  ## 3

squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num
print(sum)  ## 30

list = [1, 2, 3, 4]
if  2 in list:
    print("Way")

## print the numbers from 0 through 9
for i in range(10):
    print(i)

## Access every 3rd element in a list
i = 2
a = '123123123123123123123'
while i < len(a):
    print(a[i])
    i = i + 3
print(f'\nNext ***************\n')

list = ["Oleg","Pinchuk","Grior","1963"]
list.append('13/04')
list.insert(1,'first')
list.extend(['first','second'])
list.remove('first')
list.remove('first')
list.pop(1)
list.append(55)

print(list)
print(list.index('13/04'))

list = []
list.append('a')  ## Use append() to add elements
list.append('b')
print(list)

list = ['a', 'b', 'c', 'd']
print(list[1:-1])   ## ['b', 'c']
list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
print(list)         ## ['z', 'c', 'd']
