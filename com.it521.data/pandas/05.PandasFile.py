import pandas as pd

# 文件读取和存储
# 我们的数据大部分存在于文件中所以pandas会支持复杂的IO操作,pandas的API支持众多的文件格式 CSV SQL XLS JSON HDF5
# 最常用的HDF5和CSV文件

# read_csv

# 只读取 open close 两列
data = pd.read_csv('H://DataMining/data/stock_day.csv', usecols=['open', 'close'])
print("###### data ######")
print(data)

# 存储数据 CSV
data.to_csv('H://DataMining/data/data.csv', index=False)

# HDF5
data_hdf = pd.read_hdf('H://DataMining/data/day_eps_ttm.h5')
print("###### data_hdf ######")
print(data_hdf)

# 存储数据 HDF5
data_hdf.to_hdf('H://DataMining/data/test.h5', key='test')

# 读取Json数据

data_json = pd.read_json('H://DataMining/data/Sarcasm_Headlines_Dataset.json', orient='records', lines=True)
print("###### data_json ######")
print(data_json)

# 写入
data_json.to_json('H://DataMining/data/test_02.json',orient='records',lines=False)