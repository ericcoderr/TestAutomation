#!/usr/bin/env python
# -*- coding: UTF-8 -*-
class Script:

    @staticmethod
    def get_attr(script_name):
        splitStr = script_name.split(".", -2)
        length = len(splitStr)
        for index in range(len(splitStr)):
            if index == length - 1:
                method_name = splitStr[index]
            elif index == length - 2:
                class_name = splitStr[index]
            elif index == 0:
                module_name = splitStr[index]
            else:
                module_name = module_name + '.' + splitStr[index]

        module = __import__(module_name,{},{},[class_name])  # import module
        clz = getattr(module, class_name)
        obj = clz()  # new class
        mtd = getattr(obj, method_name)
        return mtd

