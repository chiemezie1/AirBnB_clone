#!/usr/bin/python3
"""Unittest for FileStorage class"""

import os
import unittest

import models

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up for the tests"""
        self.storage = models.storage

    def test_file_path(self):
        """Test the file_path attribute"""
        self.assertIsInstance(self.storage._FileStorage__file_path, str)

    def test_objects(self):
        """Test the objects attribute"""
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all(self):
        """Test the all method"""
        obj = BaseModel()
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)
        self.assertIn("BaseModel.{}".format(obj.id), objects)

    def test_new(self):
        """Test the new method"""
        obj = BaseModel()
        obj_id = obj.id
        self.assertIn("BaseModel.{}".format(obj_id),
                      self.storage._FileStorage__objects)

    def test_save(self):
        """Test the save method"""
        obj = BaseModel()
        obj.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload(self):
        """Test the reload method"""
        obj = BaseModel()
        obj.save()
        obj_id = obj.id
        self.storage.reload()
        objects = self.storage.all()
        self.assertIn("BaseModel.{}".format(obj_id), objects)

    def test_instance(self):
        """Test for FileStorage instance"""
        instance = FileStorage()
        self.assertIsInstance(instance, FileStorage)

    def test_file_path(self):
        """Test the file_path attribute"""
        self.assertIsInstance(self.storage._FileStorage__file_path, str)

    def test_objects(self):
        """Test the objects attribute"""
        self.assertIsInstance(self.storage._FileStorage__objects, dict)


if __name__ == "__main__":
    unittest.main()
