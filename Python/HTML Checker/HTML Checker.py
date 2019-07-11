#  File: HTML Checker.py
#  Description: Checks to see if an HTML file has matched tags

class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

def getTag(file):

    char = file.read(1)
    if (char == ""):
        return ""   #if reaches end of file

    while (char != "<"):    #goes through characters until it finds a <
        char = file.read(1)
        if (char == ""):
            return ""   #if reaches end of file

    char = file.read(1) #reads character after the <
    if (char == ""):
        return ""   #if reaches end of file
    tag = ""
    while (char != ">" and char != " "):    #reads in characters of the tag and produces a string
        tag = tag + char
        char = file.read(1)
        if (char == ""):
            return ""   #if reaches end of file

    return tag

def createTagList():
    
    file = open("htmlfile.txt", "r")
    tagList = []
    
    tag = getTag(file)      #attempts to find the first tag
    while (tag != ""):      #if not at the end of the file
        tagList.append(tag)     #adds the tag to the list
        tag = getTag(file)      #attemps to find the next tag
        
    return tagList
     
def main():

    tagList = createTagList()   #creates the tag list
    print("List of Tags:", tagList,"\n")
    stack = Stack()
    VALIDTAGS = []
    EXCEPTIONS = ["br", "meta", "hr"]

    for tag in tagList:     #goes through the tags found
        if (tag in EXCEPTIONS and tag[0] != "/"):       #if the tag is an exception
            if (tag not in VALIDTAGS):      #if the tag has not been found yet, adds the tag to the valid tags list
                VALIDTAGS.append(tag)
                print("New tag", tag, "found and added to the list of tags")
            print("Tag", tag, "does not need to match:  stack is still", stack, "\n")
        elif (tag[0] != "/"):       #if it's a start tag
            if (tag not in VALIDTAGS):      #if the tag has not been found yet, adds the tag to the valid tags list
                VALIDTAGS.append(tag)
                print("New tag", tag, "found and added to the list of tags")
            stack.push(tag)     #pushes the tag onto the stack
            print("Tag", tag, "pushed:  stack is now", stack, "\n")
        elif (tag[1:] == stack.peek()):       #if end tag and also matches the previous tag
            stack.pop()     #pops the tag from the stack if matches
            print("Tag", tag, "matches top of stack:  stack is now", stack, "\n")
        else:           #if the tag doesn't match, gives error message and breaks out of loop
            print("Error:  tag is", tag, "but top of stack is", stack.peek(), "\n")
            break
            
    if (stack.isEmpty()):
        print("\nProcessing complete. No mismatches found.")        #if the stack is empty, it prints the empty stack
    else: print("\nProcessing complete. Unmatched tags remain on stack: ", stack)   #if the stack is not empty, it prints the tags not matched

    VALIDTAGS.sort()
    print("Valid tags found: ", VALIDTAGS)
    print("Exceptions: ", EXCEPTIONS)

main()
