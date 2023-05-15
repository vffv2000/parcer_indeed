import json
import time
from art import tprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

tprint("@vffv2000")
print("Contact on Telegram for custom script development")
print('Welcome to the parser for the website https://ca.indeed.com/')
print('To start the parser, type <link> in the console')

#https://www.indeed.com/jobs?q=manager&l=chicago&fromage=1
# https://www.indeed.com/jobs?q=manager&l=chicago&fromage=1&start=10
def get_info(url):

    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get(url)
    time.sleep(5)
    count_element = driver.find_element(By.CSS_SELECTOR, 'div.jobsearch-JobCountAndSortPane-jobCount span:first-child')
    count_text = count_element.text
    count = int(count_text.replace(',', '').split()[0])//25
    print(count, " links detected")

    with open('data.txt', 'w') as f:
        f.write(str(url) + '\n')
        for i in range(10, count, 10):
            idx = url.index('&')
            new_url = url[:idx] + f"&start={i}" + url[idx:]
            f.write(str(new_url) + '\n')




def main():
    while True:
        print("Enter your URL, for example (https://www.indeed.com/jobs?q=full+time&l=Charlotte%2C+NC&vjk=8cbba115fdef3efd)")
        url_l = input("input:")
        get_info(url_l)
        print("All links have been saved to the 'data.txt' file located in the same directory as the 'find_all_links.exe' file.")
        print(' -----------------------FINAL -------------------------------')



if __name__ == "__main__":
    main()
