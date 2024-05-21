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
return: 
{
    "station_count": "15"
}

#### BOM-Station
GET: get_bom_list/?start=2021.01?end=2022.12

return:
[{
    "site": "41497",
    "Lat": "-27.1494",
    "Lon": "151.2894",
}, {...}, {...}, ...]

GET: get_bom_name/?site_id=41497
return:
{
    "name": "AAC DALBY CAMPUS", 
    "region name": ""
}
