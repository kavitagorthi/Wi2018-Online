"""Provide pytest unit tests for the mailroom assignment."""
import pytest
import mailroom


@pytest.fixture
def donors():
    """Provide the data structure to be used by test functions."""
    return mailroom.donors


class TestAddDonation(object):
    """Test add_donation."""

    def test_add_donation(self):
        """Test addition of a donation for a new donor."""
        mydonors = donors()
        mailroom.add_donation("Alex Skrn", 0.0)
        assert mydonors["Alex Skrn"] == [0.0]

    def test_add_donation2(self):
        """Test addition of a donation for an existing donor."""
        mydonors = donors()
        mailroom.add_donation("El Lissitzky", 0)
        assert mydonors["El Lissitzky"] == [34.2, 30.0, 35.5, 0]
