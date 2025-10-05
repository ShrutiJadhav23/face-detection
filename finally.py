def func1():
    try:
        l=[1,2,3,4,5]
        i=int(input("Enter The Index"))
        print(l[i])
        return 1
    except:
        print("Some error Occured")
        return 0
    #finally:
        #print("I am Always Executed")
    print("I am Always Executed")

x=func1()
print(x)