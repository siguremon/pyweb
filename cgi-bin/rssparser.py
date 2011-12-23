#!/usr/bin/env python
# coding: utf-8

import sys
from xml.etree.ElementTree import ElementTree
from urllib import urlopen

def parse_rss(url):
    """ """
    rss = ElementTree(file=urlopen(url))
    root = rss.getroot()
    rsslist = []

    for item in [ x for x in root.getiterator() if "item" in x.tag]:
        rssdict = {}
        for elem in item.getiterator():
            for k in ['link', 'title', 'description', 'author', 'pubDate']:
                if k in elem.tag:
                    rssdict[k] = elem.text
                else:
                    rssdict[k] = rssdict.get(k, "N/A")
        rsslist.append(rssdict)
    return rsslist

if __name__ == "__main__":
    argvs = sys.argv
    if len(argvs) == 2:
        print parse_rss(argvs[1])


