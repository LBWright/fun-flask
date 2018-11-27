from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure login loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type="html/text")
        self.assertTrue(b'Please login' in response.data)

    # Ensure login behaves correctly with correct credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post(
          '/login',
          data=dict(username='admin', password='admin'),
          follow_redirects=True
        )
        self.assertIn(b'You were just logged in!', response.data)

    # Ensure login behaves correctly with incorrect credentials
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post(
          '/login',
          data=dict(username='admin', password='wrongpass'),
          follow_redirects=True
        )
        self.assertIn(b'Invalid credentials. Please try again', response.data)

    # Ensure logout behaves correctly  
    def test_logout_behavior(self):
        tester = app.test_client(self)
        tester.post(
          '/login',
          data=dict(username='admin', password='admin'),
          follow_redirects=True
        )
        response = tester.get(
          '/logout',
          follow_redirects=True
        )
        self.assertIn(b'You were just logged out!', response.data)

    # Ensure that the main page requires login
    def test_main_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type="html/text", follow_redirects=True)
        self.assertTrue(b'You need to login first.' in response.data)


    # Ensure that posts appear on main page
    def test_posts_appear(self):
        tester = app.test_client(self)
        tester.post(
          '/login',
          data=dict(username='admin', password='admin'),
          follow_redirects=True
        )
        response = tester.get('/')
        self.assertTrue(b'Posts' in response.data)

if __name__ == '__main__':
    unittest.main()