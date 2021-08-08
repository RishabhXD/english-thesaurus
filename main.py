import json
from difflib import get_close_matches
data = json.load(open("data.json"))

#main function
def translate(w):
    w = w.lower()                       #for case sensitivity

    if w in data:
        return(data[w])
    elif len(get_close_matches(w,data.keys())) >0:
        yn = input("Did you mean %s instead? Y(Yes) or N(No) : " % get_close_matches(w,data.keys())[0])
        yn = yn.lower()
        if yn == "y":
            return (data[get_close_matches(w,data.keys())[0]])
        elif yn == "n":
            return("Word Doesn't Exist,Please Double Check")
        else:
            return("We Are Unable To Get You Input")
    else:
        return("Word Doesn't Exist,Please Double Check")



word = input("Enter Word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)
