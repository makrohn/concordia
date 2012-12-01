#Copyright © 2011-2012 Matthew Krohn
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

from subprocess import call
import os
for x in os.listdir("./"):
    if ".png" in str(x):
        y=str(x)
        y=y.split(".")
        for z in y:
            if z != "png":
		print "packing",z
                call(["./lpcuss2flare.sh", z, "male"])
