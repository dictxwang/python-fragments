#!/usr/bin/env python3
# -*- coding: utf8 -*-
__author__ = 'wangqiang'

import requests
from lxml import etree
import time
import os


def make_index_url(host, novel_id, page):
    return f"http://{host}/index/{novel_id}/{page}/asc"


def crawl_html_content(url):
    headers = {'User-Agent': 'Mozilla/5.0 ' \
                          '(Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 ' \
                          '(KHTML, like Gecko) Version/5.1 Safari/534.50'
             }
    resp = requests.get(url, headers=headers)
    return resp.text


def parse_index_content(content):

    tree = etree.HTML(content)
    title_eles = tree.xpath("//div[@class='atitle']")
    # parse novel name
    novel_name = title_eles[0].text

    # parse index urls at current page
    index_url_eles = tree.xpath("//dl[@class='index']/dd/a[@class='db']")
    index_urls = []
    for ele in index_url_eles:
        name = ele.text
        url = ele.attrib["href"]
        index_urls.append((name, url))

    return novel_name, index_urls


def parse_detail_content(text):

    tree = etree.HTML(text)
    title_lst = tree.xpath("//div[@class='atitle']")
    for t in title_lst:
        print(t.text)


def get_all_index_start_urls(host, novel_id):

    index_url_map = {}
    index_urls = []
    # index list page below 200
    for start_page in range(1, 200):
        index_url = make_index_url(host, novel_id, start_page)
        index_content = crawl_html_content(index_url)
        name, urls = parse_index_content(index_content)
        novel_name = name
        if urls[0][1] in index_url_map:
            # has crawled, no need continue
            break
        for url in urls:
            index_urls.append(url)
            index_url_map[url[1]] = 1
        print(f"crawl and parse index url {index_url}")
        time.sleep(1)

    return novel_name, index_urls


def clear_detail_content(content):
    content = content.replace("&emsp;", " ")
    content = content.replace("<br>", "\n")
    content = content.replace("<br/>", "\n")
    content = content.replace("<br />", "\n")
    content = content.replace("\r\n", "\n")
    for _ in range(0, 10):
        content = content.replace("\n\n", "\n")
    return content


def get_all_detail_contents(novel_name, index_urls, start_index=None):

    if start_index:
        started = False
    else:
        started = True
    for t in index_urls:
        name = t[0]
        url = t[1]
        if not started and name == start_index:
            started = True
        if not started:
            continue
        fp = open(f"data/{novel_name}/{name}.txt", mode="w", encoding="utf8", errors="ignore")

        # more page for on index
        while True:
            time.sleep(1.5)
            content = crawl_html_content(url)
            tree = etree.HTML(content)

            # parse content
            start_flag = '<div id="bcontent" class="bcontent">'
            start = content.find(start_flag) + len(start_flag)
            end = content.find("</div>", start)
            if end > start:
                novel_detail = content[start:end]
                novel_detail = clear_detail_content(novel_detail)
                fp.write(novel_detail + "\n")
                fp.flush()
                # print(f"crawl and parse detail url {url}")

            # parse next page
            next_text = "下一章"
            a_next = tree.xpath("//div[@class='footlink']/a[@id='t_next']")
            if a_next and a_next[0].text:
                next_text = a_next[0].text
                url = a_next[0].attrib["href"]

            if next_text != "下一页":
                break
        print(f"finish crawl index {novel_name}, {name}")
        fp.flush()
        fp.close()


def save_index_file(novel_name, index_urls):
    fp = open(f"data/{novel_name}/000_目录.txt", mode="w", encoding="utf8", errors="ignore")
    for t in index_urls:
        name, _ = t
        fp.write(f"{name}\n")
        fp.flush()
    fp.close()
    print("finish save novel index.")


def crawl_one_novel(host, novel_info):
    novel_id, start_index = novel_info
    try:
        print(f"job novel {novel_id} started")

        # crawl all index information
        novel_name, index_urls = get_all_index_start_urls(host, novel_id)
        print(novel_name)
        print(index_urls)

        # make data folder
        make_novel_data_folder(novel_name)

        # save index
        save_index_file(novel_name, index_urls)

        # crawl all detail contents
        get_all_detail_contents(novel_name, index_urls, start_index=start_index)

        print(f"job novel {novel_id} finished")
    except Exception as exp:
        print("error at " + novel_id)


def make_novel_data_folder(novel_name):
    novel_name = novel_name.replace(" ", "_")
    folder_name = f"data/{novel_name}"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)


if __name__ == '__main__':

    host = "wap.xxxx.com"
    novel_base_info = [
        ("44169", None),
    ]

    for novel_info in novel_base_info:
        crawl_one_novel(host, novel_info)

    print("all jobs finished")
