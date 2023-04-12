#!/usr/bin/python

###########################################################################
#
# name          : create_metadata.py
#
# purpose       : create metadata 
#
# usage         : python create_metadata.py
#
# description   :
#
###########################################################################

import copy
import json
import os
import requests
import shutil

if __name__ == "__main__" :
    assert os.path.exists( "data/all_metadata.json" ), "Metadata path does not exist"
    all_metadata = None
    metadata = []
    with open( "data/all_metadata.json", 'r' ) as f :
        all_metadata = json.load( f )

    files = os.listdir( "images" )
    tokens = [ os.path.splitext( i )[ 0 ].split( "_" ) for i in files ]
    
    for i, tok in enumerate( tokens ) :
        index = int( tok[ 1 ] )
        temp = copy.deepcopy( all_metadata[ index ] )
        temp[ "name" ] = "DOS Amigos #%u" % ( i + 1 )
        temp[ "originalId" ] = temp[ "tokenId" ]
        temp[ "tokenId" ] = i
        temp[ "attributes" ].append( { "trait_type" : "Palette", "value" : tok[ 0 ] } )

        metadata.append( temp )

    with open( "_metadata.json", 'w' ) as f :
        json.dump( metadata, f, indent=2 )
