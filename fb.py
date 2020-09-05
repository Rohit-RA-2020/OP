from selenium import webdriver

user_id = input("Enter your email-ID: ")
password = input("Enter your password: ")

browser = webdriver.Chrome('C:\\Users\\Rohit ranjan\\Downloads\\chromedriver.exe')  #give path to chrome driver
browser.get('https://www.facebook.com')

ep = browser.find_element_by_id("email")
ep.send_keys(user_id)

pw = browser.find_element_by_id("pass")
pw.send_keys(password)

login = browser.find_element_by_id("u_0_b")
login.click()
