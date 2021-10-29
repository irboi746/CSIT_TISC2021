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
