import requests #Fetches data from websites
from bs4 import BeautifulSoup #Extracts the data 
import pandas as pd #stores data in csv or excel format
import textwrap




#There are a total of 10 pages in the website I want to Scrape. To Scrape all the quotes and author names I need to speiciy in my code that im starting from page 1 and stoping at page 10.
#It would be much better if I were to stop when the page has no info or breaks because it does not exist, but am not sure how to impment this for now.
currentPage = 1
data = []
proceed = True

while(proceed):
    source = requests.get("https://quotes.toscrape.com/page/"+str(currentPage)+"/").text

    soup = BeautifulSoup(source, "html.parser")



    if currentPage > 10:
         #Uncomment line 47 if you dont want to print all 10 pages. It will only print the first page. This is useful for troubleshooting. 
        proceed = False
    else:

        #Storing all the data from an HTML div with a class named "quote" because the div contains quotes and the author's name.
        #soup.find_all finds all the divs with a class named "quote" for that page.
        #I then loop through each individual quoteBlock and assign them to a variable called "quoteInfo."
        # Then I create an empty dictionary called "item," which will eventually store quotes and author names. 
        #Then I take quoteInfo and extract the quote's text and quote's author into their respective variables "quoteText" and "authorName."
        #Then I create two keys called "Quote" and "Author" and store extracted data in their respective keys.  
        # Finally, the "item" dictionary, which now contains both the quoted text and the author's name, is appended to the data list. This list accumulates all quotes and their authors on the page.
         quoteBlock = soup.find_all("div", class_="quote")
         for quoteInfo in quoteBlock:
            item = {} 
            quoteText = quoteInfo.find("span", class_="text").text
            authorName = quoteInfo.find("small", class_="author").text
            item["Quote"] = quoteText
            item["Author"] = authorName
            data.append(item)

            
    currentPage += 1
    print("Current Page Number: ", currentPage)

    #proceed = False 


#Storing all the data from the item dictionary into a pandas data frame
df = pd.DataFrame(data)
pd.options.display.max_colwidth = None


while True:

    print("\n")
    print("================================================================")
    print("                        Data Options")
    print("1. Console")
    print("2. Exel")
    print("3. JSON")
    print("4. TXT")
    print("5. Exit Menu")
    print("================================================================")
    print("\n")

    menu = input("Where would you like the data to be stored/displayed? ")
    print("\n")
    
    match menu:
        case "1":
             for index, row in df.iterrows():
                quote = textwrap.fill(row["Quote"], width=80)
                author = textwrap.fill(row["Author"], width=80)
                print(quote + " - " + author + "\n")
        case "2": 
            df.to_excel("quotes.xlsx")
            print("Succesfully stored data as a .xlsx file!")

        case "3":
            df.to_json("quotes.json")
            print("Succesfully stored data as a .json file!")

        case "4":
             with open("source.txt", "a", encoding='utf-8') as f:
                #df.iterrows has the index and row data for rach row in the dataframe. I am iterating through each index that has a row for quotes and author name.For each itereation I am prining the quote and author namee from the current index. 

                #For example in index 0 you have a row called quote and it stores this quote  "To be or not to be". In the next row you have a row called "Author" and it contains the author's name "Shakespeare". Then both qoute and author gets printed and you move on to the next index and the same process as index 0 happens untill all qoutes and authors have been printed.
                for index, row in df.iterrows():
                    print(row["Quote"] + " - " + row["Author"], file=f)
                    print("\n", file=f)
                print("Succesfully stored data as a .txt file!")

        case "5":
            print("Exiting Menu...")
            break
        case _:
            print("Invalid option. Please try again.")
            
print("End Of Program.")