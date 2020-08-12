import requests
from bs4 import BeautifulSoup as bs


def telegram(username):
    try:
        base_url = f"https://telegram.dog/{username}"  
        r = requests.get(base_url).text
        #print(r)
        soup = bs(r,"lxml")
        #soup.text
        members_count = soup.find("div",class_="tgme_page_extra").text.replace(" ","").split("members")[0]
        #print(members_count)
        channel_name = soup.find("div", class_="tgme_page_title").text.replace("\n","")
        print(channel_name)
        description = soup.find("div",class_="tgme_page_description").text
        #print(description)
        dp = soup.find("img",class_="tgme_page_photo_image")['src']
        #print(dp['src'])
        
        data = {}
        data['name'] = channel_name #Can be used as public group also
        data['subs'] = members_count
        data['description'] = description
        data['image'] = dp
        return data
    except Exception as e:
        return {"status":False,"error":e}

telegram("sumanbots")