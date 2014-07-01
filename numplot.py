import matplotlib.pyplot as plot
fig1 = plot.figure()
ax1=fig1.add_subplot(1,1,1)
ax1.pie([3,2,9,5],[0.2,0.2,0.2,0.2],["a","b","c","d"])
ax1.set_xlabel("bar sample")
plot.show()

