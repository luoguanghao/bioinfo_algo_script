from os.path import dirname
import numpy
Inifite = 999999

dataset = open(dirname(__file__)+'dataset.txt').read().strip().split()
money = int(dataset[0])
coins = sorted([int(i) for i in dataset[1].split(',')])
coinNum = len(coins)

minMoneyNum = [0]*(money+2)
for m in range(1,money+1):
	minMoneyNum[m] = Inifite
	for c in coins:
		if ((m-c)>=0 and minMoneyNum[m-c]+1 < minMoneyNum[m]):
			minMoneyNum[m] = minMoneyNum[m-c]+1
			
print(minMoneyNum[money])