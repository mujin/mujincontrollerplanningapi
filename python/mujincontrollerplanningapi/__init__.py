# -*- coding: utf-8 -*-
# Copyright (C) 2014-2016 MUJIN Inc

__version__ = '0.1.0'

try:
    import mujincommon.i18n
    ugettext, ungettext = mujincommon.i18n.GetDomain('mujincontrollerplanningapi').GetTranslationFunctions()
    _ = ugettext
except ImportError:
    # translations don't exist, so just have dummy conversion
    _ = unicode
