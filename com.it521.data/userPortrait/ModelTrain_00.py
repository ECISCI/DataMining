import pandas as pd

data = pd.read_csv('H://DataMining/data/SklearnTest.txt')
print("###### data ######")
print(data)
print("###### data.info ######")
print(data.info())
print("###### data.index ######")
print(data.index)

train, test = data.query("is_date!=1"), data.query("is_date==1")

print("###### train 训练集 ######")
print(train)
print("###### test 测试集 ######")
print(test)

X_train = train.drop(["is_date"], axis=1)
print("###### X_train ######")
print(X_train)
#    height  house  car  handsome  job
# 4    1.68      0    1       5.1    0
# 5    1.63      1    0       5.3    1
# 6    1.78      0    0       4.5    0
# 7    1.64      0    0       7.8    2
# 8    1.65      0    1       6.6    0
X_test = test.drop(["is_date"], axis=1)
print("###### X_test ######")
print(X_test)
#    height  house  car  handsome  job
# 0    1.80      1    0       6.5    2
# 1    1.62      1    0       5.5    0
# 2    1.71      0    1       8.5    1
# 3    1.58      1    1       6.3    1

# 建立决策树模型

from  sklearn.tree import DecisionTreeClassifier

dtc = DecisionTreeClassifier(criterion='entropy')
# 训练模型 使用的是fit方法 -- 训练模型
dtc.fit(X_train,)