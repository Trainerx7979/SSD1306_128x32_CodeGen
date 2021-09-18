# SSD1306_128x32_CodeGen
Very simple, works but barely, Gui for python to generate screen code for SSD1306 and similar OLED displays.
This is just a basic GUI written in python and PyGame so I could click and turn on/off individual pixels of a monochrome Oled display.
I'm currently using the SSD1306 with micropython on an ESP32, but this should work just fine with minor if any modification for and other
Micropython or CircuitPython, Arduino, MBed, Processing, STMCube, Platform.io, etc etc.  Its simple on purpose. Even if its a bit slow.
128x32 display has 4096 pixels. This assigns them to a numpy array in the data(Y, X) format. Returning data with  a = data(Y, X) would give
you a 0 or a 1. 1 is on. 0 is off... I didn't add proper parsing for the saved text file (which is saved by pressing PAGE_DOWN key.)
So at the end of the file, at the very least, you'll have to remove the ','
Other than that, You may want to store it differently. There are a lot of better options than as a single variable but, alas, I didn't have as
much time to work on this as I'd hoped.  I know there are better tools out there. But hey, This one was just a personal weekend challenge. 

Feel free to use it or abuse it. I went with CC0, so its completely yours to use however. Even commercially.  I could have gone a different route
and used visual studio, or java, and made a much more coherent working tool. But, I was feeling especially weak on my Python skills after messing around
for two hours trying to get the ESP32 to just turn the screen on... So I figured I would work on my weaker areas...
The Gen_Code.txt is just a sample output to show what the result will look like. 


So yea, Play safe. Try to make something you've never done before, and dont eat the code. It causes indigestion.
