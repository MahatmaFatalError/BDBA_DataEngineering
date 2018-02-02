from bokeh.io import output_file, output_notebook, show
from bokeh.plotting import figure
from bokeh.models import (
    GMapPlot, GMapOptions, ColumnDataSource, Circle, Range1d, PanTool, WheelZoomTool, BoxSelectTool
)


class BokehPlotter():

    def plot_geo(self, lat_list, lon_list, notebook=False):
        map_options = GMapOptions(lat=40.711724, lng=-74.011300, map_type="roadmap", zoom=11)

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

    def plot_bar(self, x_values, y_values, notebook=False):
        source = ColumnDataSource(data=dict(x_values=x_values, y_values=y_values))

        y_range_low = 0
        y_range_high = max(y_values) * 1.1
        y_range = (y_range_low, y_range_high)

        plot = figure(x_range=x_values, y_range=y_range, plot_height=1000, title="Title")

        plot.vbar(x='x_values', width=0.9, top='y_values', source=source)

        plot.xgrid.grid_line_color = None
        plot.xaxis.major_label_orientation = 1.2
        plot.x_range.range_padding = 0.1

        if notebook:
            output_notebook()
        else:
            output_file("bar_plot.html")
        show(plot)

    def plot_time(self, x_values, y_values, notebook=False):
        # create a new plot with a datetime axis type
        plot = figure(plot_width=800, plot_height=250, x_axis_type="datetime")

        plot.line(x_values, y_values, color='navy', alpha=0.5)

        if notebook:
            output_notebook()
        else:
            output_file("time_plot.html")
        show(plot)
