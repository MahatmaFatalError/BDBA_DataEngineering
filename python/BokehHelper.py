from bokeh.io import output_file, output_notebook, show
from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, Range1d, PanTool, WheelZoomTool, BoxSelectTool
)


class BokehPlotter():

    def plotgeo(self, lat_list, lon_list, notebook=False):
        map_options = GMapOptions( lat=40.711724, lng= -74.011300, map_type="roadmap", zoom=11)

        plot = GMapPlot(x_range=Range1d(), y_range=Range1d(), map_options=map_options)
        plot.title.text = "Austin"

        # For GMaps to function, Google requires you obtain and enable an API key:
        #
        #     https://developers.google.com/maps/documentation/javascript/get-api-key
        #
        # Replace the value below with your personal API key:
        plot.api_key = "AIzaSyAsaj5xLV6L7TCawDUG411zksXuetjrvVg"

        source = ColumnDataSource(
           data=dict(
               lat=lat_list,
               lon=lon_list,
           )
        )

        circle = Circle(x="lon", y="lat", size=15, fill_color="blue", fill_alpha=0.8, line_color=None)
        plot.add_glyph(source, circle)

        plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())

        if notebook:
            output_notebook()
        else:
            output_file("gmap_plot.html")
        show(plot)