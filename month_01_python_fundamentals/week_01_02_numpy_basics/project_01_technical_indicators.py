"""
项目1: 用NumPy实现技术指标
Project 1: Technical Indicators Implementation with NumPy

技术指标:
- MA (Moving Average) - 移动平均线
- EMA (Exponential Moving Average) - 指数移动平均线
- RSI (Relative Strength Index) - 相对强弱指标
- MACD (Moving Average Convergence Divergence) - 平滑异同移动平均线

作者: [Your Name]
日期: 2025-01-12
"""

import numpy as np
from typing import Dict, Union


def calculate_ma(prices: np.ndarray, period: int) -> np.ndarray:
    """
    计算简单移动平均线 (Simple Moving Average)

    参数:
        prices: 价格数组
        period: 周期 (如20日均线)

    返回:
        MA值数组 (长度为 len(prices) - period + 1)

    示例:
        >>> prices = np.array([100, 102, 101, 105, 107])
        >>> ma = calculate_ma(prices, 3)
        >>> print(ma)  # [101.0, 102.67, 104.33]
    """

    # TODO: 实现MA计算
    # 提示: 使用 np.convolve() 或 rolling window

    i  = 2
    moving_averages = []
    while i <= prices.size:
        if i >= period:
            window_average = np.sum(prices[i - period:i]) / period
            moving_averages.append(window_average)
        i += 1
    print(moving_averages)
    return np.asarray(moving_averages)


def calculate_ema(prices: np.ndarray, period: int) -> np.ndarray:
    """
    计算指数移动平均线 (Exponential Moving Average)

    EMA计算公式:
        α = 2 / (period + 1)
        EMA[0] = prices[0]
        EMA[i] = α * prices[i] + (1 - α) * EMA[i-1]

    参数:
        prices: 价格数组
        period: 周期

    返回:
        EMA值数组 (与prices长度相同)

    示例:
        >>> prices = np.array([100, 102, 101, 105, 107])
        >>> ema = calculate_ema(prices, 3)
    """
    # TODO: 实现EMA计算
    # 提示: 使用循环或向量化计算
    i  = 1
    α = 2 / (period + 1)
    moving_averages = []
    moving_averages.append(prices[0])
    while i < prices.size:
        window_average = α * prices[i] + (1 - α) * moving_averages[i - 1]
        moving_averages.append(window_average)
        i += 1
    print(moving_averages)
    return np.asarray(moving_averages)


def calculate_rsi(prices: np.ndarray, period: int = 14) -> np.ndarray:
    """
    计算相对强弱指标 (Relative Strength Index)

    RSI计算公式:
        1. 计算价格变化: deltas = diff(prices)
        2. 分离涨跌: gains (>0), losses (<0)
        3. 计算平均涨跌幅: avg_gains, avg_losses (使用EMA)
        4. RS = avg_gains / avg_losses
        5. RSI = 100 - 100/(1 + RS)

    参数:
        prices: 价格数组
        period: 周期 (默认14)

    返回:
        RSI值数组 (0-100之间)

    解读:
        RSI > 70: 超买区域
        RSI < 30: 超卖区域

    示例:
        >>> prices = np.array([100, 102, 101, 105, 107, 106, 108, 110])
        >>> rsi = calculate_rsi(prices, period=5)
    """
    # TODO: 实现RSI计算
    # 步骤:
    # 1. 计算价格变化
    # 2. 分离涨跌
    # 3. 计算平均涨跌幅
    # 4. 计算RS和RSI
    pass


def calculate_macd(
    prices: np.ndarray,
    fast_period: int = 12,
    slow_period: int = 26,
    signal_period: int = 9
) -> Dict[str, np.ndarray]:
    """
    计算MACD指标 (Moving Average Convergence Divergence)

    MACD计算公式:
        MACD Line = EMA(12) - EMA(26)
        Signal Line = EMA(MACD, 9)
        Histogram = MACD Line - Signal Line

    参数:
        prices: 价格数组
        fast_period: 快线周期 (默认12)
        slow_period: 慢线周期 (默认26)
        signal_period: 信号线周期 (默认9)

    返回:
        字典包含:
        - 'macd': MACD线
        - 'signal': 信号线
        - 'histogram': 柱状图

    交易信号:
        - MACD上穿Signal: 买入信号
        - MACD下穿Signal: 卖出信号
        - Histogram由负转正: 看涨
        - Histogram由正转负: 看跌

    示例:
        >>> prices = np.array([...])  # 至少26+9=35个数据点
        >>> macd_data = calculate_macd(prices)
        >>> print(macd_data['macd'][-1])
    """
    # TODO: 实现MACD计算
    # 步骤:
    # 1. 计算快线EMA(12)
    # 2. 计算慢线EMA(26)
    # 3. MACD = 快线 - 慢线
    # 4. Signal = EMA(MACD, 9)
    # 5. Histogram = MACD - Signal
    pass


def calculate_all_indicators(
    prices: np.ndarray,
    ma_period: int = 20,
    ema_period: int = 12,
    rsi_period: int = 14
) -> Dict[str, np.ndarray]:
    """
    一次性计算所有技术指标

    参数:
        prices: 价格数组
        ma_period: MA周期
        ema_period: EMA周期
        rsi_period: RSI周期

    返回:
        包含所有指标的字典
    """
    return {
        'ma': calculate_ma(prices, ma_period),
        'ema': calculate_ema(prices, ema_period),
        'rsi': calculate_rsi(prices, rsi_period),
        'macd': calculate_macd(prices)
    }


# ==================== 性能测试 ====================

def performance_test():
    """测试指标计算性能"""
    import time

    # 生成测试数据
    prices = np.random.randn(500).cumsum() + 100

    # 测试MA
    start = time.time()
    ma = calculate_ma(prices, 20)
    ma_time = (time.time() - start) * 1000
    print(f"MA计算时间: {ma_time:.2f}ms")

    # 测试EMA
    start = time.time()
    ema = calculate_ema(prices, 20)
    ema_time = (time.time() - start) * 1000
    print(f"EMA计算时间: {ema_time:.2f}ms")

    # 测试RSI
    start = time.time()
    rsi = calculate_rsi(prices, 14)
    rsi_time = (time.time() - start) * 1000
    print(f"RSI计算时间: {rsi_time:.2f}ms")

    # 测试MACD
    start = time.time()
    macd = calculate_macd(prices)
    macd_time = (time.time() - start) * 1000
    print(f"MACD计算时间: {macd_time:.2f}ms")

    total_time = ma_time + ema_time + rsi_time + macd_time
    print(f"\n总计算时间: {total_time:.2f}ms")

    # 性能目标: < 100ms
    if total_time < 100:
        print("✓ 性能测试通过!")
    else:
        print("✗ 性能需要优化")


# ==================== 单元测试 ====================

def test_indicators():
    """简单的功能测试"""
    print("\n=== 功能测试 ===")

    # 创建测试数据
    prices = np.array([100, 102, 101, 105, 107, 106, 108, 110, 109, 111, 113, 112, 115, 117, 116])

    prices2 = np.array([100, 102, 101, 105, 107])
    calculate_ma(prices2, 3)

    # 测试MA
    print("\n1. 测试MA:")
    try:
        ma = calculate_ma(prices, 5)
        print(f"   MA长度: {len(ma)} (预期: {len(prices)-4})")
        print(f"   最后3个MA值: {ma[-3:]}")
    except Exception as e:
        print(f"   ✗ MA测试失败: {e}")

    # 测试EMA
    print("\n2. 测试EMA:")
    try:
        ema = calculate_ema(prices, 5)
        print(f"   EMA长度: {len(ema)} (预期: {len(prices)})")
        print(f"   首个EMA值: {ema[0]} (应等于首个价格: {prices[0]})")
        print(f"   最后3个EMA值: {ema[-3:]}")
    except Exception as e:
        print(f"   ✗ EMA测试失败: {e}")

    # 测试RSI
    print("\n3. 测试RSI:")
    try:
        rsi = calculate_rsi(prices, 5)
        print(f"   RSI长度: {len(rsi)}")
        print(f"   RSI范围: [{rsi.min():.2f}, {rsi.max():.2f}] (应在0-100)")
        print(f"   最后3个RSI值: {rsi[-3:]}")
    except Exception as e:
        print(f"   ✗ RSI测试失败: {e}")

    # 测试MACD
    print("\n4. 测试MACD:")
    try:
        macd_data = calculate_macd(prices)
        print(f"   MACD长度: {len(macd_data['macd'])}")
        print(f"   最后MACD值: {macd_data['macd'][-1]:.4f}")
        print(f"   最后Signal值: {macd_data['signal'][-1]:.4f}")
        print(f"   最后Histogram值: {macd_data['histogram'][-1]:.4f}")
    except Exception as e:
        print(f"   ✗ MACD测试失败: {e}")


# ==================== 主程序 ====================

if __name__ == "__main__":
    print("=" * 60)
    print("项目1: 技术指标实现")
    print("=" * 60)

    # 运行功能测试
    test_indicators()

    # 运行性能测试
    print("\n" + "=" * 60)
    print("性能测试")
    print("=" * 60)
    performance_test()

    print("\n" + "=" * 60)
    print("提示: 完成所有TODO后运行此文件进行测试")
    print("=" * 60)
