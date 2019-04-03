# бот ставит лайки всем кого нашел в поиске
# bot puts likes to all who found in the search

from selenium import webdriver
import time
from bs4 import BeautifulSoup
from lxml import html

driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://www.ok.ru');
#driver.execute_script("window.open('https://www.ok.ru','_blank');");

def login(login, password):	
	'''
	Login in ok.ru
	Логин в одноклассниках
	'''
	elem = driver.find_element_by_name("st.email") #find_element_by_id
	elem.send_keys(login)
	elem = driver.find_element_by_name("st.password")
	elem.send_keys(password)
	elem.submit()
	return

def searchUsers():
	'''	
	search users and return 
	Ищет пользователей и возвращает ссылки на их профили
	'''
	driver.get('https://www.ok.ru/search?st.mode=Users&st.grmode=Groups&st.posted=set&st.location=%D0%A1%D1%82%D0%B0%D0%B2%D1%80%D0%BE%D0%BF%D0%BE%D0%BB%D1%8C&st.country=10414533690&st.onSite=on')

	for i in range(1,10):	
		# Scroll down to bottom
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		# Wait to load page
		time.sleep(1)

	# Beautiful Soup
	soup = BeautifulSoup(driver.page_source)
	soup_profile = soup.findAll('a', {'class': 'gs_result_i_t_name o'})
	print ("Всего найдено профилей: ", len(soup_profile))

	return (soup_profile)

login('@mail.ru', 'password')

like = 0
for link in searchUsers():
	print (link['href'])
	driver.get("https://www.ok.ru" + link['href'])
	
	try:
		element = driver.find_element_by_xpath("//div[@class='widget  __compact __wide-count']")
		element.click()
		like += 1
		print ("поставлено классов:", like)
	except:
		pass


