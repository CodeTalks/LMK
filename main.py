#!/usr/bin/python

import sys

import pandas
from datetime import date

import log
from stock import Stock
from common import show_plot
from LMKCalculator import LMKCalculator, LMKBacktestCalculator, plot_lmk
from LMKBandCalculator import LMKBandCalculator, LMKBandBacktestCalculator, plot_lmk_band
from InitialPivotalPointCalculator import InitialPivotalPointCalculator

# ------------------------------------------------------------------------------
def lmk_analysis(symbol, start="2011/1/1", end=date.today(), use_cache=True,
                 no_volume=False, atr_factor=2, freq="D", plot=False):
    stk = Stock(symbol)
    stk.retrieve_history(start=start, use_cache=False, no_volume=no_volume)
    stk.resample_history(freq=freq)

    history = stk.history

    # LMK
    c = InitialPivotalPointCalculator(atr_factor=atr_factor)
    history.apply(c, axis=1)

    c = LMKCalculator(c)
    lmk = history.apply(c, axis=1)
    history = pandas.merge(history, lmk, left_index=True, right_index=True, sort=False)

    c = LMKBacktestCalculator()
    history.apply(c, axis=1)

    result = c.value_rate()

    if plot:
        plot_lmk(history)

    return result

def lmk_band_analysis(symbol, start="2011/1/1", end=date.today(), use_cache=True,
                      no_volume=False, atr_factor=2.0, freq="D", plot_width=0):
    stk = Stock(symbol)
    stk.retrieve_history(start=start, end=end, use_cache=use_cache, no_volume=no_volume)
    stk.resample_history(freq=freq)

    history = stk.history

    # LMKBand
    c = InitialPivotalPointCalculator(atr_factor=atr_factor)
    history.apply(c, axis=1)

    c = LMKBandCalculator(c)
    lmk_band = history.apply(c, axis=1)
    history = pandas.merge(history, lmk_band, left_index=True, right_index=True, sort=False)

    c = LMKBandBacktestCalculator()
    history.apply(c, axis=1)

    result = c.value_rate()

    if plot_width:
        plot_lmk_band(history, show_band=True, band_width=plot_width)

    return result

def main():
    for symbol in ["000001.SS", "300052.SZ", "300223.SZ",
                     "^GSPC", "AAPL", "GOOG", "VMW", "TSLA", "AMZN", "FB", "TWTR",
                     "BIDU", "QIHU", "EDU"]:
        for atr_factor in (1.0, 1.5, 2.0, 2.5, 3.0):
            for freq in ("D", "W-FRI", "W-MON"):
                continue # shortcut - commented
                no_volume = True if symbol in ("000001.SS", "^GSPC") else False
                result = lmk_analysis(symbol, no_volume, atr_factor=atr_factor, freq=freq)
                print "%s: atr_factor=%.1f, freq=%5s, lmk_result=%.2f" % (symbol, atr_factor, freq, result)
                result = lmk_band_analysis(symbol, no_volume, atr_factor=atr_factor, freq=freq)
                print "%s: atr_factor=%.1f, freq=%5s, lmk_band_result=%.2f" % (symbol, atr_factor, freq, result)


    symbol = "VMW"
    symbol = "TSLA"
    symbol = "300369.SZ"
    symbol = "000001.SS"
    atr_factor=2.0
    freq="W-FRI" #"D"
    plot_width= 7 #1
    freq="D" #"D"
    plot_width = 0
    result = lmk_band_analysis(symbol, start="2013/6/1", no_volume=False, atr_factor=atr_factor, freq=freq, plot_width=plot_width)
    print "%s: atr_factor=%.1f, freq=%5s, lmk_result=%.2f" % (symbol, atr_factor, freq, result)

    atr_factor=1.0
    result = lmk_analysis(symbol, start="2013/6/1", no_volume=False, atr_factor=atr_factor, freq=freq, plot=True)
    print "%s: atr_factor=%.1f, freq=%5s, lmk_result=%.2f" % (symbol, atr_factor, freq, result)
    show_plot()
#           000001.SS: atr_factor=2.0, freq=W-FRI, result={'LMKBand': 0.8696190000000009, 'LMK': 0.94849700000000214} *
#           300052.SZ: atr_factor=1.0, freq=W-MON, result={'LMKBand': 2.698414000000001, 'LMK': 5.4609190000000005} *
#           300052.SZ: atr_factor=2.5, freq=    D, result={'LMKBand': 5.794929999999996, 'LMK': 2.8020520000000015} *
#           300223.SZ: atr_factor=2.0, freq=W-MON, result={'LMKBand': 1.0630739999999999, 'LMK': 1.4456530000000003} *
#               ^GSPC: atr_factor=1.0, freq=W-MON, result={'LMKBand': 1.1068870000000006, 'LMK': 1.0218860000000018} *
#                AAPL: atr_factor=1.5, freq=W-FRI, result={'LMKBand': 1.3435790000000012, 'LMK': 1.3013450000000026} *
#                GOOG: atr_factor=2.0, freq=    D, result={'LMKBand': 1.4855740000000037, 'LMK': 1.7133670000000023}*
#                 VMW: atr_factor=1.0, freq=W-FRI, result={'LMKBand': 0.8812340000000007, 'LMK': 1.1376860000000022} *
#                TSLA: atr_factor=2.5, freq=W-FRI, result={'LMKBand': 4.282322, 'LMK': 5.0755420000000013} *
#                AMZN: atr_factor=2.0, freq=W-FRI, result={'LMKBand': 0.9853490000000009, 'LMK': 1.3492070000000014} *
#                  FB: atr_factor=1.0, freq=W-FRI, result={'LMKBand': 1.9850030000000005, 'LMK': 1.6613310000000017} *
#                QIHU: atr_factor=1.0, freq=    D, result={'LMKBand': 2.628371000000005, 'LMK': 2.3734070000000043} *
#                QIHU: atr_factor=1.5, freq=    D, result={'LMKBand': 1.1581020000000013, 'LMK': 3.7001110000000001} *
#                 EDU: atr_factor=2.0, freq=W-FRI, result={'LMKBand': 1.6322960000000013, 'LMK': 0.7238290000000005} *

if __name__ == "__main__":
    import logging
    from common import probe_proxy

    probe_proxy()
    #log.init(logging.INFO)
    log.init(logging.DEBUG)

    main()

# TODO:
# *. biweekly? dynamic frequency?

