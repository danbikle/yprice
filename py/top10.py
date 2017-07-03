"""
  top10.py

  This script should get price history of top10.
  Also it should generate 'unsplit' prices.
  Demo:
  ${HOME}/anaconda3/bin/python top10.py
"""

import glob
import os
import chromedriver
import mlprep
import pdb
import time

for tkr_s in ['^GSPC','^RUT','AAPL','AMZN','GOOG','MSFT','DIA','QQQ','SPY','XOM']:
    print('Busy...')
    time.sleep(6)
    print(tkr_s)
    try:
      chromedriver.get_csv(tkr_s,'history')
      # implement later:
      # mlprep.unsplit(tkr_s)
    except:
      print(tkr_s+' problem: get_csv() or unsplit() exception.')
'bye'
