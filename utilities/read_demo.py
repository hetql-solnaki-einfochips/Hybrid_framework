#file will be deleted

import pandas

data_frame=pandas.read_csv(filepath_or_buffer="../test_data/invalid_login_data.csv",delimiter=";")
print(data_frame)

df=pandas.read_excel(io="../test_data/Org_test_data.xlsx", sheet_name="test_add_valid_employee")
print(df)