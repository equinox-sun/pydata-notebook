import json
import numpy as np
from collections import defaultdict
from collections import Counter
from pandas import DataFrame,Series
import matplotlib.pyplot as plt

#看不懂
#等价于Counter(sequence)
def get_counts(sequence):
        counts = defaultdict(int) #所有的值均会被初始化为0
        for x in sequence:
            counts[x]+=1
        return counts

path = 'D:/code/pydata/pydata-notebook/datasets/bitly_usagov/example.txt'
# 列表推导式 在一组字符串 or 一组别的对象 上执行一条相同操作的简洁方式
record = [json.loads(line) for line in open(path)]
time_zones=[rec['tz'] for rec in record if 'tz' in rec]
counts =get_counts(time_zones)
# 等价于
# counts = Counter(time_zones)


#排序靠前的n个值
#等价于 count_dict.most_common(n)
def top_counts(count_dict,n=10):
    value_key_pairs = [(count,tz) for tz,count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]


frame = DataFrame(record)
tz_counts=frame['tz'].value_counts()

# fillna函数可以替换缺失值(NA)，而未知值（空字符串）则可以通过布尔型数组索引加以替换
clean_tz=frame['tz'].fillna('Missing')
clean_tz[clean_tz=='']='Unknow'
tz_counts=clean_tz.value_counts()
tz_counts[:10].plot(kind='barh',rot=0)

# x=[1,2,3,4]
# y=[1.2,2.5,4.5,7.3]
# plt.plot(x,y)
# plt.show()

# 用法基本和再matlab中画图一样
# plt.axis([x_min, x_max, y_min, y_max])
# plt.xlim(x_min, x_max)和plt.ylim(y_min, y_max)
# plt.plot(x, y, color="r", linestyle="-", linewidth=1)
# 函数plt.xticks()和plt.xticks()用来实现对x轴和y轴坐标间隔（也就是轴记号）的设定。用法上，函数的输入是两个列表，第一个表示取值，第二个表示标记。当然如果你的标记就是取值本身，则第二个列表可以忽略。