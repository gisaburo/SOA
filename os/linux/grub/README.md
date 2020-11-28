# grubを使ったシステムの起動
## grub2 source download 
Download stable release linux kernel source from [gnu.org](https://ftp.gnu.org/gnu/grub/)
```
wget <url>
```
## grub2 source compile
Extract tar.xz and move to directory
```
tar -Jxvf <filename.tar.xz>
```
config
```
./configure
```
make
```
make -j<cpucore>
make install
```
## xorriso install
```
sudo dnf install -y xorriso
```
## boot on qemu
```
qemu-system-x86_64 \
-boot order=d \
-cdrom /tmp/grub-img.iso \
-kernel bzImage \
-initrd rootfs.img \
-append "root=/dev/ram rdinit=/bin/sh"
```