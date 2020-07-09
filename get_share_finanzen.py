from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          chrome_options=chrome_options
                          )
# URL of website
share_name = "basf"
url = f"https://www.finanzen.net/realtimekurs/{share_name}"

# Opening the website
driver.get(url)

while (True):
    # sleep for a minute
    time.sleep(60)

    # Getting current URL source code
    get_title = driver.title

    # Printing the title of this URL
    print(get_title)

