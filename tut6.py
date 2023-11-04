def search_file(file,search_String):
    with open(file,"r")as f:
        filecontents = f.read()
        if search_String in file_contents:
            print(f"found{search.String} in {file}")
        else:
            print(f"Did not find {search_String} in {file}")


def delete_line(file,str):
    with open(file,"r") as f:
        file_contents = f.readlines()
    with open(file,"w")as f:
        for line in file_contents:
            if line.strip("\n")!=lineTodelete:
                f.write(line)
        print("Deleted {str} from {file}")
while True:
    choice = input("Enter search,delete or exit : ")
    if choice == "search":
        search_String = input ("Enter the string to search for :")
        search_file("user>info.txt",seach_String)
    elif choice == "delete":
        str = inpit("Enter the line to delete:")
        delete_line("user_info.txt",str)
    elif choice == "exit":
        print("Invalid choice")
