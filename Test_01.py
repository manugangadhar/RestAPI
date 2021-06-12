from selenium import webdriver
from time import sleep
import pytest

@pytest.mark.Smoke
def test_case_001():
    driver = webdriver.Chrome("C:\\DVF\\Tools\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://www.google.com/")
    sleep(2)
    driver.close()


def test_case_002():
    driver = webdriver.Chrome("C:\\DVF\\Tools\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://www.google.com/")
    sleep(2)
    driver.close()

def test_case_003():
    driver = webdriver.Chrome("C:\\DVF\\Tools\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://www.google.com/")
    sleep(2)
    driver.close()


@pytest.mark.Smoke
def test_case_004():
    driver = webdriver.Chrome("C:\\DVF\\Tools\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://www.google.com/")
    sleep(2)
    driver.close()