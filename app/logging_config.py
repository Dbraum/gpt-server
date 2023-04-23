import logging

logging_config = {
    "version": 1,
    "handlers": {
        "file_handler": {
            "class": "logging.FileHandler",
            "formatter": "myFormatter",
            "filename": "app.log"
        }
    },
    "formatters": {
        "myFormatter": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["file_handler"]
    }
}

logging.config.dictConfig(logging_config)

logger = logging.getLogger("gpt-server")

logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())  # 输出到STDERR 