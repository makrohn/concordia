#! /bin/bash
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
