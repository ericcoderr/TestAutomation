#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# read yaml file

import yaml
import json
import os
import glob
import codecs
import re
from src.common.constant import Field

class Yaml2JsonHelper:

    def __init__(self):
        pass

    def find_files(self,path,result,pattern):
#         result=[]
        if os.path.isdir(path):
            cwd = os.getcwd() #保存当前工作目录
            if path:
                os.chdir(path)

            for file_name in glob.glob(pattern):
                if os.path.isdir(file_name):
                    self.find_files(file_name,result,pattern) 
                else:
                    if os.path.splitext(file_name)[1]  == '.yaml': 
                        result.append(os.path.abspath(file_name))

            os.chdir(cwd)
        else:
            result.append(path)
        return result

    def yaml_2json(self,path):
        '''
        Read yaml from path,return dict
        '''
        result = None
        try:
            fr = codecs.open(path, 'r',Field.CHARSET_UTF8)
            result = yaml.load(fr)
            return result
        except IOError as e:
            print(e)
        finally:
            if fr is not None:
                fr.close()


    def yaml_2json_test_case(self,path):
        '''
        Read testcase yaml file
        '''
        case_dict=self.yaml_2json(path)
        #iterator case_dict
        test_cases=[]
        for(case_name,cases) in case_dict.items():
            scenarios_list=[]
            d={}
            scenarios_tmp=None

            # Only have Field.SCENARIOS_SUITES ,check app,setUp,tearDown
            if Field.SCENARIOS_SUITES in cases:
                scenarios_tmp=cases[Field.SCENARIOS_SUITES]
                if Field.APP in cases:
                    d[Field.APP]=cases[Field.APP]
                if Field.SET_UP in cases:
                    d[Field.SET_UP] = cases[Field.SET_UP]
                if Field.TEAR_DOWN in cases:
                    d[Field.TEAR_DOWN] = cases[Field.TEAR_DOWN]
                # if Field.APP_PACKAGE in cases:
                #     d[Field.APP_PACKAGE]=cases[Field.APP_PACKAGE]
                # if Field.APP_ACTIVITY in cases:
                #     d[Field.APP_ACTIVITY]=cases[Field.APP_ACTIVITY]
            else:
                scenarios_tmp=cases
            for scenarios in scenarios_tmp:
                scenarios_arr=str(scenarios).split('|')
                scenarios_dict=self.yaml_2json(self.get_path(path,'scenarios',scenarios_arr[0].strip().replace('.','/')+'.yaml'))
                dynmic_param=''
                if len(scenarios_arr)==3:
                    dynmic_param=scenarios_arr[2].strip()
                scenarios_list.append(self.scenarios(path,scenarios_arr[1].strip(),scenarios_dict[scenarios_arr[1].strip()],dynmic_param))

            d[Field.TESTCASE_NAME]= case_name.strip()
            d[Field.PACKAGE_NAME]=os.path.basename(path)
            d[Field.SCENARIOS_SUITES]= scenarios_list

            test_cases.append(d)
        return test_cases

    def  scenarios(self,path,scenarios_name,page_list,dynamic_param):
            page_step_list=[]
            for page_step in page_list:
                page_step_arr=str(page_step).split('|')
                page_step_dict=self.yaml_2json(self.get_path(path,'pages',page_step_arr[0].strip().replace('.','/')+'.yaml'))
                #join page,page is page filename
                page=page_step_dict[page_step_arr[1].strip()]
                #Replace dynamic var TODO :need optimize
                self.replace_param(dynamic_param,page)
                if Field.EXPECTATION in page:
                    page_expectation =page[Field.EXPECTATION]


                    # list
                    expectation_list=[]
                    if type(page_expectation)==list:
                        for page_expectation_tmp in page_expectation:
                            expectation={}
                            page_expectation_arr=str(page_expectation_tmp).split('|')
                            expectation[Field.VALUE]=page_expectation_arr[0].strip()
                            self.replace_param(dynamic_param,expectation)
                            if len(page_expectation_arr) ==2:
                                self.expectation_ext(page_expectation_arr[1],expectation,dynamic_param)
                            expectation_list.append(expectation)
                        page[Field.EXPECTATION]=expectation_list

                    else:# Single str
                        expectation={}
                        page_expectation_arr=str(page_expectation).split('|')
                        expectation[Field.VALUE]=page_expectation_arr[0].strip()
                        self.replace_param(dynamic_param,expectation)
                        if len(page_expectation_arr) ==2:
                            self.expectation_ext(page_expectation_arr[1],expectation,dynamic_param)
                        expectation_list.append(expectation)
                        page[Field.EXPECTATION]=expectation_list
                page.setdefault(Field.PAGE,page_step_arr[0])
                page_step_list.append(page)
            d={}
            d[Field.SCENARIOS_NAME]= scenarios_name
            d[Field.PAGE_STEPS]=page_step_list
            return d

    def expectation_ext(self,ext,dict,dynamic_param):
        if  ext.strip():
            ext_arr=ext.split(',')
            for ext_key_value in ext_arr:
                if  ext_key_value.strip():
                    params= ext_key_value.split('=')
                    if len(params)==2:
                        dict[params[0].strip()]=params[1].strip()
                        self.replace_param(dynamic_param,dict)

    def get_path(self,path,dirPath,file):
        '''
         get with version path ,e.g:Android v1.1
         path:
         dirPath:
         file:
         '''

        if os.path.basename(os.path.dirname(path)) == 'testcase':
            return os.path.abspath(os.path.join(os.path.dirname(path), os.pardir,dirPath,file))
        else:
            return os.path.abspath(os.path.join(os.path.dirname(path), os.pardir,os.pardir,dirPath,file))

    def json_2yaml(self,jsonStr,path):
        '''
         json convert yaml
        '''
        try:
            fr = open(path, 'w')
            yaml.dump(json.loads(jsonStr), fr)
        except Exception as e:
            print (e)
        finally:
            if fr is not None:
                fr.close()

    def replace_param(self,dynamic_param,page):
        if len(dynamic_param) >0:
            dynamic_param_arr = dynamic_param.split(',')
            for dynamic_param_temp in dynamic_param_arr:
                dynamic=dynamic_param_temp.split('=')
                for x,y in page.items():
                    if '$'+dynamic[0] == y:
                        page[x]=dynamic[1].replace(';',',')
