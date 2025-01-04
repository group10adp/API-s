import yfinance as yf

indian_etfs = {
    "ICICI Prudential Bluechip Fund": "ICICINIFTY.NS",  # Bluechip ETF
    "HDFC Top 100 Fund": "HDFCNIFETF.NS",  # Nifty ETF
    "Axis Bluechip Fund": "AXISNIFTY.NS",  # Nifty 50 ETF
    "Nippon India Mutual Fund": "08GPG.BO",
    "Kotak Equity Savings Fund":"0P00014HE7.BO",  # Nifty ETF
    "Reliance Life Pure Equity Fund":"0P0000NPKG.BO",  # Nifty 50 ETF


    "Aditya Birla Sun Life MNC Fund " : "0P00005V5R.BO",  # Frontline ETF
    
    
    "IDFC Nifty 50 ETF" : "IDFNIFTYET.NS",  # Nifty ETF

    "HDFC Pharma and Healthcare Fund" : "0P0001RK6V.BO",  # Balanced ETF

    "Kotak Low Duration Fund" : "0P0000GBDS.BO",  # Equity ETF
    
    "Tata AIA Life-Super Select Equity" : "0P0000NQJX.BO", 

    "Tata Multicap Dir IDCW-P" : "0P0001QCAT.BO",  # Equity ETF

    "Sundaram Select Focus Fund": "0P000162E4",  # Focus ETF
    "SBI Small Cap Fund": "0P0001BB9I.BO",
    "Tata Small Cap Fund": "0P0001EUZV.BO",  # Small Cap ETF
     "Nippon India Short Term Mn IDCW-R" : "0P0001BB5M.BO",

     "NIFTY100 ESG":"NIFTY100_ESG.NS",
     "Motilal Oswal S&P 500 Index Reg Gr":"0P0001JMZC.BO",
        "SBI PSU Dir Gr": "0P0000XVLF.BO",
    "SBI Long Term Equity Fund Dir Gr" : "0P0000XVL9.BO",
    "Groww Mutual Fund - Groww Nifty India Defence Etf" : "GROWWDEFNC.NS",


    
}



# List of ETF symbols
etf_symbols = list(indian_etfs.values())

# Fetch data for each ETF
for symbol in etf_symbols:
    try:
        etf = yf.Ticker(symbol)
        etf_info = etf.info
        print(f"{symbol}: {etf_info['shortName']} - {etf_info['regularMarketPrice']}")
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
