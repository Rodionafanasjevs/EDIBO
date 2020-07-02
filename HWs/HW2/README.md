Hometask. Linux for windows.
# Install the Windows Subsystem for Linux

Before installing any Linux distributions on Windows, you must enable the "Windows Subsystem for Linux" optional feature.
To only install WSL 1, you should now restart your machine and move on to Install your Linux distribution of choice, otherwise wait to restart and move on to update to WSL 2.

---
# Update to WSL 2
To update to WSL 2, you must meet the following criteria:
  * Running Windows 10, updated to version 2004, Build 19041 or higher.
  * Check your Windows version by selecting the Windows logo key + R, type winver, select OK. (Or enter the ver command in Windows Command Prompt). Please update to the latest Windows version if your build is lower than 19041.
Enable the 'Virtual Machine Platform' optional component
Before installing WSL 2, you must enable the "Virtual Machine Platform" optional feature.
Restart your machine to complete the WSL install and update to WSL 2.

---
# Install your Linux distribution of choice
  * Open the Microsoft Store and select your favorite Linux distribution.
![alt text](https://docs.microsoft.com/en-us/windows/wsl/media/store.png)
  * From the distribution's page, select "Get".
![alt text](https://docs.microsoft.com/en-us/windows/wsl/media/ubuntustore.png)
---
# Set up a new distribution
The first time you launch a newly installed Linux distribution, a console window will open and you'll be asked to wait for a minute or two for files to de-compress and be stored on your PC. All future launches should take less than a second. You will then need to create a user account and password for your new Linux distribution.
![alt text]https://docs.microsoft.com/en-us/windows/wsl/media/ubuntuinstall.png
---
# Set your distribution version to WSL 1 or WSL 2
You can check the WSL version assigned to each of the Linux distributions you have installed by opening the PowerShell command line and entering the command (only available in Windows Build 19041 or higher): wsl -l -v
PowerShell
  * wsl --list --verbose
To set a distribution to be backed by either version of WSL please run:
PowerShell
  * wsl --set-version <distribution name> <versionNumber>
Make sure to replace <distribution name> with the actual name of your distribution and <versionNumber> with the number '1' or '2'. You can change back to WSL 1 at anytime by running the same command as above but replacing the '2' with a '1'.
Additionally, if you want to make WSL 2 your default architecture you can do so with this command:
PowerShell
  * wsl --set-default-version 2
This will set the version of any new distribution installed to WSL 2.

[main site](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
