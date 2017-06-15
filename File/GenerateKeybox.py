# This is used for generating the Keybox file which used for applying Widevine/Attestation keybox.
from sys import argv

script, first, second, third, fourth = argv

# fileName:     Keybox index file which contain the device ID.
# prefix:       prefix name which contain the project name for device ID, such as: MERCURY_CN_.
# start:        start ID, if the start is 1, then then device ID is: MERCURY_CN_00000001.
# keyboxNum:    The number of keybox ID for this file, it should be 25000 as BBRY request.
def GenKeyboxFile(fileName, prefix, start, keyboxNum):
    fp = open(fileName, 'w')
    try:
        for num in range(int(start), int(keyboxNum)):
#            temp = "%08d" % num        # format the tring to 8 digitals with '0'.
            temp = str(num).zfill(8)    # fill with 0, untill to 8 digitals.
            buf = prefix + temp + '\n'
            fp.writelines(buf);
    except Exception, e:
        print Exception, ":", e
    finally:
        fp.close()

GenKeyboxFile(first, second, third, fourth)


