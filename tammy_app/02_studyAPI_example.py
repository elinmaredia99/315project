#This API will allow us to implement a "study" feature into our tamagotchi. You will give it a topic you want to learn about
#and it will return a link to a free online book you can read 


import requests
import json

from urllib import request

bookISBN = "0451526538"
#this is the ISBN for tom sawyer. This will work for any book ISBN 
#Need to add functionallity to find a book ISBN from a key word, aka "Tammy, I want to read Tom Sawyer", "Tammy, I want to learn about the Linux Shell" 



resp = request.urlopen("https://openlibrary.org/api/books?bibkeys=ISBN:" + bookISBN)


data = resp.read()
html = data.decode("UTF-8")

#parse this string
#returns URL to book
print (html.split(" ")[11])