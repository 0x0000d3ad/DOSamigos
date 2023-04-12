#!/usr/bin/python

###########################################################################
#
# name          : create_lists.py
#
# purpose       : create whitelists for the phases of the DOSamigos mint 
#
# usage         : python create_lists.py
#
# description   :
#
###########################################################################

import json
import os
import requests
import shutil


from eth_utils import keccak, to_checksum_address


dao_list = [ "dospunks_dao.txt", "holders_dankbots.txt", "extra_addresses.txt" ]
wl_list =  [ "dospunks_dao.txt", "holders_dankbots.txt", "extra_addresses.txt", "holders_dostrashbirds.txt", "holders_wgmis.txt" ]
list_dir = "lists"

dao_final = "final_dao.txt"
wl_final = "final_wl.txt"

# aggregate separate lists 
def make_list( addresses_list ) :
    return_value = []
    for filename in addresses_list :
        filepath = os.path.join( list_dir, filename )
        try :
            with open( filepath, 'r' ) as f :
                return_value += [ to_checksum_address( i.strip() ) for i in f.readlines() ]
        except Exception as e :
            print( "--> Problem opening list. %s" % str( e ) )

    return_value = list( set( return_value ) )
    return return_value


# output list in third web compatible format
def write_lists( addresses_list, output_filename ) :
    to_write = addresses_list
    output_filepath = os.path.join( list_dir, output_filename )

    with open( output_filepath, 'r' ) as f :
        to_write += [ to_checksum_address( i.strip() ) for i in f.readlines() ]
    to_write = list( set( to_write ) )
    to_write = [ "%s,5" % i for i in to_write ]

    with open( output_filepath.replace( "txt", "csv" ), 'w' ) as f :
        f.write( "address,maxClaimable\n" )
        f.write( "\n".join( to_write ) )


if __name__ == "__main__" :
    dao = make_list( dao_list )
    wl = make_list( wl_list )

    write_lists( dao, dao_final )
    write_lists( wl, wl_final )
