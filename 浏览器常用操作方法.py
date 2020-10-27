import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file:///C:/Users/sandysong/Desktop"
           "/pagetest/%E6%B3%A8%E5%86%8CA.html")
try:
    driver.set_window_size(500, 500)
    time.sleep(1)
    driver.set_window_position(1000, 200)
    time.sleep(1)
    driver.maximize_window()
    driver.find_element_by_id("password").send_keys("123456")
except Exception as e:
    driver.get_screenshot_as_file(
        "./img/{}test.png".format(time.strftime("%Y%m%d-%H%M%S")))
    raise e
finally:
    time.sleep(1)
    driver.quit()
