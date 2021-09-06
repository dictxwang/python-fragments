# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
pip install lxml
'''

from lxml import etree
import requests


def spider_html():
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }
    resp = requests.get("http://sogou.com", headers=header)
    resp.encoding = "utf8"
    return resp.text


def read_html():
    with open("../basis/data/lxml_001.html", mode="r", encoding="utf8") as fp:
        return fp.read()


def parse_html_content(text):

    tree = etree.HTML(text)
    # full filter path with "/"
    nav_lst = tree.xpath("/html/body/div/div[@class='header']/div[@class='top-nav']/ul/li/a")
    for nav in nav_lst:
        # get content
        text = nav.text
        # parse attribute
        href = ""
        # attribute tuple list to dict
        attrs = nav.attrib
        if "href" in attrs:
            href = attrs["href"]
        print("{}=>{}".format(text, href))

    # short filter path with "//"
    # @class @id @value @href @src can be use
    nav_lst = tree.xpath("//div[@class='top-nav']/ul/li")
    for nav in nav_lst:
        # get child nodes
        child_lst = nav.xpath("a")
        for child in child_lst:
            print(child.text)

    nav_script_lst = tree.xpath("//a[@href='javascript:void(0);']")
    for nav in nav_script_lst:
        # get parent node
        parent = nav.xpath("..")
        # print tag name
        print(parent[0].tag)

    nav_lst = tree.xpath("//div[@class='top-nav']/ul/li/a")
    for nav in nav_lst:
        # print attributes, tuple list
        print(nav.items())


if __name__ == "__main__":
    # html_text = spider_html()
    html_text = read_html()
    parse_html_content(html_text)
