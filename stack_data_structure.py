import array as arr
size=int(input("Enter size of the stack : "))
stack = arr.array('i',[ ])
top=-1

print("1. Push  2. Pop  3. Display  4. Exit")

while(1):
    opt=int(input(("Enter your option : ")))
    if(opt==1):
        if (top == size - 1):
            print("Stack overflow.")
        else:
            ele = int(input("Enter element : "))
            top = top + 1
            stack.insert(top, ele)

    elif(opt==2):
        if(top==-1):
            print("Stack is Underflow")
        else:
            print("Deleting element :",stack[top])
            stack.pop()
            top=top-1
    elif(opt==3):
        if (top == -1):
            print("Stack is empty.")
        else:
            print("Stack elements : ",end=' ')
            for k in range(0,len(stack)):
                print(stack[k],end=' ')
        print()
    elif(opt==4):
        break
    else:
        print("Invalid option.")
