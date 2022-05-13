from .models import Company, Car, Pass
import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import zipfile
import json
from threading import Thread
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import random


def get_passes_old(driver, nomer, car, type):
    fin_result = None
    while True:
        try:
            ser = ''
            driver.get('https://transport.mos.ru/gruzoviki/reestr/')
            try:
                driver.find_element_by_xpath('//a[@class="cookies-close"]').click()
            except:
                pass
            iframe = driver.find_element_by_xpath('//div/iframe')
            driver.switch_to.frame(iframe)
            try:
                karti = driver.find_element_by_xpath('//img[@title="captcha"]')
            except:
                karti = ''
            try:
                sip_token = driver.find_element_by_xpath(
                    '//input[@id="sip_search__token"]').get_attribute('value')
            except:
                sip_token = ''
            karti.screenshot(nomer + ".png")
            files = {"file": open(nomer + ".png", "rb")}
            kuku = 0
            while (True):
                args = {"key": "9e760cab5ce862403499c82b017d324c"}
                data = requests.post('http://rucaptcha.com/in.php', files=files, data=args).text

                while (True):
                    zala = requests.get(
                        'http://rucaptcha.com/res.php?key=9e760cab5ce862403499c82b017d324c&action=get&id=%s' %
                        data.split('|')[1]).text
                    if ('OK' in zala):
                        kuku = 1
                        break
                    if (zala == 'ERROR_CAPTCHA_UNSOLVABLE'):
                        break
                if (kuku == 1):
                    break
            os.remove(nomer + ".png")
            otvet_ubil = zala.split('|')[1].strip()

            driver.find_element_by_xpath('//input[@id="sip_search_captcha"]').send_keys(otvet_ubil)
            driver.find_element_by_xpath('//input[@id="sip_search_grz"]').send_keys(nomer)
            likl = driver.find_element_by_xpath('//select/option')
            driver.execute_script("arguments[0].value = arguments[1]", likl, "")
            driver.find_element_by_xpath('//select/option').click()
            driver.find_element_by_xpath('//button[text()="Поиск"]').click()
            try:
                oshibka = driver.find_element_by_xpath('//div[@class="alert alert-danger"]').text
            except:
                oshibka = ''
                file_izm = open('res.html', 'w', encoding='utf-8')
                file_izm.write(driver.page_source)
                file_izm.close()
                spis = '},'.join(
                    driver.page_source.split('var data = ')[-1].split(';')[0].replace("'", '"').split(
                        '},')[:-1]) + '}]'
                try:
                    fin_result = json.loads(spis)
                except:
                    pass
            if (oshibka == ''):
                break
        except:
            pass
    if fin_result != None:
        pass_process(car, fin_result)
    return True


def get_passes_s(passes, host, port):
    proxy_host = str(host)
    proxy_port = int(port)
    options = webdriver.FirefoxOptions()

    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference("network.proxy.type", 1)
    firefox_profile.set_preference("network.proxy.http", proxy_host)
    firefox_profile.set_preference("network.proxy.http_port", proxy_port)
    firefox_profile.set_preference("network.proxy.ssl", proxy_host)
    firefox_profile.set_preference("network.proxy.ssl_port", proxy_port)
    firefox_profile.set_preference("network.proxy.socks", proxy_host)
    firefox_profile.set_preference("network.proxy.socks_port", proxy_port)
    firefox_profile.update_preferences()
    options.profile = firefox_profile

    driver = webdriver.Remote(command_executor='http://selenium-hub:4444/wd/hub',
                              desired_capabilities=DesiredCapabilities.FIREFOX, options=options)

    for pas in passes:
        print('\nSEARCH: ' + pas.name)
        fin_result = None
        while True:
            try:
                nomer = pas.name
                ser = ''
                driver.get('https://transport.mos.ru/gruzoviki/reestr/')
                try:
                    driver.find_element_by_xpath('//a[@class="cookies-close"]').click()
                except:
                    pass
                iframe = driver.find_element_by_xpath('//div/iframe')
                driver.switch_to.frame(iframe)
                try:
                    karti = driver.find_element_by_xpath('//img[@title="captcha"]')
                except:
                    karti = ''
                try:
                    sip_token = driver.find_element_by_xpath('//input[@id="sip_search__token"]').get_attribute('value')
                except:
                    sip_token = ''
                karti.screenshot(nomer + ".png")
                fl = open(nomer + ".png", "rb")
                files = {"file": fl}
                kuku = 0
                while (True):
                    args = {"key": "9e760cab5ce862403499c82b017d324c"}
                    data = requests.post('http://rucaptcha.com/in.php', files=files, data=args).text

                    while (True):
                        zala = requests.get(
                            'http://rucaptcha.com/res.php?key=9e760cab5ce862403499c82b017d324c&action=get&id=%s' %
                            data.split('|')[1]).text
                        if ('OK' in zala):
                            kuku = 1
                            break
                        if (zala == 'ERROR_CAPTCHA_UNSOLVABLE'):
                            break
                    if (kuku == 1):
                        break
                fl.close()
                try:
                    os.remove(nomer + ".png")
                except:
                    pass
                otvet_ubil = zala.split('|')[1].strip()

                driver.find_element_by_xpath('//input[@id="sip_search_captcha"]').send_keys(otvet_ubil)
                driver.find_element_by_xpath('//input[@id="sip_search_number"]').send_keys(nomer)
                likl = driver.find_element_by_xpath('//select/option')
                driver.execute_script("arguments[0].value = arguments[1]", likl, "БА")
                driver.find_element_by_xpath('//select/option').click()
                driver.find_element_by_xpath('//button[text()="Поиск"]').click()
                try:
                    oshibka = driver.find_element_by_xpath('//div[@class="alert alert-danger"]').text
                except:
                    oshibka = ''
                    file_izm = open('res.html', 'w', encoding='utf-8')
                    file_izm.write(driver.page_source)
                    file_izm.close()
                    spis = '},'.join(
                        driver.page_source.split('var data = ')[-1].split(';')[0].replace("'", '"').split('},')[
                        :-1]) + '}]'
                    try:
                        fin_result = json.loads(spis)
                    except:
                        pass
                if (oshibka == ''):
                    break
            except Exception as e:
                print(e)
                pass
        if fin_result != None:
            print('--------FIN RES START--------')
            print(fin_result)
            print('--------FIN  RES  END--------')
            if len(fin_result) > 0:
                Car.objects.get_or_create(licence_plate=fin_result[0].get('grz').upper())
                print('GRZ: ' + fin_result[0].get('grz').upper())
                pas.ready = True
                pas.save()


def search():
    hosts = ['45.145.88.150', '212.192.228.28', '109.94.210.138', '92.249.12.223', '45.150.61.128', '195.19.169.90',
             '195.208.89.103', '195.208.92.20']
    ports = [51343, 55133, 54781, 51612, 52709, 46559, 57777, 53702]
    passes = Pass.objects.filter(ready=False)
    for i in range(32):
        ri = random.randint(0, 7)
        a_count = passes.count()
        count = int(a_count / 32) - 1
        th = Thread(target=get_passes_s, args=(passes[i * count:(i * count) + count], hosts[ri], ports[ri],))
        th.start()
