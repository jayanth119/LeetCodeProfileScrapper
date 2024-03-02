import requests
import re
import bs4

url = "https://leetcode.com/DevOgabek/"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad responses
    pattern1= r'<title>(.*?)</title>'
    html_content = response.text
    soup = bs4.BeautifulSoup(html_content, "html.parser")
    ## finding all img tags
    img = soup.find_all("img")[0]
    match = re.search(pattern1, html_content)
    if match:
      title_content = match.group(1)
      print("title" , title_content)
    else:
      print("No match found.")
      print(type(html_content))
    ## finding all div tags
    div_tags = soup.find_all("div")
    div_tag = soup.find('div', class_='flex space-x-4')
    caption = soup.find('div' , class_='text-label-2 dark:text-dark-label-2 break-words')
    ran = soup.find('div' , class_='flex items-start space-x-[9px]')
    links =  soup.find('a' , class_='hover:text-label-1 dark:hover:text-dark-label-1 cursor-pointer')
    languages = soup.find_all('span' , class_='inline-flex items-center px-2 whitespace-nowrap text-xs leading-6 rounded-full text-label-3 dark:text-dark-label-3 bg-fill-3 dark:bg-dark-fill-3 notranslate')
    avatar = soup.find_all('img' , class_='h-20 w-20 rounded-lg object-cover')
    print(avatar[0].get('src'))
    if languages is not None:
      for language in languages:
          print("language", language.text)
    else:
        print("No language found.")
    print("links" ,links.get('href'))
    print("location" , ran.text)
    print("caption " , caption.text)
    v = div_tag.text.split(title_content[0 : title_content.index('-')-1])
    print("name" , v[0])
    print(v[1])
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

