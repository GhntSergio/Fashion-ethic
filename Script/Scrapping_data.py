'''
Scrapping des donnees
'''
# Libraries
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import re
import numpy as np
import random


# All fashion collection
def Apparel(n):
    T, P, R, S, C, Sz = [], [], [], [], [], []
    s,j,k = 0, 0, 0
    for i in range(1, n):
        url = (
            "https://www.tendancefashion.fr/fr/28-toute-la-collection?order=product.position.asc&page="
            + str(i)
            + ".html"
        )
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        Titles = soup.find_all("h1", {"class": "product-title"})
        Prices = soup.find_all("span", {"price"})
        Stocks = soup.find_all("div", {"product-add-to-cart"})
        Colors = soup.find_all("div", {"wt_color"})
        Sizes = soup.find_all("div", {"wt_size"})

        # Titles
        for t in Titles:
            T.append(t.a.text.strip())
            s = s + 1
        # Prices
        for t in Prices:
            t = re.sub(r"[^0-9.,]", "", t.text)
            P.append(float(t.replace(",", ".")))
        # In stocks
        for tag in Stocks:
            if "Ajouter" in tag.form.a.span.text:
                S.append(True)
            else:
                S.append(False)
        # N_colors
        for c in Colors:
            C.append(len(c.ul.find_all("li")))
            j = j + 1
        #
        # N_size
        for siz in Sizes:
            Sz.append(len(siz.ul.find_all("li")))
            k = k + 1
        # mis au point
    if j != i:
        while j != s:
            C.append(random.randint(min(C), max(C)))
            j = j + 1

    if k != i:
        while k != s:
            Sz.append(random.randint(min(Sz), max(Sz)))
            k = k + 1
    return {"Articles": T, "Prices": P, "InStocks": S, "N_colors": C, "N_sizes": Sz}


# best sell fashion
def bestApparel(n):
    T, P, R, S, C, Sz = [], [], [], [], [], []
    s,j,k = 0, 0, 0
    for i in range(1, n):
        url = (
            "https://www.tendancefashion.fr/fr/meilleures-ventes?order=product.sales.desc&page="
            + str(i)
            + ".html"
        )
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        Titles = soup.find_all("h1", {"class": "product-title"})
        Prices = soup.find_all("span", {"price"})
        Stocks = soup.find_all("div", {"product-add-to-cart"})
        Colors = soup.find_all("div", {"wt_color"})
        Sizes = soup.find_all("div", {"wt_size"})

        # Titles
        for t in Titles:
            T.append(t.a.text.strip())
            s = s + 1
        # Prices
        for t in Prices:
            t = re.sub(r"[^0-9.,]", "", t.text)
            P.append(float(t.replace(",", ".")))
        # In stocks
        for tag in Stocks:
            if "Ajouter" in tag.form.a.span.text:
                S.append(True)
            else:
                S.append(False)
        # N_colors
        for c in Colors:
            C.append(len(c.ul.find_all("li")))
            j = j + 1
        #
        # N_size
        for siz in Sizes:
            Sz.append(len(siz.ul.find_all("li")))
            k = k + 1
        # mis au point
    if j != i:
        while j != s:
            C.append(random.randint(min(C), max(C)))
            j = j + 1

    if k != i:
        while k != s:
            Sz.append(random.randint(min(Sz), max(Sz)))
            k = k + 1
    return {"Articles": T, "Prices": P, "InStocks": S, "N_colors": C, "N_sizes": Sz}
