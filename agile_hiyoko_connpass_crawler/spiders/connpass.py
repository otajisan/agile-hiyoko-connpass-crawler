import os
import time

import scrapy

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from agile_hiyoko_connpass_crawler.items import AgileHiyokoConnpassCrawlerItem


class ConnpassSpider(scrapy.Spider):
    name = 'connpass'
    allowed_domains = [
        'agile-hiyoko-club.connpass.com',
        'connpass.com',
    ]

    handle_httpstatus_list = [302]

    login_url = 'https://connpass.com/login/'
    login_user = os.getenv('CONNPASS_LOGIN_USER')
    login_password = os.getenv('CONNPASS_LOGIN_PASS')

    def __init__(self):
        options = webdriver.ChromeOptions()
        download_path = f'{os.getcwd()}/csv/'
        prefs = {
            'download.default_directory': download_path,
        }
        options.add_experimental_option('prefs', prefs)
        options.add_argument('--headless')
        # by secret mode
        options.add_argument('--incognito')
        self.driver = webdriver.Chrome(
            ChromeDriverManager().install(),
            options=options
        )

    def start_requests(self):
        self.login_by_selenium()
        last_page_num = self.get_last_page()
        for page in range(1, last_page_num + 1):
            yield scrapy.Request(
                f'https://agile-hiyoko-club.connpass.com/event/?page={page}',
                callback=self.parse_event_list
            )

    def login_by_selenium(self):
        self.driver.get(self.login_url)
        self.driver.find_element(by=By.NAME, value='username').send_keys(self.login_user)
        self.driver.find_element(by=By.NAME, value='password').send_keys(self.login_password)
        time.sleep(3)
        submit_btn = self.driver.find_element(by=By.XPATH,
                                              value='//*[@id="login_form"]/p[5]/button')
        submit_btn.click()
        time.sleep(3)

    def get_last_page(self):
        # NOTE: page 0 -> jump last page
        self.driver.get('https://agile-hiyoko-club.connpass.com/event/?page=0')
        last_page_html = self.driver.page_source
        soup = BeautifulSoup(last_page_html, 'html.parser')
        last_page = soup.find('div', class_='paging_area').find('li', class_='active').find('span')

        return int(last_page.text)

    def parse_event_list(self, response):
        soup = BeautifulSoup(response.body, "html.parser")

        for i, event in enumerate(soup.find_all('div', class_='group_event_list')):
            event_page_link_elem = event.find('a', class_='url')
            event_page_url = event_page_link_elem.get('href')
            event_id = event_page_url.split('/')[-2]
            csv_url = f'https://connpass.com/event/{event_id}/participants_csv/'

            item = AgileHiyokoConnpassCrawlerItem()
            item['event_id'] = event_id
            item['name'] = event_page_link_elem.string
            item['url'] = event_page_url
            item['csv_url'] = csv_url

            self.download_csv(csv_url)
            yield item

    def download_csv(self, csv_url):
        self.driver.get(csv_url)
        time.sleep(3)

    def __del__(self):
        self.driver.close()
        self.driver.quit()
