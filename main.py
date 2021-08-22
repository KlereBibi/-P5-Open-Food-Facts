"""This module contains the main function of the application"""

from controllers.controller import Controller


if __name__ == '__main__':

    run = Controller()
    run.chek_database()
