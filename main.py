# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import TimeoutException
# from seleniumbase import Driver
# from selenium.common.exceptions import NoSuchElementException
# import time
# import os
# from dotenv import load_dotenv
# import pyotp
# import undetected_chromedriver as uc
# from datetime import datetime
# import sys


# # #Function to get OTC
# # def get_otp(secret_key='kknjpzscbmjvnfxk'):
# #     totp = pyotp.TOTP(secret_key)
# #     print(totp.now())
# # get_otp()

# load_dotenv()

# def get_otp(secret_key):
#     totp = pyotp.TOTP(secret_key)
#     return totp.now()
# # ------------------------------------------------------------------
# # Selenium and Browser Options

# # chrome_options = Options()
# # chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# #Chrome options with download prefs
# chrome_options = uc.ChromeOptions()
# prefs = {
#     "download.prompt_for_download": False,
#     "directory_upgrade": True,
#     "safebrowsing.enabled": True,
# }
# chrome_options.add_experimental_option("prefs", prefs)

# chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# #Driver Setup
# # driver = Driver(uc=True)
# driver = uc.Chrome(options=chrome_options)
# driver.maximize_window()
# wait = WebDriverWait(driver, 60)
# shortWait = WebDriverWait(driver, 15)

# #Login
# try:
#     web_url = "https://outlook.live.com/mail/0/"
#     # driver.uc_open_with_reconnect(web_url, 4)
#     driver.get(web_url)

#     print("Opening Website...")
            
#     signIn_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="action-oc5b26"]/span')))
#     signIn_btn.click()
#     print("Moving to signIn steps")
    
#     #Page Switch
#         # --- wait until a second window handle appears, then switch ---
#     wait.until(lambda d: len(d.window_handles) > 1)
#     driver.switch_to.window(driver.window_handles[-1])
#     time.sleep(5)

#     #Email
#     email_box = wait.until(EC.element_to_be_clickable((By.ID, "i0116")))
#     email_box.clear()
#     email_box.send_keys(os.getenv('EMAIL'), Keys.ENTER)
#     print("Email Entered.")
    
#     #Password
#     try:
#         password_box = shortWait.until(EC.element_to_be_clickable((By.ID, "i0118")))
#     except TimeoutException:
#         password_box = shortWait.until(EC.element_to_be_clickable((By.ID, "passwordEntry")))
#     password_box.clear()
#     password_box.send_keys(os.getenv('PASSWORD'), Keys.ENTER)
#     print("Password Entered.")

#     #Click on "I can't use my Microsoft Authenticator app right now"
#     sign_in_another_way = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="signInAnotherWay"]')))
#     sign_in_another_way.click()
#     print("Selected sign-in using another way")
    
#     time.sleep(5)
#     #Click on "Use a Verification Code"
#     verify_with_code = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idDiv_SAOTCS_Proofs"]/div[2]/div/div/div[2]/div')))
#     verify_with_code.click()
#     print("Clicked on verify with code")
    
#     time.sleep(5)
#     #OTC
#     try:
#         otc_input = shortWait.until(EC.element_to_be_clickable((By.ID, "idTxtBx_SAOTCC_OTC")))
#     except TimeoutException:
#         otc_input = shortWait.until(EC.element_to_be_clickable((By.XPATH, '//input[@aria-label="Code" and @placeholder="Code"]')))
#     otc_input.clear()
#     otc_input.send_keys(get_otp(os.getenv('SECRET_KEY')), Keys.ENTER)
#     print("OTP Entered.")
    
#     time.sleep(5)
#     #No Button 1
#     try:
#         no_button = wait.until(EC.element_to_be_clickable((By.ID, "idBtn_Back")))
#         no_button.click()
#         print("Selected No.")
#     except TimeoutException:
#         no_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="button" and @value="No"]')))
#         no_button.click()
#         print("Selected No.")
#     time.sleep(5)
#     try:
#         name_div = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "content")]/div[1]')))
#         print("User Name:", name_div.text)
#         name_div.click()
#     except TimeoutException:
#         print("Name element not found.")

#     time.sleep(5)
#     try:
#         wait.until(EC.presence_of_element_located((By.XPATH, '//button[@aria-label="New mail"]')))
#         print("Logged In to Outlook Successfully.")
#     except TimeoutException:
#         print("Login Failed or took too long.")
# except TimeoutException:
#     print("Login Timeout")
#     driver.quit()
#     sys.exit(1)
    
# #Search
# try:
#     time.sleep(10)
#     search_bar = wait.until(EC.element_to_be_clickable((By.ID, 'topSearchInput')))
#     search_bar.click()
#     time.sleep(5)
#     search_bar.clear()
    
    
#     #Dynamic search content
#     search_date = datetime.today()
#     formatted_date = f"{search_date.month}_{search_date.day}_{search_date.year}"
#     # For testing purpose
#     # search_bar.send_keys(f"FW: [Secure] - ABC HOLDINGS - TEAMSTERS  File dated - 6_11_2025")
#     search_bar.send_keys(f"FW: [Secure] - ABC HOLDINGS - TEAMSTERS  File dated - {formatted_date}")
#     search_bar.send_keys(Keys.ENTER)
#     print("Searched for content.")
    
#     time.sleep(5)
    
#     #Select Inbox filter
#     folders = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchScopeButtonId-option"]/span')))
#     time.sleep(2)
#     folders.click()
#     time.sleep(2)
#     Inbox = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchScopeButtonId-list1"]/span/span')))
#     Inbox.click()
        
#     print("Selected Inbox.")
#     time.sleep(10)
#     #Select the first one div
#     try:
#         first_search = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="listbox"]//div[@data-focusable-row="true"][1]')))
#         first_search.click()
#         print("Selected first search result.")
#     except NoSuchElementException:
#         print("Searched mail not found.")
#         driver.quit()
#         sys.exit(1)
        
# except TimeoutException:
#     print("Error during finding email.")
#     driver.quit()
#     sys.exit(1)
    
# #Forward Mail
# try:                                                                  
#     forward_arrow = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ItemReadingPaneContainer"]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div/div/button')))
#     forward_arrow.click()
#     print("Clicked on forward mail.")
#     time.sleep(10)
#     email_to = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="2"]')))
#     email_to.send_keys(os.getenv('EMAIL_TO'))
#     print("entered email.")
#     try:
#         content_box1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sonoraIntroHintParent"]/span[1]')))
#         content_box1.click()
#         content_box2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="editorParent_1"]/div/div[3]')))
#         content_box2.send_keys("Please find this email.")
#         print("entered content.")
#     except TimeoutException:
#         print("No content space found.")
                                                                  
#     send_mail = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Send']")))
#     send_mail.click()
#     print("Clicked on send mail,  waiting for 30s...")
#     time.sleep(30)
#     print("Email Forwarded Successfully.")
#     driver.quit()
# except TimeoutException:
#     print("Error occured while forwarding mail.")
#     driver.quit()
#     sys.exit(1)
# #Code Done


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
from datetime import datetime, timedelta
import sys

LOG_FILE = "last_forwarded.txt"
today = datetime.now().date()

def read_last_forwarded_date():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            try:
                return datetime.strptime(f.read().strip(), "%Y-%m-%d").date()
            except:
                return None
    return None

def update_last_forwarded_date():
    with open(LOG_FILE, "w") as f:
        f.write(today.strftime("%Y-%m-%d"))

def should_forward(today, last_date):
    if today.weekday() > 4:  #-->  Only from Monday(0) to Friday(4)
        return False
    if last_date is None:
        return True
    start_of_week = today - timedelta(days=today.weekday())
    return last_date < start_of_week

# Check before running main code
last_forwarded = read_last_forwarded_date()
if not should_forward(today, last_forwarded):
    print(f"[{today.strftime('%A')}] - Already forwarded this week or not a weekday. Skipping.")
    sys.exit(0)

load_dotenv()

def get_otp(secret_key):
    totp = pyotp.TOTP(secret_key)
    return totp.now() 

chrome_options = uc.ChromeOptions()
prefs = {
    "download.prompt_for_download": False,
    "directory_upgrade": True,
    "safebrowsing.enabled": True,
}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

driver = uc.Chrome(options=chrome_options)
driver.maximize_window()
wait = WebDriverWait(driver, 60)
shortWait = WebDriverWait(driver, 15)

#Login
try:
    web_url = "https://outlook.live.com/mail/0/"
    driver.get(web_url)
    print("Opening Website...")
            
    signIn_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="action-oc5b26"]/span')))
    signIn_btn.click()
    print("Moving to signIn steps")
    
    wait.until(lambda d: len(d.window_handles) > 1)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(5)

    email_box = wait.until(EC.element_to_be_clickable((By.ID, "i0116")))
    email_box.clear()
    email_box.send_keys(os.getenv('EMAIL'), Keys.ENTER)
    print("Email Entered.")
    
    try:
        password_box = shortWait.until(EC.element_to_be_clickable((By.ID, "i0118")))
    except TimeoutException:
        password_box = shortWait.until(EC.element_to_be_clickable((By.ID, "passwordEntry")))
    password_box.clear()
    password_box.send_keys(os.getenv('PASSWORD'), Keys.ENTER)
    print("Password Entered.")

    sign_in_another_way = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="signInAnotherWay"]')))
    sign_in_another_way.click()
    print("Selected sign-in using another way")
    
    time.sleep(5)
    verify_with_code = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idDiv_SAOTCS_Proofs"]/div[2]/div/div/div[2]/div')))
    verify_with_code.click()    
    print("Clicked on verify with code")
    
    time.sleep(5)
    try:
        otc_input = shortWait.until(EC.element_to_be_clickable((By.ID, "idTxtBx_SAOTCC_OTC")))
    except TimeoutException:
        otc_input = shortWait.until(EC.element_to_be_clickable((By.XPATH, '//input[@aria-label="Code" and @placeholder="Code"]')))
    otc_input.clear()
    otc_input.send_keys(get_otp(os.getenv('SECRET_KEY')), Keys.ENTER)
    print("OTP Entered.")
    
    time.sleep(5)
    try:
        no_button = wait.until(EC.element_to_be_clickable((By.ID, "idBtn_Back")))
        no_button.click()
        print("Selected No.")
    except TimeoutException:
        no_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="button" and @value="No"]')))
        no_button.click()
        print("Selected No.")
    time.sleep(5)
    # try:
    #     name_div = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "content")]/div[1]')))
    #     print("User Name:", name_div.text)
    #     name_div.click()
    # except TimeoutException:
    #     print("Name element not found.")
  
    time.sleep(5)
    try:  
        wait.until(EC.presence_of_element_located((By.XPATH, '//button[@aria-label="New mail"]')))
        print("Logged In to Outlook Successfully.")
    except TimeoutException:
        print("Login Failed or took too long.") 
except TimeoutException:
    print("Login Timeout")
    driver.quit()
    sys.exit(1)
    
#Search
try:
    time.sleep(10)
    search_bar = wait.until(EC.element_to_be_clickable((By.ID, 'topSearchInput')))
    search_bar.click()
    time.sleep(5)
    search_bar.clear()
    
    search_date = datetime.today()
    formatted_date = f"{search_date.month}_{search_date.day}_{search_date.year}"
    search_bar.send_keys(f"FW: [Secure] - ABC HOLDINGS - TEAMSTERS  File dated - {formatted_date}")
    search_bar.send_keys(Keys.ENTER)
    print("Searched for content.")
    
    time.sleep(5)
    folders = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchScopeButtonId-option"]/span')))
    folders.click()
    time.sleep(2)
    Inbox = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchScopeButtonId-list1"]/span/span')))
    Inbox.click()
    print("Selected Inbox.")   
    time.sleep(10)
 
    try:
        first_search = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="listbox"]//div[@data-focusable-row="true"][1]')))
        first_search.click()
        print("Selected first search result.")  
    except NoSuchElementException:
        print("Searched mail not found.")
        driver.quit() 
        sys.exit(1)     
         
except TimeoutException:  
    print("Error during finding email.")   
    driver.quit()  
    sys.exit(1)
        
#Forward Mail
try:                                                                  
    forward_arrow = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ItemReadingPaneContainer"]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div/div/button')))
    forward_arrow.click()   
    print("Clicked on forward mail.")   
    time.sleep(10)
    email_to = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="2"]')))
    email_to.send_keys(os.getenv('EMAIL_TO'))
    print("entered email.")
    try:
        content_box1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sonoraIntroHintParent"]/span[1]')))
        content_box1.click()
        content_box2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="editorParent_1"]/div/div[3]')))
        content_box2.send_keys("Please find this email.")
        print("entered content.")
    except TimeoutException:
        print("No content space found.")
                                                                  
    send_mail = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Send']")))
    send_mail.click()
    print("Clicked on send mail,  waiting for 30s...")
    time.sleep(30)
    print("Email Forwarded Successfully.")
    
    #Update forward date   
    update_last_forwarded_date()
    driver.quit()
except TimeoutException:
    print("Error occurred while forwarding mail.")
    driver.quit()
    sys.exit(1)
  