from utilities import read_utilities

# test_invalid_login_data = [
#     ("saul", "saul123", "Invalid credentials"),
#     ("kim", "kim123", "Invalid credentials"),
#     ("john", "john123", "Invalid credentials")
# ]
#
# test_invalid_login_data1 = [
#     ["saul", "saul123", "Invalid credentials"],
#     ["kim", "kim123", "Invalid credentials"],
#     ["john", "john123", "Invalid credentials"]
# ]
#
# test_add_valid_employee_data = [
#     ["Admin", "admin123", "John", "J", "Wick", "John Wick", "John"],
#     ["Admin", "admin123", "Peter", "p", "Wick", "Peter Wick", "Peter"]
# ]

test_add_valid_employee_data = read_utilities.get_csv_list("../test_data/invalid_login_data.csv")

test_add_valid_employee_data = read_utilities.get_sheet_as_list("../test_data/Org_test_data.xlsx",
                                                            "test_add_valid_employee")

test_invalid_profile_upload_data = read_utilities.get_sheet_as_list("../test_data/Org_test_data.xlsx",
                                                                "test_invalid_profile_upload")

