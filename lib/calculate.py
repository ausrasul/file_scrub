import sys
from utils import utils

print('')
print('######################')
print('#   CRC calculator   #')
print('######################')
print('')
print('> Calculating CRC...')
files_to_check = sys.argv[1:]

db = utils.get_crc_db()
for filename in files_to_check:
    try:
        base_name = utils.get_base_file_name(filename)
        msg = '> calculating file ' + base_name + ' ...'
        print(msg, end='\r')
        crc = utils.crc(filename)
        db[base_name] = crc
        print(msg + ' ' + crc)
    except:
        print('> ERROR: file ' + filename + ' does not exist')

utils.save_crc_db(db)

input('> Press Enter to exist')