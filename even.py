num=list(map(int,input("enter a list of integers separated by space: ").split()))
result=[]
for n in num:
    if n%2!=0:
        result.append(n)
        print("entered numbers",nums)
        print("list after removing even numbers:",result)
