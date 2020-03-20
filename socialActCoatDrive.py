print("모든 것의 가치를 산정한다는 것은 어려운 일이다. \n하지만 모든 것은 가치가 있다. 공짜라고 진짜 가치가 없는 것은 아니다. \n공기가 없다면 생명체는 살 수 없다. \n맑은 공기를 마시시 위해서 우리가 지불해야하는 가치(비용)은 얼마가 될까. \n 이 계산기는 이러한 문제를 계산해보고 가진것들의 가치를 다시한번 생각해 보자.")
print()
x=  input("activity 'If you donate your coat, how much would it be worth? How many coats will you donate?': ")

inputA= float(x) 

VOF  = inputA * 200 

#1ton= 1000l / 2$ , 10,000L 1 coat ==> 20$
WasteWaterCost = inputA * 20

#value of recycle. Direct effect : 100L wastbag/2$, Indirect effect: 1)recycle fabric=$0.5. 2)solid fuel:$0.95
VOFRecycleDirect = inputA * 2
VOFRecycleIndirect_fab = inputA * 0.5
VOFRecycleIndirect_fuel = inputA * 0.95



print()
print("According to statistics from the Ministry of Environment, the amount of waste fibers emitted during the garment production phase amounts to about 224 tons a day, and about 82,200 tons of waste fibers are generated annually.")
print("If you add the lung leather used in shoes and bags, that's going to be a lot. The only solution is incineration, as waste fiber and waste leather are not recyclable.")
print(" Clothing waste, which stood at 54,677 tons a year in 2008, increased 32.4 percent to 74,361 tons a year in 2014, and is still growing rapidly. Recycling clothes produces direct and indirect benefits.")
print("...")
print()
print("The value of a coat-donating action:$", round(VOF))
print("The cost of water to produce clothes:$", round(WasteWaterCost))
print("The value of recycle:$", round(VOFRecycleDirect))
print("the Value of recycle fabric:$", VOFRecycleIndirect_fab)
print("the Value of solid fuel:$", VOFRecycleIndirect_fuel)

