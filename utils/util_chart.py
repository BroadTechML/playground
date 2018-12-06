# -*- coding: utf-8 -*-
# Date: 2018/12/6 0006
# Author: Stone

import matplotlib.pyplot as plt
import seaborn as sns


def plt_bar(df_data, column_x, column_y, xticks_rotation=90, savedir=None, figsize=None, title=None):
    """
    条形图
    :param df_data: dataframe数据
    :param column_x: 横坐标列名
    :param column_y: 轴坐标列名
    :param xticks_rotation: 横坐标的标签显示旋转角度
    :param savedir: 保存文件夹路径
    :param figsize: 窗口大小
    :param title: 标题
    :return:
    """
    if figsize:
        plt.figure(figsize=figsize)
    plt.bar(df_data[column_x], df_data[column_y])
    plt.xticks(rotation=xticks_rotation)
    if title:
        plt.title(title)
    if savedir:
        plt.savefig(savedir + column_x + '_' + column_y + '_bar.png')
    plt.show()


def plt_boxplot(df_data, column, savedir=None, figsize=None, title=None):
    """
    箱型图
    :param df_data: dataframe数据
    :param column: 列名
    :param savedir: 保存文件夹路径
    :param figsize: 窗口大小
    :param title: 标题
    :return:
    """
    if figsize:
        plt.figure(figsize=figsize)
    plt.boxplot(df_data[column], whis=1.5)
    if title:
        plt.title(title)
    if savedir:
        plt.savefig(savedir + column + '_box.png')
    plt.show()


def sns_violinplot(df_data, column, savedir=None, figsize=None, title=None):
    """
    提琴线图
    :param df_data: dataframe数据
    :param column: 列名
    :param savedir: 保存文件夹路径
    :param figsize: 窗口大小
    :param title: 标题
    :return:
    """
    if figsize:
        plt.figure(figsize=figsize)
    sns.violinplot(data=df_data[column], split=True, inner="quart")
    sns.despine(left=True)
    if title:
        plt.title(title)
    if savedir:
        plt.savefig(savedir + column + '_violin.png')
    plt.show()


def sns_kdeplot(lst_df_data, column, savedir=None, figsize=None, title=None, lst_labels=None):
    """
    核密度图
    :param lst_df_data: dataframe数据的list（按标签分开多个类别的数据）
    :param column: 列名
    :param savedir: 保存文件夹路径
    :param figsize: 窗口大小
    :param title: 标题
    :param lst_labels: 图例的list（对应数据list）
    :return:
    """
    if figsize:
        plt.figure(figsize=figsize)
    for df_data in lst_df_data:
        sns.kdeplot(df_data[column])
    if lst_labels:
        plt.legend(labels=lst_labels, loc='best')
    if title:
        plt.title(title)
    if savedir:
        plt.savefig(savedir + column + '_kde.png')
    plt.show()


def plt_bar_columns(df_data, column_x, lst_columns, savedir=None, figsize=None, xticks_rotation=90):
    for column_y in lst_columns:
        title = column_y
        plt_bar(df_data, column_x, column_y, savedir, figsize, xticks_rotation, title)


def plt_boxplot_columns(df_data, lst_columns, savedir=None, figsize=None):
    for column in lst_columns:
        title = column
        plt_boxplot(df_data, column, savedir, figsize, title)


def sns_violinplot_columns(df_data, lst_columns, savedir=None, figsize=None):
    for column in lst_columns:
        title = column
        sns_violinplot(df_data, column, savedir, figsize, title)


def sns_kdeplot_columns(lst_df_data, lst_columns, savedir=None, figsize=None, title=None, lst_labels=None):
    for column in lst_columns:
        title = column
        sns_kdeplot(lst_df_data, column, savedir, figsize, title, lst_labels)
