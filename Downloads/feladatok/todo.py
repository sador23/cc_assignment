

#commands={'add': "add","liste":"liste","mark":"mark","archive":"archive"}
commands=["add","liste","mark","archive"]

class todo(): 
    todolist=[]
    marklist=[]
    marked="[x]"
    notmarked="[]"

    def add():
        a=input("add an item:")
        todolist.append(a)
        len(todolist)-1
        marklist.append(notmarked)
        len(notmarked)-1
        print("Item added.")

    def liste():
        print("You saved the following to-do items:")
        for i in range(0,len(marklist)):
            print(str(i+1) + " " + str(marklist[i]) + " " + todolist[i])

    def mark():



    def archive():
        for i in range(0,len(marklist)-1):
            if marklist[i]==marked:
                todolist.remove(i)
                marked.remove(i)
                print("You saved the following items : ")
                liste()
        print("archive")
    
    def command_input():
        while True:
            command=input("Please enter a command [add,liste,mark,archive]: ")
            if command in commands:
                getattr(todo,command)()


todo.command_input()