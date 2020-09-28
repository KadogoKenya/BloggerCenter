 
import unittest
from app.models import Blog

class BlogModelTest(unittest.TestCase):
    

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
         self.new_user = User(username='Ndundiro'email = "ndudndiro@proj.com" password="pass123")
        self.new_blog = Blog(title = 'Dont worry be happy', body = 'Life is what you make it.', posted =2/14/2019, id = 1, post_id = 1)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog,Blog))
        
        
    def tearDown(self):
        Post.query.delete()
        
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.id,1)
        self.assertEquals(self.new_blog.post_id,1)
        self.assertEquals(self.new_blog.title,"Dont worry be happy")
        self.assertEquals(self.new_blog.body,"Life is what you make it.")
        self.assertEquals(self.new_blog.posted,2/14/2019)
  


    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all())>0)

    def test_get_blog_by_id(self):
        self.new_blog.save_blog()
        got_blogs = Blog.get_blog(1)
        self.assertTrue(len(got_blogs) == 1)