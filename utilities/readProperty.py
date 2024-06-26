import configparser
import os

# Construct the path to config.ini using os.path.join
# config_file_path = os.path.join(os.path.abspath(os.curdir), 'configurations', 'config.ini')
# config_file_path = config_file_path = os.path.join(os.path.abspath(os.curdir), 'config.ini')
config_file_path = "C:\\Users\\ajay\\classyclix\\configurations\\config.ini"
# Initialize ConfigParser and read the config file
config = configparser.RawConfigParser()
config.read(config_file_path)
class Readconfig:
    @staticmethod
    def get_application_url():
        return config.get('commonInfo', 'baseURL')

    @staticmethod
    def get_login_email():
        return config.get('commonInfo', 'userEmail')

    @staticmethod
    def get_login_password():
        return config.get('commonInfo', 'userPassword')





"""
import configparser
import os


class ReadConfig:
    @staticmethod
    def get_application_url():
        config = configparser.RawConfigParser()
        config.read(os.path.join(os.path.abspath(os.curdir), 'configurations', 'config.ini'))
        baseURL = config.get('commonInfo', 'baseURL')
        print(baseURL)
        return baseURL

        
        

    @staticmethod
    def get_login_email():
        config = configparser.RawConfigParser()
        config.read(os.path.join(os.path.abspath(os.curdir), 'configuration', 'config.ini'))
        login_email = config.get('commonInfo', 'UserEmail')
        return login_email

    @staticmethod
    def get_login_password():
        config = configparser.RawConfigParser()
        config.read(os.path.join(os.path.abspath(os.curdir), 'configuration', 'config.ini'))
        login_password = config.get('commonInfo', 'password')
        return login_password


import configparser
import os


class ReadConfig:
    config = configparser.RawConfigParser()
    config.read(os.path.join(os.path.abspath(os.curdir), 'configuration', 'config.ini'))

    @staticmethod
    def get_application_url():
        return ReadConfig.config.get('commonInfo', 'baseURL')

    @staticmethod
    def get_login_email():
        return ReadConfig.config.get('commonInfo', 'UserEmail')

    @staticmethod
    def get_login_password():
        return ReadConfig.config.get('commonInfo', 'password')
"""