# TelecomFraud运行时模块

## 模块架构

模块实现了模型运行中的三个步骤：数据预处理、预测和多模型融合。

运行脚本不涉及具体实现逻辑，仅提供标准的输入输出参数。

`preprocessing.py` 脚本实现了数据预处理流程，提供`input`输入数据和`output`输出数据参数，提供一个`preprocessing`函数具体实现输入数据读取、处理、数据清洗和处理、特征工程、输出数据存储等过程。

类似地，`predict.py`、`ensemble.py`实现了预测和多模型同和的流程。

`functions.py`脚本定义一些通用的函数，实现文件和目录校验、数据读取等常用功能。

模块内有几个目录，其中`tmp`可用于存储上述三个过程中需要的中间数据文件；`predictions`可用于存储预测流程产生的预测结果；`output`可用于存储多模型融合预测输出结果，如果模型没有集成，也可存储预测流程产生的结果。

`models`目录可用于存储运行需要的模型序列化文件。

`site`目录：为使模块更加易用，将开发一个基于`flask`的web站点，实现本地提交流程脚本到服务器进行处理的功能。正在开发中...

`run_model.sh`：命令行运行脚本，实现脚本调度和输出整理。

`README.md`:模块说明

## 目录结构

+ __init__.py
+ preprocessing.py
+ predict.py
+ ensemble.py
+ functions.py
+ /output
+ /predictions
+ /tmp
+ /models
+ /site
    - static
    - templates
    - __init__.py
    - app.py
+ README.md

## 使用方法

    python preprocessing.py -input ./tmp/phones.csv -output ./tmp/preprocessing.csv
    python predict.py -input ./tmp/phones.csv -output ./tmp/prediction.csv -models ./models/some_model.model
    python ensemble.py -input ./tmp/some_predictions/ -output ./output/ensemble_output.csv