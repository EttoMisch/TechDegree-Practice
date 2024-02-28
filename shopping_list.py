shopping_list = []
    
def show_help():
    print("What should we pick at the store?")
    print("""
ENTER 'DONE' to stop adding items.
ENTER 'HELP' for this help.
ENTER 'SHOW' to view the full list.
""")

def add_to_list(item):
    shopping_list.append(item)
    print("{} has been added to your list! Total items in your list are {}".format(item,len(shopping_list)))
        
        
def show_list():
    print("Here's your final list:")
    for item in shopping_list:
        print("> " + item)  

                
show_help()
while True:
    new_item = input(">  ")
    
    if new_item == "DONE":
        break
    elif new_item == "SHOW":
        show_list()
        continue
    elif new_item == "HELP":
        show_help()
        continue
        
        
    add_to_list(new_item)    
                  
show_list()

print("You have {} items in your list, enjoy your shopping!".format(len(shopping_list)))
