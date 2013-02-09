GrabIPFromPcap
====================

Grab IP From Pcap

Requirements
Python: python-2.5.4.msi. python-2.6.3.msi. After installation, add the Python installation directory and its Scripts subdirectory to your PATH. Depending on your Python version, the defaults would be C:\Python25 and C:\Python25\Scripts or C:\Python26 and C:\Python26\Scripts respectively.
Scapy: latest development version from the Mercurial repository. Unzip the archive, open a command prompt in that directory and run “python setup.py install”.
pywin32: pywin32-214.win32-py2.5.exe pywin32-214.win32-py2.6.exe
WinPcap: WinPcap_4_1_1.exe. You might want to choose “[x] Automatically start the WinPcap driver at boot time”, so that non-privileged users can sniff, especially under Vista and Windows 7. If you want to use the ethernet vendor database to resolve MAC addresses or use the wireshark() command, download Wireshark which already includes WinPcap.
pypcap: pcap-1.1-scapy-20090720.win32-py25.exe pcap-1.1-scapy-20090720.win32-py2.6.exe. This is a special version for Scapy, as the original leads to some timing problems. Now works on Vista and Windows 7, too. Under Vista/Win7 please right-click on the installer and choose “Run as administrator”.
libdnet: dnet-1.12.win32-py2.5.exe dnet-1.12.win32-py2.6.exe. Under Vista/Win7 please right-click on the installer and choose “Run as administrator”
pyreadline: pyreadline-1.5-win32-setup.exe