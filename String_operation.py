

from fstring import language

s1="python is fun"
print(s1[0])
print(s1[-1])
print(len(s1))


language="python"
version="3,13"
print(language+version)

#in string * stands for repetation
print(language*3)

'''
#membership operation
#in
print("python" in language)
print("python" in version)
print("3" in version)
print("p" in version)

 #not in
print("p" not in version)
'''
#comparison of strings
#==
print("python" == "python")
print("python " == "python")
s2 = "python    "

#.strip remove space from string
print(s2.strip()=="python")

#replace
print(s2.replace("python","java"))