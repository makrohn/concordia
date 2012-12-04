import os
a=1
femaleform = ["femaledark","femalelight","femaleorc","femaletanned","femaletanned2"]
maleform = ["maledark","malelight","maleorc","maletanned","maletanned2"]
for y in os.listdir("../mods/concordia/images/avatar/hair/female"):
    y=str(y)
    y=y.split(".")
    for z in y:
        if z != "png":
            if z != "noalpha":
                for x in femaleform:
                    optionline = "".join(("option=",x,",",z,",","female",str(a)))
                    print optionline
                    a+=1
a=1
for y in os.listdir("../mods/concordia/images/avatar/hair/male"):
    y=str(y)
    y=y.split(".")
    for z in y:
        if z != "png":
            if z != "noalpha":
                for x in maleform:
                    optionline = "".join(("option=",x,",",z,",","male",str(a)))
                    print optionline
                    a+=1
