l= r"C:\Users\pokem\OneDrive\Pictures\goals.png"
l= l.split("\\")
name=  l[-1]
l=l[:-1]
l= "\\".join(l)
print(l+"\\"+name[:-4]+"_blindfold.png")