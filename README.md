# CSIT_TISC2021
## Level 1
### Challenge 1 : File1.wav
* Morse code hidden in the file. 
* Use Sonic Visualiser to open .wav file and the morse code appears.
* Flag : 

### Challenge 2 : File2.jpg
* Information Hidden in the metadata. 
* Tricky things is when it is downloaded, photo is modified. 
* Hence we will need to use online exif tool to extract metadata from image url.
* Flag : 

### Challenge 3 : File3.jpg
* Used exiftool online --> no metadata
* Used HxD to strings to see any text hidden within the file. 
* Notable Strings 2 x "picture_with_text.jpg"
* Looked into the Hex Editor for "picture_with_text.jpg" text string and saw something suspicious : "PK"
* Used binwalk to extract, xxd to look into the binaries of the unzipped file again and saw it... A suspicious looking message. 
* Cyberchef ROT 13 and FLAG:   

## Windows10.ova File
### Challenge 4 : What is the name of the user?
Windows Search --> System Information --> Flag: {TISC:Adam}

### Challenge 5 : Which time was the user's most recent logon? Convert it UTC before submitting.
--> EventViewer --> Filter Event 4624 --> Look out for Logon Type : 2

### Challenge 6 : A 7z archive was deleted, what is the value of the file CRC32 hash that is inside the 7z archive?
Download 7zip --> move into vm --> install 7zip in vm --> open archive Flag : 

### Challenge 7 : Question1: How many users have an RID of 1000 or above on the machine? What is the account name for RID of 501? What is the account name for RID of 503?
go to cmd --> wmic useraccounts get sid,name Flag 

### Challenge 8 : Question1: How many times did the user visit https://www.csit.gov.sg/about-csit/who-we-are ? How many times did the user visit https://www.facebook.com ? How many times did the user visit https://www.live.com ?
Use Nirsoft BrowsingHistoryView 

### Challenge 9 : A device with the drive letter “Z” was connected as a shared folder in VirtualBox. What was the label of the volume? Perhaps the registry can tell us the "connected" drive?
https://docs.microsoft.com/en-us/troubleshoot/windows-server/networking/mapped-network-drive-disconnected

### Challenge 10 : A file with SHA1 0D97DBDBA2D35C37F434538E4DFAA06FCCC18A13 is in the VM… somewhere. What is the name of the file that is of interest?

## Level 2
### We have detected and captured a stream of anomalous DNS network traffic sent out from one of the PALINDROME compromised servers. None of the domain names found are active. Either PALINDROME had shut them down or there's more to it than it seems. This level contains 2 flags and both flags can be found independently from the same pcap file as attached here.
Open pcap --> saw a pattern d33d(2 digit)(7char)
split 2 digit and 7 char
### DEE-NA-SAW as a need Part 2
take the python script output and throw into cyberchef
* DEE-NA-SAW part 2 has a peculiar string ***"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz+/"***
### DEE-NA-SEE as a need Part 1
* string saw above is the decoder for Part 1.
* wrote a python script to do a substitution for above string with the 2 digit numbers in part 1 (attached in this repo)
* found out that the substituted cipher is a base64 encoded data and base64 is in the form of the above ***string***
* throw into cyberchef to decode base64 with custom string
* saw PK file extension
* extract as zip file ---> "What you Seek is within"
* Flag : 





