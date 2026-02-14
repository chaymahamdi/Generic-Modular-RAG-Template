import json
import logging.config
import re

from configuration.app_settings import AppSettings

app_settings = AppSettings()
app_name = app_settings.PROJECT_NAME


class JsonFormatter(logging.Formatter):

    def match_access_logs(self, message: str):
        pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+):(?P<port>\d+) - "(?P<method>[A-Z]+) (?P<path>[^ ]+) (?P<protocol>[^"]+)" (?P<status>\d+)'
        match = re.match(pattern, message)
        return match

    def format(self, record):
        log_message = {
            "timestamp": self.formatTime(record, self.datefmt),
            "logger": record.name,
            "env": app_settings.ENVIRONMENT.value,
            "level": record.levelname,
            "app_name": app_name,
            "overall_status": "succeeded",
            "source": f"{record.filename}:{record.lineno} - {record.funcName}()",
            "trace_id": record.otelTraceID if hasattr(record, 'otelTraceID') else 0,
            "span_id": record.otelSpanID if hasattr(record, 'otelSpanID') else 0,
        }

        try:
            log_string = record.getMessage() if not isinstance(record.msg, dict) else record.msg
        except Exception:
            log_string = record.msg

        if isinstance(log_string, dict):
            log_message.update(log_string)
        else:
            match = self.match_access_logs(log_string)
            if match:
                log_message.update(match.groupdict())
            else:
                log_message["message"] = log_string

        if "reason" in log_message:
            log_message["reason"] = str(log_message["reason"])
            if record.exc_info:
                log_message["message"] = self.formatException(record.exc_info)

        return json.dumps(log_message, ensure_ascii=False)


logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(message)s",
            "use_colors": None,
        },
        "json": {
            "()": JsonFormatter,
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        }
    },
    "loggers": {
        "uvicorn": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "uvicorn.access": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        app_name: {
            "handlers": ["console"],
            "level": app_settings.LOG_LEVEL,
            "propagate": False,
        },
        "": {
            "handlers": ["console"],
            "level": "WARNING",
        },
    },
}

logging.config.dictConfig(logging_config)
logger = logging.getLogger(app_name)
