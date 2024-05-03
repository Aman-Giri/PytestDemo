import logging

def test_logging():
    logger = logging.getLogger(__name__)

    filehandler = logging.FileHandler('logfile.log')
    logger.addHandler(filehandler)  #filehandler Object

    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    filehandler.setFormatter(formatter)

    logger.setLevel(logging.INFO)
    logger.debug("A debug statement is executed")
    logger.info("Information Statement")
    logger.warning("Something is in the warning mode")
    logger.error("A major error has happened")
    logger.critical("Critical Issues")
