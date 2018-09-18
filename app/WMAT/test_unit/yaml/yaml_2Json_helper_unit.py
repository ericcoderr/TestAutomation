import sys
sys.path.append('D:\\TestAutomation\\WMAT\\')

from src.helper import yaml_2json_helper

import unittest
import os
import json


class Yaml2JsonHelperUnit(unittest.TestCase):

    def test_yaml_2json_scenarios(self):
        yaml_helper = yaml_2json_helper.Yaml2JsonHelper()
        path=os.path.abspath('../../../TestCase/Template/')
        yaml_helper.yaml_2json_test_case(path+"/Android v1.1/testcase/LoginTestCase.yaml")

    def test_get_version_path(self):
        ss='D:\TestAutomation\TestCase/'
        path =os.path.join(ss,'/a.txt')
        print(path)

    def test_utf8(self):
        yaml_helper = yaml_2json_helper.Yaml2JsonHelper()
        path='D:\\TestAutomation\\WMAT\\test_unit\\yaml\\test.yaml'
        print(yaml_helper.yaml_2json(path))

if __name__ == '__main__':
    unittest.main()


