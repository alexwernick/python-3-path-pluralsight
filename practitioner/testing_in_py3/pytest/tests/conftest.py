# test/test_my_module.py
import sys
import os

# I know this below code is terrible but need to figure out the proper way to handle this later
# Add the src directory to the system path
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
if src_path not in sys.path:
    sys.path.append(src_path)


from phonebook import Phonebook
import pytest

@pytest.fixture
def phonebook(tmpdir):
    "Provides an empty Phonebook"
    phonebook = Phonebook(tmpdir)
    yield phonebook
    phonebook.clear()