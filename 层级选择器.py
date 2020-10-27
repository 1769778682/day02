# 导包
import time
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome()
# 打开待测地址
driver.get("file:///C:/Users/sandysong"
           "/Desktop/pagetest/%E6%B3%A8%E5%86%8CA.html")
time.sleep(2)
# 业务操作
# 使用css
d = driver.find_element_by_css_selector("#pa>input")
d.send_keys("admin")
print(d)
time.sleep(2)
# driver.find_element_by_css_selector("#pa input").send_keys("123456")
# 3秒后关闭浏览器窗口
time.sleep(3)
driver.quit()