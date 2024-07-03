from requests import get
#for loop 연습하기
#pypi 연습하기 - requests 모듈 
#https://httpstat.us/ 사이트 참고해서 샅태코드 이해하기 

websites = (
  'google.com',
  'airbnb.com',
  'https://twitter.com',
  'facebook.com',
  'https://tiktok.com'
)

results = {
  
} 

#200 response 값을 웹사이트가 성공적으로 응답했다는 의미
for site in websites:
  if not site.startswith('https://'):
    site = f"https://{site}"
  response = get(site)
  if response.status_code < 200:
    results[site] = "Processing"
  elif response.status_code < 300:
    results[site] = "OK"
  elif response.status_code < 400:
    results[site] = "Redirection"
  elif response.status_code < 500:
    results[site] = "Client Error"
  else:
    results[site] = "Server Error"

print(results)