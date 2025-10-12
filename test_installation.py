"""
环境安装验证脚本
运行此脚本检查所有必要的依赖是否正确安装
"""

import sys

def test_installation():
    print("=" * 60)
    print("Python环境验证")
    print("=" * 60)
    print(f"\nPython版本: {sys.version}\n")

    tests = []

    # 核心数据处理
    try:
        import pandas as pd
        import numpy as np
        import scipy
        tests.append(("[OK]", "核心数据处理", f"Pandas {pd.__version__}, NumPy {np.__version__}"))
    except ImportError as e:
        tests.append(("[FAIL]", "核心数据处理", str(e)))

    # 数据可视化
    try:
        import matplotlib
        import seaborn as sns
        import plotly
        tests.append(("[OK]", "数据可视化", "Matplotlib, Seaborn, Plotly"))
    except ImportError as e:
        tests.append(("[FAIL]", "数据可视化", str(e)))

    # CCXT交易库
    try:
        import ccxt
        tests.append(("[OK]", "加密货币交易", f"CCXT {ccxt.__version__}"))
    except ImportError as e:
        tests.append(("[FAIL]", "加密货币交易", str(e)))

    # 技术分析
    try:
        import pandas_ta as ta
        tests.append(("[OK]", "技术分析", "Pandas-TA"))
    except ImportError as e:
        tests.append(("[SKIP]", "技术分析", "未安装(可选)"))

    # TA-Lib（可选）
    try:
        import talib
        tests.append(("[OK]", "TA-Lib(可选)", f"TA-Lib {talib.__version__}"))
    except ImportError:
        tests.append(("[SKIP]", "TA-Lib(可选)", "未安装(可选)"))

    # 回测框架
    try:
        import backtrader as bt
        tests.append(("[OK]", "回测框架", "Backtrader"))
    except ImportError as e:
        tests.append(("[FAIL]", "回测框架", str(e)))

    # 机器学习
    try:
        import sklearn
        import xgboost
        import lightgbm
        tests.append(("[OK]", "机器学习", f"Scikit-learn {sklearn.__version__}"))
    except ImportError as e:
        tests.append(("[FAIL]", "机器学习", str(e)))

    # 数据获取
    try:
        import requests
        import bs4
        tests.append(("[OK]", "数据获取", "Requests, BeautifulSoup4"))
    except ImportError as e:
        tests.append(("[FAIL]", "数据获取", str(e)))

    # Jupyter
    try:
        import jupyter
        import IPython
        tests.append(("[OK]", "Jupyter环境", f"IPython {IPython.__version__}"))
    except ImportError as e:
        tests.append(("[FAIL]", "Jupyter环境", str(e)))

    # 实用工具
    try:
        import dotenv
        import loguru
        import tqdm
        import rich
        tests.append(("[OK]", "实用工具", "dotenv, loguru, tqdm, rich"))
    except ImportError as e:
        tests.append(("[FAIL]", "实用工具", str(e)))

    # 打印结果
    print("安装状态检查:")
    print("-" * 60)
    for status, name, detail in tests:
        print(f"{status:8s} {name:20s} {detail}")

    # 统计
    success = sum(1 for t in tests if t[0] == "[OK]")
    warning = sum(1 for t in tests if t[0] == "[SKIP]")
    failed = sum(1 for t in tests if t[0] == "[FAIL]")

    print("-" * 60)
    print(f"\n总计: {success} 成功, {warning} 跳过, {failed} 失败")

    if failed == 0:
        print("\n[SUCCESS] 所有核心依赖安装成功! 可以开始使用了.")
        if warning > 0:
            print("[INFO] 有些可选依赖未安装, 不影响基本功能.")
    else:
        print("\n[ERROR] 有依赖安装失败, 请检查并重新安装.")
        print("运行: pip install -r requirements-core.txt")

    print("\n" + "=" * 60)

    return failed == 0

if __name__ == "__main__":
    success = test_installation()
    sys.exit(0 if success else 1)
