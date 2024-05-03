import inspect
import logging


class BaseTest():
    def getloggerfunction(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        filehandler = logging.FileHandler('logfile.log')
        logger.addHandler(filehandler)  # filehandler Object

        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)

        logger.setLevel(logging.INFO)
        return logger
