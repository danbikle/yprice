# chromedriver.py

# This script should drive chromedriver to get new prices of stocks.
# ref:
# http://selenium-python.readthedocs.io/locating-elements.html
# https://sites.google.com/a/chromium.org/chromedriver/downloads
# This script works well with chromedriver 2.29
# python 3.6.1 and selenium (3.4.1)

# Demo:
# driver = webdriver.Chrome()
# import chromedriver
# chromedriver.get_csv('AAPL', 'history')

import numpy  as np
import pandas as pd
import glob
import os
import pdb
import subprocess
import sys
import time
from datetime  import datetime
from fractions import Fraction
from selenium  import webdriver
from selenium.webdriver.chrome.options import Options

def get_csv(tkr_s='AAPL',ctype='history'): # valid ctype values: div, split, history
  # Given a tkr I should download a CSV file by getting an href,
  # enhancing the href, and then getting the enhanced href.
  # I should remove previous downloads:
  dl_s    = ''.join([os.environ['HOME'],'/Downloads/'])
  csv_s   = ''.join([tkr_s,'.csv']) # useful later
  dlcsv_s = ''.join([dl_s,csv_s])
  if os.path.isfile(csv_s):
    os.remove(csv_s)
  # os.path.realpath(__file__) is the path to the script you are looking at.
  # I should declare the location of parent-folder:    
  tkrprice_folder_s = ''.join([os.path.dirname(os.path.realpath(__file__)),'/../'])
  old_s             = ''.join([tkrprice_folder_s,'static/CSV/old/'])
  outfolder_s       = ''.join([tkrprice_folder_s,'static/CSV/',ctype,'/'])
  href0_s           = ''.join(['https://finance.yahoo.com/quote/',tkr_s,'/',ctype])
  # I should get mindate_i_s of the tkr from old_s:
  mcsv_s      = ''.join([old_s,csv_s])
  tkr_df      = pd.read_csv(mcsv_s).sort_values(['cdate'])
  mindate_s   = tkr_df.cdate.min()
  mindate_dt  = datetime.strptime(mindate_s, '%Y-%m-%d')
  mindate_i_s = datetime.strftime(mindate_dt,'%s')
  path_to_extension_s = ''.join([tkrprice_folder_s,'ublock/1.12.4_0'])
  chrome_options      = Options()
  chrome_options.add_argument('load-extension=' + path_to_extension_s)
  chromedriver_exec_s = ''.join([tkrprice_folder_s,'bin/chromedriver'])
  driver = webdriver.Chrome(chromedriver_exec_s,chrome_options=chrome_options)
  driver.create_options()
  href0_s = ''.join(['https://finance.yahoo.com/quote/',tkr_s,'/history'])
  try:
    driver.get(href0_s)
    time.sleep(5)
    # I should try to get the 'Download Data' link:
    lnk = driver.find_element_by_link_text('Download Data')#.click()
    # I should get href of lnk
    href_s = lnk.get_attribute("href")
    # should be like:
    # 'https://query1.finance.yahoo.com/v7/finance/download/AA?period1=1492462308&period2=1495054308&interval=1d&events=history&crumb=pYheK5rafih'
    # I should enhance the href
    href_l          = href_s.split('=')
    href_l[1]       =  ''.join([mindate_i_s,'&period2']) # Use mindate I got from older CSV
    href_l[4]       =  ''.join([ctype,'&crumb'])
    enhanced_href_s = '='.join(href_l)
    # should be like:
    # 'https://query1.finance.yahoo.com/v7/finance/download/AA?period1=460926308&period2=1495054308&interval=1d&events=split&crumb=pYheK5rafih'
    # I should driver.get() the lnk
    print('I now try to GET this URL:')
    print(enhanced_href_s)
    driver.get(enhanced_href_s)
    time.sleep(5)
  except: # selenium.common.exceptions.NoSuchElementException:
    print(tkr_s+' problem: Some exception')
  # I should move the new CSV files to a safe place
  if os.path.isfile(dlcsv_s):
    # delete bad data
    subprocess.call(['sed','-i', '/null/d', dlcsv_s ])
    os.rename(dlcsv_s,outfolder_s+csv_s)
  driver.quit()
  'bye'
  
'bye'
