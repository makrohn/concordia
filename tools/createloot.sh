#! /bin/bash
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
convert -rotate 70 -background none $1.png -crop 64x64 $1-1.png
convert -rotate 140 -background none $1.png -crop 64x64 $1-2.png
convert -rotate 210 -background none $1.png -crop 64x64 $1-3.png
convert -rotate 270 -background none $1.png $1-4.png
convert -page +0+16 -background none -flatten $1-4.png $1-4.png

convert +append $1.png $1-1-0.png $1-2-0.png $1-3-0.png $1-4.png $1.loot.png
rm $1-*.png
mv $1.loot.png ../mods/concordia/images/loot/$1.png
echo image=images/loot/$1.png > ../mods/concordia/animations/loot/$1.txt
cat item.txt >> ../mods/concordia/animations/loot/$1.txt
