import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Set up ChromeDriverManager and get the path to the chromedriver executable
executable_path = ChromeDriverManager().install()

# Create a service object with the path to the chromedriver executable
service = Service(executable_path=executable_path)

# Create an options object and set the incognito option
options = Options()
options.add_argument("--incognito")

# Instantiate the webdriver with the service and options
driver = webdriver.Chrome(service=service, options=options)

# Use the driver to navigate to https://www.demoblaze.com/
base_url = "https://www.demoblaze.com"
driver.get(base_url)
print(driver.title)
driver.find_element("id", "login2").click()

# Pause execution for 1 second
time.sleep(1)

# Check if modal has a correct title
check1 = driver.find_element('id', 'logInModalLabel').text
assert check1 == 'Log in'

# Login with a valid username and password
username= "mehrdad"
password = "885522iI!"
driver.find_element("id", "loginusername").send_keys(username)
time.sleep(1)
driver.find_element("id", "loginpassword").send_keys(password)
time.sleep(1)
wait = WebDriverWait(driver, 10)
login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[onclick="logIn()"]')))

input("Press Enter to close the browser...")
