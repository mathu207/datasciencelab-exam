import matplotlib.pyplot as plt
x=[2001,2002,2003,2004,2005,2006,2007]
y=[24000,22500,19700,17500,14500,10000,5800]
plt.xlabel("year")
plt.ylabel("value")
plt.plot(x,y,linestyle="dashdot",color="red",marker="*",markerfacecolor="green",markersize="20")
plt.title("value depreciation")
plt.show()


