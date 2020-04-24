# a = ['1','2','3','4','5',('a','b','c')]
# for x in a:
#     for c in x:
#         print(c,end='')

#递增
# for a in range(0,10,2):
#     print(a,end="/")
#
# for x in range(10,0,-2):
#     print(x)

d = [1,2,3,4,5,6,7,8]
for i in range(0,len(d),2):
    print(d[i])
b = d[len(d):0:-2]
print(b)