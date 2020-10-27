# 导包
import time
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome()
# 打开待测地址
driver.get("file:///C:/Users/sandysong"
           "/Desktop/pagetest/%E6%B3%A8%E5%86%8CA.html")
# 业务操作
# driver.find_element_by_link_text("访问 百度 网站").click()
driver.find_element_by_partial_link_text("网站").click()
# 3秒后关闭浏览器窗口
time.sleep(3)
driver.quit()