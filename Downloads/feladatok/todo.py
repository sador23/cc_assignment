commands=["add","liste","mark","archive"]
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
        print ('You saved the following to-do items:')
        liste ()
        i = input ('Which one you want to mark as completed: ')
        marklist[i] = marked
        print (str(todolist[i]) + ' is completed')


def archive():
        for i in range(0,len(marklist)-1):
            if marklist[i]==marked:
                todolist.remove(i)
                marked.remove(i)
                print("You saved the following items : ")
                liste()
    
def command_input():
        while True:
            command=input("Please enter a command [add,liste,mark,archive]: ")
            if command in commands:
                if command=="add":
                    add()
                elif command =="liste":
                    liste()
                elif command=="mark":
                    mark()
                elif command=="archive":
                    archive()

command_input()