#! /bin/bash
# script to convert output from the LPC Universal Sprite Sheet to a Flare-engine appropriate format.
#Drop the png into the base folder of your FLARE-derived game and run this script from there via the terminal.
#Drop Stefan Beller's flare packing tool into a folder called "tools" https://github.com/stefanbeller/RectangleBinPack
#Syntax:
# ./lpcuss2flare.sh <image name> <base name>
convert $1.png -crop 832x256 +repage temp.png
convert temp-0.png -crop 448x64 sc.png
convert sc-2.png sc-2.png sc-2.png sc-0.png sc-6.png sc-6.png sc-6.png sc-4.png -append -page +0+0 -define png:color-type=6 spellcast.png
rm sc*
convert temp-2.png -crop 576x64 wc.png
cp wc-4.png ../mods/concordia/images/avatar/$2/preview/$1.png
convert wc-2.png wc-2.png wc-2.png wc-0.png wc-6.png wc-6.png wc-6.png wc-4.png -append -page +0+0 -define png:color-type=6 walkcycle.png
rm wc*
convert temp-3.png -crop 384x64 sl.png
convert sl-3.png sl-3.png sl-3.png sl-0.png sl-9.png sl-9.png sl-9.png sl-6.png -append -page +0+0 -define png:color-type=6 slash.png
rm sl-*
convert temp-4.png -crop 320x64 sh.png
convert sh-4.png sh-4.png sh-4.png sh-1.png sh-10.png sh-10.png sh-10.png sh-7.png -append -page +0+0 -define png:color-type=6 shoot.png
rm sh-*
convert temp-5.png -crop 384x64 die.png
convert die-0.png die-0.png die-0.png die-0.png die-0.png die-0.png die-0.png die-0.png -append -page +0+0 -define png:color-type=6 death.png
rm die-*
convert  -define png:color-type=6 walkcycle.png slash.png spellcast.png shoot.png death.png +append $1.png
rm temp-* death.png shoot.png slash.png spellcast.png walkcycle.png
convert $1.png -define png:color-type=6 $1.png
echo image=images/avatar/$2/$1.png > ../mods/concordia/animations/avatar/$2/$1.txt
cat hero.txt >> ../mods/concordia/animations/avatar/$2/$1.txt
mv $1.png ../mods/concordia/images/avatar/$2/$1.png
cd flare
./spritesheetpacker.py --images ../../mods/concordia/images/avatar/$2/$1.png --definitions ../../mods/concordia/animations/avatar/$2/$1.txt
