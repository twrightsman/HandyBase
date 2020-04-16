# HandyBase

I created this repository in the spirit of [DefaultApp](https://tyler.io/default-app-for-mac-ios/) to provide a foundation for apps that I want to develop for the [Librem 5](https://puri.sm/products/librem-5/) without having to start from scratch.
I wanted it to have more boilerplate and be more modular than the [First Application](https://source.puri.sm/Librem5/example-apps/first-application) example app.
The app also includes things that were difficult for me (as a new GTK and PyGObject developer) to initially find and figure out such as the Gtk.Template decorator, custom stylesheets, app icons, GResource files, among others.
Finally, you can use this repo directly in GNOME Builder or follow the command line steps to build and test your Flatpak below.

**Note:** This pulls the current master branch of libhandy at build time, which may not be stable!

## Prepare for new app

Uses `rename.ul` from the `util-linux` package.

Here's how to prep the boilerplate for a new app, `com.example.CoolApp`.

```
find HandyBase -depth -name "io.github.twrightsman.HandyBase*" -exec bash -c 'rename.ul io.github.twrightsman.HandyBase com.example.CoolApp "$1"' _ {} \;
find HandyBase -depth -name "*handybase*" -exec bash -c 'rename.ul handybase coolapp "$1"' _ {} \;
grep -Rli handybase HandyBase | xargs sed -i'' 's/io\.github\.twrightsman\.HandyBase/com.example.CoolApp/g; s/io\/github\/twrightsman\/HandyBase/com\/example\/CoolApp/g; s/HandyBase/CoolApp/g; s/handybase/coolapp/g;'
```

## Install System Dependencies (Ubuntu 19.10)

```
sudo apt install flatpak qemu-system-x86
```

## Build the Flatpak bundle

All of these steps were taken from the excellent [Librem 5 Developer Documentation](https://developer.puri.sm/Librem5/index.html).

```
flatpak-builder --repo=handybase _flatpak HandyBase/io.github.twrightsman.HandyBase.json
flatpak build-bundle handybase handybase.flatpak io.github.twrightsman.HandyBase
```

## Test the Flatpak
`flatpak-builder --run _flatpak HandyBase/io.github.twrightsman.HandyBase.json handybase`

## Download Librem 5 x86\_64 image

Download the latest successful (green dot) x86\_64 build [here](https://arm01.puri.sm/job/Images/job/Image%20Build).

I use `current qemu-x86_64 buster+ci image`.

## Run x86-64 Librem 5 Image

`sudo qemu-system-x86_64 -boot menu=on -drive file=qemu-x86_64.qcow2,format=qcow2 -vga virtio -display gtk -m 2G -enable-kvm -device e1000,netdev=net0 -netdev user,id=net0,hostfwd=tcp::5555-:22`

## Copy the bundle onto the Librem 5

The password is `123456`.

`scp -P 5555 handybase.flatpak purism@localhost:~/Downloads`

## On the Librem 5 Terminal

Unlock the phone with the passcode `123456` and tap the Terminal app icon.
Use the same password for all admin authentication requests.

```
sudo resize2fs /dev/sda2
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install ~/Downloads/handybase.flatpak
```

The app should now be listed in the application tray, shown by tapping/clicking the up arrow at the bottom of the phone screen.

