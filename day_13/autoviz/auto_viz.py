import pandas as pd

from autoviz.AutoViz_Class import AutoViz_Class

print(auto_viz.__doc__)

data = {'col1': [1, 2, 3, 4, 5], 'col2': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data)

# dft = AV.AutoViz(
#     "",
#     sep=",",
#     depVar="",
#     dfte=df,
#     header=0,
#     verbose=1,
#     lowess=False,
#     chart_format="html",
#     max_rows_analyzed=150000,
#     max_cols_analyzed=30,
#     save_plot_dir=None
# )
