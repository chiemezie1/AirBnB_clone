#!/usr/bin/python3
"""Unittest for The console"""

import unittest
import os
from io import StringIO
from unittest.mock import patch
import json

import models

from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test cases for the console"""

    def setUp(self):
        """Set up for the tests"""
        self.console = HBNBCommand()
        storage = models.storage

    def test_prompt(self):
        """Test the prompt"""
        self.assertEqual("(hbnb) ", self.console.prompt)

    def test_emptyline(self):
        """Test empty line"""
        self.assertFalse(self.console.onecmd("\n"))

    def test_quit(self):
        """Test quit command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertTrue(f.getvalue().startswith(""))

    def test_EOF(self):
        """Test EOF command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertTrue(f.getvalue().startswith(""))

    def test_create(self):
        """Test create command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create"))
            self.assertTrue(f.getvalue().startswith(
                "** class name missing **\n"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create Bobo"))
            self.assertTrue(f.getvalue().startswith(
                "** class doesn't exist **\n"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create User"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create User id"))
            self.assertTrue(f.getvalue().startswith(
                "** class doesn't exist **\n"))

        with patch("sys.stdout", new=StringIO()) as f:
            old_storage = models.storage.all().copy()
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
            user_key = "User." + user_id
            self.assertTrue(user_key in models.storage.all().keys())

    def test_show(self):
        """Test show command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show"))
            self.assertTrue(f.getvalue().startswith(
                "** class name missing **\n"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show Bobo"))
            self.assertTrue(f.getvalue().startswith(
                "** class doesn't exist **\n"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show User"))
            self.assertTrue(f.getvalue().startswith(
                "** instance id missing **\n"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show User id"))
            self.assertTrue(f.getvalue().startswith(
                "** no instance found **\n"))

    def test_destroy(self):
        """Test destroy command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy"))
            self.assertTrue(f.getvalue().startswith(
                "** class name missing **\n"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy Bobo"))
            self.assertTrue(f.getvalue().startswith(
                "** class doesn't exist **\n"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy User"))
            self.assertTrue(f.getvalue().startswith(
                "** instance id missing **\n"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy User id"))
            self.assertTrue(f.getvalue().startswith(
                "** no instance found **\n"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
            user_key = "User." + user_id
            self.assertTrue(user_key in models.storage.all().keys())
            self.assertFalse(self.console.onecmd("destroy User " + user_id))
            self.assertFalse(user_key in models.storage.all().keys())

    def test_all(self):
        """Test all command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("all"))
            self.assertTrue(f.getvalue().startswith(
                "** class doesn't exist **\n"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("all Bobo"))
            self.assertTrue(f.getvalue().startswith(
                "** class doesn't exist **\n"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("all User"))
            output = f.getvalue().strip()
            self.assertTrue(output.startswith("["))
            self.assertTrue(output.endswith("]"))
            objects_array = json.loads(output)
            self.assertIsInstance(objects_array, list)
            users_count = len(
                [obj for obj in models.storage.all().keys() if "User" in obj])
            self.assertEqual(len(objects_array), users_count)

    def test_update(self):
        """Test update command"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update"))
            self.assertTrue(f.getvalue().startswith(
                "** class name missing **\n"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update Bobo"))
            self.assertTrue(f.getvalue().startswith(
                "** class doesn't exist **\n"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update User"))
            self.assertTrue(f.getvalue().startswith(
                "** instance id missing **\n"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update User id"))
            self.assertTrue(f.getvalue().startswith(
                "** no instance found **\n"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
            user_key = "User." + user_id
            self.assertTrue(user_key in models.storage.all().keys())
            self.console.onecmd("update User " + user_id + " first_name Bobo")
            user = models.storage.all()[user_key]
            self.assertTrue(hasattr(user, "first_name"))
            self.assertEqual(user.first_name, "Bobo")
