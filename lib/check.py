import sys
from utils import utils

print('')
print('######################')
print('#   CRC checker   #')
print('######################')
print('')
print('> checking CRC...')
files_to_check = sys.argv[1:]

db = utils.get_crc_db()
errors_found = False
for filename in files_to_check:
    try:
        base_name = utils.get_base_file_name(filename)
        msg = '> scrubbing file ' + base_name + ' ...'
        print(msg, end='\r')
        crc = utils.crc(filename)
        reference_crc = db.get(base_name)
        if reference_crc == None or crc != reference_crc:
            print('')
            print('> ERROR: CRC of ' + base_name + ' missmatch, expected ' + str(reference_crc or 'None ') + ', got ' + crc)
            errors_found = True
        else:
            print(' '*(len(msg)+2) , end='\r')
    except:
        print('')
        print('> ERROR: file ' + filename + ' does not exist')
        errors_found = True

if not errors_found:
    print('')
    print('')
    print('#############')
    print('#  PASSED   #')
    print('#############')
    print('')
    print('')
input('> Press Enter to exist')