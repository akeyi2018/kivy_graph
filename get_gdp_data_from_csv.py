import pandas as pd

# 各データをデータフレームに変換
data_1980_1989 = {
    '年': list(range(1980, 1990)),
    '日本': [1127.88, 1243.79, 1157.60, 1268.62, 1345.20, 1427.35, 2121.25, 2584.34, 3134.18, 3117.07],
    'アメリカ': [2857.33, 3207.03, 3343.80, 3634.03, 4037.65, 4339.00, 4579.63, 4855.25, 5236.43, 5641.60],
    '中国': [303.00, 288.70, 284.60, 305.43, 314.23, 310.13, 300.92, 327.73, 408.66, 458.18]
}

data_1990_1999 = {
    '年': list(range(1990, 2000)),
    '日本': [3196.56, 3657.35, 3988.33, 4544.77, 4998.80, 5545.57, 4923.39, 4492.45, 4098.36, 4635.98],
    'アメリカ': [5963.13, 6158.13, 6520.33, 6858.55, 7287.25, 7639.75, 8073.13, 8577.55, 9062.83, 9631.18],
    '中国': [396.59, 413.21, 492.15, 617.43, 561.69, 731.00, 860.47, 957.99, 1024.17, 1088.35]
}

data_2000_2009 = {
    '年': list(range(2000, 2010)),
    '日本': [4968.36, 4374.71, 4182.85, 4519.56, 4893.14, 4831.47, 4601.66, 4579.75, 5106.68, 5289.49],
    'アメリカ': [10250.95, 10581.93, 10929.10, 11456.45, 12217.18, 13039.20, 13815.60, 14474.25, 14769.85, 14478.05],
    '中国': [1205.53, 1333.65, 1465.83, 1656.96, 1949.45, 2290.02, 2754.15, 3555.66, 4577.28, 5088.99]
}

data_2010_2019 = {
    '年': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
    '日本': [5759.07, 6233.15, 6272.36, 5212.33, 4897.00, 4444.93, 5003.68, 4930.84, 5040.88, 5118.00],
    'アメリカ': [15048.98, 15599.73, 16253.95, 16843.23, 17550.68, 18206.03, 18695.10, 19477.35, 20533.08, 21380.95],
    '中国': [6033.83, 7492.21, 8539.58, 9624.93, 10524.24, 11113.51, 11226.90, 12265.33, 13841.81, 14340.60]
}

data_2020_2023 = {
    '年': [2020, 2021, 2022, 2023],
    '日本': [5050.68, 5011.87, 4237.53, 4230.86],
    'アメリカ': [21060.45, 23315.08, 25462.73, 26949.64],
    '中国': [14862.56, 17759.31, 17886.33, 17700.90]
}

# データを結合
data_list = [data_1980_1989, data_1990_1999, data_2000_2009, data_2010_2019, data_2020_2023]
df = pd.concat([pd.DataFrame(data) for data in data_list], ignore_index=True)

# CSVファイルに書き出し
df.to_csv('merged_data.csv', index=False)

