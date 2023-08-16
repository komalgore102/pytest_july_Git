from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


class Test_001:

    def test_sum_001(self):
        a=10
        b=30
        sum=a+b
        print(sum)
        if sum == 40:
            assert True
        else:
            assert False

    def test_login_002(self):
        driver=webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title == "Credence":
            print("Welcome....You are at credence ")
            assert True
        else:
            print("Sorry not found")
            assert False