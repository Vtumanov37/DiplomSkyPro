import configparser
import pytest

config = configparser.ConfigParser()
config.read('test_config.ini')

# @pytest.mark.skip()
def test_conf():

    prop_int = config["sectionA"].getint("prop_int") #Число

    print(prop_int)