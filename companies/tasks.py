from .models import CompaniesCar, CarFineStatus, CarHaveFinesStatus, CompaniesCarfine
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from tpass_parsers.celery import app
from django.core.cache import cache
from .services import get_passes, get_fines
import time
from django.db.models import Q
import os

@app.task
def parse_pass_all():
    proxy_host = str(os.environ.get('PROXY_PARSE_PASS_HOST', ''))
    proxy_port = int(os.environ.get('PROXY_PARSE_PASS_PORT', 1000))
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
    try:
        cars = CompaniesCar.objects.filter(need_check_passes=False).order_by('?')
        for car in cars:
            if car.licence_plate.strip() != '':
                nomer = car.licence_plate.strip()
                get_passes(driver=driver, nomer=nomer, car=car, type='all')
        driver.quit()
        time.sleep(10)
        return 'SUCCESS'
    except Exception as e:
        driver.quit()
        time.sleep(10)
        return 'ERROR: ' + str(e.args)

@app.task
def parse_pass_new():
    cars = CompaniesCar.objects.filter(need_check_passes=True).order_by('?')
    if not cars.exists():
        return '0 МАШИН'
    f_key = 'first_f_key_new_cars'
    if cache.get(f_key) == None:
        cache.add(f_key, '1')
        return 'ПЕРВЫЙ ЗАПУСК'
    lock_key = 'parsers_task_new'
    if cache.get(lock_key) != None:
        return 'ПРОЦЕСС УЖЕ ИДЕТ'
    if cache.add(lock_key, '1'):
        proxy_host = str(os.environ.get('PROXY_PARSE_PASS_HOST', ''))
        proxy_port = int(os.environ.get('PROXY_PARSE_PASS_PORT', 1000))
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

        driver = webdriver.Remote(command_executor='http://selenium-hub:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX, options=options)
        try:
            for car in cars:
                if car.licence_plate.strip() != '':
                    nomer = car.licence_plate.strip()
                    get_passes(driver=driver, nomer=nomer, car=car, type='new')
                car.need_check_passes = False
                car.save(update_fields=['need_check_passes'])
            cache.delete(lock_key)
            driver.quit()
            return 'SUCCESS'
        except Exception as e:
            cache.delete(lock_key)
            driver.quit()
            return 'ERROR: ' + str(e.args)
    else:
        return 'ДОСТУП ЗАПРЕЩЕН. ЗАДАЧА УЖЕ ВЫПОЛНЯЕТСЯ'


@app.task
def parse_fines_all():
    proxy_host = str(os.environ.get('PROXY_PARSE_PASS_HOST', ''))
    proxy_port = str(os.environ.get('PROXY_PARSE_PASS_PORT', 1000))
    cars = CompaniesCar.objects.filter(need_check_fines=False).order_by('?')
    try:
        for car in cars:
            if car.licence_plate.strip() != '' and car.ctc.strip() != '':
                nomer = car.licence_plate.strip()
                get_fines(car=car, proxy_host=proxy_host, proxy_port=proxy_port)
                car.need_check_fines = False
                car.save(update_fields=['need_check_fines'])
            else:
                car.have_fines = CarHaveFinesStatus.NONE
                car.need_check_fines = False
                car.save(update_fields=['need_check_fines', 'have_fines'])
        return 'SUCCESS'
    except Exception as e:
        return 'ERROR: ' + str(e.args)

@app.task
def parse_fines_new():
    proxy_host = str(os.environ.get('PROXY_PARSE_PASS_HOST', ''))
    proxy_port = str(os.environ.get('PROXY_PARSE_PASS_PORT', 1000))
    cars = CompaniesCar.objects.filter(need_check_fines=True).order_by('?')
    if not cars.exists():
        return '0 МАШИН'
    lock_key = 'parsers_task_new_fines'
    if cache.get(lock_key) != None:
        return 'ПРОЦЕСС УЖЕ ИДЕТ'
    if cache.add(lock_key, '1'):
        try:
            for car in cars:
                if car.licence_plate.strip() != '' and car.ctc.strip() != '':
                    nomer = car.licence_plate.strip()
                    print(nomer)
                    get_fines(car=car, proxy_host=proxy_host, proxy_port=proxy_port)
                    car.need_check_fines = False
                    car.save(update_fields=['need_check_fines'])
                else:
                    car.have_fines = CarHaveFinesStatus.NONE
                    car.need_check_fines = False
                    car.save(update_fields=['need_check_fines', 'have_fines'])
            cache.delete(lock_key)
            return 'SUCCESS'
        except Exception as e:
            cache.delete(lock_key)
            return 'ERROR: ' + str(e.args)
    else:
        return 'ДОСТУП ЗАПРЕЩЕН. ЗАДАЧА УЖЕ ВЫПОЛНЯЕТСЯ'
