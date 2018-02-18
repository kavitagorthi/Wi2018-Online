"""Provide pytest unit tests for the mailroom assignment."""
import pytest
import mailroom


@pytest.fixture()
def donors():
    """Provide a data structure for the tests."""
    mailroom.donors = {"A": [1, 2, 3], "B": [3, 4, 5]}
    yield mailroom.donors


def test_add_new_donor_donation(donors):
    """add_donation(name, amount) for a new donor."""
    # GIVEN a dict of 2 donors with 3 donations each
    # WHEN a new donor and his donation is added to the dict
    # THEN the donors dict must contain a record for this
    mailroom.add_donation("Alex Skrn", 0.0)
    assert mailroom.donors["Alex Skrn"] == [0.0]


def test_add_exist_donor_donation(donors):
    """add_donation(name, amount) for an existing donor."""
    # GIVEN a dict of 2 donors with 3 donations each
    # WHEN an existing  donor gives a donation
    # THEN his record in the donors dict must contain this donation
    mailroom.add_donation("A", 1000.0)
    assert mailroom.donors["A"][-1] == 1000.0


def test_get_last_donation(donors):
    """get_last_donation(name) for a given donor."""
    # GIVEN a dict of 2 donors with 3 donations each
    # WHEN the function is called with an existing name
    # THEN its return value should match the last item in the relevant list
    assert mailroom.get_last_donation("B") == 5


def test_get_donations(donors):
    """get_donations(name) for a given donor."""
    # GIVEN a dict of 2 donors with 3 donations each
    # WHEN the function is called with an existing name
    # THEN its return value should match the corresponding list
    assert mailroom.get_donations("A") == [1, 2, 3]


def test_get_total_given(donors):
    """get_total_given(name) for a given donor."""
    # GIVEN a dict of 2 donors with 3 donations each
    # WHEN the function is called with an existing name
    # THEN its return value should match the total calculated manually
    assert mailroom.get_total_given("B") == 12


def test_sort_donors_by_total(donors):
    """sort_donors_by_total()."""
    # GIVEN a dict of 2 donors with 3 donations each
    # WHEN the function is called
    # THEN it should return the following list
    assert mailroom.sort_donors_by_total() == ["B", "A"]


def test_print_donor_names(capsys, donors):
    """print_donor_names()."""
    mailroom.print_donor_names()
    out, _ = capsys.readouterr()
    assert out == "\nA, B\n"


def test_get_email():
    """get_email(name, amount)."""
    result = ("""\nDear A,\n
                  \nI would like to thank you for your donation of $100.\n
                  \nWe appreciate your support.\n
                  \nSincerely,\n
                  \nThe Organization\n
                  """)
    assert mailroom.get_email("A", 100) == result


def test_input_donation_zero(monkeypatch):
    """input_donation(name) with the user entering zero."""
    # GIVEN ?????
    # WHEN the user enters zero when prompted to enter an amount
    # THEN the function should return False
    monkeypatch.setattr('builtins.input', lambda x: "0")
    assert mailroom.input_donation("A") is False


# def test_input_donation_str(monkeypatch, capsys, donors):
#     """input_donation(name) with user entering a string instead of a number."""
#     # GIVEN ?????
#     # WHEN the user enters a string when prompted to enter an amount
#     # THEN the function should print a statement and re-prompt
#     monkeypatch.setattr('builtins.input', lambda x: "any_string")
#     mailroom.input_donation("A")
#     out, _ = capsys.readouterr()
#     assert out == "Input must be a number"


def test_input_donation_number(monkeypatch, donors):
    """input_donation(name) with the user entering a number."""
    # GIVEN the donors dict and ???
    # WHEN the user enters a number (not 0) when prompted to enter an amount
    # THEN the function should return True and the amount must be added
    monkeypatch.setattr('builtins.input', lambda x: "300")
    assert mailroom.input_donation("A") is True
    assert mailroom.donors["A"][-1] == 300


def test_existing_donor_interaction_user_input_zero(monkeypatch):
    """_existing_donor_interaction() user enters zero on prompt."""
    # GIVEN ?????
    # WHEN the user enters zero when prompted to enter a name
    # THEN the function should return
    monkeypatch.setattr('builtins.input', lambda x: "0")
    assert mailroom.existing_donor_interaction() is None


# def test_existing_donor_interaction_user_input_non_exit(monkeypatch):
#     """_existing_donor_interaction() user enters a non-existing name."""
#     # GIVEN ?????
#     # WHEN the user enters a name not in the dict
#     # THEN the function should re-prompt
#     monkeypatch.setattr('builtins.input', lambda x: "any_string")
#     assert ?????????

#
# def test_existing_donor_interaction_user_input_valid_name(monkeypatch):
#     """_existing_donor_interaction() user enters a non-existing name."""
#     # GIVEN ?????
#     # WHEN the user enters a valid name in the dict
#     # THEN the function should print email and return
#     monkeypatch.setattr('builtins.input', lambda x: "A")
#     assert ?????????


def test_new_donor_interaction_user_input_zero(monkeypatch):
    """new_donor_interaction() user enters 0 on promp."""
    # GIVEN ?????.
    # WHEN the user enters zero when prompted to enter a name.
    # THEN the function should return.
    monkeypatch.setattr('builtins.input', lambda x: "0")
    assert mailroom.new_donor_interaction() is None


def test_write_file(tmpdir):
    """write_file()."""
    # GIVEN a destination path and an email text
    # WHEN the function is called with such parameters
    # THEN it opens the file for writing and writes to it the email
    file = tmpdir.join('output.txt')
    mailroom.write_file(file.strpath, "some text")  # or str(file)
    assert bool(file.read()) is True
