def logger_settings():
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        },

        "handlers": {
            "logentries": {
                "class": "logentries.LogentriesHandler",
                "token": "82d29a94-ec97-48f5-b55e-d069d0199520",
                "formatter": "simple"
            },

            "file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "INFO",
                "formatter": "simple",
                "filename": "review_scraper.log",
                "maxBytes": 10485760,
                "backupCount": 20,
                "encoding": "utf8"
            },
        },

        "root": {
            "level": "INFO",
            "handlers": ["logentries", "file_handler"]
        }
    }
