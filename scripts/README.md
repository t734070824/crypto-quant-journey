# 脚本目录

此目录包含各种工具脚本和自动化任务。

## 目录结构

```
scripts/
├── data_collection/   # 数据采集脚本
├── indicators/        # 技术指标计算
├── analysis/          # 分析工具
├── utils/            # 通用工具函数
└── automation/       # 自动化任务
```

## 脚本类别

### 数据采集
- 交易所数据下载
- 新闻数据抓取
- 链上数据获取
- 社交媒体数据采集

### 数据处理
- 数据清洗和标准化
- 特征工程
- 数据聚合和转换

### 分析工具
- 市场分析脚本
- 性能评估工具
- 可视化脚本

### 自动化
- 定时任务
- 数据更新
- 报告生成

## 使用示例

```bash
# 下载历史数据
python scripts/data_collection/download_ohlcv.py --symbol BTC/USDT --days 365

# 计算技术指标
python scripts/indicators/calculate_indicators.py --input data/raw/btc.csv

# 生成分析报告
python scripts/analysis/generate_report.py --date 2025-10-12
```

## 配置

脚本配置文件位于 `config/` 目录，包括：
- API密钥配置
- 交易所设置
- 数据源配置

**注意**：不要将API密钥提交到版本控制！

## 依赖管理

所有脚本的依赖包都在项目根目录的 `requirements.txt` 中定义。
