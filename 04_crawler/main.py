# %%
from selenium import webdriver
import sys
import time

# %%
cep = sys.argv[1]

if cep:
    # %%
    driver = webdriver.Chrome('/home/adenilson/Engineering/chromedriver')

    # %%
    # driver.get('https://www.howedu.com.br')
    # driver.find_element_by_xpath(
    #    '//*[@id="PopupSignupForm_0"]/div[2]/div[1]').click()
    # driver.find_element_by_xpath(
    #    '/html/body/section[4]/div/div/div[2]/a').click()

    # %%
    cep = '80420130'
    # %%
    driver.get('https://buscacepinter.correios.com.br/app/endereco/index.php')
    elem_cep = driver.find_element_by_name('endereco')
    elem_cep.clear()
    elem_cep.send_keys(cep)

    # %%
    elem_cmb = driver.find_element_by_name('tipoCEP')
    elem_cmb.click()
    driver.find_element_by_xpath(
        '//*[@id="formulario"]/div[2]/div/div[2]/select/option[6]').click()
    # %%
    driver.find_element_by_id('btn_pesquisar').click()
    # %%
    time.sleep(0.5)
    logradouro = driver.find_element_by_xpath(
        '/html/body/main/form/div[1]/div[2]/div/div[3]/table/tbody/tr/td[1]').text
    bairro = driver.find_element_by_xpath(
        '/html/body/main/form/div[1]/div[2]/div/div[3]/table/tbody/tr/td[2]').text
    localidade = driver.find_element_by_xpath(
        '/html/body/main/form/div[1]/div[2]/div/div[3]/table/tbody/tr/td[3]').text

    # %%
    print(f"""
        Para o cep {cep}:
        Endereço: {logradouro}
        Bairro: {bairro}
        Localidade: {localidade}
        
    """)
