# Did you forget an import??

def make_soup(fname):
    """
    This function takes a string as its only parameter. 

    The string REPRESENTS the name of an html file.

    Your task is to CREATE and RETURN a BeautifulSoup object from the 
    string parameter.

    Don't worry about compressed data.
    """

def make_table(fname):
    """
    This function takes a string as its only parameter. The string, fname,
    REPRESENTS the name of an html file.

    First task:
        Use your make_soup function to create a soup object from fname.

    The BeautifulSoup object that is returned from the first task, contains
    an html parse tree that describes a table of data. If you refer back to the 
    index_lab9.html file you can see that the table is filled with
    "@}>-'-,--"  (thorny roses), and "(8>/--<"  (creepy aliens). 

    Second task:
        EXTRACT the data from the parse tree and store it into a list of lists.
        Once you are finished extracting the data from the table RETURN the 
        list of lists. 
    """
    
def remove_thorns(data):
    """
    This function takes a list of lists. The list of lists contains either
    alien "(8>/--<" or thorny rose "@}>-'-,--" emoticons.

    As you can see the rose emoticons contain virtual thorns. Your task is to
    remove the thorns on the roses. Return a NEW list of lists in which
    thorny roses "@}>-'-,--" are de-thorned "@}>----" , leave the aliens alone
    for now. 

    Restriction: 
        - You cannot alter the original list of lists.
    """

def translate_data(data, original=True, english=True):
    '''
    This function take as list of lists as its first parameter, and two
    booleans for the second and third parameters. The list of lists contains 
    either alien "(8>/--<" or DE-THORNED rose "@}>----" emoticons. The second
    and third parameters have default values of True.

    Your task is to translate emoticon text to English and vice versa.
        -First, check if the second parameter, original, is True. If that
         is the case raise a RuntimeError with the message:
             "Cannot alter source, aborting mission!"
         Otherwise do the next step below.
        -If the third parameter, english, is True you will translate
         "@}>----" to "ROSE" and "(8>/--<" to "ALIEN". If the english parameter 
         is False you will translate "ROSE" to "@}>----" and "ALIEN" to "(8>/--<". 
        -This function returns None.
        
        Example:
            data = [['@}>----', '@}>----'],           [['ROSE', 'ROSE'],
                    ['(8>/--<', '@}>----'],    <=>     ['ALIEN', 'ROSE'],
                    ['@}>----', '(8>/--<']]            ['ROSE', 'ALIEN']]
    '''

def process_data(data):
    """
    This function takes a list of lists. The list of lists contains either
    alien "(8>/--<" or thorny rose "@}>-'-,--" emoticons.


    Your task is as followed:
        - Remove the thorns form the thorny roses. What function does this?
          Remember the function that you will use will return a new list of
          lists. Never alter original data.
        - Next, translate the list of lists that was returned from the previous 
          step. Make sure to pass in the proper arguments. You want to translate
          form emoticon to English. Remember you already coded a function that
          does this!

            NOTE: After translating your list your elements are "ROSE" and "ALIEN"
            not the emoticon text version. 

        - Then, for each row in the list you want to place all the roses before
          aliens. 
                Example: 
                [['ALIEN', "ROSE", "ROSE", "ROSE", "ROSE", "ROSE", 'ALIEN'], ...]

                    Will now be ...

                [["ROSE", "ROSE", "ROSE", "ROSE", "ROSE", 'ALIEN', 'ALIEN'], ...]

        - Finally, translate the list of lists back from English to emoticon text.
          Make sure to pass in the proper arguments in the function call.
        - Return the translated list of lists.
    """

def verify_ratio(data):
    """
    This function takes a list of lists. The list of lists contains either
    alien "(8>/--<" or DE-THORNED rose "@}>----" emoticons.

    Your task it to CREATE and RETURN a dictionary that maps the alien (8>/--<
    and de-thorned rose @}>---- emoticons to the number of times they appear 
    in the list of lists.
        Example:
            data = [['@}>----', '@}>----'],
                    ['(8>/--<', '@}>----'],
                    ['@}>----', '(8>/--<']]

            Dictionary returned: 
                stats = {'@}>----':4, '(8>/--<':2}

    """

def encrypt_and_file(data, encryptionKey_dict):
    """
    This function takes a list of lists as its first parameter. The list 
    of lists contains either alien "(8>/--<" or de-thorned rose "@}>-'-,--" 
    emoticons. The second parameter is a dictionary that maps a character to
    a string integer.
        Example: 
            encryptionKey_dict = {'A': '121', 'L': '050', 'I': '932',
                                  'E': '13', 'N': '87', 'R': '11',
                                  'O': '430', 'S': '553'} 

    Your task is to encrypt the data in the list of lists. Your 
    encryptionKey_dict can only encrypt English alphabet characters so you 
    must first translate the data from emoticon text to English. 
        -You MUST translate the original data don't make a copy of it. Recall 
         that translate_data will raise a RuntimeError if you indicate that 
         you are translating the original data. Call the function with the 
         appropriate arguments to bypass raising an Error.
        -After translating, you need to encrypt, use the dictionary, 
         encryptionKey_dict to do this. For each character in the strings 
         "ALIEN" or "ROSE" you will replace with values in the encryptionKey_dict.
         Remember you are going through a lists of lists. Make sure that the
         encrypted data is transformed to an integer, see example below!
            Example:
                [["ROSE", "ROSE", "ALIEN"],...]

                Will become:
                [[1143055313, 1143055313, 1210509321387],...] #NOTE: no longer 
                                                               strings!
        -Finally save the encrypted data in json format. Name the file 
         "AlienMission.json".
        -Function returns None.


    """

def peace_or_nuke(data, encrypt_key):
    """
    This function takes a list of lists as its first parameter. The list of 
    lists contains either alien "(8>/--<" or thorny rose "@}>-'-,--" emoticons. 
    The second parameter is a dictionary that maps a character to a string
    integer.

        Example: 
            encrypt_key = {'A': '121', 'L': '050', 'I': '932',
                           'E': '13', 'N': '87', 'R': '11',
                           'O': '430', 'S': '553'} 

    Your task is verify if there are enough roses to give the aliens. If one 
    alien is left without a rose then they will nuke Earth. Unless we 
    nuke their mother ship first. Since we prefer peace over war you can't just
    nuke the mother ship. Follow the steps below before we can proceed with 
    Mission Nuke. 

        - call process_data() on the data argument store it to a variable, info
        - call verify_ratio() passing info as an argument. 
        - set a variable, flag, to True
        - You need to verify if the dictionary returned from verify_ratio()
          contains more aliens or flowers. If there are more flowers than aliens
          print the following message:
            "All missiles down, ceasefire! Mission Nuke aborted."
          and set flag to False.
          Otherwise print the following message:
            "Nuke the Mother Ship!! BOOOOM BOOOOOOOM ... POW!!!"
        - call encrypt_and_file(), pass info and encrypt_key as arguments.
        - Finally, return the variable flag.
    """
    
def main():
    """
    Use main to test your code use the fname, and encrypt to your advantage.
    You are not required to write any code in main to pass the test script. 
    """
    fname = 'index_lab11.html'
    encrypt = {'A': '121', 'L': '050', 'I': '932', 'E': '13', 'N': '87', 'R': '11', 'O': '430', 'S': '553'}

if __name__ == '__main__':
    main()