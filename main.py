import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"

#웹사이트로 request 보내기
reponse = requests.get(url)

#bs4로 웹사이트의 소스코드 가져오기
soup = BeautifulSoup(reponse.content, "html.parser")

#클래스가 jobs인것들 중 리스트만 가져오기
#[1:-1]은 맨처음과 맨끝 리스트가 필요 없기 때문
#find는 하나의 element만 반환, find_all은 리스트 반환
#list를 unpack 하는 syntax는 갯수대로 변수를 선언 = 리스트
jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

all_jobs = []

#list unpack 으로 값을 받아오는 과정에서 region이 없는 값들이 있어서 ValueError가 발생 -> find_next를 이용해서 job의 하위메뉴에서 find하고 
for job in jobs:
  title = job.find("span", class_="title").text
  company = job.find_next("span", class_="company")
  position = company.find_next("span", class_="company")
  region = position.find_next("span", class_="company")
  anchor = company.find_parent("a")
  url = anchor["href"] if anchor else "parent anchor is not found"
  #company, position, region = job.find_all("span",class_="company")

  
  
  """    
  try:
    url = job.find('div', class_ = 'tooltip--flag-logo').next_sibling['href']
  except KeyError:
    url = 'You need log-in'
  """
  job_data = {
    "title" : title,
    "company" : company.text,
    "positon" : position.text,
    "region" : region.text,
    "url" : url
  }
  all_jobs.append(job_data)

print(all_jobs)