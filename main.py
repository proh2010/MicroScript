import os
import sys
def findword(text):
    string = ""
    p = 0
    a=text.find("(")
    while a != -1:

        c = a-1
        l = 0
        while c>0 and text[c-1].isalpha():
            l+=1
            c-=1
        commtext=text[c:a]
        f=1
        i=a+1
        while f!=0 and i<len(text):
            if text[i] == ")":
                f-=1
            elif text[i] == "(":
                f+=1
            i+=1

        if f==0:
            b=i
        else:
            sys.exit()


        #print(text, " ", string,c)
        if c==a-1:
            string += text[:a].replace(" ", "")
            string += f"({findword(text[a+1:b-1])})"

        else:
            string += text[:c].replace(" ", "")
            #print(text,p,c)
            string += findcom(commtext,findword(text[a+1:b-1]))

        text = text[b:]

        p=a+1
        a = text.find("(")

    string += text
    global spaces
    if (string.count("{") > 0):

        spaces += string.count("{")
        string = string.replace('{', '')
    if (string.count("}")>0):

        spaces -= 1 + string.count("}")
        global spacesp
        spacesp=spaces
        string=string.replace('}','')
        #b=commtext.find(" ")
        #while b != -1:
        #    commtext=commtext[:b]+commtext[b+1:]# remove spaces
        #    b = commtext.find(" ")
    return string

def findcom(comtext,argument):
    if comtext == "out":
        return f"print({argument})"
    elif comtext == "in":
        return f"input({argument})"
    elif comtext == "int":
        return f"int({argument})"
    elif comtext == "am":
        return f"len({argument})"
    elif comtext == "add":
        return f"append({argument})"
    elif comtext == "del":
        return f"pop({argument})"
    elif comtext == "abs":
        return f"abs({argument})"
    elif comtext == "imp":
        return f"import {argument}"
    elif comtext == "map":
        return f"map({argument})"
    elif comtext == "cut":
        return f"split({argument})"
    elif comtext == "array":
        if  argument.count("int") > 0 or argument.count("float") > 0:
            if argument.count(",") == 0:
                return f"[]"
            elif argument.count(",") == 1:
                a = 0
                while not(argument[a].isdigit()) and a<len(argument):
                    a+=1
                if argument[a].isdigit():
                    b=a
                    while b<len(argument) and argument[b].isdigit():
                        b+=1
                    return f"[0 for i in range({argument[a:b+1]})]"
                else:
                    sys.exit()
            else:
                sys.exit()
        elif argument.count("str") > 0 or argument.count("chr") > 0:
            if argument.count(",") == 0:
                return f"[]"
            elif argument.count(",") == 1:
                a = 0
                while not(argument[a].isdigit()) and a<len(argument):
                    a+=1
                if argument[a].isdigit():
                    b=a
                    while b<len(argument) and argument[b].isdigit():
                        b+=1
                    return f"['' for i in range({argument[a:b+1]})]"
                else:
                    sys.exit()
            else:
                sys.exit()
        else:
            sys.exit()
    elif comtext == "if":

        return f"if({argument}):"
    elif comtext == "else":

        return f"else:"
    elif comtext == "elif":

        return f"elif({argument}):"
    else:
        return f"print('no command: {comtext}')"
def compiler(way):
    to = open(way, "r") #open file
    text = to.read() #to str
    to.close()


    if not os.path.exists("compile"):
        os.mkdir("compile")
    compway = "compile/" + os.path.basename(way).split('/')[-1][:-2] + ".py"
    comp = open("compile/" + os.path.basename(way).split('/')[-1][:-2] + ".py", "w")# make a new file
    comp.write("#this is compiled file of " + way + "\n")

    global spaces
    spacesp=0
    spaces = 0
    strings = list(text.split("\n"))
    for i in range(len(strings)):
        finalstr =findword(strings[i])

        comp.write(" "*4*spacesp + finalstr + "\n")
        spacesp=spaces
    comp.write("input('Enter to exit.')")
    os.startfile(os.path.abspath(compway))


compiler("test.s")