__all__ = ('Config',)

import os.path
import logging
import imp

from six.moves import configparser


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('tailor.config')

Config = configparser.ConfigParser()


def reload(path):
    path = os.path.join(path, 'config.ini')
    logger.debug('loading configuration: %s', path)
    Config.read(path)


imp.reload(
    os.path.realpath(
        os.path.join(__file__, '..', '..', 'config')
    )
)
