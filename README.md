## Change 2/21/2013

Concordia now installs the Flare executables using the source code from https://github.com/clintbellanger/flare-engine.  If you're upgrading from a prior version of Concordia, be aware that your settings will now be located in ~/.config/flare/settings.txt (or similar) and saves in ~/.local/share/saves/conc01_save*.txt (or similar).  If you have any trouble running Concordia, make sure that "concordia" is your only active mod.

## Valley of Concordia

Valley of Concordia is a a role-playing game based off of the Flare engine.  The goal is to produce an 8-bit length game within the adventure RPG genre.  Over the course of development, I hope to push the ability of FLARE to develop a storyline, even within a simple narrative structure.  I also hope it's fun!

## Copyright and License

Most of Flare is Copyright © 2011-2012 Clint Bellanger. Contributors retain copyrights to their original contributions.

All of Flare's source code is released under the GNU GPL version 3. Later versions are permitted.

Most of Valley of Concordia's art and data files are released under CC-BY-SA 3.0. Later versions are permitted.  See the AUTHORS file for more information regarding individual assets.

The Liberation Sans fonts version 2 are released under the SIL Open Font License, Version 1.1.

The GNU Unifont font is released under GPL v2, with the exception that embedding the font in a document does not in itself bind that document to the terms of the GPL.

## Links

* Source    https://github.com/makrohn/concordia
* Email     makrohn@gmail.com

## Installation

See the Flare-Engine repo for instructions on how to install Flare:

https://github.com/clintbellanger/flare-engine

Valley of Concordia is installed as a set of mods for Flare Engine. Place the contents of the "mods" folder inside Flare Engine's mods folder.

* On Windows, the mods folder will be in the same directory as the flare executable.
* On OSX, this will be inside the Flare.app folder, in Resources/mods 
* On Linux, the default location of the mods folder is /usr/local/share/flare/mods/

Then enable these mods in Flare's Configuration screen.

    concordia

## Packaging and Distributing

If you are packaging Valley of Concordia for release (e.g. on an operating system's software repo), we suggest creating two packages.

* flare-engine the package that contains the single engine reused by several games
* concordia, a package that requires flare-engine that only contains this game data

When distributing flare-game you may elect to omit these folders which are not used at runtime.

* art_src contains the raw files (e.g. Blender files) used to generate Flare's art.
* tiled contains the Tiled-native map files used to export Flare's maps
* planning contains public spoilers about where game development is headed
* tools contains some scripts that other developers may find convenient to copy or modify

## Savefile Change!

On 2/21/2013, the savefile mechanic was changed.  If you want to use your old savefiles from before the change, copy them from your Concordia save directory to your Flare save directory, and rename them from save#.txt to conc01_save#.txt
