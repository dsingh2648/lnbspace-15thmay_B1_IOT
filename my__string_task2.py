s = input("Enter your string : ")
x = {i:s.count(i) for i in s}
x_length = len(x)
x_value = list(x.values())
x_max = max(x_value)
x_new = [x_max - x_value[i] for i in range(x_length)]


if(x_new.count(0)==x_length or x_new.count(0)==1):
    print("yaa!!it's My String")

else:
    print("oops!!it's not my string")



