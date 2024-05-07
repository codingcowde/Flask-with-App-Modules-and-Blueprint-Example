from flask import Flask
from auth.routes import auth
import logging.config



# Define logging configuration
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
        },
    },
    'handlers': {
        'file_login': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'login.log',
            'maxBytes': 10000,
            'backupCount': 3,
        },
        'file_app': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'app.log',
            'maxBytes': 10000,
            'backupCount': 3,
        },
    },
    'loggers': {
        'login': {
            'handlers': ['file_login'],
            'level': 'INFO',
            'propagate': False,
        },
        'app': {
            'handlers': ['file_app'],
            'level': 'INFO',
            'propagate': False,
        }
    }
}

# Apply logging configuration
logging.config.dictConfig(LOGGING_CONFIG)

# The use logger like:  logging.getLogger('app').info('Index page accessed')


app = Flask(__name__)
app.register_blueprint(auth, url_prefix='/auth')
