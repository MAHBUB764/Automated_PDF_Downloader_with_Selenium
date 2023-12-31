from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
custom_option= webdriver.ChromeOptions()
custom_option.add_experimental_option('prefs', {
    "download.default_directory": "E:\PROJECT\PDF\D", #Change default directory for downloads
    "download.prompt_for_download": False, #To auto download the file
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome 

})

""" custom_option.add_experimental_option("prefs",{
    "Download.default_directory":"E:\PROJECT\PDF Scrape\D",
    "Download.prompt_for_download":False,
    "Plugins.always_open_pdf_externally":True
}) """

custom_option.add_experimental_option("detach",True)
custom_option.add_argument("--start-maximized")
driver=webdriver.Chrome(options=custom_option)

URL="https://us.idec.com/idec-us/en/USD/Programmable-Logic-Controller/Micro-PLC/FT1A-SmartAXIS/p/FT1A-H24RC"
driver.get(URL)
    
driver.implicitly_wait(5)

close_it=driver.find_element(By.XPATH,"//div[@id='js-cookie-notification']")

if close_it:
    driver.find_element(By.XPATH,"//div[@id='js-cookie-notification']/button").click()
else:
    print("Button not found")
find_a_tag=driver.find_elements(By.XPATH,"//a")
count=0
for a in find_a_tag:
    """ ###The provided code snippet is meant to find anchor elements (<a>) on a webpage, 
                    #erify if they link to a PDF file and have the word "download" in their text, 
                    andnd then click on those links to potentially download up to 5 PDF files ###"""
    
    
    if a.get_attribute('href') and 'pdf' in a.get_attribute ('href') and 'download' in a.text.lower():
        a.click()
        driver.implicitly_wait(2)
        count +=1
        if count >=5:
            break
else:
    print("URL EROR")


