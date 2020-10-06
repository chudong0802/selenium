from selenium import webdriver
import  time

option = webdriver.ChromeOptions()
option.add_argument('-kiosk')
driver = webdriver.Chrome(chrome_options=option)

#自动化登录
login_url = 'http://10.16.31.77:3000/login'
driver.get(login_url)
# driver.maximize_window()
time.sleep(1.5)

driver.find_element_by_name("user").send_keys("Guest")
driver.find_element_by_css_selector("input[placeholder='password']").send_keys("Guest")
time.sleep(1)

driver.find_element_by_class_name("css-6ntnx5-button").click()
time.sleep(3)


#滚动到指定元素
while True:
    for i in range(1,19):
        target = driver.find_element_by_xpath("//div[@class='react-grid-item'][{}]//div[@class='panel-title']".format(i))
        time.sleep(10)
        driver.execute_script("arguments[0].scrollIntoView();",target)
    for j in range(18,1,-1):
        target1 = driver.find_element_by_xpath("//div[@class='react-grid-item'][{}]//div[@class='panel-title']".format(j))
        time.sleep(10)
        driver.execute_script("arguments[0].scrollIntoView();", target1)





# #将滚动条移动到页面的底部
# js="var q=document.documentElement.scrollTop=1000"
# driver.execute_script(js)
# time.sleep(3)
# #将滚动条移动到页面的顶部
# js="var q=document.documentElement.scrollTop=0"
# driver.execute_script(js)
# time.sleep(3)
# #若要对页面中的内嵌窗口中的滚动条进行操作，要先定位到该内嵌窗口，在进行滚动条操作
# js="var q=document.getElementById('id').scrollTop=100000"
# driver.execute_script(js)
# time.sleep(3)
