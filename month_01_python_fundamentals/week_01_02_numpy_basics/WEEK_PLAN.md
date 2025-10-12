# Week 1-2 学习计划: NumPy基础与技术指标实现

**学习时间**: 第1-2周 (14天)
**核心目标**: 掌握NumPy向量化计算,实现基础技术指标

---

## 📅 每日学习计划

### Day 1-2: Python高级特性 + NumPy基础

**理论学习 (3小时)**
- [ ] Python装饰器原理和应用
- [ ] 生成器和迭代器
- [ ] NumPy数组创建和基本操作
- [ ] NumPy广播机制 (Broadcasting)

**实践任务**
- [ ] 编写3个装饰器: @timer, @cache, @validate_input
- [ ] 创建NumPy数组并测试广播机制

**学习资源**
- NumPy官方快速入门: https://numpy.org/doc/stable/user/quickstart.html
- Python装饰器教程

---

### Day 3-4: 项目1 - 移动平均线 (MA & EMA)

**理论学习 (1小时)**
- [ ] MA (Simple Moving Average) 计算原理
- [ ] EMA (Exponential Moving Average) 计算公式
- [ ] 理解平滑系数 α = 2/(N+1)

**实践任务**
- [ ] 实现 `calculate_ma(prices, period)` 函数
- [ ] 实现 `calculate_ema(prices, period)` 函数
- [ ] 对比循环实现 vs 向量化实现的性能

**代码示例**
```python
import numpy as np

def calculate_ma(prices, period):
    """计算简单移动平均线"""
    return np.convolve(prices, np.ones(period)/period, mode='valid')

def calculate_ema(prices, period):
    """计算指数移动平均线"""
    alpha = 2 / (period + 1)
    ema = np.zeros_like(prices)
    ema[0] = prices[0]

    for i in range(1, len(prices)):
        ema[i] = alpha * prices[i] + (1 - alpha) * ema[i-1]

    return ema
```

**验收标准**
- [ ] MA计算结果与TradingView一致
- [ ] EMA计算结果与TradingView一致
- [ ] 500条数据计算时间 < 10ms

---

### Day 5-6: 项目1 - RSI指标

**理论学习 (1小时)**
- [ ] RSI (Relative Strength Index) 计算原理
- [ ] 理解RS = 平均涨幅 / 平均跌幅
- [ ] RSI = 100 - 100/(1+RS)

**实践任务**
- [ ] 实现 `calculate_rsi(prices, period=14)` 函数
- [ ] 使用NumPy向量化计算
- [ ] 处理边界情况 (前N个数据点)

**代码框架**
```python
def calculate_rsi(prices, period=14):
    """计算RSI指标"""
    deltas = np.diff(prices)

    gains = np.where(deltas > 0, deltas, 0)
    losses = np.where(deltas < 0, -deltas, 0)

    # 使用EMA计算平均涨跌幅
    avg_gains = calculate_ema(gains, period)
    avg_losses = calculate_ema(losses, period)

    rs = avg_gains / (avg_losses + 1e-10)  # 避免除零
    rsi = 100 - 100 / (1 + rs)

    return rsi
```

**验收标准**
- [ ] RSI范围在0-100之间
- [ ] RSI > 70 表示超买
- [ ] RSI < 30 表示超卖

---

### Day 7-8: 项目1 - MACD指标

**理论学习 (1小时)**
- [ ] MACD (Moving Average Convergence Divergence) 原理
- [ ] MACD = EMA(12) - EMA(26)
- [ ] Signal Line = EMA(MACD, 9)
- [ ] Histogram = MACD - Signal

**实践任务**
- [ ] 实现 `calculate_macd(prices)` 函数
- [ ] 返回三条线: MACD, Signal, Histogram
- [ ] 绘制MACD图表

**代码框架**
```python
def calculate_macd(prices):
    """计算MACD指标"""
    ema_12 = calculate_ema(prices, 12)
    ema_26 = calculate_ema(prices, 26)

    macd_line = ema_12 - ema_26
    signal_line = calculate_ema(macd_line, 9)
    histogram = macd_line - signal_line

    return {
        'macd': macd_line,
        'signal': signal_line,
        'histogram': histogram
    }
```

**验收标准**
- [ ] MACD线穿越Signal线产生买卖信号
- [ ] Histogram的正负变化正确
- [ ] 能够绘制清晰的MACD图表

---

### Day 9-10: 项目1完善 + 单元测试

**任务清单**
- [ ] 为所有指标编写单元测试
- [ ] 添加详细的函数文档字符串
- [ ] 代码重构和优化
- [ ] 创建 `indicators.py` 模块

**单元测试示例**
```python
import unittest
import numpy as np

class TestTechnicalIndicators(unittest.TestCase):
    def setUp(self):
        # 创建测试数据
        self.prices = np.array([100, 102, 101, 105, 107, 106, 108, 110, 109, 111])

    def test_ma_length(self):
        """测试MA返回的长度"""
        ma = calculate_ma(self.prices, period=5)
        self.assertEqual(len(ma), len(self.prices) - 4)

    def test_rsi_range(self):
        """测试RSI范围在0-100"""
        rsi = calculate_rsi(self.prices, period=5)
        self.assertTrue(np.all((rsi >= 0) & (rsi <= 100)))

    def test_ema_first_value(self):
        """测试EMA第一个值等于价格第一个值"""
        ema = calculate_ema(self.prices, period=5)
        self.assertEqual(ema[0], self.prices[0])

if __name__ == '__main__':
    unittest.main()
```

---

### Day 11-12: 项目2 - 批量币种数据获取

**理论学习 (2小时)**
- [ ] 学习ccxt库基本用法
- [ ] 理解OHLCV数据格式
- [ ] 了解API限流机制

**实践任务**
- [ ] 安装ccxt: `pip install ccxt`
- [ ] 编写 `fetch_multiple_symbols()` 函数
- [ ] 批量获取10个币种的历史数据

**代码框架**
```python
import ccxt
import pandas as pd

def fetch_multiple_symbols(symbols, timeframe='1h', limit=500):
    """批量获取多个币种数据"""
    exchange = ccxt.binance()
    all_data = {}

    for symbol in symbols:
        try:
            ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
            df = pd.DataFrame(
                ohlcv,
                columns=['timestamp', 'open', 'high', 'low', 'close', 'volume']
            )
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            all_data[symbol] = df
            print(f"✓ {symbol} 数据获取成功")
        except Exception as e:
            print(f"✗ {symbol} 获取失败: {e}")

    return all_data

# 测试
symbols = ['BTC/USDT', 'ETH/USDT', 'BNB/USDT', 'SOL/USDT', 'ADA/USDT']
data = fetch_multiple_symbols(symbols)
```

**验收标准**
- [ ] 成功获取10个币种数据
- [ ] 每个币种500条K线数据
- [ ] 数据格式正确(OHLCV)

---

### Day 13-14: 项目2 - 批量指标计算和报告

**实践任务**
- [ ] 对所有币种批量计算技术指标
- [ ] 生成跨币种对比报告
- [ ] 找出超卖/超买的币种

**代码框架**
```python
def calculate_indicators_batch(data_dict):
    """批量计算技术指标"""
    results = []

    for symbol, df in data_dict.items():
        prices = df['close'].values

        # 计算所有指标
        df['ma_20'] = calculate_ma(prices, 20)
        df['ema_12'] = calculate_ema(prices, 12)
        df['rsi'] = calculate_rsi(prices, 14)

        macd_data = calculate_macd(prices)
        df['macd'] = macd_data['macd']
        df['signal'] = macd_data['signal']

        # 获取最新值
        latest = {
            'symbol': symbol,
            'price': df['close'].iloc[-1],
            'rsi': df['rsi'].iloc[-1],
            'macd': df['macd'].iloc[-1],
            'signal': df['signal'].iloc[-1]
        }

        # 判断信号
        if latest['rsi'] < 30:
            latest['status'] = '超卖'
        elif latest['rsi'] > 70:
            latest['status'] = '超买'
        else:
            latest['status'] = '中性'

        results.append(latest)

    return pd.DataFrame(results)

# 生成报告
report = calculate_indicators_batch(data)
print(report.sort_values('rsi'))
```

**验收标准**
- [ ] 批量计算10个币种 < 2秒
- [ ] 报告包含所有关键指标
- [ ] 能够识别超卖/超买币种

---

## 📊 Week 1-2 总结检查

### 必须完成
- [ ] 项目1: 实现4个技术指标 (MA, EMA, RSI, MACD)
- [ ] 项目2: 批量币种指标计算器
- [ ] 所有代码通过单元测试
- [ ] 技术指标性能达标 (500条数据<100ms)

### 可选扩展
- [ ] 添加更多指标 (Bollinger Bands, ATR)
- [ ] 实现指标可视化
- [ ] 优化代码性能

### 学习笔记
在 `month_01_python_fundamentals/README.md` 中记录:
- 遇到的问题和解决方案
- 关键知识点总结
- 性能优化心得

---

## 📚 推荐学习资源

### NumPy
- 官方文档: https://numpy.org/doc/
- NumPy教程视频

### 技术指标
- TradingView指标百科
- Investopedia技术分析

### CCXT
- 官方文档: https://docs.ccxt.com/
- CCXT示例代码

---

**下周预告**: Week 3-4 将学习Pandas数据处理,实现更复杂的数据分析功能!

**最后更新**: 2025-01-12
