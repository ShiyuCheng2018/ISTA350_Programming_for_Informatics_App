'''
IMPORTANT:

This lab is different from what you have been doing. As you can see,
there is some code that is already provided for your convenience. 

You are to complete all sections that are labeled with:

    #-------------------- TO DO ITEM ## --------------------#
    #   Instructions                                        #
    #-------------------------------------------------------#

You will be implementing two classes: FoodItem and SandwichShop.
'''

class FoodItem:
    '''
    This class creates a FoodItem object. A FoodItem has a name and a 
    price ($).
    '''
    
    def __init__(self, ingredient, cost):
        '''
        This method takes in a string (name) that represents an ingredient
        name and a float (price) that represents the price associated to the
        ingredient.                    
        '''
        #---------------------------- TO DO ITEM #1 ---------------------------#
        #   You will initialize two instance variables: name and price.        #
        #   Be sure to store the string parameter in the name instance         #
        #   variable and the float parameter in the price instance variable.   #
        #----------------------------------------------------------------------#
        self.name = ingredient
        self.price = cost

    def __repr__(self):
        '''
        This method returns the string representation of a FoodItem.
        A FoodItem has a name and a price. The returned string is 
        formatted specifically for this module.

        Example of FoodItem representation:
            Red Bell Pepper            $0.50
            Pickles                    $0.25
        '''
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GIVEN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<# 
        return self.name.ljust(27) +str("${:3.2f}".format(self.price))
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

class SandwichShop:
    '''
    This class creates a SandwichShop Object. A SandwichShop object serves to
    hold an inventory of FoodItems that is used to create a virtual sandwich. 
    The contents of the sandwich is determined by a user. This class contains 
    a total of 7 methods. You will be completing 5 of them.  
    '''

    def __init__(self, name):
        '''
        This method takes one parameter, name, that represents a person's name.

        This method has a total of 8 instance variables. The fist variable is 
        self.name which holds the string that was passed as a parameter. The 
        next 5 instance variables are lists. Each list represents a different 
        food category: meats, vegetables, breads, cheeses, and sauces. Each list
        will be populated with FoodItem objects. The 7th instance variable is
        self.selections which is a list that represents future FoodItems that
        a user will select to create their sandwich, Self.selections is to remain
        empty in the initializer. The 8th instance variable is self.storage which
        is a dictionary that maps an integer to a food category instance variable.
        This dictionary will be used to retrieve the food category instance 
        variables (lists) when a user is selecting FoodItems (this will be done 
        later on). 
        '''
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GIVEN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
        self.name = name

        self.meats = []
        self.sauces = []
        self.vegies = []
        self.breads = []
        self.cheeses = []

        self.selections = [] 
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

        #------------------------------ TO DO ITEM #2 ------------------------------#
        #                                                                           #
        #  Your task is to read the data in the file named choices.csv and          #
        #  populate the five lists that represent the different food categories:    #
        #  self.meats, self.sauces, self.vegies, self.breads, and self.cheeses.     #
        #                                                                           #
        #  You will be populating the lists with FoodItems. Keep in mind that       #
        #  each FoodItem instance requires a name (string) and a price (float).     #
        #                                                                           #
        #  The file choices.csv contains three pieces of information on each line.  #
        #  First, is a food category (meat, sauce, vegetable, bread, or cheese).    #
        #  Second, is an ingredient name. Third, is the price for the ingredient.   #
        #                                                                           #
        #     Snippet of lines in the file: (NOTE THE FORMAT it's a csv file.)      #
        #         meat,Maple Glazed Honey Ham,2.30                                  #
        #         cheese,Monterey Jack,1.40                                         #
        #         sauce,Caesar,0.50                                                 #
        #         vegetable,Spinach,0.15                                            #
        #---------------------------------------------------------------------------#

        content = open('choices.csv').readlines()
        for line in content:
            m_list = line.strip().split(",")
            cata = m_list[0]
            food_name = m_list[1]
            price = m_list[2]

            if cata == 'meat':
                self.meats.append(FoodItem(food_name, float(price)))
            elif cata == 'cheese':
                self.cheeses.append(FoodItem(food_name, float(price)))
            elif cata == 'bread':
                self.breads.append(FoodItem(food_name, float(price)))
            elif cata == 'sauce':
                self.sauces.append(FoodItem(food_name, float(price)))
            else:
                self.vegies.append(FoodItem(food_name, float(price)))

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GIVEN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#        
        self.storage = {1: self.breads, 2: self.cheeses, 3: self.meats, \
                        4: self.vegies, 5: self.sauces}
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

        
    def __repr__(self):
        '''
        This method returns a string representation of the final SandwichShop 
        selected FoodItems. 
        '''
        
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GIVEN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<# 
        result = "\n"
        if len(self.selections) > 3:
            result += "Wooow look at the size of that thing!\n"
        result += "That is one good looking virtual sandwich " + self.name + "!\n\n"
        result += "The items you selected:\n\n"
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

        #----------------------------- TO DO ITEM #3 -----------------------------#
        #                                                                         #
        #  Your task is to iterate through the self.selections instance variable. #
        #  and print each item.                                                   #
        #  Recall that this variable is a list of FoodItems that the a user       #
        #  selected to be in their virtual sandwich. You are also required to     #
        #  calculate the total price of the sandwich. This will be easier to do   #
        #  while you are iterating through the FoodItems. Once this is completed  #
        #  include an additional String "\n Your grand total: $" and concatenate  # 
        #  that to the variable that holds the summed up price for the sandwich.  #
        #  Round the total to two decimal places. Don't forget to return the      #
        #  result!                                                                #
        #-------------------------------------------------------------------------#

        for item in self.selections:
            print(item)


    
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GIVEN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
    @staticmethod
    def print_items_in_list(lst, remove = False):
        '''
        This static method takes two parameters a list and a boolean. The list
        will represent one of the food instance variable lists. 

        The method will print all the items in the list and will list them
        numerically. A user will be asked to select a food item by selecting a
        number that corresponds to the food item listed. If the user inputs an
        invalid number or the number that corresponds to "Abandon Ship!" the 
        function will return False. False indicates that the user did not wish
        to select a FootItem listed. If the user inputs a valid number than 
        A FoodItem will be returned. If the current purpose is to remove a 
        FoodItem then an index is returned. 

        Your Optional Task:
            Analyze the given code, ask question if you have any.
        '''
        print()
        valid_opt_lst = []
        food_items = []
        for i in range(len(lst)):
            print((" " + str(i+1) + ")").rjust(4) + " " + repr(lst[i]))
            valid_opt_lst.append(i+1)
            food_items.append(lst[i])
        print((" " + str(len(food_items) +1) + ")").rjust(4) + " Abandon Ship!")
        print()
        opt_key = int(input("Select a number: "))
        if opt_key in valid_opt_lst:
            if remove:
                return opt_key-1
            else:
                return food_items[opt_key-1]
        else:
            return False
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#


    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GIVEN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
    def remove_item(self):
        '''
        This method will delete a FoodItem from the self.selections list.
        The print_items_in_list static method will be called to display the current
        (if any) items as well as ask the user to select the item the wish to 
        delete. 
        Your Optional Task:
            Analyze the given code, ask question if you have any.
        '''
        if len(self.selections) != 0:
            item_key = SandwichShop.print_items_in_list(self.selections, True)
            if item_key == 0 or item_key:
                del self.selections[item_key] #Removing FoodItem 
            else:
                print("No item removed!")
        else:
            print("No items to remove!")
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#


    def add_item(self, code):
        '''
        This method takes one integer parameter, code, that represents a key 
        for the self.storage instance variable. 

        The overall purpose of this method is to append to the self.selections 
        list instance variable. 
        '''
        if code != 6:

            #----------------------------- TO DO ITEM #4 -----------------------------#
            #                                                                         #
            #  Your task is to append a FoodItem to the self.selections instance      #
            #  variable. You will need to call the print_items_in_list static method  #
            #  which returns the correct FoodItem to append to the list. Again, the   #
            #  prints_items_in_list method returns the FoodItem, all you have to do   #
            #  is pass in the correct parameter for the method.                       #
            #                                                                         #
            #  HINT: You need to use the self.storage dictionary!                     #
            #                                                                         #
            #  After you have successfully completed the task above, check if the     #
            #  value that was returned is not False if this is true go ahead and      #
            #  append the FoodItem otherwise print the following message "Nothing     #
            #  selected!"                                                             #
            #-------------------------------------------------------------------------#
            self.selections.append(self.print_items_in_list(self.storage[code]))
            ###################### Code in the space above!!! ###########################
        else:
            print("No items added!")


    @staticmethod 
    def select_main_option():
        '''
        This static method displays a menu with 3 options. A user will be asked
        to select a number that corresponds to a desired option. If the number
        selected is valid then the method will return it, otherwise the user
        is notified and is prompted to try again. This is the main menu for the
        sandwich shop. A user will have the option to add and remove items and
        decide when their order is complete. 
        '''
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GIVEN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
        print()
        print(" Construct Sandwich ".center(50, '-'))
        print("1) Add Item")
        print("2) Remove Item")
        print("3) All Done!")
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

        #------------------------------ TO DO ITEM #5 ------------------------------#
        #  Your task is to create a loop that will continue to ask the user         #
        #  to "Select a number". If the user selects a valid number then return      #
        #  the number, otherwise notify the user by printing the following message  #
        #  "Not an option try again!" and continue the process. Determine what is   #
        #  valid in terms of user input, from the code that is given above.         #
        # --------------------------------------------------------------------------#
        choice = int(input("Select a number: "))
        while choice not in [1, 2, 3]:
            print("Not an option try again!")
            choice = int(input("Select a number: "))
        return choice

    @staticmethod
    def select_sandwich_options():
        '''
        This static method displays a menu with 6 options. A user will be asked
        to select a number that corresponds to a desired option. If the number
        selected is valid then the method will return it, otherwise the user
        is notified and is prompted to try again. The menu for this method
        shows 5 food categories: Bread, Cheese, Meat, Vegetable, and Sauce. 
        The 6th option, "Abort!", is provided just in case the user does not
        wish to select an option.
        '''
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GIVEN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
        print()
        print(" Select an Item ".center(50, '-'))
        print("1) Bread")
        print("2) Cheese")
        print("3) Meat")
        print("4) Vegetable")
        print("5) Sauce")
        print("6) Abort!")
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

        #------------------------------ TO DO ITEM #6 ------------------------------#
        #  Your task is to create a loop that will continue to ask the user         #
        #  to "Select a number". If the user selects a valid number then return      #
        #  the number, otherwise notify the user by printing the following message  #
        #  "Not an option try again!" and continue the process. Determine what is   #
        #  valid in terms of user input from the code that is given above.          #
        #  Yes, this is basically the same task in TO DO ITEM #5 :)                 #
        # --------------------------------------------------------------------------#
        choice = int(input("Select a number for your sandwich option: "))
        while choice not in [1, 2, 3, 4, 5, 6]:
            print("Not an option try again!")
            choice = int(input("Select a number: "))
        return choice


def main():
    '''
    The main method will use the SandwichShop class to simulates a restaurant 
    that makes Virtual sandwiches YUM! Main will make use of the methods
    in the class.
    '''
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GIVEN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
    print("Welcome to The One and Only Virtual Sandwich Shop!")
    print()
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

    #------------------------------ TO DO ITEM #7 ------------------------------#
    #  Your task is to create a SandwichShop object and assign it to a          #
    #  variable. Recall that a SandwichShop object requires a name that         #
    #  represents a person.                                                     #
    #                                                                           #
    #   Before you create a SanwichShop object, ask the user for their name    #
    #   using the following string "Please enter your name: ". Now you have a   #
    #   name, create the object!                                                #
    #   This can be done in one line of code.                                   #
    # --------------------------------------------------------------------------#
    buy = SandwichShop(input("Please enter your name: "))

    print()

    #------------------------------ TO DO ITEM #8 --------------------------------#
    #  Your task is to simulate the ENTIRE virtual sandwich shop experience.      #
    #  Steps:                                                                     # 
    #     1) Create a while loop that is controlled by a boolean.                 #
    #     2) Assign a variable to the method call of select_main_options from the #
    #        SandwichShop class. Note that this method returns either 1,2 or 3    #
    #     3) Check if the variable holds the value of 1 if this is true assign    #
    #        a new variable to the method call of select_sandwich_options. Recall #
    #        that select_sandwich_options returns a number. Next call the         #
    #        add_item method and pass in the number returned as an argument.      #
    #     4) Else if the number is 2 call the remove_item method.                 #
    #     5) Else if the number is 3 print your SandhwichShop object and break    #
    #        the loop.                                                            #
    # ----------------------------------------------------------------------------#
    done = False
    while not done:
        choice = buy.select_main_option()
        if choice == 1:
            option = buy.select_sandwich_options()
            buy.add_item(option)
        elif choice == 2:
            buy.remove_item()
        elif choice == 3:
            repr(buy)
            done = True




    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GIVEN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
    print()
    print("Enjoy!")
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

if __name__ == '__main__':
    main()
            
        