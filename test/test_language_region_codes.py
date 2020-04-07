#!/usr/bin/env python3

import pytest

from language_region_utilities.validator import LanguageRegionValidator


# Test the normalize() method
def test_normalize():
    validator = LanguageRegionValidator()

    # In our normalized form, letters are lowercased, and
    # the hyphen is the separator.
    assert validator.normalize("enus") == "en-us"
    assert validator.normalize("ENUS") == "en-us"
    assert validator.normalize("ENus") == "en-us"
    assert validator.normalize("EnUs") == "en-us"
    assert validator.normalize("en-us") == "en-us"
    assert validator.normalize("en-US") == "en-us"
    assert validator.normalize("en_us") == "en-us"
    assert validator.normalize("en_US") == "en-us"

    # If the code can't be normalized, an exception should be thrown.
    with pytest.raises(ValueError):
        normalized = validator.normalize("This is not a valid code.")


# Test the is_likely() method
def test_is_likely():
    validator = LanguageRegionValidator()

    # Language/region combinations which are both valid and likely
    assert validator.is_likely("en-us")
    assert validator.is_likely("ja-jp")
    assert validator.is_likely("de-de")
    assert validator.is_likely("so-so")
    assert validator.is_likely("ps-af")

    # Invalid language and region codes
    # (Neither is officially assigned)
    assert not validator.is_likely("qq-xx")

    # Valid language and region codes, but unlikely combination
    assert not validator.is_likely("mn-ie")
    assert not validator.is_likely("cs-jm")

