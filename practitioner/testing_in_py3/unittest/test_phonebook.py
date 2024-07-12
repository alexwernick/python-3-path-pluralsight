import unittest
from phonebook import Phonebook 

class PhonebookTest(unittest.TestCase):

    def setUp(self) -> None:
        self.phonebook = Phonebook()
    
    def tearDown(self) -> None:
        pass

    def test_lookup_by_name(self):
        self.phonebook.add("Bob", "12345")
        number = self.phonebook.lookup("Bob")

        self.assertEqual(number, "12345")

    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    def test_empty_phonebook_is_consistent(self):
        is_consistent = self.phonebook.is_consistent()
        self.assertTrue(is_consistent)

    def test_is_consistent_when_all_different(self):
        self.phonebook.add("Bob", "12345")
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Anna", "012345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_inconsistent_when_two_identical(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Sue", "12345") # identical to bob
        self.assertFalse(self.phonebook.is_consistent())
        
    def test_is_inconsistent_when_one_contains_prefix_of_another(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Sam", "1234") # prefix of bob
        self.assertFalse(self.phonebook.is_consistent())

