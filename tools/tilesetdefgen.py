#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Copyright © 2012 Matthew Krohn
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

print "This script assumes all tiles in your tileset block are the same height, will be centered horizontally, offset up by half a tile, and the tile block is left justified."
tile = 16
tilesetname = raw_input("Tilesetdef: ")
tilesetimage = raw_input("Tileset image: ")
imagex = int(raw_input("Width of the tileset image: "))
gridsize = raw_input("Game Grid Tile Size (x*y): ")
gridsize = gridsize.split("*")
gridx = int(gridsize[0])
gridy = int(gridsize[1])
tilex = int(gridsize[0])
tiley = int(raw_input("Height of a tile in this tileset block: "))
y = 0
imagey = int(raw_input("Height of the tile block: "))
x = 0
imagex = imagex - (imagex % gridx)
done = False
with open(tilesetname, "w") as tileset:
	tileset.write("img=" + tilesetimage + "\n" + "\n")
	while done == False:
		while y < imagey:
		    while x < imagex:
		        tileset.write("tile=" + str(tile) + "," + str(x) + "," + str(y) + "," + str(tilex) + "," + str(tiley) + "," + str(tilex-(gridx/2)) + "," + str(tiley-(gridy/2)) + "\n")
		        x += tilex
		        tile +=1
		    y += tiley
		    x = 0
		tileset.write("\n")
		areyoudone = raw_input("Are there more tiles in this tileset? [y/n] ")
		if areyoudone == "y":
			done = False
			tiley = int(raw_input("Height of a tile in this tileset block: "))
			imagey = imagey + int(raw_input("Height of the tile block: "))
		if areyoudone == "n":
			done = True
