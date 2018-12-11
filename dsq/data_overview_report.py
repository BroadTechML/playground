import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def plot_miss_count(df, figsize=(10, 12), title="missing counts"):
    '''
    df : DataFrame
    figsize : tuple(x, y)
    title : str
    '''
    miss_val_count = df.isnull().sum()
    miss_val_pct = 100 * miss_val_count / df.shape[0]
    miss_val_pct = pd.DataFrame(miss_val_pct)
    miss_val_pct = miss_val_pct.rename(columns={0:'percent'})
    return pd.DataFrame(miss_val_pct), miss_val_pct.sort_values(by='percent').plot(kind='barh', figsize=figsize, title=title)

def df_to_markdown(df, float_format='%.2g'):
    """
    Export a pandas.DataFrame to markdown-formatted text.
    DataFrame should not contain any `|` characters.
    """
    from os import linesep
    return "".join([
        '|' + '|'.join(df.columns)+'|\n',
        '|' + '|'.join(4 * '-' for i in df.columns)+'|\n',
        '|' + df.to_csv(sep='|', index=False, header=False, float_format=float_format).replace("\n", "|\n|")+'|'
    ])
    
def replace_other(report):
    report = report.replace("('", "")
    report = report.replace("',)", "")
    report = report.replace(",", "\n")
    return report

class DataOverviewTemplate:
    def __init__(self, data_info):
        self.name=data_info['name'],
        self.sample_number=data_info['sample_number'],
        self.feature_number=data_info['feature_number'],
        self.is_labeled=data_info['is_labeled'],
        self.class_weight=data_info['class_weight'],
        self.feature_dtypes=data_info['feature_dtypes'],
        self.numeric_features=data_info['numeric_features'],
        self.string_features=data_info['string_features'],
        # self.missing_counts=data_info['missing_counts'],
        self.missing_counts_plot=data_info['missing_counts_plot'],
        self.description=data_info['description']
    def load_template(self, report_template):
        with open(report_template, "r", encoding='gbk') as template:
            self.template = template.read()
            return self.template    
    def report(self):
        return self.template.format(self=self)

if __name__ == "__main__":
    filename = r"E:\projects\TelecomFraud\data\xdr\xdr_cs_maplulog_suspecter_1024.csv"
    outputdir = r"E:\projects\TelecomFraud\data\output"
    if not os.path.exists(os.path.join(outputdir, 'src')):
        os.mkdir(os.path.join(outputdir, 'src'))
    df = pd.read_csv(filename).replace("\\N", np.nan)
    (sample_number, feature_number) = df.shape
    is_labeled = 'label' in df.columns

    feature_dtypes = df.dtypes.to_dict()
    feature_dtypes = ", ".join(["{0}:    {1}".format(k, feature_dtypes[k]) for k in feature_dtypes.keys()])
    numeric_features = "    ".join(list(df.dtypes[df.dtypes!='object'].index))
    string_features = "    ".join(list(df.dtypes[df.dtypes=='object'].index))
    missing_counts, missing_counts_plot = plot_miss_count(df)
    # missing_counts = df_to_markdown(missing_counts)
    plt.savefig(os.path.join(outputdir, 'src/missing_counts.png'))
    description = df_to_markdown(df.describe())

    data_info = dict(
        name=os.path.split(filename)[-1],
        sample_number=sample_number,
        feature_number=feature_number,
        is_labeled=is_labeled,
        class_weight=0,
        feature_dtypes=feature_dtypes,
        numeric_features=numeric_features,
        string_features=string_features,
        # missing_counts=missing_counts,
        missing_counts_plot=os.path.join(outputdir, 'src/missing_counts.png'),
        description=description    
    )
    report = DataOverviewTemplate(data_info)
    report.load_template(r"E:\documents\tech-notes\工作笔记\数据可视化\data_overview_template.md")
    with open(r"E:\projects\TelecomFraud\data\output\report.md", "w+") as output:
        output.write(replace_other(report.report()))






