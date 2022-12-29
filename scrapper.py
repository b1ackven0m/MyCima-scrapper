from bs4 import BeautifulSoup
import requests 
from os import system
from sys import argv 
if len(argv) != 4:
	print("Usage : {0} quality chat_id link".format(argv[0]))
else:
	base = argv[3]
	tid = argv[2]
	qual = argv[1]

	page = requests.get(base).text

	soup = BeautifulSoup(page,"html.parser")

	for a in soup.find_all("a",href=True):
		movie = a["href"]
		if "watch" in movie:
			print("found a movie  : ",movie)
			dbase = requests.get(movie).text
			dsoup = BeautifulSoup(dbase,"html.parser")
			for quilaty in dsoup.find_all("a",href=True):
				hd = quilaty["href"]
				if qual  in hd and not "/quality" in hd:
					linkList = hd.split("/")[4].split(".")
					linkList.remove(linkList[len(linkList) -1])
					linkList.insert(len(linkList) -1, ".")
					filenamae = "".join(linkList)
					print(filenamae)
					system("cd Downloads && wget '" + hd + "' -o {0}".format(filenamae))
					system("telegram-upload Downloads/* --to  " + tid)
					system("rm -rf Downloads/*")
