def getdate():
    import datetime
    return datetime.datetime.now()

def take(k):
    if k==1:
        a = int(input("Enter 1 for exersise and 2 for food "))
        if(a==1):
            value = input("type here\n")
            with open ("Ajay_ex.txt" , "a") as f:
                f.write(str([str(getdate())])+": "+value+"\n")
                print("successfully written")
        elif(a==2):
            value = input("type here\n")
            with open ("Ajay_food.txt" , "a") as f:
                f.write(str([str(getdate())])+": "+value+"\n")
                print("successfully written")
    elif(k==2):
        a = int(input("Enter 1 for exersise and 2 for food "))
        if(a==1):
            value = input("type here\n")
            with open ("Saket_ex.txt" , "a") as f:
                f.write(str([str(getdate())])+": "+value+"\n")
                print("successfully written")
        elif(a==2):
            value = input("type here\n")
            with open ("Saket_food.txt" , "a") as f:
                f.write(str([str(getdate())])+": "+value+"\n")
                print("successfully written")

    elif(k==3):
        a = int(input("Enter 1 for exersise and 2 for food "))
        if(a==1):
            value = input("type here\n")
            with open ("Robin_ex.txt" , "a") as f:
                f.write(str([str(getdate())])+": "+value+"\n")
                print("successfully written")
        elif(a==2):
            value = input("type here\n")
            with open ("Robin_food.txt" , "a") as f:
                f.write(str([str(getdate())])+": "+value+"\n")
                print("successfully written")
    else:
        print("Please enter valid input 1(Ajay),2(Saket),3(Robin)")
def retrieve(k):
    if k==1:
        a=int(input("Enter 1 for execersise and 2 for food"))
        if (a==1):
            with open("Ajay_ex.txt" , "a")as f:
                for i in f:
                    print(i,end="")
        elif(a==2):
             with open("Ajay_food.txt")as f:
                for i in f:
                    print(i,end="")
    elif(k==2):
        a=int(input("Enter 1 for execersise and 2 for food"))
        if (a==1):
            with open("Saket_ex.txt")as f:
                for i in f:
                    print(i,end="")
        elif(a==2):
             with open("Saket_food.txt")as f:
                for i in f:
                    print(i,end="")
    elif(k==3):
        a=int(input("Enter 1 for execersise and 2 for food"))
        if (a==1):
            with open("Robin_ex.txt")as f:
                for i in f:
                    print(i,end="")
        elif(a==2):
             with open("Robin_food.txt")as f:
                for i in f:
                    print(i,end="")
    else:
        print("Please enter valid input 1(Ajay),2(Saket),3(Robin)")

print("HELTH MANAGMENT SYSTEM: ")
b= int(input("Press 1 for log the value and 2 for Retrieve"))

if b==1:
    c=int(input("Press 1 for Ajay 2 for Saket 3 for Robin"))
    take(c)
else:
    c= int(input("Press 1 for Ajay 2 for Saket 3 for Robin"))
    retrieve(c)
