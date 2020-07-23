import pygetwindow as gw
import time

while True:
	VisionWindows = gw.getWindowsWithTitle('VisionLab')
	for VisionWindow in VisionWindows:
		if VisionWindow.width == 201 and VisionWindow.height == 166:

			VisionWindow.close()
	time.sleep(0.1)
