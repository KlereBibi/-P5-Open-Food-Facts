# coding: utf-8 

"""This module contains the main function of the application"""

from models.managers.apimanager import ApiManager

def main():

    """Main function of the game. """

    run = ApiManager()
    run.save_data()

if __name__ == '__main__':
    main()