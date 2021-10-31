from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
my_url='https://www.imdb.com/search/title?count=100&groups=oscar_best_picture_winners&sort=year,desc&ref_=nv_ch_osc'

#opening up connection,grabbing the page
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()

#html parsing
page_soup= soup(page_html,"html.parser")

#grabs each product
containers=page_soup.findAll("div",{"class":"lister-item mode-advanced"})


filename= "imdb.csv"
f= open(filename, "w")


headers= "name , ratings , Duration\n"

f.write(headers)


for container in containers:
   name=container.a.img["alt"]                                     #grabs name of the movie
   title_container=container.findAll("span",{"class":"value"})
   ratings=title_container[0].text                                   #grabs ratings of movie

   Runtime=container.findAll("span",{"class":"runtime"})  
   Duration=Runtime[0].text                                             #grabs the duration of movie

   print("name: " + name)
   print("ratings: " + ratings)
   print("Duration: " + Duration)


   f.write(name + "," + ratings + "," + Duration + "\n")
      
f.close()   


