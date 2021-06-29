# %%
from selenium import webdriver
import sys
import time
import pandas as pd

# %%
driver = webdriver.Chrome('/home/adenilson/Engineering/chromedriver')


def tem_item(xpath, driver=driver):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False


driver.get('https://pt.wikipedia.org/wiki/Nicolas_Cage')
driver.implicitly_wait(10)


# %%
tb_filmes = '/html/body/div/div/div[1]/div[2]/main/div[2]/div[3]/div[1]/table[2]'

# %%
i = 0
while not tem_item(tb_filmes):
    i += 1
    if i > 50:
        break
    pass
tabela = driver.find_element_by_xpath(
    '/html/body/div/div/div[1]/div[2]/main/div[2]/div[3]/div[1]/table[2]')

# %%
with open('print.png', 'wb')as f:
    f.write(driver.find_element_by_xpath(
        '/html/body/div/div/div[1]/div[2]/main/div[2]/div[3]/div[1]/table[1]/tbody/tr[2]/td/div/div/div/a/img').screenshot_as_png)


# driver.close()
# %%
df = pd.read_html(
    '<table>' + tabela.get_attribute('innerHTML') + '</table>')[0]
df.head()
df.to_csv('filmes_cage.csv', sep=';', index=False)
