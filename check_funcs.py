#!/usr/bin/env python3
# This script contains helper functions for main
import re


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


def ID_CHECK(val):
    # Checks to make sure ID is a number.
    if (str is None):
        return (None)
    try:
        number = int(val)
    except ValueError:
        return (False)
    return (True)


def SALUTION_CHECK(val):
    # Check for one of three options
    if (val == "Mr." or val == "Ms." or val == "Dr."):
        return (True)
    return (False)


def FIRST_NAME_CHECK(val):
    # Just check only letters, first letter uppercase, no space after.
    # ADD: Check for uppercase letter in first letter.
    if (val is None):
        return (False)
    if (hasNumbers(val) is False and (' ' in val) is False and val[0] != " " or val[len(val) - 1] != " " and val[0].isupper() is True):
        return (True)
    return (False)


def MIDDLE_NAME_CHECK(val):
    # Focus on skipping
    if (val is None):
        return (True)
    if (hasNumbers(val) is False):
        return (True)
    return (False)


def LAST_NAME_CHECK(val):
    # Return true if only letters, no spaces before first or after last word.
    if (hasNumbers(val) is False and val[0] != " " and val[len(val) - 1] != " "):
        return (True)
    return (False)


def SUFFIX_CHECK(val):
    # JD, Ed.D, MBA, Esq, Ph.D, M.D, CFP, MA, MPH.
    # Can be a lot dont focvus and skip.
    return (True)


def PARTNER_CHECK(val):
    # so the only options are formal and student?
    if (val == "formal" or val == "student"):
        return (True)
    return (False)


def SCHOOL_CHECK(val):
    # check for spaces at first & last word, error if blank?
    # Check for uppercase on every word except of's?
    if (val is None):
        return (False)
    if (val is not None and val != " " and val != ""):
        return (True)
    if (val[0] == " " or val[len(val) - 1] == " "):
        return (False)
    return (False)


def INTERNSHIP_CHECK(val):
    # Check for spaces at first & last word.
    # Check for uppercase on every word except of's?
    # if blank give error,
    if (val is None):
        return (False)
    if (val[0] == " " or val[len(val) - 1] == " "):
        return (False)
    return (False)


def INTERNSHIP_TYPE_CHECK(val):
    # Check for spaces at first & last word unkless just one word?
    # give error if blank.
    if (val is None):
        return (False)
    if (val[0] == " " or val[len(val) - 1] == " "):
        return (False)
    return (False)


def PLACEMENT_CHECK(val):
    # Check for spaces at first & last word, error if blank?
    # give error if blank.
    if (val is None):
        return (False)
    if (val[0] == " " or val[len(val) - 1] == " "):
        return (False)
    return (False)


def PLACEMENT_DATE_CHECK(val):
    # Check for only these options and year.
    value = str(val).split()[0]
    try:
        year = int(val.split()[1])
    except ValueError:
        return (False)
    words = ["Summer", "Fall", "Spring", "Winter"]
    if (value in words):
        return (True)
    return (False)


def END_DATE_CHECK(val):
    # Ask if only these options otherwise confirm second word is a year.
    words = ["Summer", "Fall", "Spring", "Winter"]
    value = str(val).split()[0]
    if (val == "Permanent" or value in words):
        return (True)
    return (False)


def NEW_SOURCE_CHECK(val):
    # only employer and pesa? No other options.
    # make sure is not blank.
    if (val is None):
        return (False)
    if (val == "employer" or val == "PESA"):
        return (True)
    return (False)


def STATUS_CHECK(val):
    # only these 4 options otherwise error? if blank give error?
    # make sure is not blank.
    if (val is None):
        return (False)
    if (val == "citizen" or val == "permanent" or val == "visa"):
        return (True)
    if (val == "unknown"):
        return (True)
    return (False)


def FIRST_GEN_CHECK(val):
    # only these 2 options otherwise error? if blank give error
    if (val is None):
        return (False)
    if (val == "first" or val == "multiple" or val == "second"):
        return (True)
    if (val == "third"):
        return (True)
    return (False)


def INTERNATIONAL_CHECK(val):
    # only these 2 options otherwise error?
    if (val is None):
        return (False)
    if (val == "national" or val == "international"):
        return (True)
    return (False)


def GENDER_CHECK(val):
    # Give error if none otherwise those 3 options.
    if (val is None):
        return (False)
    if (val == "Male" or val == "Female" or val == "non-binary"):
        return (True)
    return (False)


def AGE_CHECK(val):
    # Check each number is an int and has format with "to".
    # Check for "under 16" otheriwse verify that cell matches"number to number"
    if (val is None):
        return (False)
    if (val is not None and val != " "):
        return (True)
    return (False)


def ETHNICITY_CHECK(val):
    # error if blank
    if (val is None):
        return (False)
    eth = ["African American", "American Indian / Alaskan Native",
           "Asian", "Filipino", "Hispanic", "Middle Eastern",
           "Multi-Ethnicity", "Other", "Pacific Islander", "Unknown", "White",
           "White Non-Hispanic"]
    if (val in eth):
        return (True)
    return (False)


def REENTRY_CHECK(val):
    # error if blank
    if (val is None):
        return (False)
    if (val == "clear" or val == "re-entry"):
        return (True)
    return (False)


def FOSTER_CHECK(val):
    # give error if blank
    if (val is None):
        return (False)
    if (val == "non-foster" or val == "foster"):
        return (True)
    return (False)


def OCCUPATION_CHECK(val):
    # Return True if blank otherwise just check spacing at first and last word.
    if (val is None):
        return (True)
    if (val[0] == " " or val[len(val) - 1] == " "):
        return (False)
    return (False)


def COMPANY_CHECK(val):
    # Return True if blank Otherwise just check spacing at first and last word.
    if (val is None):
        return (True)
    if (val[0] == " " or val[len(val) - 1] == " "):
        return (False)
    return (False)


def EMAIL_CHECK(val):
    # Return True if blank Otherwise if not blank check formatting.
    pattern = re.compile("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")
    if (val is None):
        return (True)
    if (pattern.match(val) is None):
        if (val is not None and val != " "):
            return (True)
        return (False)
    else:
        return (True)
    return (False)


def WEBSITE_CHECK(val):
    # Return True if blank.
    if (val is None or val != "" and val != " " or val):
        return (True)
    return (False)


def PHONE_NUMBER_CHECK(val):
    # Return true if blank but if not check format.
    if (val is None):
        return (True)
    pattern = re.compile("^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$")
    if (pattern.match(val) is None):
        return (False)
    else:
        return (True)
    return (False)


def FIRST_CONTACT_CHECK(val):
    # Return false if blank.
    if (val is None):
        return (False)
    contact = ["Business Event", "MEGA Phase 1", "Political Event",
               "Professional Event", "PESA"]
    if (val in contact or val != " "):
        return (True)
    return (False)


def BEST_PERSON_CHECK(val):
    # Return False if blank.
    if (val is None):
        return (False)
    if (val != " " or val is not None):
        return (True)
    return (False)


def ADDRESS_CHECK(val):
    # NO RULE JUST SET TO PASS
    return (True)


def SUITE_CHECK(val):
    # PASS - add to later
    return (True)


def CITY_CHECK(val):
    # Return False if blank or should be N/A (True).
    if (val is None):
        return (False)
    if (val == "N/A"):
        return (True)
    if (val != " "):
        return (True)
    return (False)


def STATE_CHECK(val):
    # Return False if blank, return ture if N/A or one of the states.
    if (val is None):
        return (False)
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
              "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
              "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
              "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "PR", "RI", "SC",
              "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    if (val in states or val == "N/A"):
        return (True)
    return (False)


def ZIP_CHECK(val):
    # Return False if none, unless N/A or zip then check format.
    if (val == "N/A"):
        return (True)
    if (val is None):
        return (False)
    pattern = re.compile("^[0-9]{5}(?:-[0-9]{4})?$")
    if (pattern.match(str(val)) is None):
        if (val is not None and val != " "):
            return (True)
        return (False)
    else:
        return (True)


def COUNTRY_CHECK(val):
    # Returns true if country is one of three options.
    if (val is None):
        return (False)
    if (val != "" and (' ' in val) is False or val == "N/A"):
        return (True)
    if (val == "USA" or val == "Republic of Armenia"):
        return (True)
    return (False)


def HOMELESS_CHECK(val):
    # Returns true for Settled or Homeless.
    if (val is None):
        return (False)
    if (val == "Settled" or val == "Homeless"):
        return (True)
    return (False)


def SOURCE_CHECK(val):
    # Return true if blank or one of 3 names.
    if (val is None):
        return (True)
    if (val == "Joseph Lopez" or val == "John Paul Tabakian"):
        return (True)
    if (val == "Christopher Castillo"):
        return (True)
    return (False)


def VET_CHECK(val):
    # Return true if blank or one of three options.
    if (val is None or val == "Marines" or val == "Veteran" or val == "Army"):
        return (True)
    return (False)
