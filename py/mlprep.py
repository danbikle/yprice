""" 
  mlprep.py
  This module should help me prep CSV data.
"""

# Demo:
# import mlprep
# mlprep.unsplit('AAPL')

import numpy  as np
import pandas as pd
import glob
import os
import pdb
import sys
from fractions  import Fraction
from subprocess import call

def unsplit(tkr='AAPL'):
  """Should use information in split/TKR.csv to unsplit prices in history/TKR.csv 
  to fill usplit/TKR.csv.
  """
  # os.path.realpath(__file__) is the path to the script you are looking at.
  # I should declare the location of parent-folder and dependent paths:
  tkrprice_folder_s = ''.join([os.path.dirname(os.path.realpath(__file__)),'/../'])
  tkrh_s            = ''.join([tkrprice_folder_s,'static/CSV/history/',tkr,'.csv'])
  tkrs_s            = ''.join([tkrprice_folder_s,'static/CSV/split/'  ,tkr,'.csv'])
  usplitf_s         = ''.join([tkrprice_folder_s,'static/CSV/usplit/'            ])
  usplit_s          = ''.join([usplitf_s                              ,tkr,'.csv'])
  # I should create a folder to capture unsplit prices:
  call(['mkdir','-p',usplitf_s])
  # I should create a DF from prices:
  tkrh_df         = pd.read_csv(tkrh_s)[['Date','Close']]
  tkrh_df.columns = ['cdate','cp']
  # I should create a DF from splitdates:
  tkrs_df         = pd.read_csv(tkrs_s)
  tkrs_df.columns = ['splitdate','splitratio']
  # I should create a column to capture unsplit prices:
  tkrh_df['uscp'] = tkrh_df.cp
  # I should iterate through the splitdates:
  for row in tkrs_df.itertuples():
    # I should match each row in tkrs_df with many rows in tkrh_df and then unsplit
    p0_sr = (tkrh_df.cdate   >= row.splitdate)
    tkrh_df.loc[p0_sr,'uscp'] = float(Fraction(row.splitratio)) * tkrh_df[p0_sr].uscp
  # I should write the unsplit prices to csv
  tkrh_df.to_csv(usplit_s,index=False,float_format='%6.3f')
'bye'
