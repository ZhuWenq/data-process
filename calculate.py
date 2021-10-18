import pandas as pd
import numpy as np

df = pd.read_csv('prediction_model.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
df_2020 = df['2020']
df_div = df_2020.set_index('Div')
#print(df_div)
#print(df_div.loc[('办公商务'),"MAU"])

print(df_div.loc[:,"MAU"].mean())

div_ls=['办公商务','出行服务','电话通讯','房产服务','健康美容','教育学习','金融理财','旅游服务','拍摄美化',
        '汽车服务','生活服务','实用工具','手机游戏','数字阅读','系统工具','新闻资讯','医疗服务','移动购物',
        '移动社交','移动视频','移动音乐','育儿母婴','智能设备','主题美化']

ls_avg=[['Div','avg_MAU','avg_time_spend','TGI_MAU','TGI_Timespend']]
for i in div_ls:
    temp=[]
    temp.append(i)
    group = df_div.loc[(i), "MAU"].groupby('Div')
    avg=float(np.array(group.mean()))
    temp.append(avg)
    tgi = avg/df_div.loc[:,"MAU"].mean()*100
    group = df_div.loc[(i), "Act_t_s"].groupby('Div')
    avg = float(np.array(group.mean()))
    temp.append(avg)
    temp.append(tgi)
    tgi = avg / df_div.loc[:, "Act_t_s"].mean() * 100
    temp.append(tgi)
    ls_avg.append(temp)


print(ls_avg)
csv_np = np.array(ls_avg)
print(csv_np)
csv_df = pd.DataFrame(csv_np)
arr=csv_df.values
csv_dff=pd.DataFrame(arr[1:,1:],index=arr[1:,0],columns=arr[0,1:])
csv_dff.index.name=arr[0,0]
print(csv_dff)
csv_dff.to_csv('avg_tig.csv', float_format='%.2f', encoding='utf_8_sig', date_format='%Y-%m-%d')



