# {self.name}数据概览报告

## 基本信息

+ 文件名：{self.name}

+ 样本数量：{self.sample_number}

+ 特征数量：{self.feature_number}

+ 是否有标签：{self.is_labeled}

+ 类别比例：{self.class_weight}

+ 特征数值类型列表：
{self.feature_dtypes}

+ 数值型特征：
{self.numeric_features}

+ 字符型特征：
{self.string_features}



## 数据缺失情况

![]({self.missing_counts_plot})

## 特征统计特征

{self.description}



