import os
import matplotlib.pyplot as plt
from netCDF4 import Dataset as netcdf_dataset
import numpy as np

from cartopy import config
import cartopy.crs as ccrs


dataset = netcdf_dataset('data.nc')
dimensions = dataset.variables.keys()

sst = dataset.variables['u10'][0, :, :]
lats = dataset.variables['latitude'][:]
lons = dataset.variables['longitude'][:]

print(sst, lats, lons)
ax = plt.axes(projection=ccrs.PlateCarree())

plt.contourf(lons, lats, sst, 60,
             transform=ccrs.PlateCarree())

ax.coastlines()

plt.show()