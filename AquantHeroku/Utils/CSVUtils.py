import random
import time


class CSVUtils:

    @staticmethod
    def getQueryValuesFromCSV(csvData):
        valueArr = []
        rowCounter = 0
        headers = []
        for row in csvData:
            if rowCounter != 0:
                value = CSVUtils.parseValuesFromRow(headers,row)
                valueArr.append(value)
            else:
                headers = row
            rowCounter += 1
        return valueArr

    @staticmethod
    def parseValuesFromRow(headers, row):
        rowDic = {}
        rowCounter = 0
        for title in headers:
            val = row[rowCounter]
            rowDic.update({title: val})
            rowCounter += 1

        if 'AquantID' not in headers:
            rowDic['AquantID'] = CSVUtils.calculateAquantID()
        rowDic['CreatedDate'] = time.strftime('%Y-%m-%d %H:%M:%S')
        rowDic['LastModified'] = time.strftime('%Y-%m-%d %H:%M:%S')
        return rowDic

    @staticmethod
    def calculateAquantID():
        return random.randrange(0, 10000001, 2)



