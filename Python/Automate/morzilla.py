from selenium import webdriver

browser = webdriver.Firefox()

browser.get('https://www.google.com')

elem = browser.find_element_by_css_selector('.gLFyf')
print(elem)
#elem.click()
elem.send_keys('cs:go')
elem.submit()

'''
browser.back()
browser.forward()
browser.refresh()
browser.quit()
'''