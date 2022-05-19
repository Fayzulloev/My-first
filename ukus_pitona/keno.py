from bs4 import BeautifulSoup


with open("http://abdur.cc/newKeno/") as file:
    src = file.read()
#print(src)

soup = BeautifulSoup(src, "lxml")

title = soup.title
print(title)