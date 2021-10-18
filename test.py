import pandas as pd
import numpy as np

df = pd.read_excel('C:/Users/ZWQ/Desktop/interview/Prediction model.xlsx')
df = df.drop(1)
data = np.array(df)
# print(data)
ls_data = []

for i in range(len(data)):
    temp = []
    if i == 0:
        temp.append('Date')
        temp.append('Div')
    else:
        if data[i][1] > 9:
            date = str(data[i][0]) + '-' + str(data[i][1]) + '-' + '01'
        else:
            date = str(data[i][0]) + '-0' + str(data[i][1]) + '-' + '01'
        temp.append(date)
        temp.append('商务办公')
    point = 0
    for j in data[0]:
        if isinstance(j, str):
            temp.append(data[i][point])
        point = point + 1
    # print(temp)
    ls_data.append(temp)
csv_np = np.array(ls_data)
print(csv_np)
csv_df = pd.DataFrame(csv_np)
print(csv_df)
csv_df.to_csv('2.csv', index=0, float_format='%.2f', encoding='utf_8_sig', date_format='%Y-%m-%d')
