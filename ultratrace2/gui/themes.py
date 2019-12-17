import logging
import os
import platform

from typing import Optional

from .. import utils

try:
    from ttkthemes import ThemedTk
except ImportError:
    logging.warning('Unable to load themes')
    from tkinter import Tk as ThemedTk


def get_theme(name: str) -> Optional[str]:
    if name is not None:
        return name

    if platform.system() == 'Linux':
        try:

            import xrp

            Xresources_path = os.path.join(os.environ['HOME'], '.Xresources')
            if os.path.exists(Xresources_path):
                Xresources = xrp.parse_file(Xresources_path)
                if '*TtkTheme' in Xresources.resources:
                    return Xresources.resources['*TtkTheme']
                if '*TkTheme' in Xresources.resources:
                    return Xresources.resources['*TkTheme']
                return 'clam'

        except Exception as e:
            logging.warning('Error loading themes: ' + str(e))

    return None
