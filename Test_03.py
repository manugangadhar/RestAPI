from selenium import webdriver
import pytest
from time import sleep


@pytest.fixture()
def precondition():
    global driver
    driver = webdriver.Chrome("C:\\DVF\\Tools\\chromedriver_win32\\chromedriver.exe")


def test_case_001(precondition):
    driver.get("https://www.google.com/")
    sleep(2)
    driver.close()


def test_case_002(precondition):
    driver.get("https://www.google.com/")
    sleep(2)
    driver.close()

def test_case_003(precondition):
    driver.get("https://www.google.com/")
    sleep(2)
    driver.close()


def test_case_004(precondition):
    driver.get("https://www.google.com/")
    sleep(2)
    driver.close()