import os
from datetime import datetime
from pytz import timezone
from it_blog_crawling import parsing_beautifulsoup, kakao_data, line_data, aws_data, kurly_data, clova_data
from github_utils import get_github_repo, upload_github_issue


if __name__ == "__main__":
    access_token = os.environ['MY_GITHUB_TOKEN']
    repository_name = "mlops_crawling"

    seoul_timezone = timezone('Asia/Seoul')
    today = datetime.now(seoul_timezone)
    today_date = today.strftime("%Y년 %m월 %d일")

    kakao_url = "https://tech.kakao.com/blog/#posts"    
    kakao_soup = parsing_beautifulsoup(kakao_url)

    line_url = "https://engineering.linecorp.com/ko/blog/"

    clova_url = "https://engineering.clova.ai/"
    clova_soup = parsing_beautifulsoup(clova_url)

    aws_url = "https://aws.amazon.com/ko/blogs/tech/"
    aws_soup = parsing_beautifulsoup(aws_url)

    kurly_url = "https://helloworld.kurly.com/"
    kurly_soup = parsing_beautifulsoup(kurly_url)

    blog_contents = ''
    
    issue_title = f"IT 개발블로그 모음집({today_date})"
    blog_contents += kakao_data(kakao_soup)
    blog_contents += '\n'

    blog_contents += line_data(line_url)
    blog_contents += '\n'

    blog_contents+= clova_data(clova_soup)
    blog_contents += '\n'

    blog_contents += aws_data(aws_soup)
    blog_contents += '\n'

    blog_contents += kurly_data(kurly_soup)

    repo = get_github_repo(access_token, repository_name)
    upload_github_issue(repo, issue_title, blog_contents)
    print(blog_contents)
    print("Upload Github Issue Success!")
