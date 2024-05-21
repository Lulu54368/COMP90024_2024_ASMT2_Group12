# Team 12
# Meilun Yao   1076213
# Yingyi Luan 1179002
# Yuntao Lu 1166487
# Jiayi Xu 1165986
# Zheyuan Wu 1166034
# 查看geopandas版本
import geopandas as gpd
gpd.__version__

from shapely.geometry import Point, Polygon
import folium


# Set filepath
fp = "data/SA2-Map/SA2_2021_AUST_SHP_GDA2020/SA2_2021_AUST_GDA2020.shp"


# Create an empty geopandas GeoDataFrame
# newdata = gpd.GeoDataFrame()
newdata = gpd.read_file(fp)


df = newdata.to_crs(epsg=4326)
df = df.dropna(axis=0, subset=['geometry'])

# # Let's see what we have at the moment
# print(df)

# -27.304074, 133.749853
m = folium.Map(location=[-27.304074, 133.749853], zoom_start=4, tiles='CartoDB positron')

for _, r in df.iterrows():
    #without simplifying the representation of each borough, the map might not be displayed
    #sim_geo = gpd.GeoSeries(r['geometry'])
    sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j, style_function=lambda x: {'fillColor': 'orange'})
    folium.Popup(r['SA2_NAME21']).add_to(geo_j)
    geo_j.add_to(m)
m








import pandas as pd
population = pd.read_csv("./ABS_-_Regional_Population__SA2__2001-2020.csv/abs_regional_population_sa2_2001_2020-4826266136351011880.csv")

population = population[[' sa2_maincode_2016', ' pop_density_2020_people_per_km2']]
population = population.rename({' sa2_maincode_2016': 'SA2_CODE21', ' pop_density_2020_people_per_km2': 'density'}, axis=1)

tempdf = df[['geometry', 'SA2_CODE21']]
tempdf.SA2_CODE21 = tempdf.SA2_CODE21.astype('int64')

result = pd.merge(tempdf, right=population, how='left', on=['SA2_CODE21'])
result.density.fillna(0, inplace=True)
# int type and float type can not show on folium
result.density = result.density.astype('object')


m = folium.Map(location=[-27.304074, 133.749853], zoom_start=4, tiles='CartoDB positron')

for _, r in result.iterrows():
    #without simplifying the representation of each borough, the map might not be displayed
    #sim_geo = gpd.GeoSeries(r['geometry'])
    sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j, style_function=lambda x: {'fillColor': 'orange'})
    folium.Popup(r['density']).add_to(geo_j)
    geo_j.add_to(m)
m


