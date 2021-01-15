#!/usr/bin/env python3
# This script contains helper functions for main
import re


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def ID_CHECK(val):
    if (str == None):
        return (None)
    try:
        number=int(val)
    except:
        return (False)
    return (True)

def SALUTION_CHECK(val):
    if (val == "Mr." or val == "Ms." or val == "Dr."):
        return (True)
    return (False)

def FIRST_NAME_CHECK(val):
    if (val == None):
        return (False)
    if (hasNumbers(val) == False and (' ' in val) == False):
        return (True)
    return (False)

def MIDDLE_NAME_CHECK(val):
    if (val == None):
        return (True)
    if (hasNumbers(val) == False and (' ' in val) == False):
        return (True)
    return (False)

def LAST_NAME_CHECK(val):
    if (hasNumbers(val) == False and val != "" and val != " "):
        return (True)
    return (False)

def SUFFIX_CHECK(val):
    if (val == None or val != "" and (' ' in val) == False):
        return (True)
    return (False)

def PARTNER_CHECK(val):
    if (val == "formal" or val == "student"):
        return (True)
    return (False)

def SCHOOL_CHECK(val):
    if (val != None and val != " " and val != ""):
        return (True)
    return (False)

def INTERNSHIP_CHECK(val):
    if (val != None and val != " " and val != ""):
        return (True)
    return (False)

def INTERNSHIP_TYPE_CHECK(val):
    if (val != None and val != " " and val != ""):
        return (True)
    return (False)

def PLACEMENT_CHECK(val):
    if (val != None and val != " " and val != ""):
        return (True)
    return (False)

def PLACEMENT_DATE_CHECK(val):
    value = str(val).split()[0]
    words = ["Summer", "Fall", "Spring", "Winter"]
    if (value in words):
        return (True)
    return (False)

def END_DATE_CHECK(val):
    words = ["Summer", "Fall", "Spring", "Winter"]
    value = str(val).split()[0]
    if (val == "Permanent" or value in words):
        return (True)
    return (False)

def STATUS_CHECK(val):
    if (val == "citizen" or val == "permanent" or val == "visa" or val == "unknown"):
        return (True)
    return (False)

def FIRST_GEN_CHECK(val):
    if (val == "first" or val == "multiple"):
        return (True)
    return (False)

def INTERNATIONAL_CHECK(val):
    if (val == "national" or val == "international"):
        return (True)
    return (False)

def GENDER_CHECK(val):
    if (val == "Male" or val == "Female"):
        return (True)
    return (False)

def AGE_CHECK(val):
    if (val != None and val != " "):
        return (True)
    return (False)

def ETHNICITY_CHECK(val):
    eth = ["African American", "American Indian / Alaskan Native",
           "Asian", "Filipino", "Hispanic", "Middle Eastern", "Multi-Ethnicity", "Other", "Pacific Islander", "Unknown", "White", "White Non-Hispanic"]
    if (val in eth):
        return (True)
    return (False)

def REENTRY_CHECK(val):
    if (val == "clear" or val == "re-entry"):
        return (True)
    return (False)

def FOSTER_CHECK(val):
    if (val == "non-foster" or val == "foster"):
        return (True)
    return (False)

def OCCUPATION_CHECK(val):
    if (val == None or val != "" or val != " "):
        return (True)
    return (False)

def COMPANY_CHECK(val):
    if (val == None or val != "" or val != " "):
        return (True)
    return (False)

def EMAIL_CHECK(val):
    pattern = re.compile("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")
    if (val == None):
        return (True)
    if (pattern.match(val) == None):
        if (val != None and val != " "):
            return (True)
        return (False)
    else:
        return (True)
    return (False)

def WEBSITE_CHECK(val):
    if (val == None or val != "" and val != " " or val):
        return (True)
    return (False)

def PHONE_NUMBER_CHECK(val):
    if (val == None):
        return (True)
    pattern = re.compile("^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$")
    if (pattern.match(val) == None):
        return (False)
    else:
        return (True)
    return (False)

def FIRST_CONTACT_CHECK(val):
    contact = ["Business Event", "MEGA Phase 1", "Political Event", "Professional Event",
               "PESA"]
    if (val in contact or val != " "):
        return (True)
    return (False)

def BEST_PERSON_CHECK(val):
    if (val != " " or val != None):
        return (True)
    return (False)

def ADDRESS_CHECK(val):
    if (val != " " or val != None):
        return (True)
    return (False)

def SUITE_CHECK(val):
    if (val != " " or val == None):
        return (True)
    return (False)

def CITY_CHECK(val):
    if (val != " "):
        return (True)
    return (False)

def STATE_CHECK(val):
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
              "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "PR", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    if (val in states or val == "N/A"):
        return (True)
    return (False)

def ZIP_CHECK(val):
    if (val == "N/A"):
        return (True)
    if (val == None):
        return (False)
    pattern = re.compile("^[0-9]{5}(?:-[0-9]{4})?$")
    if (pattern.match(str(val)) == None):
        if (val != None and val != " "):
            return (True)
        return (False)
    else:
        return (True)
    return (False)

def COUNTRY_CHECK(val):
    if (val != "" and (' ' in val) == False or val == "N/A" or val == "USA" or val == "Republic of Armenia"):
        return (True)
    return (False)

def HOMELESS_CHECK(val):
    if (val == "Settled" or val == "Homeless"):
        return (True)
    return (False)

def SOURCE_CHECK(val):
    if (val == "Joseph Lopez" or val == "John Paul Tabakian" or val == "Christopher Castillo"):
        return (True)
    return (False)

def VET_CHECK(val):
    if (val == None or val != "" or val == "Marines" or val == "Veteran" or val == "Army"):
        return (True)
    return (False)

def NEW_SOURCE_CHECK(val):
    if (val == "employer" or val == "PESA"):
        return (True)
    return (False)
