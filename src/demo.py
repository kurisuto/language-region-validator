#!/usr/bin/env python3

from language_region_utilities.validator import LanguageRegionValidator


def main():

    validator = LanguageRegionValidator()

    # The following demonstrates how we internally normalize
    # language/region codes.
    print(validator.normalize("en-us"))
    print(validator.normalize("en_US"))
    print(validator.normalize("enus"))


    # The following returns True, because en-us (English as written in
    # the United States) is a likely language/region combination.
    print(validator.is_likely("ENUS"))

    # The following returns False, because mn-ie (Mongolian as written
    # in Ireland) is a valid but unlikely language/region combination.
    print(validator.is_likely("mn-ie"))


if __name__ == "__main__":
    main()

