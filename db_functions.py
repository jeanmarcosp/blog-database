# Xenia Dela Cueva
# Jeanmarcos Perez
# Lab 4
# Creates the server string using our config file

from configparser import ConfigParser


def read_db_config(filename='config.ini', section='mongodb'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return db

# takes the parser dictionary and converts it to mongo server string to pass in to connect
def create_mongo_server():
    mongo_dict = read_db_config()

    server_string= mongo_dict['server']
    server_string += mongo_dict['username'] + ':'
    server_string += mongo_dict['password'] + '@'
    server_string += mongo_dict['cluster']
    server_string += "/test"

    return server_string
