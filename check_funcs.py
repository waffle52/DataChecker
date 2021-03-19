#!/usr/bin/env python3
# This script contains helper functions for main
import re


def hasNumbers(inputString):
    try:
        input = str(inputString)
    except:
        return (True)
    return any(char.isdigit() for char in input)

def ID_CHECK(val, info):
    # Checks to make sure ID is a number.
    try:
        if (str is None):
            return (None)
        number = int(val)
    except ValueError:
        print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
        return (False)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (True)


def SALUTION_CHECK(val, info):
    # Check for one of three options
    try:
        if (val == "Mr." or val == "Ms." or val == "Dr." or val == "Mx."):
            return (True)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (False)


def FIRST_NAME_CHECK(val, info):
    # Just check only letters, first letter uppercase, no space after.
    # ADD: Check for uppercase letter in first letter.
    try:
        if (val is None):
            return (False)
        if (hasNumbers(val) is False and (' ' in val) is False and val[0] != " " or val[len(val) - 1] != " " and val[0].isupper() is True):
            return (True)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (False)


def MIDDLE_NAME_CHECK(val, info):
    # Focus on skipping
    try:
        if (val is None):
            return (True)
        if (hasNumbers(val) is False):
            return (True)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (False)


def LAST_NAME_CHECK(val, info):
    # Return true if only letters, no spaces before first or after last word.
    try:
        if (hasNumbers(val) is False and val[0] != " " and val[len(val) - 1] != " "):
            return (True)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (False)


def SUFFIX_CHECK(val, info):
    # JD, Ed.D, MBA, Esq, Ph.D, M.D, CFP, MA, MPH.
    # Can be a lot dont focvus and skip.
    return (True)


def PARTNER_CHECK(val, info):
    # so the only options are formal and student?
    try:
        if (val == "formal" or val == "student"):
            return (True)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (False)


def SCHOOL_CHECK(val, info):
    # check for spaces at first & last word, error if blank?
    # Check for uppercase on every word except of's?
    try:
        if (val is None):
            return (False)
        if (val is not None and val != " " and val != ""):
            return (True)
        if (val[0] == " " or val[len(val) - 1] == " "):
            return (False)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (False)


def INTERNSHIP_CHECK(val, info):
    # Check for spaces at first & last word.
    # Check for uppercase on every word except of's?
    # if blank give error.
    try:
        if (val is None):
            return (False)
        if (val[0] == " " or val[len(val) - 1] == " "):
            return (False)
    except TypeError:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            pass
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (True)


def INTERNSHIP_TYPE_CHECK(val, info):
    # Check for spaces at first & last word unkless just one word?
    # give error if blank.
    try:
        if (val is None):
            return (False)
        if (val[0] == " " or val[len(val) - 1] == " "):
            return (False)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (True)


def PLACEMENT_CHECK(val, info):
    # Check for spaces at first & last word, error if blank?
    # give error if blank.
    try:
        if (val is None):
            return (False)
        if (val[0] == " " or val[len(val) - 1] == " "):
            return (False)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (True)


def PLACEMENT_DATE_CHECK(val, info):
    # Check for only these options and year.
    try:
        value = str(val).split()[0]
        year = int(val.split()[1])
        words = ["Summer", "Fall", "Spring", "Winter"]
        if (value in words):
            return (True)
    except ValueError:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
        return (False)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
        return (False)
    return (False)


def END_DATE_CHECK(val, info):
    # Ask if only these options otherwise confirm second word is a year.
    try:
        words = ["Summer", "Fall", "Spring", "Winter"]
        value = str(val).split()[0]
        if (val == "Permanent" or value in words):
            return (True)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (False)


def NEW_SOURCE_CHECK(val, info):
    # only employer and pesa? No other options.
    # make sure is not blank.
    try:
        if (val is None):
            return (False)
        if (val == "employer" or val == "PESA"):
            return (True)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (False)


def STATUS_CHECK(val, info):
    # only these 4 options otherwise error? if blank give error?
    # make sure is not blank.
    try:
        if (val is None):
            return (False)
        if (val == "citizen" or val == "permanent" or val == "visa" or val == "refugee" or val == "temporary"):
            return (True)
        if (val == "unknown"):
            return (True)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (False)


def FIRST_GEN_CHECK(val, info):
    # only these 2 options otherwise error? if blank give error.
    try:
        if (val is None):
            return (False)
        if (val == "first" or val == "multiple" or val == "second"):
            return (True)
        if (val == "third"):
            return (True)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (False)


def INTERNATIONAL_CHECK(val, info):
    # only these 2 options otherwise error?
    try:
        if (val is None):
            return (False)
        if (val == "national" or val == "international"):
            return (True)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (False)


def GENDER_CHECK(val, info):
    # Give error if none otherwise those 3 options.
    try:
        if (val is None):
            return (False)
        if (val == "Male" or val == "Female" or val == "Non-Binary"):
            return (True)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (False)


def AGE_CHECK(val, info):
    # Check each number is an int and has format with "to".
    # Check for "under 16" otheriwse verify that cell matches"number to number"
    try:
        if (val is None):
            return (False)
        if (val is not None and val != " "):
            return (True)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (False)


def ETHNICITY_CHECK(val, info):
    # error if blank
    try:
        if (val is None):
            return (False)
        eth = ["African American", "American Indian / Alaskan Native",
               "Asian", "Filipino", "Hispanic", "Middle Eastern",
               "Multi-Ethnicity", "Other", "Pacific Islander", "Unknown",
               "White", "White Non-Hispanic", "Multi-Ethnic"]
        if (val in eth):
            return (True)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (False)


def REENTRY_CHECK(val, info):
    # error if blank
    try:
        if (val is None):
            return (False)
        if (val == "clear" or val == "re-entry"):
            return (True)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (False)


def FOSTER_CHECK(val, info):
    # give error if blank
    try:
        if (val is None):
            return (False)
        if (val == "non-foster" or val == "foster"):
            return (True)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (False)


def OCCUPATION_CHECK(val, info):
    # Return True if blank otherwise just check spacing at first and last word.
    try:
        if (val is None):
            return (True)
        if (val[0] == " " or val[len(val) - 1] == " "):
            return (False)
    except TypeError:
        print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
        pass
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (True)


def COMPANY_CHECK(val, info):
    # Return True if blank Otherwise just check spacing at first and last word.
    try:
        if (val is None):
            return (True)
        if (val[0] == " " or val[len(val) - 1] == " "):
            return (False)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (True)


def EMAIL_CHECK(val, info):
    # Return True if blank Otherwise if not blank check formatting.
    try:
        pattern = re.compile("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")
        if (val is None):
            return (True)
        if (pattern.match(val) is None):
            if (val is not None and val != " "):
                return (True)
            return (False)
        else:
            return (True)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (False)


def WEBSITE_CHECK(val, info):
    # Return True if blank.
    try:
        if (val is None or val != "" and val != " " or val):
            return (True)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (False)


def PHONE_NUMBER_CHECK(val, info):
    # Return true if blank but if not check format.
    try:
        if (val is None or type(val) != str):
            return (True)
        pattern = re.compile("^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$")
        if (pattern.match(val) is None):
            return (False)
        else:
            return (True)
    except TypeError:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
        pass
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (False)

def PHONE_IGNORE(val, info):
    # pass
    pass


def FIRST_CONTACT_CHECK(val, info):
    # Return false if blank.
    try:
        if (val is None):
            return (False)
        contact = ["Business Event", "MEGA Phase 1", "Political Event",
                   "Professional Event", "PESA"]
        if (val in contact or val != " "):
            return (True)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (False)


def BEST_PERSON_CHECK(val, info):
    # Return False if blank.
    try:
        if (val is None):
            return (False)
        if (val != " " or val is not None):
            return (True)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (False)


def ADDRESS_CHECK(val, info):
    # NO RULE JUST SET TO PASS
    return (True)


def SUITE_CHECK(val, info):
    # PASS - add to later
    return (True)


def CITY_CHECK(val, info):
    # Return False if blank or should be N/A (True).
    try:
        if (val is None):
            return (False)
        if (val == "N/A"):
            return (True)
        if (val != " "):
            return (True)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
            return (False)
    return (False)


def STATE_CHECK(val, info):
    # Return False if blank, return ture if N/A or one of the states.
    try:
        if (val is None):
            return (False)
        states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
                  "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                  "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                  "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "PR", "RI", "SC",
                  "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
        if (val in states or val == "N/A"):
            return (True)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
        return (False)
    return (False)


def ZIP_CHECK(val, info):
    # Return False if none, unless N/A or zip then check format.
    try:
        if (val == "N/A"):
            return (True)
        if (val is None):
            return (False)
        pattern = re.compile("^[0-9]{5}(?:-[0-9]{4})?$")
        if (pattern.match(str(val)) is None):
            if (val is not None and val != " "):
                return (True)
            return (False)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
        return (False)
    return (True)


def COUNTRY_CHECK(val, info):
    # Returns true if country is one of three options.
    try:
        if (val is None):
            return (False)
        if (val != "" and (' ' in val) is False or val == "N/A"):
            return (True)
        if (val == "USA" or val == "Republic of Armenia"):
            return (True)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
        return (False)
    return (False)


def HOMELESS_CHECK(val, info):
    # Returns true for Settled or Homeless.
    try:
        if (val is None):
            return (False)
        if (val == "Settled" or val == "Homeless"):
            return (True)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
        return (False)
    return (False)


def SOURCE_CHECK(val, info):
    # Return true if blank or one of 3 names.
    try:
        if (val is None):
            return (True)
        if (val == "Joseph Lopez" or val == "John Paul Tabakian"):
            return (True)
        if (val == "Christopher Castillo"):
            return (True)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
        return (False)
    return (False)


def VET_CHECK(val, info):
    # Return true if blank or one of three options.
    try:
        if (val is None or val == "Marines" or val == "Veteran" or val == "Army" or val == "Navy"):
            return (True)
    except:
        if (info.get_info('e') == 1):
            print("{}-error: {} at col: {} - row: {}"
                  .format(info.get_info("name"), val, info.get_info('x'),
                          info.get_info('y')))
        return (False)
    return (False)
