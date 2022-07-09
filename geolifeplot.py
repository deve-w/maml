# 数据集的 维度 经度 高度 日期 时间
#
# Line1~6：可以忽略，是一些基本的描述
#
# Field1：纬度
#
# Field2：经度
#
# Field3：设置为0
#
# Field4：海拔（-777表示无效值）
#
# Field5：日期（从1899/12/30开始经过的天数）
#
# Field6：日期String形式
#
# Field7：时间String格式

#
import os
import matplotlib.pyplot as plt

num = 000
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
lat = []  # 维度
lng = []  # 经度
for num in range(10):
    # 总路径
    path = os.getcwd() + "\\data\\Geolife Trajectories 1.3" + "\\Data" +"\\00" +str(num.__abs__())+ "\\Trajectory"
    # 001的路径
    # print(os.listdir(os.getcwd()+"\\Geolife Trajectories 1.3"+"\\Data"+"\\003"+"\\Trajectory"
    plts_001 = os.scandir(path)
    # 每一个文件的绝对路径
    for item in plts_001:
        path_item = path + "\\" + item.name
        with open(path_item, 'r+') as fp:
            for item in fp.readlines()[6::322]:
                item_list = item.split(',')
                lat.append(item_list[0])
                lng.append(item_list[1])

    lat_new = [float(x) for x in lat]
    lng_new = [float(x) for x in lng]
    plt.ylim((min(lat_new), max(lat_new)))
    plt.xlim((min(lng_new), max(lng_new)))

    plt.title("00" +str(num.__abs__())+"轨迹测试")
    plt.xlabel("经度")  # 定义x坐标轴名称
    plt.ylabel("维度")  # 定义y坐标轴名称
    plt.plot(lng_new, lat_new)  # 绘图
    plt.show()  # 展示