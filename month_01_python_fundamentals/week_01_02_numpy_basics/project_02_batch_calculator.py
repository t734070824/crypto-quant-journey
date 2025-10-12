"""
项目2: 批量币种技术指标计算器
Project 2: Batch Cryptocurrency Technical Indicator Calculator

功能:
- 批量获取多个币种的历史数据
- 批量计算所有币种的技术指标
- 生成跨币种对比报告
- 识别超卖/超买的币种

作者: [Your Name]
日期: 2025-01-12
"""

import ccxt
import pandas as pd
import numpy as np
from typing import Dict, List
from project_01_technical_indicators import (
    calculate_ma,
    calculate_ema,
    calculate_rsi,
    calculate_macd
)


# ==================== 数据获取 ====================

def fetch_multiple_symbols(
    symbols: List[str],
    timeframe: str = '1h',
    limit: int = 500
) -> Dict[str, pd.DataFrame]:
    """
    批量获取多个币种的历史数据

    参数:
        symbols: 币种列表 (如 ['BTC/USDT', 'ETH/USDT'])
        timeframe: 时间周期 ('1m', '5m', '15m', '1h', '4h', '1d')
        limit: 获取数据条数

    返回:
        字典 {symbol: DataFrame}

    示例:
        >>> symbols = ['BTC/USDT', 'ETH/USDT', 'BNB/USDT']
        >>> data = fetch_multiple_symbols(symbols, '1h', 500)
        >>> print(data['BTC/USDT'].head())
    """
    # TODO: 实现数据获取
    # 步骤:
    # 1. 初始化交易所 exchange = ccxt.binance()
    # 2. 遍历symbols
    # 3. 对每个symbol调用 exchange.fetch_ohlcv()
    # 4. 转换为DataFrame
    # 5. 处理异常 (某些币种可能获取失败)
    pass


# ==================== 指标计算 ====================

def calculate_indicators_batch(
    data_dict: Dict[str, pd.DataFrame]
) -> pd.DataFrame:
    """
    批量计算所有币种的技术指标

    参数:
        data_dict: 币种数据字典

    返回:
        包含所有币种指标的DataFrame

    列:
        - symbol: 币种名称
        - price: 当前价格
        - ma_20: 20日均线
        - ema_12: 12日指数均线
        - rsi: RSI值
        - macd: MACD值
        - signal: Signal值
        - status: 状态 (超买/超卖/中性)

    示例:
        >>> report = calculate_indicators_batch(data)
        >>> print(report.sort_values('rsi'))
    """
    # TODO: 实现批量指标计算
    # 步骤:
    # 1. 遍历data_dict
    # 2. 对每个币种计算所有指标
    # 3. 获取最新指标值
    # 4. 判断超买超卖状态
    # 5. 汇总到DataFrame
    pass


# ==================== 信号分析 ====================

def find_oversold_coins(report: pd.DataFrame, rsi_threshold: float = 30) -> pd.DataFrame:
    """
    找出超卖的币种

    参数:
        report: 指标报告
        rsi_threshold: RSI阈值 (默认30)

    返回:
        超卖币种的DataFrame
    """
    # TODO: 筛选RSI < threshold的币种
    pass


def find_overbought_coins(report: pd.DataFrame, rsi_threshold: float = 70) -> pd.DataFrame:
    """
    找出超买的币种

    参数:
        report: 指标报告
        rsi_threshold: RSI阈值 (默认70)

    返回:
        超买币种的DataFrame
    """
    # TODO: 筛选RSI > threshold的币种
    pass


def find_bullish_macd_crossover(report: pd.DataFrame) -> pd.DataFrame:
    """
    找出MACD金叉的币种 (MACD > Signal)

    参数:
        report: 指标报告

    返回:
        MACD金叉币种的DataFrame
    """
    # TODO: 筛选MACD > Signal的币种
    pass


# ==================== 报告生成 ====================

def generate_trading_signals(report: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    """
    生成交易信号报告

    返回:
        字典包含:
        - 'oversold': 超卖币种
        - 'overbought': 超买币种
        - 'macd_bullish': MACD金叉币种
        - 'macd_bearish': MACD死叉币种
    """
    return {
        'oversold': find_oversold_coins(report),
        'overbought': find_overbought_coins(report),
        'macd_bullish': find_bullish_macd_crossover(report),
        'macd_bearish': report[report['macd'] < report['signal']]
    }


def print_report(signals: Dict[str, pd.DataFrame]):
    """
    打印交易信号报告

    参数:
        signals: 交易信号字典
    """
    print("=" * 80)
    print("加密货币技术指标分析报告")
    print("=" * 80)

    print("\n🔴 超卖币种 (RSI < 30):")
    if len(signals['oversold']) > 0:
        print(signals['oversold'][['symbol', 'price', 'rsi']].to_string(index=False))
    else:
        print("   无")

    print("\n🔵 超买币种 (RSI > 70):")
    if len(signals['overbought']) > 0:
        print(signals['overbought'][['symbol', 'price', 'rsi']].to_string(index=False))
    else:
        print("   无")

    print("\n📈 MACD金叉 (看涨):")
    if len(signals['macd_bullish']) > 0:
        print(signals['macd_bullish'][['symbol', 'price', 'macd', 'signal']].to_string(index=False))
    else:
        print("   无")

    print("\n📉 MACD死叉 (看跌):")
    if len(signals['macd_bearish']) > 0:
        print(signals['macd_bearish'][['symbol', 'price', 'macd', 'signal']].to_string(index=False))
    else:
        print("   无")

    print("\n" + "=" * 80)


# ==================== 性能测试 ====================

def performance_test():
    """测试批量计算性能"""
    import time

    print("\n=== 性能测试 ===")

    # 主流币种列表
    symbols = [
        'BTC/USDT', 'ETH/USDT', 'BNB/USDT', 'SOL/USDT', 'ADA/USDT',
        'XRP/USDT', 'DOGE/USDT', 'DOT/USDT', 'MATIC/USDT', 'LINK/USDT'
    ]

    # 测试数据获取
    print("\n1. 数据获取测试:")
    start = time.time()
    data = fetch_multiple_symbols(symbols, '1h', 500)
    fetch_time = time.time() - start
    print(f"   获取10个币种数据耗时: {fetch_time:.2f}秒")
    print(f"   成功获取: {len(data)}/{len(symbols)} 个币种")

    # 测试指标计算
    print("\n2. 指标计算测试:")
    start = time.time()
    report = calculate_indicators_batch(data)
    calc_time = time.time() - start
    print(f"   计算10个币种指标耗时: {calc_time:.2f}秒")

    # 性能目标: 批量计算 < 2秒
    if calc_time < 2:
        print("   ✓ 性能测试通过!")
    else:
        print("   ✗ 性能需要优化")

    return data, report


# ==================== 主程序 ====================

def main():
    """主程序"""
    print("=" * 80)
    print("项目2: 批量币种技术指标计算器")
    print("=" * 80)

    # 定义要分析的币种
    symbols = [
        'BTC/USDT',  # 比特币
        'ETH/USDT',  # 以太坊
        'BNB/USDT',  # 币安币
        'SOL/USDT',  # Solana
        'ADA/USDT',  # Cardano
        'XRP/USDT',  # Ripple
        'DOGE/USDT', # 狗狗币
        'DOT/USDT',  # Polkadot
        'MATIC/USDT',# Polygon
        'LINK/USDT'  # Chainlink
    ]

    print(f"\n正在分析 {len(symbols)} 个币种...")
    print("币种列表:", ', '.join([s.split('/')[0] for s in symbols]))

    try:
        # 1. 获取数据
        print("\n步骤1: 获取历史数据...")
        data = fetch_multiple_symbols(symbols, timeframe='1h', limit=500)
        print(f"✓ 成功获取 {len(data)} 个币种的数据")

        # 2. 计算指标
        print("\n步骤2: 计算技术指标...")
        report = calculate_indicators_batch(data)
        print(f"✓ 完成 {len(report)} 个币种的指标计算")

        # 3. 生成信号
        print("\n步骤3: 生成交易信号...")
        signals = generate_trading_signals(report)

        # 4. 打印报告
        print_report(signals)

        # 5. 保存结果 (可选)
        report.to_csv('crypto_indicators_report.csv', index=False)
        print("\n✓ 报告已保存到: crypto_indicators_report.csv")

    except Exception as e:
        print(f"\n✗ 错误: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    # 运行主程序
    main()

    # 可选: 运行性能测试
    # data, report = performance_test()
