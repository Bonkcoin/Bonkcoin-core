
Debian
====================
This directory contains files used to package boncoind/boncoin-qt
for Debian-based Linux systems. If you compile boncoind/boncoin-qt yourself, there are some useful files here.

## boncoin: URI support ##


boncoin-qt.desktop  (Gnome / Open Desktop)
To install:

	sudo desktop-file-install boncoin-qt.desktop
	sudo update-desktop-database

If you build yourself, you will either need to modify the paths in
the .desktop file or copy or symlink your boncoin-qt binary to `/usr/bin`
and the `../../share/pixmaps/boncoin128.png` to `/usr/share/pixmaps`

boncoin-qt.protocol (KDE)

