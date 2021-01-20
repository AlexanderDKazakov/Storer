# -*- coding: utf-8 -*-

__all__ = (
    '__version__',
    'Storer'
)

import pkg_resources 
__version__ = pkg_resources.get_distribution("Storer").version

__short_description__ = "Minimalist storage class for any purpose."
__license__ = "MIT"
__author__ = "Alexander D. Kazakov"
__author_email__ = "alexander.d.kazakov@gmail.com"
__github_username__ = "AlexanderDKazakov"

from Storer.Storer import Storer