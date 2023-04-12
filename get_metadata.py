#!/usr/local/bin/python3

###########################################################################
# 
# name          : get_metadata.py
# 
# purpose       : get nakamigos metadata 
# 
# usage         : ./get_metadata.py
# 
# description   :
# 
###########################################################################

from selenium import webdriver

contract_address = "0xd774557b647330C91Bf44cfEAB205095f7E6c367"
url = "https://x2y2.io/eth/0xd774557b647330C91Bf44cfEAB205095f7E6c367/%u"

elements = "elements"

if __name__ == "__main__" :
    if not os.path.exists( elements ) :
        try :
            os.mkdir( elements )
        except :
            pass

    driver = webdriver.Chrome()
    for i in range( 20000 ) :
        driver.get( url % i  )
        with open( "elements/%u.json" % i, 'w' ) as f :
            f.write( driver.page_source )
    driver.close()
