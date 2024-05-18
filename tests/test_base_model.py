from datetime import datetime
import unittest


from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_instance(self):
        """Test for BaseModel instance"""
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)

    def test_id(self):
        """Test for BaseModel id"""
        instance = BaseModel()
        self.assertIsInstance(instance.id, str)

    def test_created_at(self):
        """Test for BaseModel created_at"""
        instance = BaseModel()
        self.assertIsInstance(instance.created_at, datetime)

    def test_updated_at(self):
        """Test for BaseModel updated_at"""
        instance = BaseModel()
        self.assertIsInstance(instance.updated_at, datetime)

    def test_str(self):
        """Test for BaseModel __str__ method"""
        instance = BaseModel()
        self.assertIsInstance(str(instance), str)

    def test_save(self):
        """Test for BaseModel save method"""
        instance = BaseModel()
        updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(updated_at, instance.updated_at)

    def test_to_dict(self):
        """Test for BaseModel to_dict method"""
        instance = BaseModel()
        self.assertIsInstance(instance.to_dict(), dict)

    def test_to_dict_class(self):
        """Test for BaseModel __class__ key in to dict"""
        instance = BaseModel()
        self.assertEqual(instance.to_dict()["__class__"], "BaseModel")
