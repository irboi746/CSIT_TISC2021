# CSIT_TISC2021
## Level 1
### File1.wav
* Morse code hidden in the file. 
* Use Sonic Visualiser to open .wav file and the morse code appears.
* Flag : 

### File2.jpg
* Information Hidden in the metadata. 
* Tricky things is when it is downloaded, photo is modified. 
* Hence we will need to use online exif tool to extract metadata from image url.
* Flag : 

### File3.jpg
* Used exiftool online --> no metadata
* Used HxD to strings to see any text hidden within the file. 
* Notable Strings 2 x "picture_with_text.jpg"
* Looked into the Hex Editor for "picture_with_text.jpg" text string and saw something suspicious : "PK"
* Used binwalk to extract, xxd to look into the binaries of the unzipped file again and saw it... A suspicious looking message. 
* Cyberchef ROT 13 and FLAG:   

### Windows10.ova File
#### 
1. Name of the User : Windows Search --> System Information --> Flag: {TISC:Adam}
2. LastLogonTime : --> EventViewer --> Filter Event 4624 --> Look out for Logon Type : 2
3. Download 7zip --> move into vm --> install 7zip in vm --> open archive Flag : 
4. go to cmd --> wmic useraccounts get sid,name Flag : 
5. Use Nirsoft BrowsingHistoryView --> 2-0-0
6. https://docs.microsoft.com/en-us/troubleshoot/windows-server/networking/mapped-network-drive-disconnected
