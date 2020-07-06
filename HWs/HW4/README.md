# GnuPlot Installation Guide
GnuPlot is a command-line driven graphing utility with cross-platform support.
# Windows
  * Download the latest version of the installer from gnuplot site.
  * Run the downloaded file and allow it to run as administrator if requested 
  * On the setup window select the language and follow the instructions on screen.
  * During the installation you may select the gnuplot to be added to the PATH that will allow you to run commands from anywhere on the command line. If you choose not to do so you may add it manually later or cd to the gnuplot installed directory prior to running commands.

The default installation location of gnuplot on Windows is C:\Program Files (x86)\gnuplot

---
# Linux
The installation on Linux can be done through the different package managers as follows.

  * Arch

$ sudo pacman -S gnuplot

  * Debian and Ubuntu

$ sudo apt-get update
$ sudo apt-get install gnuplot

  * CentOS / RedHat

$ sudo yum check-update
$ sudo yum install gnuplot

  * Fedora

$ sudo dnf check-update
$ sudo dns install gnuplot
