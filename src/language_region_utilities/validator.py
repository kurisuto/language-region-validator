#!/usr/bin/env python3
import sys
import os
import logging
import re

logging.basicConfig(format='%(message)s', level=logging.INFO)


class LanguageRegionValidator:

    def _read_language_region_codes(self):

        likely_codes = set()
        
        script_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(script_directory)
        pathname = os.path.join(parent_directory, "data", "language_region_codes.txt")
    
        with open(pathname, 'r') as inputfile:
            for line in inputfile:
                line = line.strip()

                if line.startswith("#"):
                    continue

                code, language, region = line.split("\t")
                likely_codes.add(code)

        return(likely_codes)
                
                
    
    def __init__(self):
        self.likely_codes = self._read_language_region_codes()

        self.VALID_CODE = re.compile("[a-z][a-z][-_]?[a-z][a-z]$", re.ASCII | re.IGNORECASE)




    # The ISO standards don't specify whether the language/region
    # codes should be in uppercase or lowercase.  They also don't
    # specify whether there should be any separator between the
    # language code and the region code, or what that separator should
    # be.  All of these are valid: enus en-us en-US EN_US EnUs
        
    # We internally normalize them to the form en-us.  If it's a form
    # we can't normalize, we throw an exception.  There's no checking
    # here as to whether the language code or region code is officially
    # assigned.

    def normalize(self, code):

        if not re.match(self.VALID_CODE, code):
            raise ValueError(f"Could not normalize {code}.")        

        code = code.lower()

        if len(code) == 4:
            code = code[0:2] + "-" + code[2:4]

        code = code.replace("_", "-")

        return code
        

    def is_likely(self, code):
        normalized = self.normalize(code)
        return normalized in self.likely_codes

    
