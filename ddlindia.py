from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.proxy import *
import time
import os
def download_tifs(dndir):
	#myProxy = "10.93.0.37:3333"
	myProxy=""
	proxy = Proxy({
    	'proxyType': 'MANUAL',
    	'httpProxy': myProxy,
    	'ftpProxy': myProxy,
    	'sslProxy': myProxy,
    	'noProxy': '' # set this value as desired
    	})

	fp = webdriver.FirefoxProfile()
	fp.set_preference("browser.download.folderList",2)
	fp.set_preference("browser.download.manager.showWhenStarting",False)
	fp.set_preference("browser.download.dir", dndir)
	fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.ms-excel")
	wd = webdriver.Firefox(firefox_profile=fp)
	start =1
	for i in xrange(start,766):
		#files_in_folder=len(os.listdir(dndir))
		url = 'http://www.new.dli.ernet.in/scripts/FullindexDefault.htm?path1=/rawdataupload/upload/0101/869&first='+str(i)+'&last=755&barcode=5990010101867'
		print 'Getting ', url
		wd.get(url)
		# Wait for the dynamically loaded elements to show up
		WebDriverWait(wd, 20)
		u=1
		filename = 00000055
		if i<10:
			pre = '0000000'
		elif i<100:
			pre = '000000'
		elif i<1000:
			pre = '00000'
		filename = pre+str(i)+'.tif'
		while(filename not in os.listdir(dndir)):
			u=u+1
			time.sleep(1)
		print filename,'File downloaded'

def main():
	dndir = os.getcwd()+'/hari'
	print dndir
	download_tifs(dndir)

main()
