def printList(List):
    """
    This function will go through the list and print index and value
    """
    for i, s in enumerate(List):
        print("Album", i, "Rating is ",s)
list = [4, 3, 2]
printList(list)
#help(printList()) will print the Document String
