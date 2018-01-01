# -*- coding: utf-8 -*-
import xlwt
import xlrd
import csv
import numpy as np
from collections import OrderedDict

CONST_SOURCE = 'İZMİR'
CITY_COUNT = 81

def calcDist(distMat, cityList, source, destination):
	source = source.decode("utf-8")
	if source not in cityList:
		return
	
	print source + ' is source city and destination is set to ' + destination
	
	distanceDict = OrderedDict()
	parentDict = OrderedDict()
	path = []
	
	distanceDict.update({source: 0})
	
	#Create Dictionary of distances
	for city in cityList:
		if city != source:
			distanceDict.update({city: float('inf')})
	
	for i in range (0, CITY_COUNT):
		for key,val in distanceDict.iteritems():
						
			if val != float('inf'):
				edgeList = np.nonzero(distMat[cityList.index(key)])[0]
				
				for edge in edgeList:
					city = cityList[edge]
					dist = distMat[cityList.index(key)][edge]
			
					if distanceDict[city] == float('inf'):
						distanceDict[city] = dist+ val
						parentDict[city] = key
					else:
						temp = distanceDict[city]
						distanceDict[city] = min(distanceDict[city], (val + dist))
						if temp != distanceDict[city]:
							parentDict[city] = key
							
	temp = parentDict[destination]
	while temp != source:
		path.append(temp)
		temp = parentDict[temp]
	path.append(source)
	
	print '\nShortest distance is: ' + str(distanceDict[destination]) + 'km'
	print '\nPath is as follows:'
	
	for city in reversed(path):
		print city + '->',
	print destination	 
	

	
	
	
						

def main():
	row, col = CITY_COUNT, CITY_COUNT;
	distMat = [[0 for x in range(row)] for y in range(col)]
	neighbors = [[0 for x in range(row)] for y in range(col)]

	#Creating neighbor matrix
	edgeFile = csv.reader(open("edges.csv"))
	row, col = 0,0;
	for city in edgeFile:
		for edge in city:
			neighbors[row][col] = edge
			col = col + 1
		row = row + 1
		col = 0


	distancesWorkBook = xlrd.open_workbook('city_distance.xls',encoding_override= 'cp1252')
	distanceSheet = distancesWorkBook.sheet_by_index(0);

	cityList = []



	#Creating city list
	for count in range (0, CITY_COUNT):
		cityList.append(distanceSheet.cell(2,count+2).value)

	#Creating distance matrix
	for row in range (0, CITY_COUNT):
		for col in range (0, CITY_COUNT):
			distMat[row][col] = distanceSheet.cell(row+3,col+2).value
			if row == col: distMat[row][col] = 0

	for row in range (0, CITY_COUNT):
		for col in range (0, CITY_COUNT):
			distMat[row][col] = distMat[row][col] * int(neighbors[row][col])
	
	
	#Getting destination city
	print 'Please use uppercase Turkısh letters'
	select = raw_input('Input destination:')
	cityDecoded = select.decode("utf-8")
	source = CONST_SOURCE.decode("utf-8")
	#Checking if destination city is valid
	if ( cityDecoded not in cityList):
		print 'Destination is not valid'

	elif cityDecoded != source:
		calcDist(distMat, cityList, CONST_SOURCE, cityDecoded)
	else:
		print 'Destination choosen as source city'


if __name__ == "__main__":
	main()
	

