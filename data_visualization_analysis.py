import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def create_descriptive_statistics_subplot(axes, a, b):
    axes.bar(['Mean', 'Median'], [np.mean(a), np.median(a)], color='blue', alpha=0.7, label='Variable 1')
    axes.bar(['Mean', 'Median'], [np.mean(b), np.median(b)], color='green', alpha=0.7, label='Variable 2')
    axes.legend()
    axes.set_title('Descriptive Statistics: Mean and Median')

def create_correlation_subplot(axes, data):
    sns.heatmap(np.corrcoef(data.T), annot=True, ax=axes)
    axes.set_title('Correlation Analysis')

def create_histogram_subplot(axes, a, b):
    axes.hist(a, bins=15, color='blue', alpha=0.7, label='Variable 1')
    axes.hist(b, bins=15, color='green', alpha=0.7, label='Variable 2')
    axes.legend()
    axes.set_title('Histogram of Variables')

def create_scatter_subplot(axes, a, b):
    axes.scatter(a, b, alpha=0.7)
    axes.set_xlabel('Variable 1')
    axes.set_ylabel('Variable 2')
    axes.set_title('Scatter Plot of Variable 1 vs Variable 2')

# 데이터 생성
np.random.seed(0)
data = np.random.randn(100, 2)
a = data[:, 0]
b = data[:, 1]

# 그래프 생성
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

create_descriptive_statistics_subplot(axes[0, 0], a, b)
create_correlation_subplot(axes[0, 1], data)
create_histogram_subplot(axes[1, 0], a, b)
create_scatter_subplot(axes[1, 1], a, b)

# 레이아웃 설정 및 그래프 표시
plt.tight_layout()
plt.show()