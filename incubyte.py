def add(x):
    if len(x) == 0:
        return 0
    else:
        y = x.split(',')
        sum = 0
        for i in y:
            if i.isalpha():
                sum += ord(i) - 96
            elif int(i) > 1000:
                continue
            elif int(i) < 0:
                print(str(i) +" Negative not Allowed")
                continue
            else:
                sum += int(i)

        return sum

x = input("Enter String:")
a = add(x)
print("Sum is : " +str(a))