#!/usr/bin/python

###########################################################################
#
# name          : nakamigos.py
#
# purpose       : get images    
#
# usage         : python nakamigos.py
#
# description   :
#
###########################################################################

import json
import os
import requests
import shutil

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

images = "images"
url = "https://img.x2y2.io/v2/1/0xd774557b647330c91bf44cfeab205095f7e6c367/%u/1440/image.jpg"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

if __name__ == "__main__" :

    if not os.path.exists( images ) :
        try :
            os.mkdir( images )
        except :
            pass

    for i in range( 20000 ) :
        url_temp = url % i
        print( url_temp, end='\r' )
        response = requests.get( url_temp, stream=True, headers=headers )
        filepath = os.path.join( images, "%05u.jpg" % i )
        with open( filepath, 'wb' ) as f :
            shutil.copyfileobj( response.raw, f )
