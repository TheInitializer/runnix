# runnix
![Run window](https://github.com/TheInitializer/runnix/blob/screenshots/Run_003.png)
![Eventvwr window](https://github.com/TheInitializer/runnix/blob/screenshots/Event Viewer_004.png)

runnix is a program I wrote that mimics the Run box on Windows, but is meant to be run on Linux. It's for those tech support scams that involve opening up event viewer and telling people that the logs are "wiruses", etc.

Want to install it on a VM and troll some scammers? Read the instructions below!

Instructions
------------
#### :computer: Set up environment
Get a Linux distro with the Cinnamon or XFCE desktop environment such as Linux Mint ([linuxmint.com](https://www.linuxmint.com/)). Those DEs can be customized to look very much like Windows.

After you download and set up your distribution, get the Windows 10 theme from [github.com/Elbullazul/Windows-10/](https://github.com/Elbullazul/Windows-10/). Then go into Settings > Themes and change the theme to Windows 10.

There are many other customizations you can do to make your system look more like Windows, but you can figure that out. Try customizing the panel and applets.

#### :arrow_down: Get runnix
First off make sure you have PyQt5 installed, open up a terminal and type in:

    sudo apt-get install python-pyqt5

Next, it's time to download runnix! Click the "Download Zip" button at the top of this page, or type into terminal:

    git clone https://github.com/TheInitializer/runnix.git
  
Wherever you ran that from, there should be a new folder called "runnix". It's probably in your home folder. Take note of where that folder is, then go into Settings > Keyboard. Click "Custom Shortcuts", then press the + button. A dialog will pop up, under "Name" write `runnix` and under "Command" write `python <path to runnix>/runnix.py` where `<path to runnix>` is wherever the runnix folder is. Usually this will be `/home/YourUsername/runnix`, so in that case write `python /home/username/runnix/runnix.py`.

Press Add, then an entry should come up at the top of the screen. Click the text that says `Disabled`, then press the Windows key followed by the letter R, R as in Rundi. The shortcut `Windows`+`R` should now be bound to runnix. Close the Keyboard Settings window, then press `Windows`+`R` again to test it. A Run box should pop up...

Have fun!

Contributing
------------
I'd appreciate suggestions or bug reports. If you have any, click the Issues tab at the top of this page and open a new issue. I'll be happy to help.

If you know Python and PyQt, then feel free to PR.
