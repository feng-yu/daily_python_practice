"""
test the exception handle in following structure:
try:
...
except:
...
else:
...
finally:
...

"""

import logging
import time


logging.basicConfig(filename="C:\\Users\\User\\PycharmProjects\\daily_python_practice\\log\\exceptiontest.log",
                    level=logging.DEBUG,
                    format="[%(asctime)s]-[%(levelname)s] %(message)s")
logger = logging.getLogger()


def read_file_time(path):
    """return the content in file at 'path' and measure the required time"""
    start_time = time.time()
    try:
        file = open(path, mode='rb')
        data = file.read()
        return data
    except FileNotFoundError as err:
        logger.error(err)
        raise
    else:
        file.close()
    finally:
        end_time = time.time()
        da = end_time - start_time
        logger.info("Read %s take %f " % (path, da))


logger.info("Read 153K file")
read_file_time("C:\\Temp\\Scan2.PDF")

logger.info("Read 1.15M file")
read_file_time("C:\\Temp\\pic\\251e-hwzkfpu7662455.jpg")

logger.info("Read a no-existence file")
read_file_time("C:\\Temp\\Scan-no-existence.PDF")

