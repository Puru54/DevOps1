import unittest
from app import MESSAGE, Handler
 
class AppTests(unittest.TestCase):
    def test_default_message_exists(self):
        self.assertTrue(MESSAGE)
 
    def test_handler_is_defined(self):
        self.assertTrue(Handler)
 
if __name__ == "__main__":
    unittest.main()
