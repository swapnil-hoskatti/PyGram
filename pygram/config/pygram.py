import os

from pygram.config import BaseConfig
from pygram.utils.const import ABSPATH_BASE
from pygram.filters import nss

class PyGramConfig(BaseConfig):
    NAME                = 'PyGram'
    VERSION             = '0.1.0'
    WINDOW_ASPECT_RATIO = 3 / 2
    WINDOW_WIDTH        = 320
    WINDOW_HEIGHT       = int(WINDOW_ASPECT_RATIO * WINDOW_WIDTH)

    ACCEPTED_FILES      = [ ]
    DEFAULT_FILE        = os.path.join(ABSPATH_BASE, 'data', 'lenna.png')

    FILTERS             = [
        {
            'name': 'normal',
            'command': lambda image: image
        },
        {
            'name': '1977',
            'command': lambda image: nss(image)
        }
    ]

    BTNGRID_ROWS        = 1
    BTNGRID_COLS        = 3
