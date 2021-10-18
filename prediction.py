# coding:utf-8
import pandas as pd
import numpy as np
from fbprophet import Prophet
import matplotlib.pyplot as plt

div_ls = ['办公商务', '出行服务', '电话通讯', '房产服务', '健康美容', '教育学习', '金融理财', '旅游服务', '拍摄美化',
          '汽车服务', '生活服务', '实用工具', '手机游戏', '数字阅读', '系统工具', '新闻资讯', '医疗服务', '移动购物',
          '移动社交', '移动视频', '移动音乐', '育儿母婴', '智能设备', '主题美化']

df = pd.read_csv('prediction_model.csv')
df_div = df.set_index('Div')
print(df_div)

for i in div_ls:
    # print(df_div.loc[('办公商务'), ['Date', "MAU"]])
    df_date = df_div.loc[(i), ['Date', "MAU"]]
    '''
        df_date['Date'] = pd.to_datetime(df_date['Date'])
        df_date = df_date.set_index(['Date'])
        print(df_date)
        '''
    np_date = np.array(df_date)
    # print(np_date)

    df_temp = pd.DataFrame(np_date, columns=['ds', 'y'])
    print(df_temp)

    model = Prophet(changepoint_prior_scale=0.001)
    model.fit(df_temp)
    future = model.make_future_dataframe(periods=500, freq='D')
    future.tail()
    forecast = model.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    fig1 = model.plot(forecast, xlabel='ds', ylabel='yhat')
    string = i + '-MAU'
    print(string)
    plt.title(string)
    plt.show()
    fig2 = model.plot_components(forecast)
    plt.show()
