import requests
import html2text
#the main function
def scrape(url, keyword):
    #get the data form the url
    urlc = 0
    for string in url:
        response = requests.get(url[urlc])
        #make sure it's a successfull request
        if response.status_code != 200:
            print(response)
            print("request FAILED! The server/site directory doesn't exist or doesn't want you etc.")
        else:
            print(response)
            #if it is, look for keyword
            if keyw in (response.text).lower():
                #if all goes well, HTML source code is printed
                print('success!')
                print(response.text)
                print(cleantext(response.text))
            else:
                print('Does not include keyword :(')
            urlc += 1
def cleantext(content):
    htmlcontent = content
    text_maker = html2text.HTML2Text()
    text = text_maker.handle(htmlcontent)
    return text


#ask for URL and keyword
url = input('Enter your URL(s)\n')
url = url.split()
keyw = input('Enter a keyword to search for\n')

#check that the idiot added http(s)
urld = 0
for string in url:
    if ("http" and "://") not in url[urld]:
        url[urld] = "http://" + url[urld]
    urld += 1
scrape(url, keyw)



