import requests #Fetches data from websites
from bs4 import BeautifulSoup #Extracts the data 
import pandas as pd #stores data in csv or excel format
currentPage = 1
data = []
proceed = True

while(proceed):
    source = requests.get("https://quotes.toscrape.com/page/"+str(currentPage)+"/").text

    soup = BeautifulSoup(source, "html.parser")


    endOfQuotes = soup.find("div", class_="col-md-8").text


    if currentPage > 10:
        proceed = False
    else:

        #quoteBlock is the class that contians both the quote and the author's name
        #quote gets appended first and then author's name. This process gets looped untill all quotes and author names get appeneded
         quoteBlock = soup.find_all("div", class_="quote")
         for quote in quoteBlock:
            item = {}
            item["Quote"] = quote.find("span").text
            item["Author"] = quote.find("small", class_="author").text
            data.append(item)

            
            # #quote var is storing the quote text
             #quote = quoteBlock.span.text

            # #the first thing to append to the file is the quote.
            # with open("source.txt", "a", encoding='utf-8') as f:
            #     print(file=f) #Prints empty lines before quote
            #     print(quote, file=f)
        
            # #author var stores the author's name            
             #author = quoteBlock.find("small", class_="author").text

            # #author's name gets appeneded right after the quote gets appeneded
            # with open("source.txt", "a", encoding='utf-8') as f:
            #     print(author, file=f)

            
    currentPage += 1
    print("Current Page Number: ", currentPage)
    #proceed = False
df = pd.DataFrame(data)
#df.to_json("quotes.json")
df.to_excel("quotes.xlsx")
#print(soup.title.text)

print("End Of Program.")