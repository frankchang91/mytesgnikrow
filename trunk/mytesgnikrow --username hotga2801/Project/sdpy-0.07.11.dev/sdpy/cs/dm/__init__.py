#!/usr/bin/env python

from info import __doc__

# --- Exporte ----------------------------------------------------------------
from dm import *

__all__ = filter(lambda s:not s.startswith('_'),dir())

from numpy.testing import NumpyTest
test = NumpyTest().test
