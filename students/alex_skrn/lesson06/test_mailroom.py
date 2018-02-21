"""Provide pytest unit tests for the mailroom assignment."""
import pytest
from unittest.mock import Mock
import mailroom


@pytest.fixture()
def donors():
    """Provide a data structure for the tests."""
    mailroom.donors = {"A": [1, 2, 3], "B": [3, 4, 5]}
    yield mailroom.donors


# @pytest.fixture()
# def main_dispatch():
#     """Provide a dispatch dict for the tests."""
#     main_dispatch = {"1": mailroom.send_thank_you_interaction,
#                      "2": mailroom.create_report,
#                      "3": mailroom.send_all_menu,
#                      "4": mailroom.quit,
#                      }
#     return main_dispatch


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
    # WHEN the user enters zero when prompted to enter an amount
    # THEN the function should return False
    monkeypatch.setattr('builtins.input', lambda _: "0")
    assert mailroom.input_donation("A") is False


# def test_input_donation_str(monkeypatch, capsys, donors):
#     """input_donation(name) with user entering a str instead of a number."""
#     # WHEN the user enters a string when prompted to enter an amount
#     # THEN the function should print a statement and re-prompt
#     monkeypatch.setattr('builtins.input', lambda _: "any_string")
#     mailroom.input_donation("A")
#     out, _ = capsys.readouterr()
#     assert out == "Input must be a number"


def test_input_donation_number(monkeypatch, donors):
    """input_donation(name) with the user entering a number."""
    # WHEN the user enters a number (not 0) when prompted to enter an amount
    # THEN the function should return True and the amount must be added
    monkeypatch.setattr('builtins.input', lambda _: "300")
    assert mailroom.input_donation("A") is True
    assert mailroom.donors["A"][-1] == 300


def test_old_donor_interaction_user_input_zero(monkeypatch):
    """_old_donor_interaction() user enters zero on prompt."""
    # WHEN the user enters zero when prompted to enter a name
    # THEN the function should return
    monkeypatch.setattr('builtins.input', lambda _: "0")
    assert mailroom.old_donor_interaction() is None


# def test_old_donor_interaction_user_input_non_exist(monkeypatch):
#     """_old_donor_interaction() user enters a non-existing name."""
#     # WHEN the user enters a name not in the dict
#     # THEN the function should re-prompt
#     monkeypatch.setattr('builtins.input', lambda _: "any_string")
#     assert ?????????

#
# def test_old_donor_interaction_user_input_valid_name(monkeypatch):
#     """_old_donor_interaction() user enters a non-existing name."""
#     # WHEN the user enters a valid name in the dict
#     # THEN the function should print email and return
#     monkeypatch.setattr('builtins.input', lambda _: "A")
#     assert ?????????


def test_new_donor_interaction_user_input_zero(monkeypatch):
    """new_donor_interaction() user enters 0 on promp."""
    # WHEN the user enters zero when prompted to enter a name
    # THEN the function should return
    monkeypatch.setattr('builtins.input', lambda _: "0")
    assert mailroom.new_donor_interaction() is None


def test_new_donor_interaction_user_input_name(monkeypatch, capsys):
    """new_donor_interaction(); User enters a name on prompt."""
    # WHEN the user enters a name when prompted to enter a name
    # THEN the function should print the thank-you email
    monkeypatch.setattr('builtins.input', lambda _: "Any_name")
    # Fake all functions inside new_donor_interaction()
    email_text = ("""\nDear Alex,\n
                  \nI would like to thank you for your donation of $15.5.\n
                  \nWe appreciate your support.\n
                  \nSincerely,\n
                  \nThe Organization\n
                  """)
    mailroom.get_email = Mock()
    mailroom.get_email.return_value = email_text

    mailroom.input_donation = Mock()
    mailroom.input_donation.return_value = True

    mailroom.get_last_donation = Mock()
    mailroom.get_last_donation.return_value = True

    mailroom.new_donor_interaction()
    out, _ = capsys.readouterr()
    assert out.strip() == email_text.strip()


def test_write_file(tmpdir):
    """write_file()."""
    # GIVEN a destination path and an email text
    # WHEN the function is called with such parameters
    # THEN it opens the file for writing and writes to it the email
    file = tmpdir.join('output.txt')
    mailroom.write_file(file.strpath, "some text")  # or str(file)
    assert file.read() == "some text"


def test_write_cwd(monkeypatch, tmpdir, capsys, donors):
    """write_cwd() User writes all emails to cwd."""
    # Check that the print statement in the function is okey
    # Check that the function indeed created 2 files
    # Check that the files created are not empty at least
    monkeypatch.chdir(tmpdir)
    mailroom.write_cwd()
    out, _ = capsys.readouterr()  # out has an extra \n, hence .strip() below
    result = ("\nAll letters saved in {}\n".format(str(tmpdir))).strip()
    assert out.strip() == result
    assert len(tmpdir.listdir()) == 2
    for file in tmpdir.listdir():
        assert bool(file.read()) is True


def test_write_select_dir(tmpdir, capsys, donors):
    """write_select_dir(). User selects a directory."""
    # Check that the print statement in the function is okey
    # Check that the function indeed created 2 files
    # Check that the files created are not empty at least
    mailroom.ask_user_dir = Mock()
    mailroom.ask_user_dir.return_value = tmpdir
    mailroom.write_select_dir()
    out, _ = capsys.readouterr()
    result = ("\nAll letters saved in {}\n".format(str(tmpdir))).strip()
    assert out.strip() == result
    assert len(tmpdir.listdir()) == 2
    for file in tmpdir.listdir():
        assert bool(file.read()) is True


def test_write_select_dir_user_cancel():
    """In write_select_dir() the user hits cancel."""
    # When the user hits cancel when asked to select a directory
    # Then the function should return
    mailroom.ask_user_dir = Mock()
    mailroom.ask_user_dir.return_value = ""
    assert mailroom.write_select_dir() is None


# def test_menu_selection_user_choice_quit(monkeypatch):
#     """menu_selection(). User chooses 4 to quit."""
#     monkeypatch.setattr('builtins.input', lambda _: "4")
#     assert mailroom.menu_selection("Select >>", main_dispatch()) is None


# def test_menu_selection_user_choice_invalid(monkeypatch, capsys):
#     """menu_selection(). User enters an invalid choice."""
#     monkeypatch.setattr('builtins.input', lambda _: "invalid_input")
#     mailroom.menu_selection("Select >>", main_dispatch())
#     assert 0
#     out, _ = capsys.readouterr()
#     # print(repr(out))
#     assert out.strip() == "\nInvalid choice. Try again".strip()
