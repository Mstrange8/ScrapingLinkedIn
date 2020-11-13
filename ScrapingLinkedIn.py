import requests
from bs4 import BeautifulSoup

URL = 'https://www.linkedin.com/jobs/search/?f_E=1&keywords=python&sortBy=DD'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_='jobs-search-two-pane__pagination')
job_elems = results.find_all('li', class_='artdeco-pagination__indicator artdeco-pagination__indicator--number')
for job_elem in job_elems:

    try:
        test = job_elem.find('span', class_='job-result-card__easy-apply-label').text
    except AttributeError:
        pass

