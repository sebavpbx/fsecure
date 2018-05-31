# -*- coding: utf-8 -*-

from selenium import webdriver

job_position = "Quality Engineer"
city = "Poznań"
url = "https://www.f-secure.com/en/web/about_global/careers/job-openings"

city_path = "//span[normalize-space(text()) = '" + city + "']"

driver = webdriver.Firefox()
driver.get(url)

driver.find_element_by_xpath("//button[@data-id='job-city']").click()
driver.find_element_by_xpath(city_path).click()

assert job_position in driver.page_source

driver.close()
