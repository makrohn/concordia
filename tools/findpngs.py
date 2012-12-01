from subprocess import call
import os
for x in os.listdir("./"):
    if ".png" in str(x):
        y=str(x)
        y=y.split(".")
        for z in y:
            if z != "png":
		print "packing",z
                call(["./lpcuss2flare.sh", z, "female"])
