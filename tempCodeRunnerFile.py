from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from seleniumbase import Driver
from selenium.common.exceptions import NoSuchElementException
import time
import os
from dotenv import load_dotenv
import pyotp
import undetected_chromedriver as uc
from datetime import datetime
import sys


# #Function to get OTC
def get_otp(secret_key='kknjpzscbmjvnfxk'):
    totp = pyotp.TOTP(secret_key)
    print(totp.now())
get_otp()