def countwordsfromfiles():
    filename = input("enter any file : ")
    count=0
    userinput=open(filename,"r")
    for i in userinput:
        words=i.split(" ")
        print(words)
        count=count+len(words)
    print("number of words " + str(count))

countwordsfromfiles()