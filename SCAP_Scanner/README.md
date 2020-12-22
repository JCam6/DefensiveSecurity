# SCAP Security and Compliance Scanning <img title="Open-Source" alt="Open-Source" width="40px" src="https://raw.githubusercontent.com/github/explore/master/collections/tools-for-open-source/tools-for-open-source.png"/>

**Open-Source Content**

Security profiles available here are generated from OpenSCAP without warranty.

More information available publicly at: https://www.open-scap.org/tools/

**Usage Example with SCAP Workbench**

Step 1) Download SCAP workbench from the package manager within your distribution of Linux.

```bash
Debian:~$ apt-get install scap-workbench
Red_Hat:~$ yum install scap-workbench
Fedora:~$ dnf install scap-workbench
```
Step 2) Download the SCAP Security Guides according to the OS.

```bash
apt install ssg-debian
apt install ssg-debderived
apt install ssg-nondebian
```

```bash
wget <filelinkfromthisrepo>
```
Step 3) Start SCAP Workbench and load content for the OS that will be scanned. :point_down:

```bash
scap-workbench /path/to/file/downloaded/above
```

Step 4) Choose the profile to scan (i.e. level or security benchmark) and select scan. Authenticate if required. :point_down:

<img src="scap2.PNG" alt="scan" class="inline"/>

Step 5) Close the diagnostic window and select show report. Review the compliance score and suggested steps for remediation. :point_down:

<img src="scap3.PNG" alt="review" class="inline"/>
