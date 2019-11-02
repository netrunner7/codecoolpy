# idea bank v1
# import sys
# print "This is the name of the script: ", sys.argv[0]
# print "Number of arguments: ", len(sys.argv)
# print "The arguments are: " , str(sys.argv)



def write_to_file(typed_idea):          #zapisujemy idea
    file = open("ideas.txt","a") 
    file.write(typed_idea)
    file.write("\n")
    file.close()
    
def read_file():                        #czytamy plik
    file = open("ideas.txt", "r")
    x = 0
    for line in file:
        x = x + 1
        print(str(x)+"." , line)
    file.close()

def delete_idea(todelete):
    delme = int(todelete)
    listofideas = []
    file = open("ideas.txt", "r")
    for line in file:
        listofideas.append(line)
    del listofideas[delme - 1]
    file.close()
    file = open("ideas.txt", "w")
    for i in listofideas:
        file.write(i)
    file.close()
    
def main():
    import sys
    try:
        if str(sys.argv[1]) == "list":
            print("Idea list:" , "\n")
            read_file()
            exit
        if str(sys.argv[1]) == "delete":
            todelete = sys.argv[2]
            print("Deleting" , todelete)
            delete_idea(todelete)
            exit
    except:
        print("What is your new idea:")
        typed_idea = input()
        if typed_idea == "deleteall":              #funkcja do kasowania pliku
            file = open("ideas.txt", "w")
            file.close()
            print("File Deleted")
            exit
        else:
            write_to_file(typed_idea)
            read_file()

main()