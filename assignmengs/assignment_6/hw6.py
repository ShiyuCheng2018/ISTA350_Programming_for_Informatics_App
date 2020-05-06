"""
Author: Shiyu Cheng (23329948)
ISTA 350 Hw6
SL: Jacob Heller
Date: 4/17/20
Summary: Intro to web scrapping. Grabs the data you need from the web, put it into 
an html parser, and save the result into a file.
"""
from bs4 import BeautifulSoup
import requests, zlib, gzip, os


def get_soup(url=None, fname=None, gzipped=False):
    """
    This function has three parameters. The first is a string representing a URL and has
    a default argument of None. The second is a string named fname representing a filename
    also with default argument of None. The third is a Boolean named gzipped with a default
    value of False. True is passed to this parameter if the html to be parsed is gzipped.
    If the filename is not None, the file is opened and then passed the resulting file pointer
    to the BeautifulSoup constructor, and return the resulting object. If the url is None,
    a RuntimeError with a message is returned. If it is not None, a get request is sent to the
    server. If the response content is zipped, it is unzipped. Then the content is passed
    to the BeautifulSoup constructor and the resulting object is returned.
    :param url: string
    :param fname: string
    :param gzipped: boolean
    :return: BeautifulSoup
    """
    if fname:
        return BeautifulSoup(open(fname))
    if not url:
        raise RuntimeError("Either url or filename must be specified.")
    request = requests.get(url)
    if gzipped:
        return BeautifulSoup(zlib.decompress(request.content, 16 + zlib.MAX_WBITS))
    return BeautifulSoup(request.content)


def save_soup(fname, soup):
    """
    this function takes two arguments, a filename and a soup object. It saves a textual
    representation of the soup object in the file.
    :param fname: string
    :param soup: soup
    :return:
    """
    with open(fname, 'w') as file:
        file.write(repr(soup))
    file.close()


def scrape_and_save():
    """
    this function scrapes the following addresses, soupifies
     the contents, and stores a textual representation of these
     objects in the files 'wrcc_pcpn.html', 'wrcc_mint.html',
     and 'wrcc_maxt.html'
    :return:
    """
    save_soup('wrcc_pcpn.html',
              get_soup('https://wrcc.dri.edu/WRCCWrappers.py?sodxtrmts+028815+por+por+pcpn+none+msum+5+01+F'))
    save_soup('wrcc_mint.html',
              get_soup('https://wrcc.dri.edu/WRCCWrappers.py?sodxtrmts+028815+por+por+mint+none+mave+5+01+F'))
    save_soup('wrcc_maxt.html',
              get_soup('https://wrcc.dri.edu/WRCCWrappers.py?sodxtrmts+028815+por+por+maxt+none+mave+5+01+F'))


def main():
    """
    The current directory is checked for any one of the files that scrape_and_save creates.
    If it is not there, a print statement prints and scrapes and saves the addresses.
    :return:
    """
    _default = False
    for html in os.listdir():
        if html in ['wrcc_pcpn.html', 'wrcc_mint.html', 'wrcc_maxt.html']:
            _default = True
    if not _default:
        print('---- scraping and saving ----')
        scrape_and_save()
