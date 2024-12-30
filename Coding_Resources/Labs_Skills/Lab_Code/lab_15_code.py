"""
Module Name: Programming Lab 15
Description: Libraries: Logging and OS Navigation
Author: Clinton Garwood
Date: August 2024
License: MIT
"""


def create_file_logger():
    """
    Full example: Custom Log File Writer
    Seven Steps (from creation though configuration and usage)
    :return: file_logger
    """
    import logging
    # 1) Create a logger to report data to files
    file_logger = logging.getLogger('file_logger')

    # 2) Set its logging level
    file_logger.setLevel(logging.INFO)

    # 3) Using FileHandler (see also StreamHandler) assign filename
    file_handler = logging.FileHandler('test_file.data')

    # 4) Define data format (write/displayed) (i.e., time, message, filename)
    file_format = logging.Formatter('%(asctime)s - %(message)s - %(filename)s:%(lineno)d')

    # 5) Add the format (file_format) to the handler (file_handler)
    file_handler.setFormatter(file_format)

    # 6) Add the handler (file_handler) to the logger (file_logger)
    file_logger.addHandler(file_handler)

    # 7) Usage shows above and below setLevel settings
    file_logger.debug('DEBUG does not get written to a file. - line 36')
    file_logger.info('This will be written to the file. - line 37')

    return file_logger


def create_stream_logger():
    """
    Workflow is the same as create_file_logger without usage
    :return: stream_logger
    """
    import logging
    stream_logger = logging.getLogger('stream_logger')
    stream_logger.setLevel(logging.DEBUG)
    stream_handle = logging.StreamHandler()
    stream_format = logging.Formatter('%(asctime)s - %(message)s')
    stream_handle.setFormatter(stream_format)
    stream_logger.addHandler(stream_handle)
    return stream_logger


def create_default_logger():
    """
    This function initializes `logging` and returns a logger object
    :return: logger
    """
    import logging

    # After `import logging` the feature is immediately available
    # Uncomment below to generate/view log messages sensitivity formats
    logging.debug(f" Debug. - line 66")
    logging.info(f" Info.")
    logging.warning(f" Warning.")
    logging.error(f" Error.")
    logging.critical(f" Critical.\n")

    # A generic logger, named logger is available
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.debug(f'Logger Object Initialized - line 75')

    # Various additional loggers can also be created
    # main_logger = logging.getLogger(__name__)  # for main function
    # custom_logger = logging.getLogger('special_case')  # named loggers

    return logger


def main():
    print(f'\nWelcome to Lab 15: Logging Library and Log File Data')

    # Old way to call main:
    # main()
    # New way to call main:
    # if __name__ == "__main__":
    #     main()
    # --  blank line still remains at the bottom of the file

    # Discuss the timing (scope) for where to use `import`
    # import logging

    # Create generic_logger log a message to it
    generic_logger = create_default_logger()
    generic_logger.debug("This Represents Simple Usage - line 99")

    # Create file_logger and log two messages to it
    file_logger = create_file_logger()
    file_logger.info("Use `os` for Operating System and File Management - line 102")
    file_logger.debug("line 103 This message is ignored")

    # Create stream_logger and log a message to it
    stream_logger = create_stream_logger()
    stream_logger.debug("This will print to the console - line 107.")

    return


if __name__ == "__main__":
    main()
