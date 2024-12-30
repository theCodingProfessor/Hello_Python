### Lab 15: "Python Libraries (i.e., logging)"

#### Assignment Overview
In this lab, you will learn to work with the built-in Python `logging` library to develop data handling and file management skills. You will learn how to direct messages using a custom logging object both to the console and into log files.

#### Learning Objectives
- Understand the usage of the Python `logging` library.
- Develop skills to configure and customize loggers.
- Learn to direct log messages to different destinations, such as the console and log files.

#### Instructions
**15.1) Create File**
- Create a properly formatted Python file named `logger_library.py`

**15.2) Define Stub Functions and Main Function**
- Start by creating three stub functions: `create_default_logger`, `create_stream_logger`, and `create_file_logger`.
- Define a `main` function that will call these stub functions:
```python
def main():
    print(f'\nWelcome to Lab 15: Python Libraries (i.e., logging)')

    # Review the timing (scope) for where to use the statement
    # import logging

    # Call create_default_logger and use the generic_logger returned
    generic_logger = create_default_logger()
    generic_logger.debug("This Represents Simple Usage")
    
    file_logger = create_file_logger()
    file_logger.info("Use `os` for Operating System and File Management")
    file_logger.debug("This message is ignored")

    # Call create_stream_logger and use stream_logger
    stream_logger = create_stream_logger()
    stream_logger.debug("This will print to the console.")

    return

main()

```

**15.3) Implement `create_default_logger` Function**
Import the `logging` library, use the default logging behavior, create a generic logging object, and return it:
```python
def create_default_logger():
    """
    This function initializes `logging` and returns a logger object
    :return: logger
    """
    import logging

    # After `import logging` the feature is immediately available
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.debug(f'Logger Object Initialized')

    return logger
```

**15.4) Implement `create_file_logger` Function**
Follow the seven steps to create a file logger, customize it to write data into a text file, and return the file logger:
```python
def create_file_logger():
    """
    Full example: Custom Log File Writer
    Seven Steps (from creation through configuration and usage)
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

    # 7) Usage - shows above and below setLevel settings
    file_logger.debug('DEBUG does not get written to a file.')
    file_logger.info('This will be written to the file.')

    return file_logger
```

**15.5) Implement `create_stream_logger` Function**
Import the `logging` library, create a StreamLogger, and customize it to pipe data to the console:
```python
def create_stream_logger():
    """
    Workflow is the same as create_file_logger - without usage
    :return: stream_logger
    """
    import logging
    stream_logger = logging.getLogger('pipe_stream')
    stream_logger.setLevel(logging.DEBUG)
    stream_handle = logging.StreamHandler()
    stream_format = logging.Formatter('%(asctime)s - %(message)s')
    stream_handle.setFormatter(stream_format)
    stream_logger.addHandler(stream_handle)
    return stream_logger
```

#### Submission
- Submit a single source code file named: `logger_library.py`.

#### Assessment Criteria
- Correctly implemented and configured logging functions.
- Proper use of the logging library to direct messages to the console and log files.
- Accurate implementation of the main function and its calls to the logging functions.
- Clear and well-documented code with appropriate comments.

#### Additional Notes
- Ensure your code is properly formatted and follows Python coding standards.
- Test your code to verify that the logging functions work as expected.
- Refer to the official Python logging documentation for additional details and examples.

<hr>

Additional Topics: 

[Python `logging` Library Documentation](https://docs.python.org/3/library/logging.html)
**`logging`**:
   - **Purpose**: Provides a flexible framework for emitting log messages from Python programs. It helps in recording events, debugging, and keeping track of application behavior.
   - **Common Functions**:
     - `logging.basicConfig()`: Configures the root logger.
     - `logging.debug()`, `logging.info()`, `logging.warning()`, `logging.error()`, `logging.critical()`: Log messages of varying severity levels.
     - `logging.getLogger()`: Retrieves a logger object for a specified name.

   ```python
   import logging
   logging.basicConfig(level=logging.DEBUG)
   logging.info("This is an info message")
   ```

<hr>

#### Additional Code
Demonstration File 

```python
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

    # 7) Usage - shows above and below setLevel settings
    file_logger.debug('DEBUG does not get written to a file.')
    file_logger.info('This will be written to the file.')

    return file_logger


def create_stream_logger():
    """
    Workflow is the same as create_file_logger - without usage
    :return: stream_logger
    """
    import logging
    stream_logger = logging.getLogger('pipe_stream')
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
    logging.debug(f" Debug.")
    # logging.info(f" Info.")
    # logging.warning(f" Warning.")
    # logging.error(f" Error.")
    # logging.critical(f" Critical.\n")

    # A generic logger, named logger is available
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.debug(f'Logger Object Initialized')

    # Various additional loggers can also be created
    # main_logger = logging.getLogger(__name__)  # for main function
    # custom_logger = logging.getLogger('special_case')  # named loggers

    return logger


def main():
    print(f'\nWelcome to Lab 18: Reading and Formatting File Data')

    # Old way to call main:
    # main()
    # New way to call main:
    # if __name__ == "__main__":
    #     main()
    # -- see at bottom of file, blank line still remains

    # Discuss the timing (scope) for where to use `import`
    # import logging

    # Call default_logger and use the generic_logger returned
    generic_logger = create_default_logger()
    generic_logger.debug("This Represents Simple Usage")

    file_logger = create_file_logger()
    file_logger.info("Use `os` for Operating System and File Management")
    file_logger.debug("This message is ignored")

    # Call create_stream_logger and use stream_logger
    stream_logger = create_stream_logger()
    stream_logger.debug("This will print to the console.")

    return


if __name__ == "__main__":
    main()

```

<hr>
