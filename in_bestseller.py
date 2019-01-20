import requests
from bs4 import BeautifulSoup
import csv
book=[]
for pgNo in range(1,6):
	url="https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_{}?ie=UTF8&pg={}".format(pgNo,pgNo)
	page = requests.get(url)
	soup=BeautifulSoup(page.content,'html.parser')
	soup1=soup.find("div",{"id":"zg_centerListWrapper"}).find_all("div",{"class":"zg_itemImmersion"})
	temp=[]
	soup1=list(soup1)
	for i in soup1:
		try:
			book_name=(i.find("div",{"class":"p13n-sc-truncate p13n-sc-line-clamp-1"}).text).strip()	 
		except:
	 		book_name = "Not available"
		try:
	 		book_url="https://www.amazon.in"+(i.find("a",{"class":"a-link-normal"}))['href']
		except:
			book_url = "Not available"
		try:
			book_author=i.find("div",{"class":"a-row a-size-small"}).text
		except:
	 		book_author="Not available"
		try:
	 		book_price="Rs "+(i.find("span",{"class":"p13n-sc-price"}).text).strip()
		except:
	 		book_price="Not available"
		try:
	 		book_noOfRatings=i.find("a",{"class":"a-size-small a-link-normal"}).text
		except:
	 		book_noOfRatings="Not available"
		try:
	 		j=i.find("div",{"class":"a-icon-row a-spacing-none"})
	 		book_AverageRating=(j.find("a",{"class":"a-link-normal"}))['title']
		except:
	 		book_AverageRating="Not available"
		temp=[book_name,book_url,book_author,book_price,book_noOfRatings,book_AverageRating]
		book.append(temp)

field=["Name","URL","Author","Price","Number of Ratings","Average Rating"]
with open("./output/in_book.csv","w") as f:
	writer = csv.writer(f)
	writer.writerow({x: x for x in field})
	for i in book:
		writer.writerow(i)
    