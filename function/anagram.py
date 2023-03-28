
def anagaram( a1,a2):
    if sorted(a1) == sorted(a2):
        print("Given String is a anagram")
    else:
        print("Gievn String is not an anagram")

a1 = input("Please Enter the First string here : ")
a2 = input("Please Enter the Second String here : ")

anagaram(a1,a2)