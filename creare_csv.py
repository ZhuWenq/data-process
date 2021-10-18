import pandas as pd
import numpy as np

df = pd.read_excel('C:/Users/ZWQ/Desktop/interview/Prediction model.xlsx')
data = np.array(df)
ls_data = []
# print(data[1][2])

for i in range(len(data)):
    temp = []
    if i == 0:
        temp.append('Date')
        temp.append('Div')
        temp.append('MAU')
        temp.append('Act_p')
        temp.append('Act_f')
        temp.append('Act_t_s')
        ls_data.append(temp)
    elif i == 1:
        continue
    else:
        if data[i][1] > 9:
            date = str(data[i][0]) + '-' + str(data[i][1]) + '-' + '01'
        else:
            date = str(data[i][0]) + '-0' + str(data[i][1]) + '-' + '01'
        temp.append(date)
        for j in range(1, 25):
            temp1 = temp.copy()
            str1 = data[1][j + 1]
            temp1.append(str1)
            for t in range(4):
                p = 1 + (j + 24 * (t))
                num = data[i][p]
                temp1.append(num)
            ls_data.append(temp1)
csv_np = np.array(ls_data)
print(csv_np)
csv_df = pd.DataFrame(csv_np)
arr = csv_df.values
csv_dff = pd.DataFrame(arr[1:, 1:], index=arr[1:, 0], columns=arr[0, 1:])
csv_dff.index.name = arr[0, 0]
print(csv_dff)
csv_dff.to_csv('prediction_model.csv', float_format='%.2f', encoding='utf_8_sig', date_format='%Y-%m-%d')
