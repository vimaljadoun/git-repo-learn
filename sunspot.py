import numpy as np
import matplotlib.pyplot as plt
#font and axis equation setup using LATEX
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 12,
        }
plt.rcParams.update(plt.rcParamsDefault)


import matplotlib.pyplot as plt

# Read two-column data
year, sunspots = np.loadtxt("sunspotdata.txt",unpack=True,comments="#")

#plot
plt.plot(year,sunspots,'-', label='Sun')
plt.xlabel('Year')
plt.ylabel('Sunspot Number')
plt.title('Relative Sunspot Numbers')
plt.legend()
plt.minorticks_on()
plt.tick_params(axis="x", which="minor", direction="in", top=True)
plt.tick_params(axis="x", which="major", direction="in", top=True, labeltop=False, bottom=True, labelbottom=True)
plt.tick_params(axis="y", which="minor", direction="in", right=True)
plt.tick_params(axis="y", which="major", direction="in", right=True, labelright=False, left=True, labelleft=True)
plt.tight_layout()
plt.savefig('sunspot.png',dpi=300)
plt.show()
