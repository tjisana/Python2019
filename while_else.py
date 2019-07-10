# data = [1,3,4,5,6,9,16]

# for x in data:
#     if x == 4:
#         print("Found 4")
#         break
# else:
#     raise ValueError("4 not found")

# print("Cooking with gas")
def inclusive_range(*args, **kwargs):
    l = len(args)
    start = 0
    step = 1
    if kwargs:
        if 'step' in kwargs:
            start = kwargs['start']
            stop = kwargs['stop']
            step = kwargs['step']
    else:
        if l==0:
            raise TypeError("Expected at least 1 argument, got {}".format(l))
        elif l==1:
            stop = args[0]
        elif l==2:
            start, stop = args
        elif l==3:
            start, stop, step = args
        else:
            raise TypeError("Expected at least 1 argument, got {}".format(l))
    
    while start <= stop:
        yield start
        start+=step
        
for x in inclusive_range(start=1,stop=4,step=1):
    print(x)

for x in range(1,4,1):
    print(x)