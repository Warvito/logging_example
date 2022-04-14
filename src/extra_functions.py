import logging

logger = logging.getLogger("Operator")


def extra_function(with_error=False):
    logger.info("I am inside extra_functions/extra_function!")
    if with_error:
        try:
            c = 5 / 0
        except Exception as e:
            logger.error("Exception occurred", exc_info=True)
