import bs4, requests, webbrowser
url = input()
response = requests.get(url)
html = response.content
code = bs4.BeautifulSoup(html, 'html.parser')
links = code.findAll('a')
list = []
for link in links:
    link = link.get('href')
    if link.startswith('https://one.akwam.cz/episode'):
        if link not in list:
            list.append(link)        
newlist = []
for link in list:
    response = requests.get(link)
    html = response.content
    code = bs4.BeautifulSoup(html, 'html.parser')
    newlinks = code.findAll('a')
    for newlink in newlinks:
        newlink = newlink.get('href')
        if newlink.startswith('http://re.akwam.news/link'):
           if newlink not in newlist:
               newlist.append(newlink)
flist = []
for i in newlist:
    flist.append(i)

fflist = []
list = []
for link in flist:
    response = requests.get(link)
    html = response.content
    code = bs4.BeautifulSoup(html, 'html.parser')
    newlinks = code.findAll('a')
    for newlink in newlinks:
        newlink = newlink.get('href')
        if newlink.startswith('https://akwam.to/download'):
           if newlink not in fflist:
               fflist.append(newlink)
list = []
for link in fflist:
    response = requests.get(link)
    html = response.content
    code = bs4.BeautifulSoup(html, 'html.parser')
    newlinks = code.findAll('a')
    for newlink in newlinks:
        newlink = newlink.get('href')
        if newlink.startswith('https://s'):
           if newlink not in list:
               list.append(newlink)

for i in list:
    print(i)
print(len(list))



    