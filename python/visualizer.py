from python.BokehHelper import BokehPlotter
from python.DBHelper import DBHelper

plotter = BokehPlotter()
db = DBHelper("bdba")
count = 0
lon_list = []
lat_list = []

results = db.select_all_entries_where(table_name="service_request", key="borough", value="BROOKLYN")

for result in results:
    lat_list.append(result["latitude"])
    lon_list.append(result["longitude"])
    count += 1
print(count)

plotter.plotgeo(lat_list=lat_list, lon_list=lon_list, notebook=False)