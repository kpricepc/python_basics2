x = lambda a : a + 10
print(x(6)) 

x = lambda a, b : a * b
print(x(10, 15)) 

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

List = [[1,3,2],[4,6,13,11],[5,9,7,19]]
sortList = lambda x: (sorted(i) for i in x)
Largest = lambda x, f : [y[len(y)-1] for y in f(x)]
res = Largest(List, sortList)
print(res)