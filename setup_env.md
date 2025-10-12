# Python环境设置指南

## 创建虚拟环境

### 使用venv（推荐）

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 使用conda

```bash
# 创建虚拟环境
conda create -n crypto-quant python=3.10

# 激活环境
conda activate crypto-quant
```

## 安装依赖

### 基础安装

```bash
# 安装所有依赖
pip install -r requirements.txt
```

### 分步安装（如果遇到问题）

```bash
# 1. 核心数据处理
pip install pandas numpy scipy

# 2. 可视化
pip install matplotlib seaborn plotly

# 3. 加密货币交易
pip install ccxt python-binance

# 4. 技术分析
pip install pandas-ta

# 5. 回测框架
pip install backtrader backtesting vectorbt

# 6. 机器学习
pip install scikit-learn xgboost lightgbm

# 7. 其他工具
pip install requests beautifulsoup4 python-dotenv loguru tqdm rich
```

### TA-Lib特殊安装

TA-Lib需要特殊处理：

**Windows:**
```bash
# 下载预编译的wheel文件
# 访问: https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib
# 下载对应Python版本的文件，例如: TA_Lib-0.4.28-cp310-cp310-win_amd64.whl

pip install TA_Lib-0.4.28-cp310-cp310-win_amd64.whl
```

**Linux:**
```bash
# 安装依赖
sudo apt-get install build-essential wget
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
tar -xzf ta-lib-0.4.0-src.tar.gz
cd ta-lib/
./configure --prefix=/usr
make
sudo make install

# 安装Python包
pip install ta-lib
```

**Mac:**
```bash
brew install ta-lib
pip install ta-lib
```

## 验证安装

创建测试脚本 `test_installation.py`：

```python
import sys
print(f"Python版本: {sys.version}")

# 测试核心库
import pandas as pd
import numpy as np
print("✓ Pandas和NumPy")

# 测试可视化
import matplotlib.pyplot as plt
import seaborn as sns
print("✓ Matplotlib和Seaborn")

# 测试CCXT
import ccxt
print("✓ CCXT")

# 测试技术分析
import pandas_ta as ta
print("✓ Pandas-TA")

# 测试TA-Lib（可能失败）
try:
    import talib
    print("✓ TA-Lib")
except ImportError:
    print("✗ TA-Lib (可选)")

# 测试机器学习
import sklearn
print("✓ Scikit-learn")

print("\n所有核心依赖安装成功！")
```

运行测试：
```bash
python test_installation.py
```

## 配置API密钥

创建 `.env` 文件（不要提交到git）：

```bash
# 交易所API
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here

# 新闻API
NEWS_API_KEY=your_news_api_key

# Twitter API
TWITTER_API_KEY=your_twitter_key
TWITTER_API_SECRET=your_twitter_secret
```

## Jupyter配置

启动Jupyter Lab：
```bash
jupyter lab
```

安装Jupyter扩展（可选）：
```bash
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
```

## 常见问题

### 问题1: pip安装速度慢
使用国内镜像：
```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 问题2: 依赖冲突
使用虚拟环境隔离：
```bash
python -m venv venv_new
venv_new\Scripts\activate
pip install -r requirements.txt
```

### 问题3: TA-Lib安装失败
如果无法安装TA-Lib，可以只使用pandas-ta，它提供了大部分常用指标。

### 问题4: 内存不足
安装时添加 `--no-cache-dir`：
```bash
pip install -r requirements.txt --no-cache-dir
```

## 更新依赖

```bash
# 更新所有包
pip install --upgrade -r requirements.txt

# 更新特定包
pip install --upgrade pandas numpy
```

## 导出当前环境

```bash
# 导出已安装的包
pip freeze > requirements_frozen.txt
```

## IDE配置

### VSCode
1. 安装Python扩展
2. 选择虚拟环境：Ctrl+Shift+P → "Python: Select Interpreter"
3. 选择 `venv/Scripts/python.exe`

### PyCharm
1. File → Settings → Project → Python Interpreter
2. 添加虚拟环境
3. 选择 `venv/Scripts/python.exe`

## 下一步

环境设置完成后，可以开始：
1. 运行 `notebooks/` 中的示例笔记本
2. 测试 `scripts/` 中的数据采集脚本
3. 开发你的第一个交易策略

祝学习愉快！
