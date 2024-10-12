import requests

#the main function
def scrape(url, keyword):
    #get the data form the url
    response = requests.get(url)
    #make sure it's a successfull request
    if response.status_code != 200:
        print(response)
        print("request FAILED! The server/site directory doesn't exist or doesn't want you.")
    else:
        print(response)
        #if it is, look for keyword
        if keyw in (response.text).lower():
           #if all goes well, HTML source code is printed
           print('success!')
           print(response.text)
        else:
           print('Does not include keyword :(')



#ask for URL and keyword
url = input('Enter ONE url, support for more coming soon\n')
keyw = input('Enter a keyword to search for\n')

#check that the idiot added http(s)

if ("http" and "://") in url:
    scrape(url, keyw)
else:
    url = "http://" + url
    scrape(url, keyw)



