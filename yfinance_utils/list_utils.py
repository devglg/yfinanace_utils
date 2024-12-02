#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2024 Lehi Gracia
#
#

from yfinance_utils.sample_lists.mag7 import mag7
from yfinance_utils.sample_lists.nasdaq100 import nasdaq100
from yfinance_utils.sample_lists.snp500 import snp500
from yfinance_utils.sample_lists.aero_def import aero_def
from yfinance_utils.sample_lists.nasdaq import nasdaq
from yfinance_utils.sample_lists.nyse import nyse
from yfinance_utils.sample_lists.remove import remove

def get_all_tickers():
    all = mag7 + nasdaq100 + snp500 + aero_def + nasdaq + nyse
    return list(set(all) - set(remove))

def get_aero_def():
    return list(set(aero_def) - set(remove))

def get_mag7():
    return list(set(mag7) - set(remove))

def get_snp500():
    return list(set(snp500) - set(remove))

def get_nasdaq100():
    return list(set(nasdaq100) - set(remove))

def get_nasdaq():
    return list(set(nasdaq) - set(remove))

def get_nyse():
    return list(set(nyse) - set(remove))