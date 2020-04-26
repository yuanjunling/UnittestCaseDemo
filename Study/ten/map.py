from functools import reduce

list_x = [1,2,3,4,5,6,7,8]
list_y = [1,4,9,16,25,36,49,64]
r = map(lambda x,y:x*x+y,list_x,list_y)
print(list(r))

# for i in list_x:
#     print(square(i),end='')

r = reduce(lambda x,y:x+y,list_x,10)
print(r)

