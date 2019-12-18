#DSE BD Closing Price Scraper
#by
#http://github.com/IngeniousArtist

#Import Functions
import csv
from datetime import datetime
from selenium import webdriver
from bs4 import BeautifulSoup

#Start Timer
start_time = datetime.now()

#Initialize ChromeDriver and load Website
chromedriver_location = "/Users/shahriyer/Desktop/code/chromedriver"
driver = webdriver.Chrome(chromedriver_location)
driver.get('http://dsebd.org/data_archive.php')

#XPaths for form
from_date = '//*[@id="ClosePDate"]'
to_date = '//*[@id="ClosePDate1"]'
button = '/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[2]/td[2]/input'

#Change form attributes to get Previous Data
from_element =driver.find_element_by_xpath(from_date)
driver.execute_script("arguments[0].min = '2015-01-01'", from_element)
to_element =driver.find_element_by_xpath(to_date)
driver.execute_script("arguments[0].min = '2015-01-01'", to_element)

#Fill out the form
driver.find_element_by_xpath(from_date).send_keys("01/01/2019")
driver.find_element_by_xpath(to_date).send_keys("30/06/2019")
driver.find_element_by_xpath(button).click()

#Download Source and Beautify
content = driver.page_source
soup = BeautifulSoup(content, 'lxml')

#Close ChromeDriver
driver.close()

#Find Table from HTML File
stock_table = soup.find("table", attrs={"border":"0", "cellpadding":"3", "width":"100%","bgcolor":"#808000", "cellspacing":"1"})
stock_table_data = stock_table.tbody.find_all("tr") 

#Create 2D Array of Data length
print("Number of Rows in Dataset:")
print(len(stock_table_data))
data = [[] for x in range(len(stock_table_data)-1)]

#Append Table to Data
for i in range(len(stock_table_data)-1):
    for td in stock_table_data[i].find_all("td"):
        data[i].append(td.font.text)

#Write to CSV file
with open("/Users/shahriyer/Desktop/code/Data_2019_1.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(data)

#Calculate Time
finish_time = datetime.now() - start_time
print("TIME TAKEN TO COMPLETE:")
print(finish_time)


