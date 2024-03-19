import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """
    Class for testing the BaseModel class
    """
    
    def setUp(self) -> None:
        """
        Sets up the object needed for the tests
        """
        self.testBaseModel = BaseModel()
    
    def test_save(self):
        """
        Test the method .save() from the object
        """
        self.testBaseModel.save()
        self.assertEqual(self.testBaseModel.updated_at, datetime.now())
        
    def test_to_dict(self):
        """
        Test the method .to_dict() from the object
        """
        test_dictionary = self.testBaseModel.to_dict()
        self.assertTrue(isinstance(test_dictionary, dict))
        
    
    