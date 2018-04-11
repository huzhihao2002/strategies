'''
策略出处: https://www.botvs.com/strategy/54256
策略名称: 数字货币定投
策略作者: ankye
策略描述:

数字货币通用定投策略，支持多交易所同时定投

# 参数说明
orderAmount #定投金额 BTCCNY和BCCCNY 单位 CNY, BCCBTC 单位 BTC 等等

accountLimitMoney #账户限额,保留一部分钱，账户达到最低限额就停止定投


orderTimeInterval #定投间隔,单位秒, 每分钟=60 每小时= 3600  每天=86400 每周=604800

maxBidPrice  #最大交易价格，超过价格就跳过，等待下次交易机会出现


参数                 默认值    描述
-----------------  -----  -------------------
orderAmount        true   order amount
maxBidPrice        false  max bid price
accountLimitMoney  false  account limit money
orderTimeInterval  60     Order Time Interval
'''

def onTick():
	
	exchange_count = len(exchanges)
	for i in range(exchange_count):
		account = exchanges[i].GetAccount()

		marketName = exchanges[i].GetName()
		depth = exchanges[i].GetDepth()
		Log("Market ",marketName,exchanges[i].GetCurrency(),"Account Balance [",account["Balance"],"] Stocks[",account["Stocks"],"]")
		if account and depth and account["Balance"] > accountLimitMoney :
			bidPrice = depth["Asks"][0]["Price"] 
			if bidPrice <  maxBidPrice :
				amount = orderAmount
				if amount <= account["Balance"]:
					exchanges[i].Buy(amount)
				else:
					Log("Account Balance is less than bid Amount")
			else:
				Log("Bid Price >= maxBidPrice, not process")
		else:
			Log("Account Balance <= accountLimitMoney")
def main() :
	while 1:
		
		onTick()
		time.sleep(orderTimeInterval)
