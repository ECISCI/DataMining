import pandas as pd


# 从CSV中读取数据
data = pd.read_csv('H://DataMining/data/SklearnTest.txt')
#  height  house  car  handsome  job  is_date
# 0    1.80      1    0       6.5    2        1
# 1    1.62      1    0       5.5    0        1
# 2    1.71      0    1       8.5    1        1
# 3    1.58      1    1       6.3    1        1
# 4    1.68      0    1       5.1    0        0
# 5    1.63      1    0       5.3    1        0
# 6    1.78      0    0       4.5    0        0
# 7    1.64      0    0       7.8    2        0
# 8    1.65      0    1       6.6    0       -1

# train_set 训练集 拿到数据中 is_date 不等于 -1 的所有数据集 (这里指数据的前 7 行)
# test_set  测试集 拿到数据中 is_date 等于 -1 的所有数据集   (这里指数据的最后一行)
train_set, test_set = data.query("is_date!=-1"), data.query("is_date==-1")

# Y_train 拿到 索引 与 is_date 列
# Y_test  拿到 索引 与 is_date 列
Y_train, Y_test = train_set["is_date"], test_set["is_date"]

# Y_train 拿到 索引 与 除去is_date 列 的所有列
# Y_test  拿到 索引 与 除去is_date 列 的所有列
X_train, X_test = train_set.drop(["is_date"], axis=1), test_set.drop(["is_date"], axis=1)


#建立决策树模型
from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier(criterion="entropy")
#训练模型使用的是fit方法---训练模型
dtc.fit(X_train,Y_train)

#预测新数据的结果
y_pred=dtc.predict(X_test)

#打印结果
print(y_pred)