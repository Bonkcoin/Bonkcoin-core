# Boncoin Snap Packaging

Commands for building and uploading a Boncoin Core Snap to the Snap Store. Anyone on amd64 (x86_64), arm64 (aarch64), or i386 (i686) should be able to build it themselves with these instructions. This would pull the official Boncoin binaries from the releases page, verify them, and install them on a user's machine.

## Building Locally
```
sudo apt install snapd
sudo snap install --classic snapcraft
sudo snapcraft
```

### Installing Locally
```
snap install \*.snap --devmode
```

### To Upload to the Snap Store
```
snapcraft login
snapcraft register boncoin-core
snapcraft upload \*.snap
sudo snap install boncoin-core
```

### Usage
```
boncoin-unofficial.cli # for boncoin-cli
boncoin-unofficial.d # for boncoind
boncoin-unofficial.qt # for boncoin-qt
boncoin-unofficial.test # for test_boncoin
boncoin-unofficial.tx # for boncoin-tx
```

### Uninstalling
```
sudo snap remove boncoin-unofficial
```