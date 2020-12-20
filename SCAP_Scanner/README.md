# SCAP Security and Compliance Scanning <img title="Open-Source" alt="Open-Source" width="40px" src="https://raw.githubusercontent.com/github/explore/master/collections/tools-for-open-source/tools-for-open-source.png"/>

**Open-Source Content**

Security profiles available here are generated from OpenSCAP without warranty.

More information available publicly at: https://www.open-scap.org/tools/

**Usage Example with SCAP Workbench**

Download SCAP workbench from the package manager within your distribution of Linux.

```bash
Debian:~$ apt-get install scap-workbench
Red_Hat:~$ yum install scap-workbench
Fedora:~$ dnf install scap-workbench
```
Download the SCAP Security Guides.

```bash
apt-get install scap-security-guide
wget <filelinkfromthisrepo>
sudo cp <filefromthisrepo> /usr/share/xml/scap/ssg/content/
```
Start SCAP Workbench.

Load content for the OS that will be scanned.

Choose the profile to scan (i.e. level or security benchmark).

Select Scan.

View fail/pass results and suggested steps for remediation. 
