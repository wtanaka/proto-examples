#! /usr/bin/python

# See README.txt for information and build instructions.

import photo_pb2
import sys

# Iterates though all people in the AddressBook and prints info about them.
def ListGallery(photo_gallery):
  for photo in photo_gallery.photos:
    print "photo ID:", photo.id
    print "  Name:", photo.name
    if photo.HasField('url'):
      print "  url:", photo.url

    for one_tag in photo.tag:
      if one_tag.type == photo_pb2.Photo.PHOTO:
        print "  Photo tag #:",
      elif one_tag.type == photo_pb2.Photo.DRAWING:
        print "  Drawing tag #:",
      elif one_tag.type == photo_pb2.Photo.PAINTING:
        print "  Patinting tag#:",
      print one_tag.tagid

# Main procedure:  Reads the entire address book from a file and prints all
#   the information inside.
if len(sys.argv) != 2:
  print "Usage:", sys.argv[0], "ADDRESS_BOOK_FILE"
  sys.exit(-1)

photo_gallery = photo_pb2.PhotoGallery()

# Read the existing address book.
f = open(sys.argv[1], "rb")
photo_gallery.ParseFromString(f.read())
f.close()

ListGallery(photo_gallery)
