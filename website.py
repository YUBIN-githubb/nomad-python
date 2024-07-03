from requests import get
#for loop 연습하기
#pypi 연습하기 - requests 모듈 

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
  if response.status_code >= 100 and response.status_code < 400:
    results[site] = "OK"
  else:
    results[site] = "FAILED"

print(results)