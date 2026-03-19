"""
Python Visual in Power BI — Dual-Metric Heatmap
Shows Shipped Sales AND Gross Margin % in the same cell.
Standard Power BI matrices can't display two metrics per cell.
7 dashboard pages use this pattern at Advantage Solutions.
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def format_sales(value):
    if pd.isna(value) or value == 0: return ""
    elif value < 1e6: return f"${value/1e3:.1f}K"
    elif value < 1e9: return f"${value/1e6:.1f}M"
    else: return f"${value/1e9:.1f}B"

sales_pivot = dataset.pivot_table(
    index="ACCOUNT2", columns="DIVISION",
    values="SHIPPED SALES", aggfunc='sum')
igm_pivot = dataset.pivot_table(
    index="ACCOUNT2", columns="DIVISION",
    values="IGM%", aggfunc='mean')

combined = sales_pivot.applymap(format_sales) + " : " + \
    (igm_pivot * 100).round(1).astype(str) + "%"

plt.figure(figsize=(20, 8))
sns.heatmap(sales_pivot, mask=sales_pivot.isna(),
    annot=combined, fmt="", cmap="Reds",
    linewidths=.5, annot_kws={"size": 10})
plt.title('Shipped Sales and IGM% by Account and Division')
plt.tight_layout()
plt.show()
