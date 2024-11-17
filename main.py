#Modules that are required
#Requests and html2text must be installed
try:
    import requests
    import html2text
    import json
    import os
except Exception as e:
    depend = input(e, 'Dependencies are not installed, download?\n')
    if depend.lower() == 'y':
        try:
            os.system('pip install requests && pip install html2text')
            import requests
            import html2text
            import json
            import os
        except Exception as e:
            print('Error installing dependencies:', e)
            exit(2)
    else:
        exit(1)



#the main function, gets contents of page
def scrape(url, keyword):
    response = requests.get(url[i])
    #make sure it's a successfull request
    #I could probably do this better
    if response.status_code != 200:
        if response.status_code == 404:
            print("404 not found")
        elif response.status_code == 403:
            print("403 forbidden")
        else:
            if "5" in str(response.status_code):
                print("Server Error")
            elif "3" in str(response.status_code):
                print("Multiple Choices")
            print("Error", response.status_code)
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
            return "failed, site does not include keyword"

#HTML cleaner function, turns html source into what the page would generally look like in a browser
def cleantext(content):
    htmlcontent = content
    text_maker = html2text.HTML2Text()
    text = text_maker.handle(htmlcontent)
    return text


#ask for URL and keyword
url = input('Enter your URL(s)\n')
url = url.split()
keyw = input('Enter a keyword to search for (leave blank for no keyword)\n')

#check that the idiot added http(s)

for i, string in enumerate(url):
    if ("http" and "://") not in url[i]:
        url[i] = "http://" + url[i]

# big ugly loop (not actually that bad, i just don't like loops)
for i, string in enumerate(url):
    html = scrape(url, keyw)
    cleaned = cleantext(html)
    if "failed" in html:
        print(html)
    else:
        #ask if they want terminal output
        show = input("Print HTML source? y/n\n").lower()
        show2 = input("Print cleaned text? y/n\n").lower()
        if show == "y":
            print(html)
        if show2 == "y":
            print(cleaned)
    # export data to file for data extraction
    with open('data.txt', 'a') as f:
        f.write(str(html))
        f.write(cleaned)
        f.close()
    print('Exported to data.txt\n')
