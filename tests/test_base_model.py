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

#!/usr/bin/python3#
"""Unittest for BaseModel class"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.model = BaseModel()
        self.model.name = "My First Model"
        self.model.my_number = 89

    def test_init(self):
        """Test the initialization of the BaseModel instance"""
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertEqual(self.model.name, "My First Model")
        self.assertEqual(self.model.my_number, 89)

    def test_unique_id(self):
        """Test that each instance has a unique id"""
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_save(self):
        """Test the save method updates the updated_at attribute"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)
        self.assertTrue(self.model.updated_at > old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method"""
        model_dict = self.model.to_dict()
        time_cr = model_dict['created_at']
        time_up = model_dict['updated_at']
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['name'], 'My First Model')
        self.assertEqual(model_dict['my_number'], 89)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertEqual(format_datetime(time_cr), self.model.created_at)
        self.assertEqual(format_datetime(time_up), self.model.updated_at)

    def test_str(self):
        """Test the __str__ method"""
        model_str = str(self.model)
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(model_str, expected_str)

    def test_init_kwargs(self):
        """Test initialization with kwargs"""
        sample_data = '2024-05-17T12:00:00.000000'
        kwargs = {
            'id': '123456',
            'created_at': sample_data,
            'updated_at': sample_data,
            'name': 'My Deserialized Model',
            'my_number': 42
        }
        model2 = BaseModel(**kwargs)

        self.assertEqual(model2.id, '123456')
        self.assertEqual(model2.created_at, format_datetime(sample_data))
        self.assertEqual(model2.updated_at, format_datetime(sample_data))
        self.assertEqual(model2.name, 'My Deserialized Model')
        self.assertEqual(model2.my_number, 42)


def format_datetime(datetime_str):
    """Format datetime string"""
    return datetime.fromisoformat(datetime_str)


if __name__ == '__main__':
    unittest.main()
