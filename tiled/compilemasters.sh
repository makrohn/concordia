convert -append terrain/greenrow.png terrain/waterrow.png terrain/caverow.png terrain/shortobjects.png terrain/remainder.png masters/32.png
cp tallobjects/64objects.png masters/64.png
convert -append tallobjects/96objects.png walls/shortwalls.png masters/96.png
convert -append tallobjects/128objects.png walls/tallwalls.png masters/128.png
convert -append masters/32.png masters/64.png masters/96.png masters/128.png ../mods/concordia/images/tilesets/master.png
