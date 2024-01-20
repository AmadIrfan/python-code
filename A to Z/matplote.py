import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [10,9,8,7,6,5,4,3,2,1]


plt.plot(x,y,color='green')
plt.title('Daily Steps')
plt.xlabel('steps')
plt.ylabel('Date')
plt.xticks(rotation=90)
plt.savefig('adsad')
plt.show()
