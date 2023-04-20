from bs4 import BeautifulSoup
from google.cloud import storage
from google.oauth2 import service_account
import requests

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.3029.110 Safari/537.3"
}

credentials_dict={
  "type": "service_account",
  "project_id": "model-calling-343600",
  "private_key_id": "335dbf18dd9d776e0d3292722fc42884ea187483",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDdUkOmSaWx22s7\nPzp1r39BHeXEhsT5k9pkS3LGjGk2vzle7A6G0A9lzmgesXeSJhiOxl0DHKE8rA2p\n/Vf5/vEFDnYnaZgoTPLVRwKzv72a+/F6JGK5ZyL3QOWVWZ/imBkODl6xitP8aTn1\nqjc25olZ+/eIFxvR5UseWP8c7NvCNv0YvMN+BJ6ey2b4ikTluxdN7e7LF1krCPC0\nvTwMpyyeIRBk5lAcH3PpRboX3l/zNyju6dH4VYfaWnjEwxbLbw4WGD2sR+zUT+Ba\nO+z2iSI2xVy9jzFYjcea58l1aclYEOAYQjPBZM5zkBPtV6PDDMWGa15nqoQhxJJw\nqgZevyizAgMBAAECggEAapHDG14ZGAREpRm0B5kC2JMR4UjXrimgnmyqDqrrur3n\nXSqjcAzdbTMvdaAUqF4Jsy4W+Xmetf1O8wyXgTxeSAYHpMC20KkEwOfZiD4KiYdJ\nZnwAwa/E6XPpWLn4P/7nCZqnxCvKGZ99lippPdlSR+8I6RHfhnk3a5yE8yOmSeSV\nH6+RK4rqZdYo92X2XGQzMt/EQi138hKSRbQE+HhQWLPjHWYdAJi28u/8EHaKuBct\nUE2HQAe12laDpRu09Trtvg/AHYd/Vx1h5L+wTtMTwAV+3j9EG81nGOLQjvoctSpq\nDlLa968BI7TIIEi4bm1UNjv6G7KjCUCdTehJO3A0IQKBgQD3jVf/4RRLAplfFeX9\nDsaSlxvFk1YKNG2T7sXCzO0EPHBQOK7lqD6C3W0ugMV8ObJEvt0I2yLlWzCLEXon\ncShTj8c1DLeXD3IpQBmYOw7xTxT4Ji8FRpPjo8rYQpwG1Syl4xXhGnxsQOP6bkCr\nc2asCKWw4cC8WpF/T2notWUyQwKBgQDk38ObMlenTHaSwV2Zne/0WuaUH0hSDs07\n6o8WTqrwx5yNcbRh9AwaTNearv/QHLNz5K4Hho14HAtvO4lMJlmv8kE+5oRlEFhf\ni3+0Adce9baVYXwLC2KB8SSjHHDYElDqC0YX4c+5Ps0BJIyui3Rl/m6KcKUSQhJB\nhRmbChhg0QKBgQCXC9NJ+dgb/LYAYqg2RDG9eB4l68Rv7ZV+0g4w0kE8eHQ/PpbY\n4lNiHiFkYoYdSkcP0zWjFbKxJ3bzI/LY5h6o/e2a3OuYbIBH0yjKzh5L9ujgkMvX\n+Dx8hZBbbCkvshrQDUNoWnTYyK9SOruS4ZMgHRacWuLzCoAEojwJFcVtaQKBgQCo\nRqEx5VSvC7gOdJ9WB9paBc+MTmfE9V8OU4n6s8JZH9pJ4LToZB/V4nOPJmWtZLzI\nU/VkURiIm84IbXSoCXZdt7cjASeMivT+4rj053l8KNqigDdMg4Vc1qjCSHHrW6Qk\nQD+75Wnt4G+oDHBnEN928hfiL6oef3eetra52DVOUQKBgQDMKEG+ILJ2b7a2/+eK\nNZMm+IjsCYg1b+waCcOmQPhg8pCzUhOuc3FGMg/eyzPLlgKF2LyYrlueNS1Frla+\nF5BNPZsWQUaC8OiI6VCdQ1Wv4aauHMgJgOHo0Rej564ih1oy5XDBfQchQc8HSl2B\n+8A8sJKqplNGwGht0RsDgkFU9Q==\n-----END PRIVATE KEY-----\n",
  "client_email": "storagedataops@model-calling-343600.iam.gserviceaccount.com",
  "client_id": "104637843235005142622",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/storagedataops%40model-calling-343600.iam.gserviceaccount.com"
}

try:
 
 res=requests.get(
    f'https://www.google.com/search?q=SaoPauloCidade&oq=SaoPauloCidade&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
 print("Loading...")
 soup=BeautifulSoup(res.text,'html.parser')
 info= soup.find_all("span", class_="LrzXr kno-fv wHYlTd z8gr9e")[0].getText()
 print(info)
 credentials=service_account.Credentials.from_service_account_info(credentials_dict)
 storage_client=storage.Client(credentials=credentials)
 bucket=storage_client.get_bucket('weather_sampa')
 blob=bucket.blob('weather_info.txt')
 blob.upload_from_string(info+"\n")
 
 print('File upload.')
 with open("weather_info.txt",'a') as f:
     f.write(info+"\n")
 print("Finished")   
except Exception as ex:
    print(ex)