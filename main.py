import requests #Fetches data from websites
from bs4 import BeautifulSoup #Extracts the data 
import pandas as pd #stores data in csv or excel format
import pickle

# 
def scraper():

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


            quoteBlock = soup.find_all("div", class_="quote")
            for quote in quoteBlock:
                item = {}
                quoteText = quote.find("span", class_="text").text
                authorName = quote.find("small", class_="author").text
                print(quoteText)
                item["Quote"] = quoteText
                item["Author"] = authorName
                data.append(item)

                
        currentPage += 1
        print("Current Page Number: ", currentPage)
        proceed = False

    df = pd.DataFrame(data)

    f=open('data.txt','wb')  #opened the file in write and binary mode 
    pickle.dump(df,f) #dumping the content in the variable 'df' into the file in hex
    f.close() #closing the file

scraper()

# with open("source.txt", "a", encoding='utf-8') as f:
#     print(df, file=f)



def openDf():
    f=open('data.txt','rb') #opening the file to read the data in the binary form
    newdf = pickle.load(f)
    return newdf

openDf()

def SaveAsText():
    with open("source.txt", "a", encoding='utf-8') as f:

        testdf = openDf()
        quotes = list(testdf["Quote"])
        authors = list(testdf["Author"])
        for i in range(len(quotes)):
            print(authors[i], file=f)
            print(quotes[i], file=f)
            print("",file=f)
        
        #print(list(openDf()["Author"]), file=f)

SaveAsText()
        

print("End Of Program.")