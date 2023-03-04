from abc import ABC, abstractmethod, abstractproperty, abstractstaticmethod

from bs4 import BeautifulSoup

import request_manager


class PriceTracker(ABC):
    @abstractmethod
    def __init__(self, baseUrl):
        __baseUrl = baseUrl

    @abstractmethod
    def getMaxPageAmmount(self):
        pass

    @abstractmethod
    def getItemList(self, page):
        pass

    @abstractmethod
    def getItemsLinks(self, items_list):
        pass

    @abstractmethod
    def getItemPrice(self, link):
        pass


class NetshoesTracker(PriceTracker):
    def __init__(self, baseUrl):
        self.__baseUrl = baseUrl

    def getMaxPageAmmount(self):
        __html_text = request_manager.doRequest(self.__baseUrl)
        if __html_text != "":
            soup = BeautifulSoup(__html_text, "html.parser")
            pages = soup.find("div", attrs={"class": "pagination"})
            pageLinks = pages.find_all("a")
            max_page = 0
            for link in pageLinks:
                link = link.text
                if link.isnumeric() and int(link) > max_page:
                    max_page = int(link)
            return max_page
        else:
            raise ValueError("Invalid html body")

    def getItemList(self, page):
        print(f"\nGetting items from page {page}")
        __html_text = request_manager.doRequest(f"{self.__baseUrl}&page={page}")
        soup = BeautifulSoup(__html_text, "html.parser")
        item_list = soup.find("div", attrs={"class": "wrapper"})
        return item_list.findChildren("a")

    def getItemsLinks(self, item_list):
        print(f"Getting links...")
        item_links = []
        for item in item_list:
            link = item["href"].replace("//", "https://")
            item_links.append(link)
        return item_links

    def getItemPrice(self, link):
        __html_text = request_manager.doRequest(link)
        soup = BeautifulSoup(__html_text, "html.parser")
        price = soup.find("div", attrs={"class": "default-price"})
        price_formatted = price.find("strong").text.replace("R$", "").replace(" ", "").replace(",", ".")
        return price_formatted
