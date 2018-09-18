#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import os

class fileNames():

    def generateReportName(self,deviceType, svnVersion, caseName):
        now = time.strftime('%Y%m%d-%H%M', time.localtime(time.time()))
        reportFileName = now + "_" + svnVersion + "_" + deviceType + "_" + caseName + ".html"
        return reportFileName

    def generate_report_name_without_case(self,deviceType, svnVersion):
        now = time.strftime('%Y%m%d-%H%M', time.localtime(time.time()))
        reportFileName = now + "_" + svnVersion + "_" + deviceType  + ".html"
        return reportFileName

    def generateImageName(self,reprotFileName,case_method):
        reportFile = os.path.split(reprotFileName)
        reportPath = reportFile[0]
        reportName = reportFile[1]

        imagePath = reportPath + '/image/'
        imgFileName = imagePath + os.path.splitext(reportName)[0] + '_' + case_method +'.png'

        return imgFileName
