Raspberry Pi Cooler
===================
Start a cooler when the Raspberry Pi gets too hot

Usage
=====
0. `pip install gpio`
1. Create the circuit according to the schematic below.
2. Attach it to GPIO #7 of the Raspberry Pi and to a ground pin.
3. Start the (very simple) `temperature.py` script with the `start` or `stop` arguments in order to start/stop the cooler
4. Ideally modify the `MAX_TEMP` variable in the script and add it to your crontab, eg. for automatically starting or stopping the fan for chunks of 5 minutes:
`*/5 * * * * /home/pi/localhost/temperature.py`

Schematic
=========
![Raspberry Pi Cooler](/schematic.png?raw=true "Raspberry Pi Cooler")

The pinout can be displayed by:

* `pip install gpiozero`
* `pinout`

Reference:
https://pinout.xyz/

Disclaimer
==========
I'm not an expert in electronics, so take my circuit as something a beginner may create.


LICENSE (MIT)
=============
Copyright (c) 2015 Barbu Paul - Gheorghe

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
