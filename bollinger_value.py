# 볼린저 밴드 계산을 위한 데이터 추출
def get_data_frame(symbol0,candle_time):
    markets('{}'.format(symbol0))
    bars = binance1.fetch_ohlcv(symbol0,'{}'.format(candle_time))
    sleep(rest_time)
    df = pd.DataFrame(bars, columns=['date', 'open', 'high', 'low', 'close','volume']) 
    for line in bars:        
        del line[5:]
    df = pd.DataFrame(bars, columns=['date', 'open', 'high', 'low', 'close']) 
    return df

# 볼린저 밴드 계산
def bollinger_trade_logic(symbol0,candle_time):
    global ma,upper,lower
    symbol_df = get_data_frame(symbol0,candle_time)
    period = 20
    ma = symbol_df['sma'] = symbol_df['close'].rolling(period).mean()
    symbol_df['std'] = symbol_df['close'].rolling(period).std()
    upper = symbol_df['upper'] = symbol_df['sma']  + (2 * symbol_df['std'])
    lower= symbol_df['lower'] = symbol_df['sma']  - (2 * symbol_df['std'])

# 볼린저 밴드 중앙선 값 
def bb_ma(symbol0,candle_time):
    bollinger_trade_logic(symbol0,candle_time)
    bb_ma=ma[498]
    return bb_ma

# 볼린저 밴드 상단선 값 
def bb_upper(symbol0,candle_time):
    bollinger_trade_logic(symbol0,candle_time)
    bb_upper=upper[498]
    return bb_upper

# 볼린저 밴드 하단선 값 
def bb_lower(symbol0,candle_time):
    bollinger_trade_logic(symbol0,candle_time)
    bb_lower=lower[498]
    return bb_lower