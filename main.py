import numbers

import requests
from bs4 import BeautifulSoup

import price_tracker
import schemas
from config import baseUrlNetshoes


def main():
    NetShoes = price_tracker.NetshoesTracker(baseUrlNetshoes)
    max = NetShoes.getMaxPageAmmount()

    link_list = []
    for page in range(1, 10):
        item_list = NetShoes.getItemList(page)
        items = []
        for item in item_list:
            name = item["title"]
            link = item["href"].replace("//", "https://")
            price = NetShoes.getItemPrice(link)
            tempItem = schemas.Item(name, link, price)
            items.append(tempItem)

        link_list.extend(NetShoes.getItemsLinks(item_list))
    print()


if __name__ == "__main__":
    main()
# import matplotlib.pyplot as plt
# import numpy as np
# teste = np.pi
# x = np.linspace(0, 10, 400)
# y = np.sin(x)
#
# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()