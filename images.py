#!/usr/bin/python

###########################################################################
#
# name          : images.py
#
# purpose       : image validation
#
# usage         : python images.py
#
# description   :
#
###########################################################################

import json
import os
import random
import requests
import shutil

from PIL import Image

images_dir = "images"
final_dir = "images_release"
metadata = "_metadata.json"

def check_images() :
    files = os.listdir( images_dir )
    filenames = []
    for filename in files :
        filepath = os.path.join( images_dir, filename ) 
        im = Image.open( filepath )
        width, height = im.size
        if width != 1600 :
            print( "--> %s width: %u" % ( filename, width ) )
            filenames.append( filename )
        if height != 1600 :
            print( "--> %s height: %u" % ( filename, height ) )
            filenames.append( filename )

    filenames = list( set( filenames ) )
    for f in filenames :
        print( f )

def copy_images_for_release() :
    if not os.path.exists( final_dir ) :
        os.mkdir( final_dir )

    files = os.listdir( images_dir )
    filenames = []
    for i, filename in enumerate( files ) :
        print( "--> %04u" % i, end="\r" )
        filepath = os.path.join( images_dir, filename ) 
        destpath = os.path.join( final_dir, "%u.png" % i )
        shutil.copy( filepath, destpath )        

    shutil.copy( metadata, os.path.join( final_dir, metadata ) )

def shuffle_images() :
    m = None
    with open( metadata, 'r' ) as f :
        m = json.load( f )

    files = os.listdir( images_dir )
    data = list( zip( files, m ) )
    random.shuffle( data )

    for i, datum in enumerate( data ) :
        print( "--> %04u" % i, end="\r" )
        filepath = os.path.join( images_dir, datum[ 0 ] )
        destpath = os.path.join( final_dir, "%u.png" % i )
        datum[ 1 ][ "name" ] = "DOS Amigos #%u" % ( i + 1 )
        datum[ 1 ][ "tokenId" ] = i 
        shutil.copy( filepath, destpath )

    m2 = [ i[ 1 ] for i in data ]
    metapath = os.path.join( final_dir, metadata )
    with open( metapath, 'w' ) as f :
        json.dump( m2, f, indent=2 )

def fix_name() :
    m = None
    metapath = os.path.join( final_dir, metadata )
    with open( metapath, 'r' ) as f :
        m = json.load( f )

    for i, datum in enumerate( m ) :
        datum[ "name" ] = "DOSamigos #%u" % ( i + 1 )

    with open( metapath, 'w' ) as f :
        json.dump( m, f, indent=2 )



if __name__ == "__main__" :
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--copy",     help="Copy images for release", action="store_true")
    parser.add_argument("-s", "--shuffle",  help="Shuffle images",          action="store_true")
    parser.add_argument("-f", "--fix_name", help="Fix names",               action="store_true")
    options = parser.parse_args()

    if options.copy :
        copy_images_for_release()
    if options.shuffle :
        shuffle_images()
    if options.fix_name :
        fix_name()
