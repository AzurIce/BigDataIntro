import numpy as np
import pandas
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# rc = {'font.sans-serif': 'SimHei',
#       'axes.unicode_minus': False}
# sns.set(context='notebook', style='ticks', rc=rc)

# df = pd.read_csv('./top100_video_detail.csv')

def df():
    df = pd.read_csv('./top100_video_detail2.csv')
    df[f'log_view'] = df['view'].apply(np.log)
    df[f'log_like'] = df['like'].apply(np.log)
    df[f'log_coin'] = df['coin'].apply(np.log)
    df[f'log_favorite'] = df['favorite'].apply(np.log)
    df[f'log_share'] = df['share'].clip(lower=1).apply(np.log)
    return df

categories = [
    (1, "动画"),
    # (13, "番剧"),
    # (167, "国创"),
    (3, "音乐"),
    (129, "舞蹈"),
    (4, "游戏"),
    (36, "知识"),
    (188, "科技"),
    (234, "运动"),
    (223, "汽车"),
    (160, "生活"),
    (211, "美食"),
    (217, "动物圈"),
    (119, "鬼畜"),
    (155, "时尚"),
    # 资讯
    # 和广告去掉了
    (5, "娱乐"),
    (181, "影视"),
    # (177, "纪录片"),
    # (23, "电影"),
    # (11, "电视剧"),
]