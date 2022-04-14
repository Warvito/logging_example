import logging
import sys

logger = logging.getLogger("Operator")


def setup_logger(
        logger_name: str,
        format: str = "%(asctime)s %(levelname)s: %(message)s",
        level: int = logging.INFO,
) -> logging.Logger:
    """Setups logger: name, level, format etc."""
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    formatter = logging.Formatter(format)
    # ch = logging.StreamHandler(sys.stdout)
    ch = logging.StreamHandler(sys.stderr)
    ch.setLevel(level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    file_formatter = logging.Formatter("%(filename)s:%(funcName)s - %(asctime)s %(levelname)s: %(message)s")
    file_ch = logging.FileHandler("/media/walter/Storage/Projects/logging_example/outputs/logs/errors.log")
    file_ch.setLevel(logging.ERROR)
    file_ch.setFormatter(file_formatter)
    logger.addHandler(file_ch)

    return logger


def util_function():
    logger.info("I am inside util/util_function!")
