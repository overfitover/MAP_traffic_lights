import numpy as np
import os

def read_data(file):
    '''
    @description:读取原始数据并转换成需要数据
    :param file: 文件名
    :return: 读取的数据
    '''
    f = open(file)
    lines = f.readlines()
    data = []
    line_data = []
    lights = {1:'red_light', 2: 'green_light'}
    for line in lines:
        data_line = list(line.split())

        line_data.append(lights[int(data_line[0])])
        line_data.append(int(float(data_line[1])))
        line_data.append(int(float(data_line[2])))
        line_data.append(int(float(data_line[3])))
        line_data.append(int(float(data_line[4])))
        data.append(line_data)

        line_data = []
    return data

# print(read_data('../ground-truth/00000.txt'))

def write_data(file, data):
    f = open(file, 'a')
    for i in range(len(data)):
        for j in range(5):                 # 一个object数据
            f.writelines(str(data[i][j]))
            if j < 4:
                f.writelines(' ')
        if i < len(data)-1:
            f.writelines('\n')

    f.close()

# write_data('00.txt', [['red_light', 898, 420, 960, 583]])


def read_all_data(file_dir):
    '''
    description:
    :param file_dir: 文件所在父文件夹
    :return: 读取所有的文件
    '''
    for file in os.listdir(file_dir):
        file_name = file_dir + file
        data = read_data(file_name)
        # print(data)
        if os.path.exists(file_name):
            os.remove(file_name)
        write_data(file_name, data)

    return 'write over'

file_dir = '../ground-truth/'
read_all_data(file_dir)

