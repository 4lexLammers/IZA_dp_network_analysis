# This script downloads discussion papers (dp) from 
# the IZA-Institute of Labor Economics (ftp.iza site)
# From: 1998 (dp1)
# To: 08-2017 (10961)
# Files are saved within the folder in which this file is stored
# Version: v1.0
# by Alexander Lammers

from urllib.request import urlopen
import time

# Paper to download uo to this ceiling
endnumber = 11153

# Seconds to wait between every download
seconds = 1

# Initial value for number of papers not downloaded
notfind = 0

for paper in range(10961,endnumber):
	try:
		print (paper)
		response = urlopen("http://ftp.iza.org/dp%d.pdf"%(paper,))
		file = open("dp%d.pdf"%(paper,), 'wb')
		file.write(response.read())
		file.close()
		print("Completed")
		#time.sleep(seconds)
	except:
		print("Could not find dp%d.pdf"%(paper,))
		print("Moving to next file")
		notfind += 1
		#time.sleep(seconds)
		pass
print ("There are %d papers not found" %notfind)
input()