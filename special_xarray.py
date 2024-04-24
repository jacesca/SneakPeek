"""
pip install xarray
pip install matplotlib
pip install netCDF4 


pip install "xarray[io]"        # Install optional dependencies for handling I/O
pip install "xarray[accel]"     # Install optional dependencies for accelerating xarray
pip install "xarray[parallel]"  # Install optional dependencies for dask arrays
pip install "xarray[viz]"       # Install optional dependencies for visualization
pip install "xarray[complete]"  # Install all the above

Documentation:
https://docs.xarray.dev/en/stable/getting-started-guide/quick-overview.html
"""

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import xarray as xr


print('------------------------------------------------------')
print('CREATE A DATA XARRAY..................................')
data = xr.DataArray(
    np.random.randn(2, 3), 
    dims=("x", "y"), 
    coords={"x": [10, 20]})
print(data, end='\n\n')
print(type(data), end='\n\n\n\n')

other_data = xr.DataArray(pd.Series(range(3), index=list("abc"), name="foo"))
print(other_data)


print('------------------------------------------------------')
print('KEY PROPERTIES........................................')
print('Like in pandas:', data.values, sep='\n')
print('Dimensions:', data.dims, '\n\n')
print('Coords:', data.coords, '\n\n')
print(data.coords["x"],'\n\n')
print(data.coords["y"])

data.attrs['Doc'] = 'Testing...'
print('Attributes: ', data.attrs)

print('------------------------------------------------------')
print('INDEXING..............................................')

print(data.values, '\n\n')

# positional and by integer label, like numpy
print(data[0, :].values)

# loc or "location": positional and coordinate label, like pandas
print(data.loc[10].values)

# isel or "integer select":  by dimension name and integer label
print(data.isel(x=0).values)

# sel or "select": by dimension name and coordinate label
print(data.sel(x=10).values)

print('------------------------------------------------------')
print('ATTRIBUTES............................................')

data.attrs["long_name"] = "random velocity"
data.attrs["units"] = "metres/sec"
data.attrs["description"] = "A random variable created as an example."
data.attrs["random_attribute"] = 123
print(data.attrs)

print('------------------------------------------------------')
print('COMPUTATION...........................................')

print(
    # Similar to numpy array
    'Similar to numpy array:',
    data.values,
    (data + 10).values,
    np.sin(data).values,
    data.T.values,
    data.sum().values,
    
    # Aggregation
    '\nAggregation:',
    data.mean(dim="x").values,
    data.mean(dim="y").values,
)

print('------------------------------------------------------')
print('ARITHMETIC OPER BROADCAS BASED ON DIMENSIONS..........')

a = xr.DataArray(np.random.randint(10, size=3), [data.coords["y"]])
b = xr.DataArray(np.random.randint(10, size=4), dims="z")

print(
    a, 
    b, 
    a + b,
    b + a, 
    sep='\n\n\n'
)
 
print('------------------------------------------------------')
print('OTHER CALCULATIONS....................................')

print(
    data.values,
    data[:-1].values,
    data[:1].values,
    (data - data.T).values, # do not need to worry about the order of dimensions
    (data[:-1] - data[:1]).values, # align based on index labels
    sep='\n\n'
)

print('------------------------------------------------------')
print('GROUP BY..............................................')

labels = xr.DataArray(["E", "F", "E"], [data.coords["y"]], name="labels")
print(
    labels.values,
    data.values,
    data.groupby(labels).groups,
    data.groupby(labels).mean("x").values,    
    data.groupby(labels).mean("y").values,   
    data.groupby(labels).map(lambda x: x - x.min()).values,
    sep='\n\n'
)

print('------------------------------------------------------')
print('PLOTTING..............................................')
print(
    data.values,
    data[:-1].values,
    sep='\n\n'
)

plt.figure(0)
data.plot()
plt.figure(1)
data[:-1].plot()


print('------------------------------------------------------')
print('PANDAS................................................')
series = data.to_series()

df_firsttransformation = data.to_dataframe(name='Testing')
df_final = data.to_dataframe(name='Testing').unstack()
reversing_unstack = df_final.stack()

print(
    data.values,
    
    data.to_pandas(),
    # df_firsttransformation,
    data.to_dataframe(name='Testing').unstack(),
    # reversing_unstack,
    
    series,
    series.to_xarray(),
    
    sep='\n\n'
)
print('------------------------------------------------------')
print('DATASETS..............................................')

ds = xr.Dataset(dict(foo=data, bar=("x", [1, 2]), baz=np.pi))
print(
    data,
    ds,
    ds["foo"],
    ds["foo"].values,
    ds.foo,
    ds.foo.values,
    ds.bar,
    ds.bar.values,
    ds.bar.sel(x=10).values,
    sep='\n\n'
)

print('------------------------------------------------------')
print('WRITING NETCDF FILES..................................')

ds.to_netcdf("example.nc")
reopened = xr.open_dataset("example.nc")
print(
    reopened,
    reopened.foo.values,
    reopened.bar.values,
    reopened.baz.values,
    sep='\n\n'
)

print('------------------------------------------------------')
plt.show()
