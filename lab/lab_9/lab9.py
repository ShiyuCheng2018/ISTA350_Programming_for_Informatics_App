import requests

def get_page(url):
    """
    This function takes a string that represents a url.
    
    Your task is to send a request from the url given as a parameter.
    From this request, return a string containing the content of the request.
    """

def how_bold(c):
    """
    This function takes a string containing the content of a webpage.
    
    Using the provided string, return a count of how many times 
    the string '<b>' (the bold tag) appears in the page.
    """

def get_title(c):
    """
    This function takes a string containing the content of a webpage.
    
    Using the provided string, return the title of the page.
    The title is enclosed between the '<title>' and '</title>' tags.
    """

def upgrade_python(c):
    """
    This function takes a string containing the content of a webpage.
    
    Return a new copy of the content string, but with
    all instances of "Python" replaced with "Anaconda".
    Maintain the same capitalization in the replacement words as with the originals.
    """
    
def main():
    get_page('http://www.pythonchallenge.com/')
    
if __name__ == '__main__':
    main()
