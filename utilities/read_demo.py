#file will be deleted

import pandas

data_frame=pandas.read_csv(filepath_or_buffer="../test_data/invalid_login_data.csv",delimiter=";")
print(data_frame)
