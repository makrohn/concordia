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

print "This script assumes all tiles in your tileset block are the same height, will be centered horizontally, offset up by half a tile, and the tile block is left justified."
tile = int(raw_input("Starting tile number: "))
gridx = 32
gridy = 32
tilex = 32
tiley = int(raw_input("Height of a tile in this tileset block: "))
imagex = 960
y = int(raw_input("Top edge of the tile block: "))
imagey = int(raw_input("Bottom edge of the tile block: "))
tilesetname = raw_input("Tileset: ")
filepath = tilesetname
x=0
tileline=""
imagex = imagex - (imagex % gridx)
while y < imagey:
    while x < imagex:
        tileline = "".join(("tile=",str(tile),",",str(x),",",str(y),",",str(tilex),",",str(tiley),",",str(tilex-(gridx/2)),",",str(tiley-(gridy/2)),"\n"))
        with open(filepath, "a") as tileset:
            tileset.write(tileline)
        x += tilex
        tile +=1
    y += tiley
    x = 0
