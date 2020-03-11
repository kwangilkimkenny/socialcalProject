print("모든 것의 가치를 산정한다는 것은 어려운 일이다. \n하지만 모든 것은 가치가 있다. 공짜라고 진짜 가치가 없는 것은 아니다. \n공기가 없다면 생명체는 살 수 없다. \n맑은 공기를 마시시 위해서 우리가 지불해야하는 가치(비용)은 얼마가 될까. \n 이 계산기는 이러한 문제를 계산해보고 가진것들의 가치를 다시한번 생각해 보자.")
print()
x=  input("activity 'the value of lowering heating by ? degree.': ")

inputA= float(x) 

Valueofyear  = inputA * 23 * 231
Valueofday = Valueofyear / 365

print()
print("It can reduce the temperature by one degree by 231 kilograms a year.")
print("CER(certified emission reduction) is $23 for 1 KG")
print()
print("value of day:$", round(Valueofday))
print("value of year:$", round(Valueofyear))

