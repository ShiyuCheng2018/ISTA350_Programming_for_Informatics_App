"""
Author: Shiyu Cheng (23329948)
ISTA 350 Hw8
SL: Jacob Heller
Date: 4/31/20
Summary: Intro to web scrapping. Grabs the data you need from the web, put it into 
an html parser, and save the result into a file.
"""

from bs4 import BeautifulSoup
import requests, zlib, gzip, os, json
import pandas as pd, numpy as np, matplotlib.pyplot as plt

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


def is_num(my_str):
    try:
        float(my_str)
        return True
    except ValueError:
        return False


def load_lists(soup, flag):
    """
    takes in soup obj and flag abd returns list of lists containing the useful data
    in the soup obj. The soup obj contains an html parse tree that describes a table of data
    You will extract the data from the parse tree and store it in the list of lists. In the
    process you will also transpose the data so that the columns in the table are rows in the lists
    of lists and vice versa. Suggest nested for loops.
    Outter loop you traverse the documents table rows and in the inner loop you traverse each rows
    table data fields. the first datum in each row should be a year, which you will need to convert
    to an int. Use if num to find ----- and replace with flag in its place
    :param soup: soup
    :param flag:
    :return: list
    """
    lists = []
    for tr in soup.find_all('tr')[1::]:
        row = []
        for td in tr.find_all('td'):
            if td.get_text() == "-----":
                row.append(int(flag))
            elif is_num(td.get_text()):
                if float(td.get_text()) < 1894:
                    row.append(float(td.get_text()))
                else:
                    row.append(int(td.get_text()))
        if row:
            if row[0] > 1893:
                lists.append(row)
    result = []
    for i in range(len(lists[0])):
        col = []
        for lis in lists:
            col.append(lis[i])
        result.append(col)
    return result


def replace_na(data, row, col, flag, precision=5):
    """
    'na' is an abbreviation for not available.  This is standard jargon for missing data.  In our case,
    we have replaced all missing data with the flag -999as we loaded our list of lists.  We want to clean
    our data by putting in reasonable values where data was missing.  We are particularly interested in trends
    with time, so replacing missing data with averages of data from nearby years is a natural approach.
    The data for a given month through the years is represented by a row (because we transposed it from
    the website format).  Therefore, when confronted with the flag in a position in a row, we will take the
    data from the 5 previous positions in that month's row and 5 following positions and use this to calculate
    an average.  In clean_data, we will replace the flag with the average.  In this function, we will calculate
    and return that average for clean_data to use.  We must delete any occurrences of the flag in the 5
    following years, as that would really mess up the average. This function returns a replacement value for
    data[r][c  ] with the average of the surrounding 10 years.  Its first parameter is the list, the second
    and third are the row and column, respectively, the next is the flag, and the last is a precision with a
    default value of 5.  If one of the surrounding years also contains the flag, leave that position out of
    the average.  Round the replacement value to the precision specified by the last argument.
    :param data: list
    :param row:
    :param col:
    :param flag:
    :param precision: int
    :return:
    """
    count, total, used = 0, 0, 0
    curr = col
    while count != 5:
        curr += 1
        if curr > len(data[row]) - 1:
            break
        count += 1
        if data[row][curr] != flag:
            total += data[row][curr]
            used += 1
    count = 0
    curr = col
    while count != 5:
        curr -= 1
        if curr < 0:
            break
        count += 1
        if data[row][curr] != flag:
            total += data[row][curr]
            used += 1
    replace = round(total / used, precision)
    data[row][col] = replace
    return replace


def clean_data(data, flag, precision=5):
    """
    this function traverses the list of lists and every time it finds the flag, it calls replace_na to replace the flag.
    Its parameters are the list, the flag, and a precision with a default value of 5 to be passed on to replace_na.
    :param data: list
    :param flag:
    :param precision:
    :return: none
    """
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == flag:
                replace_na(data, row, col, flag, precision)


def recalculate_annual_data(data, value=False, precision=5):
    """
    on the website, the last column is the total rainfall for the year or the average annual temperature.
    We have transposed this data, so this information is now in the last row, i.e. the last inner list.
    Because we have replace missing data with reasonable approximations, the data in our annual column no
    longer matches the value calculated from the monthly data.  Therefore, we need to recalculate our annual
    data. This function has three parameters.  The first is the list of lists (we are recalculating
    the last row); the second a Boolean with a default value of False.  The Boolean argument is True if the
    annual data should be averages (temperature data); False if they should be totals (precipitation data).
    The third argument is a precision with a default value of 5.  Round the recalculated annual data to
    this precision.In order to minimize round-off errors messing with the test, when recalculating
    averages, round the sum before dividing by N, then round again after div id in
    :param value:
    :param data: 2d list
    :param bool: boolean
    :param precision: int
    :return:
    """
    result = []
    _list = data[1:-1]
    for each in range(len(_list[0])):
        current = 0
        total = 0
        while current != len(_list):
            total += _list[current][each]
            current += 1
        result.append(total)
    if value:
        for each in range(len(result)):
            result[each] = round(round(result[each], precision) / len(_list), precision)
    data[-1] = result
    return result


def clean_and_jsonify(fnames, flag, precision=5):
    """
    this function takes three arguments. The first is a list of filenames to be cleaned and saved to files as json
    objects. The second is the flag. The third is a precision to be passed on to functions that clean_and_jasonify
    calls. It has a default value of 5. For each file in the first argument, get soup, transform it into a list of
    lists, clean the list, recalculate the annual data, and store it in a file as a json object (as described in
    class). Name your JSON files the same as your html files but with the extension .json. So your wrcc_pcpn.html
    will result in a file called wrcc_pcpn.json.
    :param fnames: list
    :param flag:
    :param precision:
    :return: none
    """
    for file in fnames:
        data = load_lists(get_soup(fname=file), flag)
        clean_data(data, flag, precision)

        files = os.listdir()
        names = ['wrcc_pcpn.html', 'wrcc_mint.html', 'wrcc_maxt.html']
        for f in files:
            if f in names:
                if "pcpn" in f:
                    recalculate_annual_data(data, False)
                else:
                    recalculate_annual_data(data, True)
                print(f)
                with open(f[:-4] + "json", 'w') as fp:
                    json.dump(data, fp)


def get_panda(fname):
    """
    This function takes a string of a filename. File contains a json object representing a list of lists. Load the
    list and store it into a variable. Return a datafrom that has the same data s the list with row labels (index)
    that are 3 letter abbreviations for the months and the year and columns are integers representing years.
    :param fname: string
    :return: DataFrame
    """
    with open(fname) as file:
        json_file = json.load(file)
    dates = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Ann']
    return pd.DataFrame(json_file[1::], index=dates, columns=json_file[0])

def print_stats(fname):
    '''
    This function takes a filename as its sole argument.   Creates a DataFramefrom the data in the file.  Prints
    a DataFrame containing a statistical summary of that data
    :param fname:
    :return:
    '''
    print('----- Statistics for', fname, '-----\n')
    df = get_panda(fname)
    # get_stats(df)

def smooth_data(df, precision = 5):
    '''
    This function takes a DataFrameas its first argument and returns a DataFramewith the same index and
    columns but each data point has been replaced with the 11-year average of the surrounding data including
    the data point itself.  The second argument specifies a precision for each datum (number of decimal places)
    in the new DataFrameand has a default value of 5.  For example, the minimum temperature for March, 2000
    will be replaced by the average of the minimum temperatures from March, 1995 to March 2005.  If there are
    not enough years to go five years out one way or the other from the central data point, use the available
    year
    :param df:
    :param precision:
    :return:
    '''
    smooth_df = df.copy()
    for row in range(len(smooth_df.index)):
        for col in range(len(smooth_df.columns)):
            count = 0
            used = 0
            for each in range(col-5, col+6):
                if -1 < each < (len(smooth_df.columns)):
                    count += df.iloc[row, each]
                    used += 1
            smooth_df.iloc[row, col] = round(count/used, precision)
    return smooth_df

def main():
    _default = False
    for html in os.listdir():
        if html in ['wrcc_pcpn.html', 'wrcc_mint.html', 'wrcc_maxt.html']:
            _default = True
    if not _default:
        print('---- scraping and saving ----')
        scrape_and_save()

    fnames = ['wrcc_pcpn.html', 'wrcc_mint.html', 'wrcc_maxt.html']
    clean_and_jsonify(fnames, -999, 2)
