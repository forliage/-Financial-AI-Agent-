import pandas as pd
import yfinance as yf
import tushare as ts
from datetime import datetime, timedelta
from .config_manager import get_tushare_token

# 初始化 Tushare Pro API
# 只有在 .env 文件中配置了token，我们才能初始化
TUSHARE_TOKEN = get_tushare_token()
if TUSHARE_TOKEN:
    ts.set_token(TUSHARE_TOKEN)
    pro = ts.pro_api()
else:
    pro = None
    print("警告: 未在 .env 文件中配置 TUSHARE_TOKEN。无法获取A股数据。")


def get_a_share_code(ticker: str) -> str:
    """
    将普通A股代码转换为Tushare所需的格式 (例如 '600519' -> '600519.SH')
    """
    ticker = ticker.split('.')[0] # 去掉可能存在的 .SZ/.SS 后缀
    if ticker.startswith('6'):
        return f"{ticker}.SH"  # 上海交易所
    else:
        return f"{ticker}.SZ"  # 深圳交易所 (包括00, 30, 02开头)

def fetch_stock_data(
    ticker: str, 
    period: str = "1y"
) -> pd.DataFrame | None:
    """
    获取指定股票代码的历史行情数据。
    能自动识别是A股代码还是国际市场代码。

    Args:
        ticker (str): 股票代码。
                      - A股示例: '600519' (贵州茅台), '000001.SZ' (平安银行)
                      - 美股示例: 'AAPL' (苹果), 'GOOG' (谷歌)
        period (str, optional): 获取数据的时间范围。默认为 "1y" (一年).
                                支持 yfinance 的所有时间段: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max

    Returns:
        pd.DataFrame | None: 包含OHLCV（开、高、低、收、量）数据的DataFrame，
                              索引为日期。如果失败则返回None。
    """
    print(f"正在为 '{ticker}' 获取数据...")
    try:
        # 启发式规则：判断是否为A股代码
        is_a_share = (ticker.isdigit() and len(ticker) == 6) or \
                     ticker.upper().endswith('.SS') or \
                     ticker.upper().endswith('.SZ')

        if is_a_share:
            if not pro:
                print("错误: Tushare API 未初始化，请检查你的TUSHARE_TOKEN配置。")
                return None
            
            # 使用 Tushare 获取A股数据
            end_date = datetime.now()
            # 简单地根据period估算天数
            days_map = {"1y": 365, "2y": 730, "5y": 1825, "10y": 3650, "max": 7300}
            days_to_subtract = days_map.get(period, 365) # 默认为1年
            start_date = end_date - timedelta(days=days_to_subtract)

            start_date_str = start_date.strftime('%Y%m%d')
            end_date_str = end_date.strftime('%Y%m%d')
            
            ts_code = get_a_share_code(ticker)
            
            # 使用 pro_bar 接口获取前复权日线行情
            df = pro.pro_bar(ts_code=ts_code, adj='qfq', 
                             start_date=start_date_str, end_date=end_date_str)
            
            if df is None or df.empty:
                print(f"错误: Tushare 未能获取到 '{ticker}' 的数据。")
                return None
            
            # --- 数据清洗和格式化 ---
            # Tushare返回的列名是小写的，我们需要统一格式
            df.rename(columns={
                'trade_date': 'Date', 'open': 'Open', 'high': 'High',
                'low': 'Low', 'close': 'Close', 'vol': 'Volume'
            }, inplace=True)
            # Tushare返回的日期是 YYYYMMDD 字符串，需要转换
            df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')
            # Tushare默认按日期降序返回，我们需要升序
            df.sort_values('Date', inplace=True)
            # 设置日期为索引
            df.set_index('Date', inplace=True)
            # 只保留我们需要的列
            df = df[['Open', 'High', 'Low', 'Close', 'Volume']]

        else:
            # 使用 yfinance 获取国际市场数据 (这部分逻辑不变)
            stock = yf.Ticker(ticker)
            df = stock.history(period=period)
            
            if df.empty:
                print(f"错误: yfinance 未能获取到 '{ticker}' 的数据。可能是代码错误或网络问题。")
                return None
        
        print(f"成功获取 '{ticker}' 的数据，共 {len(df)} 条记录。")
        return df

    except Exception as e:
        print(f"获取 '{ticker}' 数据时发生未知错误: {e}")
        return None