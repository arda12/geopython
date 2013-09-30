from datetime import datetime,timedelta
from mpl_toolkits.basemap import Basemap
import netCDF4 as nc
m = Basemap(llcrnrlon=0,llcrnrlat=-80,urcrnrlon=360,urcrnrlat=80,projection='mill', lat_1=40)

m.drawcoastlines()
points = ginput(4)
m(-87,30, inverse = True)
[m(*point,inverse =True) for point in points]
#kwargs {'inverse': True}
def foo(*args, **kwargs):
    print args
    print kwargs
    
#foo(1,2,3,b,a=True)
# foo(1,2,3,a=True,b=b)

# for more detail    
m3 = Basemap(llcrnrlon=-120,llcrnrlat=10,urcrnrlon=-50,urcrnrlat=50,projection='mill', lat_1=40, resolution = 'i')
m3.fillcontinents() # fill with color
m3.drawcoastlines(linewidth = 0.2)
m3.drawstates()

m3.drawcountries(l=2)
m3.drawrivers()
m3.llcrnrlat
type(m3.coastsegs)
#m3.coastsegs[400]
zip((1,2,3),(4,5,6),(8,9,10))
x,y = zip(*m3.coastsegs[400])
pairs =zip(x,y)
date = datetime.now().strf
nc=netCDF4.Dataset("http://nomads.ncep.noaa.gov:9090/dods/gfs_hd/gfs_hd%s/gfs_hd_%sz"%\
        (date[0:8],date[8:10]))

#imshow() # for showing the matrice
m3.drawmeridians(arange(0,90,5),labels([0,1,1,0])
m3.drawparallels(arange(0,90,5),labels([0,1,1,0])
