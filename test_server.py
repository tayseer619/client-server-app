from ipaddress import ip_address
from pickle import TRUE
import unittest
import server
import pytest
import client



class TestCalc(unittest.TestCase):
    @pytest.mark.one
    def test_main(self):
        # result= server.main(server.IP,server.PORT)
        assert server.PORT == client.PORT

    @pytest.mark.two
    def test_name(self):
        # result= server.main(server.IP,server.PORT)
        assert server.myHostName == 'tayseer'

    # @pytest.mark.three
    # def test_3(self):
    #     result= server.
        
        
if __name__ == "__main__":
    unittest.main()





























# import unittest
# import sqlite3

# class DB:
#     def __init__(self, dbname='mydb.db'):
#         try:
#             self.connection = sqlite3.connect(dbname)
#         except:
#             print('Error')
#         finally:
#             pass

    

# class Hello:
#     def hi(self):
#         db = DB('sqlite3_database.db')
#         cursor = db.connection.cursor()

# db = DB('sqlite3_database.db')
# h = Hello() # make our instance
# h.hi() # use the method "hi" associated with the class (our function name within the class)
