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

from subprocess import call
import os
import sys
from shutil import copyfile
def createPackingCommand(imageName,folderName):
    splitname=str(imageName).split(".")
    for part in splitname:
        if part != "png":
            print "packing",part,"to",folderName
            call(["./lpcuss2flare.sh", part, folderName])
for files in os.listdir("./"):
    if ".png" in str(files):
        if len(sys.argv) > 1:
            createPackingCommand(files,str(sys.argv[1]))
        else:
            print "Needs an argument for nonassigned sprites!"
    elif "." not in str(files) and "bestEnclosingRect" not in str(files) and "flare" not in str(files):
        for subfiles in os.listdir(files):
            if ".png" in str(subfiles):
                copyfile(files + "/" + subfiles,subfiles)
                createPackingCommand(subfiles,files)
            elif "." not in str(subfiles):
                for subsubfiles in os.listdir(files + "/" + subfiles):
                    if ".png" in str(subsubfiles):
                        copyfile(files + "/" + subfiles + "/" + subsubfiles,subsubfiles)
                        createPackingCommand(subsubfiles,files + "/" + subfiles)
