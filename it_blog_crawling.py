import requests
from bs4 import BeautifulSoup


def parsing_beautifulsoup(url):

    data = requests.get(url)

    html = data.text
    return BeautifulSoup(html, 'html.parser')

def kakao_data(soup):

    upload_contents = '[kakao]\n'
    kakao_posts = soup.select(".elementor-post_title")

    for post in kakao_posts:
        post_title = post.select("a")[0].text.strip()
        kakao_post_url = post.select("a")[0].attrs["href"]
        
        content = f"<a href={kakao_post_url}>" + post_title + "</a>" + "<br/>\n"
        upload_contents += content
    
    return upload_contents

def line_data(url):

    data = requests.get(url)
    html = data.content.decode('utf-8','replace')
    soup = BeautifulSoup(html,'html.parser')

    line_posts = soup.select(".title")

    line_contents = '[LINE]\n'
    url_prefix = "https://engineering.linecorp.com/"

    for post in line_posts:
        if post.select("a"):
            line_post_title = post.select("a")[0].text
            url_suffix = post.select("a")[0].attrs["href"]
            line_post_url = url_prefix + url_suffix

            content = f"<a href={line_post_url}" + line_post_title + "</a>" + "<br/>\n"
        
        line_contents += content
    
    return line_contents

def carrot_data(soup):
    carrot_posts = soup.select('.postItem')

    carrot_contents = '[당근마켓]\n'

    for post in carrot_posts:
        carrot_url = post.select("a")[0].attrs['data-action-value']
        carrot_post_title = post.select("a")[0].select('.u-textScreenReader')[0].text
        
        content = f"<a href={carrot_url}" + carrot_post_title + "</a>" +"</br>\n"
        carrot_contents += content

    return carrot_contents

def kurly_data(soup):

    kurly_posts = soup.select(".post-link")

    url_prefix = "https://helloworld.kurly.com"

    kurly_contents = '[마켓컬리]\n'

    for post in kurly_posts:
        kurly_post_title = post.select("h3")[0].text.strip()
        url_suffix = post.attrs['href']
        url = url_prefix+url_suffix

        content = f"<a href={url}" + kurly_post_title + "</a>" + "</br>\n"
        kurly_contents += content

    return kurly_contents