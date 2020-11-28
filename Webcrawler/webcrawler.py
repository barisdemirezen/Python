import bs4 as bs
import urllib.request
import requests
import re

def bracket_remover(text):
    pattern = r'\[.*?\]'
    paragraph = re.sub(pattern, '', text)
    print(paragraph)

def wikipedia():
    search = input("Please input your wikipedia search string\n")
    url = "https://en.wikipedia.org/wiki/" + str(search)
    url = url.replace(' ','%20')
    if (requests.get(url)).status_code == 200:
        source = urllib.request.urlopen(url).read()
        soup = bs.BeautifulSoup(source,'html.parser')
        print((soup.find(id="firstHeading")).text)
        tags = soup.find_all('p',attrs={'class':None})
        if len(tags)>=2:
            for a in range(2):
                if tags[a]!=None:
                    paragraph = tags[a].text
                    bracket_remover(paragraph)
                else:
                    continue
        elif len(tags)==1:
            paragraph = tags[0].text
            bracket_remover(paragraph)       
    else:
        print("Cannot find results in wikipedia.")
    main()
    
def weather():
    location = input("Please input your weather search location\nInput empty for automatic location[may be wrong!]\n")
    url= "https://www.bing.com/search?q="+str(location)+"%20hava%20durumu"
    url = url.replace(' ','%20')
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source,'html.parser') 
    if soup.find('div',attrs={'class':'wtr_locTitle wtr_nowrap wtr_ellipses'}) != None:
        print(soup.find('div',attrs={'class':'wtr_locTitle wtr_nowrap wtr_ellipses'}).text +" forecast for right now "+ soup.find('div',attrs={'class':'wtr_caption'}).text + " " + soup.find('div',attrs={'class':'wtr_currTemp b_focusTextLarge'}).text + " degree")
    else:
        print("Cant find location.")
    main()

def searchProduct():
    productName = input("Please enter your word to search. We will find cheapest in web ( dont use turkish characters[ç,ğ,ı,ö,ş,ü]:\n")    
    url= "https://www.cimri.com/arama?q="+str(productName)
    url = url.replace(' ','%20')
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source,'html.parser') 
    product =soup.find_all('h3',attrs={'class':'product-title'})
    if len(product)!=0:
        productprice=soup.find_all('a',attrs={'s14oa9nh-0 fFCyge'})
        print(product[0].text+"\n")
        print(productprice[0].text)
    else:
        print("Cant find product")
    main()
      
def main():
    print("\n\nWelcome to webcrawler. Here is a menu for options:\nPlease dont use turkish characters in anyprocess[ç,ğ,ı,ö,ş,ü]\n"
      "0-Exit\n1-wikipedia\n2-weather\n3-Search cheapest product\nPlease input index of process to begin")
    process = input("")
    if process=='0':
        exit()
    elif process=='1':
        wikipedia()
    elif process == '2':
        weather()
    elif process == '3':
        searchProduct()
    else:
        print('Unexpected input. Please try again.\n')
        main()

main()


