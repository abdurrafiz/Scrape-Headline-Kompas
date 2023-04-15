from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt

def get_drvier():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://account.kompas.com/login")
  return driver

def main():
  driver = get_drvier()
  driver.find_element(by="id", value="email").send_keys("hafizh.abdurrahman1997@gmail.com")
  driver.find_element(by="id", value="password").send_keys("kolorijo" + Keys.RETURN)
  time.sleep(11)
  driver.find_element(by="xpath", value="/html/body/div[1]/div[1]/div[1]/a").click()
  while True:
    time.sleep(3)
    print("Headlines")
    berita = driver.find_element(by="xpath", value="/html/body/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/ul/div/div")
    print(berita.text)
    write_file(str(berita.text))
    print("----------")
    driver.refresh()

def write_file(text):
  """Write input text into a text file"""
  filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
  with open(filename, 'w') as file:
    file.write(text)

main()