import requests
#ask for URL
url = input('Enter ONE url starting with http(s)://, support for more coming soon\n')
#ask for their desired keyword to search for
keyw = input('Enter a keyword to search for\n')
#get the data form the url
response = requests.get(url)

print(response)
#make sure it's a success
if response.status_code != 200:
    print("request FAILED! The server probably doesn't want you scanning.")
else:
    #if it is, look for keyword
    if keyw in response.text:
        #if all goes well, source code is printed
        print('success!')
        print(response.text)
    else:
        print('Does not include keyword :(')
