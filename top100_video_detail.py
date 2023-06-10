from pprint import pprint

import requests
import pandas as pd
from tqdm import tqdm

# Bilibili API URL for top 100 videos
url = "https://api.bilibili.com/x/web-interface/ranking/v2"

# List of categories to scrape
categories = [
    (1, "动画"),
    # (13, "番剧"),
    # (167, "国创"),
    (3, "音乐"),
    (129, "舞蹈"),
    (4, "游戏"),
    (36, "科技"),
    (160, "生活"),
    (119, "鬼畜"),
    (155, "时尚"),
    (5, "娱乐"),
    (181, "影视"),
    # (177, "纪录片"),
    # (23, "电影"),
    # (11, "电视剧"),
    (217, "游戏赛事"),
    # (71, "综艺"),
    (211, "美食"),
    (217, "动物圈"),
    # (22, "其他"),
]


def get_category_name(tid):
    for _tid, _name in categories:
        if _tid == tid:
            return _name
    return None


def get_data(_tid):
    videos = []
    # Send GET request to the API URL with the parameters
    response = requests.get(url, params={'rid': f'{_tid}'})
    # Extract the JSON data from the response
    # pprint(response.json())
    data = response.json()["data"]["list"]
    # pprint(data)
    # Loop through each video in the data and extract the relevant information
    for video in data:
        tid = video["tid"]
        bvid = video["bvid"]
        title = video["title"]
        desc = video["desc"]
        pubdate = video["pubdate"]
        owner_mid = video["owner"]["mid"]
        owner_name = video["owner"]["name"]
        stat = video["stat"]
        view = stat["view"]
        danmaku = stat["danmaku"]
        reply = stat["reply"]
        favorite = stat["favorite"]
        coin = stat["coin"]
        share = stat["share"]
        like = stat["like"]
        dislike = stat["dislike"]
        # Append the video information to the list
        videos.append((get_category_name(_tid), tid, bvid, title, desc, pubdate, owner_mid, owner_name, view, danmaku,
                       reply, favorite, coin, share, like, dislike))
    return videos


if __name__ == '__main__':
    # res = get_data(1)
    # pprint(res)
    # print(get_category_name(1))
    # exit(0)
    # Create an empty list to store the video information
    video_list = []

    # Loop through each category and scrape the top 100 videos
    for tid, name in tqdm(categories):
        try:
            video_list.extend(get_data(tid))
        except Exception as e:
            print(f'Get data of {tid} failed')
    # Create a pandas DataFrame from the video list
    df = pd.DataFrame(video_list,
                      columns=["category", "tid", "bvid", "title", "desc", "pubdate", "owner_mid", "owner_name", "view",
                               "danmaku", "reply", "favorite", "coin", "share", "like", "dislike"])

    # print(df)
    # Save the DataFrame to a CSV file
    df.to_csv("top100_video_detail.csv", index=False)
