# Data
SUDO-ABS-PopulationDensity
loc: data/SUDO-ABS-PopulationDensity/abs_regional_population_sa2_2001_2020-4826266136351011880.json
format: 
`sa2_name_2016: string`
`area_km2: double/float`
`gccsa_name_2016: string`
`state_code_2016: int`
`state_name_2016: string`
`sa2_maincode_2016: int`
`sa4_code_2016: int`
`pop_density_2020_people_per_km2: double`
`sa4_name_2016: string`
`gccsa_code_2016: string`
`sa3_name_2016: string`
`sa3_code_2016: int`

SA2-Map
地图数据应该不用存

BOM-Station
loc: data/BOM-Station/BOM-Station.json
format: 
`Site: int(id)`
`Name: string`
`Lat: float/double`
`Lon: float/double`
`Start: MM YYYY`
`End: MM YYYY`
`Years: float/double`
`%: int`
`AWS: N, Y or None`




# API 
#### SUDO-ABS-PopulationDensity

GET: get_population_list
`只要维州的数据？？？`
return: 
```
[{
    "sa2_name_2016": "Braidwood", 
    "area_km2": "3418.352539",
    "sa2_maincode_2016": "101021007",
    "pop_density_2020_people_per_km2": "1.255300"
},{
    "sa2_name_2016": "Karabar", 
    "area_km2": "3418.352539",
    "sa2_maincode_2016": "101021008",
    "pop_density_2020_people_per_km2": "1198.854248"
}, 
{...},{...},...]
```


#### SA2-Map
GET: get_map_region_info/?region_id=101021007?start=2021.01?end=2022.12
`这里的region_id为sa2_maincode_2016, 通过id找到当前区域有多少个在运行的site。（这个MAP数据我不知道能不能存到后端，但是处理API需要这个MAP信息！！！）`
return: 
{
    "station_count": "15"
}

#### BOM-Station
GET: get_bom_list/?start=2021.01?end=2022.12
`仅选择维州的,选择start和end在运行的site`
return:
[{
    "site": "41497",
    "Lat": "-27.1494",
    "Lon": "151.2894",
}, {...}, {...}, ...]

GET: get_bom_name/?site_id=41497
`用经纬度坐标对应到Map上面的某个区域，所属区域的名字叫做region name`
return:
{
    "name": "AAC DALBY CAMPUS", 
    "region name": ""
}