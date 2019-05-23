#!/usr/bin/env python
# -*- coding:utf-8 -*-

import chardet

""" 定义条目 """
COLUMN = {
    'staff_id':     0,
    'name':         1,
    'age':          2,
    'phone':        3,
    'dept':         4,
    'enroll_data':  5
    }


def staff_read():
    staff_list = []
    try:
        file_read = open('staff_table','r',encoding='utf-8')
        for line in file_read:
            staff_list.append(line.strip())
        file_read.close()
        return staff_list
    except FileNotFoundError:
        print('信息文件丢失')


def staff_update(staff_list):
    file_update = open('staff_table','w+',encoding='utf-8')
    for value in staff_list:
        file_update.write(value + '\n')
    file_update.close()


# 打印结果的条目
def column_print(column_list):
    """打印条目编号
    将需要打印的关键字列表，转换成对应的数字列表
    :param column_list:
        需要打印的条目的关键字列表
    :return:
        返回打印条目关键字对应数字的列表
    """
    column = []
    if isinstance(column_list,list):
        for value in column_list:
            if value in COLUMN.keys():
                column.append(COLUMN[value])
            elif value == '*':
                for key in COLUMN.keys():
                    column.append(COLUMN[key])
            else:
                print('输出信息项有误，将以默认输出全部信息项方式打印结果：')
                for key in COLUMN.keys():
                    column.append(COLUMN[key])
    else:
        print('参数类型错误： print_column 函数只接受列表类型参数')
    return column


# 定义打印查找结果
def find_print(print_column, result_list):
    """打印查找结果
    将查找匹配结果，按所需条目打印
    :param print_column:
        需要打印的条目编号
    :param result_list:
        需要打印的结果列表
    :return:
        无
    """
    column_list = column_print(print_column)
    string_column = ''
    for value in print_column:
        string_column = string_column + '{:>20}'.format(value)
    print(string_column)
    for result in result_list:
        string_print = ''
        for column in column_list:
            string_print = string_print + '{:>20}'.format(result[column])
        print(string_print)


# 查找关键字的条目
def column_search(keyword):
    """定义查找条目编号
    将查找的关键字，转换成对应的数字
    :param keyword:
        需要进行查找的关键字
    :return:
        返回一个整型数字
    """
    column = 0
    if keyword in COLUMN.keys():
        column = COLUMN[keyword]
    else:
        print('搜索条件有误，请重新输入')
    return column


# 定义查找功能
def search(keyword, condition, val):
    """定义查找
    根据关键字和条件进行查找
    :param keyword:
        进行查找的关键字
    :param condition:
        进行查找的表达式条件
    :param val:
        进行查找的对比值
    :return:
        返回查找结果
        查找成功返回 True
        查找失败返回 False
    """
    keyword = str(keyword)
    condition = str(condition)
    val = str(val)
    if condition == '=':
        result = eval(keyword + '==' + val)
    elif condition == 'like':
        result = val in keyword
    else:
        result = eval(keyword + condition + val)
    return result


# 定义 find
def find(staff_list, info_column, keyword, condition,val):
    # 结果列表
    result_list = []
    # 查找条目
    search_col = column_search(keyword)
    # print(search_col)
    # print(staff_list)

    for value in staff_list:
        read_list = value.split(',')
        if search(read_list[search_col], condition, val):
            result_list.append(read_list)
            # print(result_list)

    find_print(info_column.split(','), result_list)


staff_info = staff_read()
find(staff_info, 'name,age,phone,dept', 'age', '>', 21)



