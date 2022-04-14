import logging

from extra_functions import extra_function
from util import setup_logger, util_function


def main():
    logger = setup_logger(
        logger_name="Operator",
        level=logging.ERROR
    )

    logger.debug("I am a DEBUG inside run_code/main!")
    logger.info("I am an INFO inside run_code/main!")
    logger.warning("I am a WARNING inside run_code/main!")
    logger.error("I am an ERROR inside run_code/main!")
    logger.critical("I am a CRITICAL inside run_code/main!")

    extra_function()
    util_function()
    extra_function(with_error=True)

    print("The end")


if __name__ == '__main__':
    main()
