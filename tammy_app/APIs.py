from py_edamam import Edamam
from py_edamam import exceptions
import json
import re
from urllib import request

class NutritionAPI:
	interface = Edamam(nutrition_appid='6f9dc22f',
        nutrition_appkey='393b148cf6906ab330cc9a6ae559aec8',
        recipes_appid='b5be6d40',
        recipes_appkey='fa40ec68961d0a99e2fb9c90513866a0',
        food_appid='c5e6101e',
        food_appkey='4b63317314060fc3252a2dc4ef4fcb7c')

	@staticmethod
	def submit(food):
		try:
			return NutritionAPI.interface.search_nutrient(food)
		except exceptions.LowQualityQuery:
			print("Query failed, please refine your query")

class StudyAPI:

	# Example code
	# 	s1 = subject("math",0)
	# 	s1.displayInfo()
	# 	s1.incrementTimeSpent(30)
	# 	s1.displayInfo()
	# 	s1.getBookInfo(bookISBN)

	class subject:
		name = "default subject name"
		timeSpent = 0

		def __init__(self, givenName, givenTimeSpent):
			self.name = givenName
			self.timeSpent = givenTimeSpent

		def incrementTimeSpent(self, incrementAmount):
			self.timeSpent = (self.timeSpent + incrementAmount)

		def displayInfo(self):
			print("Time spent on " + self.name + ": " + str(self.timeSpent))

		# def getISBN(subject)
			#gets the ISBN of a book about this subject

		def getBookInfo(self, ISBN):
			#returns:
			# 	->author 
			#	->Title
			#	-># of pages
			#	->date of publication 
			resp = request.urlopen("https://openlibrary.org/api/books?bibkeys=ISBN:" + ISBN + "&jscmd=data&format=json")
			data = resp.read()
			html = data.decode("UTF-8")

			v = html.find("subject_places")
			w = html.find("publish_date")	
			x = html.find("authors")
			y = html.find("title")
			z = html.find("number_of_pages")

			print("title:" + html[y+9:y+37])
			print("author:" + html[x+83:x+93])
			print("subject places:" + html[v+175:v+192])
			print("publish date:" + html[w+16:w+20])
			print("number of pages:" + html[z+18:z+21])

	@staticmethod
	def completedBook(ISBN):
		resp = request.urlopen("https://openlibrary.org/api/books?bibkeys=ISBN:" + ISBN + "&jscmd=data&format=json")
		data = resp.read()
		html = data.decode("UTF-8")
		z = html.find("number_of_pages")
		if (z == -1):	# Page count not found, abort
			return None

		z += 18
		start = z

		# Scan to end of the number
		while (html[z] != ','):
			z += 1

		# returns number of pages in book
		return html[start:z]

		