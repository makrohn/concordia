#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Copyright 2012 Matthew Krohn
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
