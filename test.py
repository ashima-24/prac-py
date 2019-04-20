largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done": break
        n = int(num)
        if largest is None:
            largest = n
            smallest =n
        if n > largest:
            largest = n
        if n < smallest:
            smallest = n
        #print(largest)
    except :
        k =1
if k ==1 :
    print("Invalid input")
print("Maximum", largest)
print("Minimum",smallest)
