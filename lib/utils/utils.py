import os
import zlib
import json

def get_base_file_name(filename):
    if os.path.exists(filename):
        return os.path.basename(filename)
    else:
        raise NameError('File does not exist' + filename)

def get_crc_db():
    with open(os.path.dirname(os.path.abspath(__file__)) + os.path.sep +  "crc_db.json") as db_file:
        data = json.load(db_file)
        return data

def save_crc_db(db):
    with open(os.path.dirname(os.path.abspath(__file__)) + os.path.sep +  "crc_db.json", 'w') as db_file:
        json.dump(db, db_file)

def crc(fileName):
    prev = 0
    for eachLine in open(fileName,"rb"):
        prev = zlib.crc32(eachLine, prev)
    return "%X"%(prev & 0xFFFFFFFF)


