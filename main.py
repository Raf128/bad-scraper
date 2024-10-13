#Modules that are required
#Requests and html2text must be installed
import requests
import html2text
import sys

#the main function, gets contents of page
def scrape(url, keyword):
    #get the data form the url
    urlc = 0
    for string in url:
        response = requests.get(url[urlc])
        #make sure it's a successfull request
        if response.status_code != 200:
            print(response)
            print("request FAILED! The server/site directory doesn't exist or doesn't want you etc.")
            return "failed, connection error"
        else:
            print(response)
            #if it is, look for keyword
            if keyw in (response.text).lower():
                #if all goes well, HTML source code is obtained
                print('success!')
                return response.text
            else:
                #if not, it will simply state that it failed
                print('Does not include keyword :(')
                return "failed, site does not inclue keyword"
            urlc += 1

#HTML cleaner function, turns html source into what the page would generally look like in a browser
def cleantext(content):
    htmlcontent = content
    text_maker = html2text.HTML2Text()
    text = text_maker.handle(htmlcontent)
    return text


#ask for URL and keyword (this is stupid)
url = input('Enter your URL(s)\n')
url = url.split()
keyw = input('Enter a keyword to search for (leave blank for no keyword)\n')

#check that the idiot added http(s)
urld = 0
for string in url:
    if ("http" and "://") not in url[urld]:
        url[urld] = "http://" + url[urld]
    urld += 1


html = scrape(url, keyw)
cleaned = cleantext(html)

#ask if they want terminal output
show = input("Print HTML source? y/n\n").lower()
show2 = input("Print cleaned text? y/n\n").lower()
if show == "y":
    print(html)
if show2 == "y":
    print(cleaned)

# export data to file for data extraction
print('Exported to data.txt')
sys.stdout = open('data.txt', 'wt')
print(html)
print(cleaned)
