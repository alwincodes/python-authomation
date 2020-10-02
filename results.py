# for this to work you will need chrome driver and install selenium
# to install selenium type pip install selenium in your cmd
# for chrome driver search google boii
from time import sleep
from selenium import webdriver
# this only works when mgu page is running 
# path specifies the dir in which chromedriver is stored so change it according to your pc config
path="C:\Program Files (x86)\chromedriver.exe"
# enter your desired rollno range
rollno_start=12345678912
rollno_end=12345678915
driver=webdriver.Chrome(path)
rollnos=[*range(rollno_start, rollno_end, 1)]
# mgu results page
driver.get("https://117.239.158.204/exQpMgmt/index.php/public/ResultView_ctrl/")
# this 2 stmnts are to skip googles security page when visiting mgu results page bcoz mgus page dosen't have https
driver.find_element_by_xpath("/html/body/div/div[2]/button[3]").click()
driver.find_element_by_xpath("/html/body/div/div[3]/p[2]/a").click()
# sleep is given to make sure the page completely loads before executing further commands mgu site slow af
sleep(4)
# the for loop repeats for every roll no in the list rollnos
for rollno in rollnos:
  print(f"getting result for {rollno}")
  sem = driver.find_element_by_xpath("/html/body/center/table/tbody/tr[2]/td/div/table/tbody/tr[2]/td/form/fieldset/table/tbody/tr[2]/td[3]/select/option[9]")
  sem.click()
  prn = driver.find_element_by_xpath("/html/body/center/table/tbody/tr[2]/td/div/table/tbody/tr[2]/td/form/fieldset/table/tbody/tr[4]/td[3]/input")
  prn.clear()
  prn.send_keys(rollno)
  search=driver.find_element_by_xpath("/html/body/center/table/tbody/tr[2]/td/div/table/tbody/tr[2]/td/form/fieldset/table/tbody/tr[6]/td[3]/button")
  search.click()
  sleep(4)
  notavail=driver.find_element_by_xpath("/html/body/center/table/tbody/tr[2]/td/div/table/tbody/tr[4]/td").text
  # if the roll no is invalid this condition will make sure that a screenshot is not taken
  if notavail =="Result Not Available !!":
    print("notavail")
  else:
    driver.get_screenshot_as_file(f"{rollno}.png")
    print(f"{rollno} screenshot taken 📸 ")

print("check the dir for result screenshots")
driver.quit()