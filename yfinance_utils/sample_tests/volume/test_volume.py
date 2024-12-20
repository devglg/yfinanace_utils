#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2024 Lehi Gracia
#

import warnings
warnings.filterwarnings("ignore")

import pprint
import yfinance
from yfinance_utils import list_utils
from yfinance_utils import volume_utils

ticklist = list_utils.get_nasdaq100()
df_ticks = {}
counter = 0

t = yfinance.Tickers(ticklist)

for tick in ticklist:
    data =  volume_utils.get_percent_volume(t.tickers[tick], period='1mo', days_back=2)
    if data["percentage"] and data["average"]: 
        pprint.pprint(f"{t.tickers[tick].info['symbol']:6} volume is {data["percentage"]:4}% from Average {data["average"]:13,}")




