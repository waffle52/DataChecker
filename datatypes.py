#!/usr/bin/env python3
# this script holds data structures.
from check_funcs import *

# list of functions to call on excel file in order
func_list = [ID_CHECK, SALUTION_CHECK, FIRST_NAME_CHECK,
                     MIDDLE_NAME_CHECK, LAST_NAME_CHECK, SUFFIX_CHECK,
                     PARTNER_CHECK, SCHOOL_CHECK, INTERNSHIP_CHECK,
                     INTERNSHIP_TYPE_CHECK, PLACEMENT_CHECK,
                     PLACEMENT_DATE_CHECK, END_DATE_CHECK, NEW_SOURCE_CHECK,
                     STATUS_CHECK, FIRST_GEN_CHECK, INTERNATIONAL_CHECK,
                     GENDER_CHECK, AGE_CHECK, ETHNICITY_CHECK,
                     REENTRY_CHECK, FOSTER_CHECK,
                     OCCUPATION_CHECK, COMPANY_CHECK,
                     EMAIL_CHECK, EMAIL_CHECK, WEBSITE_CHECK,
                     WEBSITE_CHECK, PHONE_NUMBER_CHECK,
                     PHONE_NUMBER_CHECK, PHONE_NUMBER_CHECK,
                     PHONE_NUMBER_CHECK, PHONE_NUMBER_CHECK,
                     PHONE_NUMBER_CHECK, PHONE_NUMBER_CHECK,
                     FIRST_CONTACT_CHECK, BEST_PERSON_CHECK, ADDRESS_CHECK,
                     SUITE_CHECK, CITY_CHECK, STATE_CHECK, ZIP_CHECK,
                     COUNTRY_CHECK, HOMELESS_CHECK, SOURCE_CHECK, VET_CHECK]

# error codes to report type of error in txt file
error_codes = {}
