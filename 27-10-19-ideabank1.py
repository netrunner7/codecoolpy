# idea bank v1

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
    
def main():
    print("What is your new idea:")
    typed_idea = input()
    if typed_idea == "delete":              #funkcja do kasowania pliku
        file = open("ideas.txt", "w")
        file.close()
        print("File Deleted")
        exit
    else:
        write_to_file(typed_idea)
        read_file()

main()