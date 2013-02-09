GrabIPFromPcap
====================

Grab IP From Pcap
---
This is a simple script that i've used quite often at work to extract out IPs from Pcap(s). 
I do hope that this will prove somewhat useful to some of you if not all of you.

Requirements
---
  - Python:
    - [python-2.5.4.msi](http://www.python.org/ftp/python/2.5.4/python-2.5.4.msi)
    - [python-2.6.3.msi](http://www.python.org/ftp/python/2.6.3/python-2.6.3.msi)
  After installation, add the Python installation directory and its Scripts subdirectory to your PATH. 
  Depending on your Python version, the defaults would be C:\Python25 and C:\Python25\Scripts or C:\Python26 and C:\Python26\Scripts respectively.

  - Scapy:
    - [latest development version](http://hg.secdev.org/scapy/archive/tip.zip) from the [Mercurial repository](http://hg.secdev.org/scapy).
  Unzip the archive, open a command prompt in that directory and run "python setup.py install"

  - pywin32: 
    - [pywin32-214.win32-py2.5.exe](http://surfnet.dl.sourceforge.net/sourceforge/pywin32/pywin32-214.win32-py2.5.exe) [pywin32-214.win32-py2.6.exe](http://downloads.sourceforge.net/project/pywin32/pywin32/Build%20214/pywin32-214.win32-py2.6.exe)

  - WinPcap: 
    - [WinPcap_4_1_1.exe.](http://www.winpcap.org/install/bin/WinPcap_4_1_1.exe)
  You might want to choose "[x] Automatically start the WinPcap driver at boot time", so that non-privileged users can sniff, especially under Vista and Windows 7.
  If you want to use the ethernet vendor database to resolve MAC addresses or use the wireshark() command, download Wireshark which already includes WinPcap.

  - pypcap: 
    - [pcap-1.1-scapy-20090720.win32-py25.exe](http://www.secdev.org/projects/scapy/files/pcap-1.1-scapy-20090720.win32-py2.5.exe) [pcap-1.1-scapy-20090720.win32-py2.6.exe](http://www.secdev.org/projects/scapy/files/pcap-1.1-scapy-20090720.win32-py2.6.exe).
  This is a special version for Scapy, as the original leads to some timing problems. 
  Now works on Vista and Windows 7, too. Under Vista/Win7 please right-click on the installer and choose "Run as administrator".

  - libdnet: [dnet-1.12.win32-py2.5.exe](http://libdnet.googlecode.com/files/dnet-1.12.win32-py2.5.exe) [dnet-1.12.win32-py2.6.exe](http://www.secdev.org/projects/scapy/files/dnet-1.12.win32-py2.6.exe).
Under Vista/Win7 please right-click on the installer and choose "Run as administrator"

  - pyreadline: 
    - [pyreadline-1.5-win32-setup.exe](http://ipython.scipy.org/dist/pyreadline-1.5-win32-setup.exe)
