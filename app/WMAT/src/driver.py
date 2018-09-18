#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from src.helper.yaml_2json_helper import Yaml2JsonHelper
import threading
from appium import webdriver
from src.common.constant import Field

class MyDriver:
    mutex = threading.Lock()

    @staticmethod
    def get_devices(path,device_list):
        yaml_2json_helper = Yaml2JsonHelper()
        desired_caps = yaml_2json_helper.yaml_2json(path)
        if not None and len(device_list)>0:
            device_arr=device_list.split(',')
        else:
            device_arr=desired_caps[Field.ACTIVE].split(',')
        devices=desired_caps[Field.DEVICES]
        device_list=[]
        for device in device_arr:
            if device in devices:
                device_list.append(devices[device])
        return device_list

    @staticmethod
    def get_driver(desired_caps):
        url=desired_caps[Field.URL]
        desired_caps.pop(Field.URL)
        desired_caps['autoAcceptAlerts']='true'
        driver=webdriver.Remote(url,desired_caps)
        return driver

    @staticmethod
    def get_platform(driver):
        return driver.desired_capabilities[Field.PLATFROM_NAME]

    @staticmethod
    def is_ios(driver):
        return "ios" == MyDriver.get_platform(driver)
