# movie=[]
# movie.append(input("enter your first fav movies"))
# movie.append(input("enter your second fav movies"))
# movie.append(input("enter your third fav movies"))

# print(movie)


lit1=[2,2,2]
copy_lit1=lit1.copy()
lit1.reverse()
print(lit1)
if(lit1==copy_lit1):
    print("list is tuple")
else:
    print("list is not a tuple")