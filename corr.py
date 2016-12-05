import matplotlib.pyplot as plt, numpy as np, numpy.random, scipy

#data definition
N = 1000;
xdat, ydat = np.random.normal(size=N), np.random.normal(size=N)
#xdat, ydat = np.sin(np.arange(1, N)),np.cos(np.arange(1, N)+10)
#xdat, ydat = np.array([1,2,3,4,4,4,4,4,4,4]), np.array([1,2,3,4,4,4,4,4,4,4])


#histogram definition
xyrange = [[np.nanmin(xdat),np.nanmax(xdat)],[np.nanmin(ydat),np.nanmax(ydat)]] # data range
bins = [100,100] # number of bins
thresh = 1  #density threshold

#linear regression
from scipy import stats
mask = ~np.isnan(xdat) & ~np.isnan(xdat)
slope, intercept, r_value, p_value, std_err = stats.linregress(xdat[mask], ydat[mask])
line = slope * xdat + intercept

# histogram the data
hh, locx, locy = scipy.histogram2d(xdat, ydat, range=xyrange, bins=bins)
posx = np.digitize(xdat, locx)
posy = np.digitize(ydat, locy)

#select points within the histogram
ind = (posx > 0) & (posx <= bins[0]) & (posy > 0) & (posy <= bins[1])
hhsub = hh[posx[ind] - 1, posy[ind] - 1] # values of the histogram where the points are
xdat1 = xdat[ind][hhsub < thresh] # low density points
ydat1 = ydat[ind][hhsub < thresh]
hh[hh < thresh] = np.nan # fill the areas with low density by NaNs

plt.imshow(np.flipud(hh.T),cmap='jet',extent=np.array(xyrange).flatten(), interpolation='none', origin='upper')
plt.colorbar()
plt.plot(xdat1, ydat1, '.',color='darkblue')
plt.plot(xdat, line, 'r', label = 'Korrelation \n' + str(round(r_value, 3))
                                       + r'$\pm$' + str(round(std_err, 3)))
plt.legend(loc='upper left', ncol=1, fancybox=True, shadow=True,
           fontsize='20')
plt.grid()
plt.show()

