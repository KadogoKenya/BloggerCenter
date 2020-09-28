import unittest
from app.models import User

class UserTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(username="Ndundiro", email = "ndudndiro@proj.com", password="pass123")


    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)


    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password("12345"))





         
import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
    
    def setUp(self):
        self.new_user = User(id = 1, username = "ndundiro", email = "ndundirokamau@gnail.com", password = "12345")
        
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,User))
        
        
    def tearDown(self):
        User.query.delete()
        
        
    def test_password_setter(self):
        self.assertTrue(self.new_user.password is not None)
        

            
    def test_password_verification(self): 
        
        self.assertTrue(self.new_user.verify_password('12345'))