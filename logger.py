import logging

def log_settings(message):
    logger = logging.getLogger("read_files")
    logger.setLevel(logging.INFO)

    # create the logging file handler
    fh = logging.FileHandler("mylog.log")

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(fh)

    logger.info(message)






