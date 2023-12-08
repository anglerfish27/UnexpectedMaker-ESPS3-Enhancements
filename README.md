# UnexpectedMaker-ESPS3-Enhancements Helper File!
First off all rights, permissions ect... go to Seon Rozenblum from Unexpected Maker. I have NO AFFLIATION or partnership with his buisness. I'm just a private individual adding on to his code.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Chunks of this code is from his own code so I do not own the entire code base. This code was made INDEPENDANT from Unexpected Maker/Seon - meaning this code is **no way related to him, his buisness, or products.** This is my creation and its written for his hardware because I am a big fan of his products, this is in no way sponsored or sanctioned by him. So if this code sucks and it blows up in your face you CANNOT blame him or his buisness. I'm just a beginner MP coder who loves his microprocessors. The ntptime.py belongs to the Micropython organisation and is not mine, I just made a tiny modifcation for UTC offset. Heck I wouldn't be surprised if MP has already incorporated UTC offset on their own. Either way the code belongs to them.

So long story short if it belongs to them, you gotta follow their rules for acceptible use. If you are using code that is mine you are free to edit/share/do whatever you want with it. That's a lot of CYA huh? Ok moving on..


Work in progress - creating a nice Helper.py file as a Class that contains some of the methods used by UM as well as others for other common tasks to consolidate them into one place. I'm a newbie so if the looks horrible you know why!

This Helper.py (eventually) is geared to consolidating common tasks performed on the ESP32 S3 chips (Mainly using Unexpected Maker TinyS3,ProS3,FeatherS3). Some of the code would simply not work on other ESP32 boards because they are specific to the HW design of Unexpected Makers's ESP32S3 boards.

However you can pick it apart and adjust for your own hardware as needed. Right now (11/23) it is VERY ROUGH. Alpha stage at best!

This does make use of the edited ntptime.py file from the official Micropython build in terms of UTC offset. In fact the version on github would need to be edited now that we went through DST change. So the offset for say the U.S. Eastcoast would be ```UTC_OFFSET = -18000 ```.

The goal is that if you have a Feather S3, ProS3, or TinyS3 you can perform a varetity of actions that your program may need at some point. 

Things in the works such as (not everything has been implemented or optimized!!:

-Connect to Wi-Fi

-Validate outside network connectivity (Wi-Fi Check)

-Display IP info

-Onboard RGB LED - Turn it on, off, enable different colors which can be used to indicate status of your code or whatever..

-Setting RTC via NTP

-Powersave features - such as lower CPU freq

-Reconnect to Wi-Fi if you get disconnected

-USB Connected? True/False

-JST Battery voltage (if you a battery plugged in)

-Alerts on voltage levels (adjustible) but Likely set to about 3.1V as a default.

-Display version info for things such as MP version, bootloader version, mac-address info ect..

-Whatever else I think of or you suggest!

I will be working on this on and off, not that anyone is probably reading this anyways. I'm a newbie and if for some reason you are reading this and have comments on my code and how to optimize it and why something is poorly coded please share the feedback! For example I'm going to create a toggle method for the LED instead of the current way but I wanted a core at least somewhat functional.


Copyright 2019 Unexpected Maker

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
