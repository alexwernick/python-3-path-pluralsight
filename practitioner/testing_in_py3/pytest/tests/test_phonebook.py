import pytest

def test_lookup_by_name(phonebook):
    phonebook.add("Bob", "12345")
    number = phonebook.lookup("Bob")
    assert number == "12345"

def test_contains_all_names(phonebook):
    phonebook.add("Bob", "12345")
    assert phonebook.all_names() == {"Bob"}

def test_missing_name(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")

@pytest.mark.parametrize(
        "entry1,entry2,is_consistent", [
        (("Bob", "12345"), ("Anna", "0123"), True),
        (("Bob", "12345"), ("Anna", "12345"), False),
        (("Bob", "12345"), ("Anna", "1234"), False)
    ]
)
def test_is_consistent(phonebook, entry1, entry2, is_consistent):
    phonebook.add(*entry1)
    phonebook.add(*entry2)
    assert phonebook.is_consistent() == is_consistent