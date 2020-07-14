## lsdtt_drivermaker.py
##=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
## This is a collection of widget definitions and a driver that
## lets users write lsdtopotools driver files using a series of ipython widgets
##=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
## SMM
## 13/07/2020
##=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#from __future__ import absolute_import, division, print_function, unicode_literals
from __future__ import absolute_import, division, print_function

from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets


class lsdttdm():
    """
    This is the drivermaker object. Uses an ipythong widgets interface

    Args:
        command_line_tool (str): The lsdtopotools command line tool that you will use

    Returns:
        Creates a drivermaker object

    Author: SMM

    Date: 13/07/2020
    """
    def __init__(self,command_line_tool = "lsdtt-basic-metrics"):

        self.command_line_tool = command_line_tool
        self.check_command_line_tools()

        # Registering the attributes
        if (command_line_tool == "lsdtt-basic-metrics"):
            print("I am creating a lsdtt-basic-metrics input menu")
            self.preprocessing = self.make_preprocessing()
            self.basic_raster_printing = self.make_basic_raster_printing()
            self.trimming_options = self.make_trimming_options()
            self.geojson = self.make_geojson()
            self.slope_calculations = self.make_slope_calculations()
            self.roughness_calculations = self.make_roughness_calculations()
            self.drainage_area_calculations = self.make_drainage_area()
            self.single_channel_calculations = self.make_single_channel()
            self.basic_channel_network_calculations = self.make_basic_channel_network()
            self.basin_extraction_calculations = self.make_basin_extraction()
            self.wiener_calculations = self.make_wiener()
            self.burner_calculations = self.make_raster_burning()
            self.JA_calculations = self.make_junction_angles()
            self.chi_calculations = self.make_simple_chi()

            self.tab_nest = self.make_widget_lsdtt_basic_metrics()

        else:
            print("I didn't understand the command line tool")

        print("======================================================================================")
        print("Okay, your input widget is initiated. Call grab_widget to start entering parameters.")
        print("When you have finished, run the read_widgets tool.")
        print("This will give you a dictionary that can be passed to an lsdtt_driver object .")
        print("======================================================================================")

    def make_widget(self):
        """
        This returns the nested tabs so that ipython can open the widget

        Returns:
            A widget object

        Author: SMM

        Date: 13/07/2020
        """
        #this_widget = self.tab_nest
        return self.tab_nest

    def read_widgets(self):
        """
        This reads the output of the widget and passes it into a parameter dictionary.
        The parameter dictionary can be passed to the lsdtt_driver that is in lsdviztools

        Returns:
            A dictionary with parameter values

        Author: SMM

        Date: 13/07/2020
        """
        parameter_dict = {}
        if (self.command_line_tool == "lsdtt-basic-metrics"):
            parameter_dict = self.read_widgets_lsdtt_basic_metrics()

        return parameter_dict



    def check_command_line_tools(self):
        """
        Makes sure the command line tool is valid

        Returns:
            A bool: true if it is valid, false if it has changed to the default ("lsdtt-basic-metrics")

        Author: SMM

        Date: 10/07/2020
        """

        valid_clt = ["lsdtt-basic-metrics","lsdtt-channel-extraction","lsdtt-chi-analysis"]

        if (self.command_line_tool not in valid_clt):
            print("Warning: incorrect command line tool. Defaulting to lsdtt-basic-metrics")
            self.command_line_tool = "lsdtt-basic-metrics"
        else:
            print("You have selected the command line tool: "+self.command_line_tool)





    def make_widget_lsdtt_basic_metrics(self):
        '''
        This there will be a nesting of tabs and accordions

        Returns:  A widget object. This is a wrapper that gets sent to

        Author: SMM

        Date: 13/07/2020
        '''

        widget_dicts = []

        self.pp_widget = self.make_vertical_widgets(widget_dict = self.preprocessing)
        self.print_widget = self.make_vertical_widgets(widget_dict = self.basic_raster_printing)
        self.trimming_widget = self.make_vertical_widgets(widget_dict = self.trimming_options)
        self.geojson_widget = self.make_vertical_widgets(widget_dict = self.geojson)
        self.burner_widget = self.make_vertical_widgets(widget_dict = self.burner_calculations)

        widget_dicts.append(self.preprocessing)
        widget_dicts.append(self.basic_raster_printing)
        widget_dicts.append(self.trimming_options)
        widget_dicts.append(self.geojson)
        widget_dicts.append(self.burner_calculations)


        basic_accordion = widgets.Accordion(children=[self.pp_widget, self.print_widget, self.trimming_widget,self.geojson_widget,self.burner_widget])
        basic_accordion.set_title(0, 'Preprocessing')
        basic_accordion.set_title(1, 'Basic raster printing')
        basic_accordion.set_title(2, 'Raster trimming')
        basic_accordion.set_title(3, 'Convert points to geojson')
        basic_accordion.set_title(4, 'Burning raster data to csv')

        self.slope_widget = self.make_vertical_widgets(widget_dict = self.slope_calculations)
        self.roughness_widget = self.make_vertical_widgets(widget_dict = self.roughness_calculations)
        self.da_widget = self.make_vertical_widgets(widget_dict = self.drainage_area_calculations)
        self.wiener_widget = self.make_vertical_widgets(widget_dict = self.wiener_calculations)

        widget_dicts.append(self.slope_calculations)
        widget_dicts.append(self.roughness_calculations)
        widget_dicts.append(self.drainage_area_calculations)
        widget_dicts.append(self.wiener_calculations)

        basic_accordion2 = widgets.Accordion(children=[self.slope_widget,self.roughness_widget,self.da_widget,self.wiener_widget])
        basic_accordion2.set_title(0, 'Slope calculations')
        basic_accordion2.set_title(1, 'Roughness calculations')
        basic_accordion2.set_title(2, 'Drainage area calculations')
        basic_accordion2.set_title(3, 'Wiener filter')



        self.single_channel_widget = self.make_vertical_widgets(widget_dict = self.single_channel_calculations)
        self.basic_channel_network_widget = self.make_vertical_widgets(widget_dict = self.basic_channel_network_calculations)
        self.basin_extraction_widget = self.make_vertical_widgets(widget_dict = self.basin_extraction_calculations)
        self.JA_widget = self.make_vertical_widgets(widget_dict = self.JA_calculations)

        widget_dicts.append(self.single_channel_calculations)
        widget_dicts.append(self.basic_channel_network_calculations)
        widget_dicts.append(self.basin_extraction_calculations)
        widget_dicts.append(self.JA_calculations)

        basic_accordion3 = widgets.Accordion(children=[self.single_channel_widget,self.basic_channel_network_widget,self.basin_extraction_widget,self.JA_widget])
        basic_accordion3.set_title(0, 'Extracting a single channel')
        basic_accordion3.set_title(1, 'Basic channel network')
        basic_accordion3.set_title(2, 'Basin extraction')
        basic_accordion3.set_title(3, 'Junction angles')

        self.chi_widget = self.make_vertical_widgets(widget_dict = self.chi_calculations)

        widget_dicts.append(self.chi_calculations)

        basic_accordion4 = widgets.Accordion(children=[self.chi_widget])
        basic_accordion4.set_title(0, 'Simple chi. (Use lsdtt-chi-analysis for more complex chi analysis)')



        tab_nest = widgets.Tab()
        tab_nest.children = [basic_accordion, basic_accordion2,basic_accordion3, basic_accordion4]
        tab_nest.set_title(0, 'Prep and basic print')
        tab_nest.set_title(1, 'Slope, drainage, etc')
        tab_nest.set_title(2, 'Channels and basins')
        tab_nest.set_title(3, 'Chi ananlysis')


        self.widget_list = widget_dicts
        return tab_nest

    def read_widgets_lsdtt_basic_metrics(self):
        '''
        This reads the values from the widget into a dictionary. It is wrapped by the runction read_widgets

        Returns:  A dictionary with parameter values

        Author: SMM

        Date: 13/07/2020
        '''

        value_dict = {}
        for wdict in self.widget_list:


            for key,widge in wdict.items():
                # We need some logic here because the value dict needs to be in strings
                if isinstance(widge.value,bool):
                    if widge.value:
                        this_value = "true"
                    else:
                        this_value = "false"
                else:
                    this_value = str(widge.value)

                value_dict.update({key: this_value})



        return value_dict


    def make_accordion_widgets(self, widget_dict = {}):
        '''
        This makes widgets in the accordion style

        Args:
            widge_dict (dictionary): the dictionary of widgets that gets turned into an accordion

        Returns: The accordion widget

        Author: SMM

        Date: 13/07/2020
        '''

        widget_list = []
        for key,widge in widget_dict.items():
            widget_list.append(widge)

        this_accordion = widgets.Accordion(children=widget_list)
        return this_accordion


    def make_vertical_widgets(self, widget_dict = {}):
        '''
        This makes widgets in the vertical style

        Args:
            widge_dict (dictionary): the dictionary of widgets that gets turned into a vertical widget

        Returns: The vertical widget widget

        Author: SMM

        Date: 13/07/2020
        '''

        widget_list = []
        for key,widge in widget_dict.items():
            widget_list.append(widge)

        this_box = widgets.VBox(widget_list)
        return this_box

    def make_preprocessing(self):
        '''
        This creates all the widgets for preprocessing

        Author: SMM

        Date: 13/07/2020
        '''
        wide_style = {'description_width': 'initial'}

        this_dict = {}

        minimum_elevation = widgets.BoundedFloatText(
                    value=0,
                    min=-10000.0,
                    max=10000.0,
                    step=0.1,
                    description='minimum_elevation:',
                    disabled=False,
                    style=wide_style)
        this_dict.update({"minimum_elevation": minimum_elevation})

        maximum_elevation = widgets.BoundedFloatText(
                    value=30000,
                    min=-10000.0,
                    max=30000.0,
                    step=0.1,
                    description='maximum_elevation:',
                    disabled=False,
                    style=wide_style)
        this_dict.update({"maximum_elevation": maximum_elevation})

        min_slope_for_fill = widgets.FloatLogSlider(
                    value=0.0001,
                    base=10,
                    min=-5, # max exponent of base
                    max=-1, # min exponent of base
                    step=0.2, # exponent step
                    description='min_slope_for_fill:',
                    style=wide_style)
        this_dict.update({"min_slope_for_fill": min_slope_for_fill})

        raster_is_filled = widgets.Checkbox(
                    value=False,
                    description='raster_is_filled',
                    disabled=False,
                    indent=False)
        this_dict.update({"raster_is_filled": raster_is_filled})

        remove_seas = widgets.Checkbox(
                    value=True,
                    description='remove_seas',
                    disabled=False,
                    indent=False)
        this_dict.update({"remove_seas": remove_seas})

        carve_before_fill = widgets.Checkbox(
                    value=False,
                    description='carve_before_fill',
                    disabled=False,
                    indent=False)
        this_dict.update({"carve_before_fill": carve_before_fill})

        only_check_parameters = widgets.Checkbox(
                    value=False,
                    description='only_check_parameters',
                    disabled=False,
                    indent=False)
        this_dict.update({"only_check_parameters": only_check_parameters})

        return this_dict


    def make_raster_burning(self):
        '''
        This creates all the widgets for raster burning

        Author: SMM

        Date: 13/07/2020
        '''

        wide_style = {'description_width': 'initial'}
        this_dict = {}
        burn_raster_to_csv = widgets.Checkbox(
                    value=False,
                    description='burn_raster_to_csv',
                    disabled=False,
                    indent=False)
        this_dict.update({"burn_raster_to_csv": burn_raster_to_csv})

        burn_raster_prefix= widgets.Text(
                    value="NULL",
                    description='burn_raster_prefix',
                    disabled=False,
                    indent=False,
                    style=wide_style)
        this_dict.update({"burn_raster_prefix": burn_raster_prefix})

        burn_data_csv_column_header= widgets.Text(
                    value="burned_data",
                    description='burn_data_csv_column_header',
                    disabled=False,
                    indent=False,
                    style=wide_style)
        this_dict.update({"burn_data_csv_column_header": burn_data_csv_column_header})

        csv_to_burn_name= widgets.Text(
                    value="NULL",
                    description='csv_to_burn_name',
                    disabled=False,
                    indent=False,
                    style=wide_style)
        this_dict.update({"csv_to_burn_name": csv_to_burn_name})

        return this_dict


    def make_geojson(self):
        '''
        This is a single widget for converting csv to geojson

        Author: SMM

        Date: 14/07/2020
        '''
        wide_style = {'description_width': 'initial'}

        this_dict = {}

        convert_csv_to_geojson = widgets.Checkbox(
                    value=False,
                    description='convert_csv_to_geojson',
                    disabled=False,
                    indent=False)
        this_dict.update({"convert_csv_to_geojson": convert_csv_to_geojson})

        return this_dict

    def make_wiener(self):
        '''
        This is a single widget for converting csv to geojson

        Author: SMM

        Date: 14/07/2020
        '''
        wide_style = {'description_width': 'initial'}

        this_dict = {}

        print_wiener_filtered_raster = widgets.Checkbox(
                    value=False,
                    description='print_wiener_filtered_raster',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_wiener_filtered_raster": print_wiener_filtered_raster})

        return this_dict

    def make_basic_raster_printing(self):
        '''
        This creates all the widgets for basic raster printing

        Author: SMM

        Date: 13/07/2020
        '''

        wide_style = {'description_width': 'initial'}
        this_dict = {}
        write_hillshade = widgets.Checkbox(
                    value=False,
                    description='write_hillshade',
                    disabled=False,
                    indent=False)
        this_dict.update({"write_hillshade": write_hillshade})

        print_raster_without_seas= widgets.Checkbox(
                    value=False,
                    description='print_raster_without_seas',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_raster_without_seas": print_raster_without_seas})

        print_distance_from_outlet = widgets.Checkbox(
                    value=False,
                    description='print_distance_from_outlet',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_distance_from_outlet": print_distance_from_outlet})

        print_fill_raster = widgets.Checkbox(
                    value=False,
                    description='print_fill_raster',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_fill_raster": print_fill_raster})

        print_relief_raster = widgets.Checkbox(
                    value=False,
                    description='print_relief_raster',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_relief_raster": print_relief_raster})

        relief_window = widgets.BoundedFloatText(
                    value=200,
                    min=1,
                    max=20000,
                    step=1,
                    description='relief_window:',
                    disabled=False,
                    style=wide_style)
        this_dict.update({"relief_window": relief_window})

        return this_dict

    def make_trimming_options(self):
        '''
        This creates all the widgets for raster trimming

        Author: SMM

        Date: 14/07/2020
        '''

        wide_style = {'description_width': 'initial'}
        this_dict = {}
        remove_nodes_influenced_by_edge = widgets.Checkbox(
                    value=False,
                    description='remove_nodes_influenced_by_edge',
                    disabled=False,
                    indent=False)
        this_dict.update({"remove_nodes_influenced_by_edge": remove_nodes_influenced_by_edge})

        isolate_pixels_draining_to_fixed_channel= widgets.Checkbox(
                    value=False,
                    description='isolate_pixels_draining_to_fixed_channel',
                    disabled=False,
                    indent=False)
        this_dict.update({"isolate_pixels_draining_to_fixed_channel": isolate_pixels_draining_to_fixed_channel})

        fixed_channel_csv_name= widgets.Text(
                    value="single_channel_nodes",
                    description='fixed_channel_csv_name:',
                    disabled=False,
                    indent=False,
                    style=wide_style)
        this_dict.update({"fixed_channel_csv_name": fixed_channel_csv_name})

        print_trimmed_raster = widgets.Checkbox(
                    value=False,
                    description='print_trimmed_raster',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_trimmed_raster": print_trimmed_raster})

        trimming_buffer_pixels = widgets.BoundedIntText(
                    value=0,
                    min=-0,
                    max=50,
                    step=1,
                    description='trimming_buffer_pixels:',
                    disabled=False,
                    style=wide_style)
        this_dict.update({"trimming_buffer_pixels": trimming_buffer_pixels})

        return this_dict


    def make_slope_calculations(self):
        '''
        This creates all the widgets for calculating slope, curvature, etc

        Author: SMM

        Date: 14/07/2020
        '''

        wide_style = {'description_width': 'initial'}
        this_dict = {}

        calculate_window_size = widgets.Checkbox(
                    value=False,
                    description='calculate_window_size',
                    disabled=False,
                    indent=False)
        this_dict.update({"calculate_window_size": calculate_window_size})

        surface_fitting_radius = widgets.BoundedFloatText(
                    value=30,
                    min=1,
                    max=500,
                    step=1,
                    description='surface_fitting_radius:',
                    disabled=False,
                    style=wide_style)
        this_dict.update({"surface_fitting_radius": surface_fitting_radius})

        print_slope = widgets.Checkbox(
                    value=False,
                    description='print_slope',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_slope": print_slope})

        print_aspect= widgets.Checkbox(
                    value=False,
                    description='print_aspect',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_aspect": print_aspect})

        print_curvature = widgets.Checkbox(
                    value=False,
                    description='print_curvature',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_curvature": print_curvature})

        print_planform_curvature = widgets.Checkbox(
                    value=False,
                    description='print_planform_curvature',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_planform_curvature": print_planform_curvature})

        print_profile_curvature= widgets.Checkbox(
                    value=False,
                    description='print_profile_curvature',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_profile_curvature": print_profile_curvature})

        print_tangential_curvature = widgets.Checkbox(
                    value=False,
                    description='print_tangential_curvature',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_tangential_curvature": print_tangential_curvature})

        print_point_classification = widgets.Checkbox(
                    value=False,
                    description='print_point_classification',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_point_classification": print_point_classification})

        print_directional_gradients= widgets.Checkbox(
                    value=False,
                    description='print_directional_gradients',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_directional_gradients": print_directional_gradients})

        calculate_basin_statistics = widgets.Checkbox(
                    value=False,
                    description='calculate_basin_statistics',
                    disabled=False,
                    indent=False)
        this_dict.update({"calculate_basin_statistics": calculate_basin_statistics})

        return this_dict

    def make_roughness_calculations(self):
        '''
        This creates all the widgets for calculating slope, curvature, etc

        Author: SMM

        Date: 14/07/2020
        '''

        wide_style = {'description_width': 'initial'}
        this_dict = {}

        print_REI_raster = widgets.Checkbox(
                    value=False,
                    description='print_REI_raster',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_REI_raster": print_REI_raster})

        REI_window_radius = widgets.BoundedFloatText(
                    value=10,
                    min=1,
                    max=500,
                    step=1,
                    description='REI_window_radius',
                    disabled=False,
                    style=wide_style)
        this_dict.update({"REI_window_radius": REI_window_radius})

        REI_critical_slope = widgets.BoundedFloatText(
                    value=1.0,
                    min=0.4,
                    max=2.0,
                    step=0.05,
                    description='REI_critical_slope:',
                    disabled=False,
                    style=wide_style)
        this_dict.update({"REI_critical_slope": REI_critical_slope})

        print_roughness_rasters= widgets.Checkbox(
                    value=False,
                    description='print_roughness_rasters',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_roughness_rasters": print_roughness_rasters})

        roughness_radius = widgets.BoundedFloatText(
                    value=3,
                    min=1,
                    max=500,
                    step=0.2,
                    description='roughness_radius',
                    disabled=False,
                    style=wide_style)
        this_dict.update({"roughness_radius": roughness_radius})

        return this_dict

    def make_drainage_area(self):
        '''
        This creates all the widgets for calculating slope, curvature, etc

        Author: SMM

        Date: 14/07/2020
        '''

        wide_style = {'description_width': 'initial'}
        this_dict = {}

        print_dinf_drainage_area_raster = widgets.Checkbox(
                    value=False,
                    description='print_dinf_drainage_area_raster',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_dinf_drainage_area_raster": print_dinf_drainage_area_raster})

        print_d8_drainage_area_raster = widgets.Checkbox(
                    value=False,
                    description='print_d8_drainage_area_raster',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_d8_drainage_area_raster": print_d8_drainage_area_raster})

        print_QuinnMD_drainage_area_raster = widgets.Checkbox(
                    value=False,
                    description='print_QuinnMD_drainage_area_raster',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_QuinnMD_drainage_area_raster": print_QuinnMD_drainage_area_raster})

        print_FreemanMD_drainage_area_raster = widgets.Checkbox(
                    value=False,
                    description='print_FreemanMD_drainage_area_raster',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_FreemanMD_drainage_area_raster": print_FreemanMD_drainage_area_raster})

        print_MD_drainage_area_raster = widgets.Checkbox(
                    value=False,
                    description='print_MD_drainage_area_raster',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_MD_drainage_area_raster": print_MD_drainage_area_raster})

        return this_dict

    def make_single_channel(self):
        '''
        This creates all the widgets for calculating slope, curvature, etc

        Author: SMM

        Date: 14/07/2020
        '''

        wide_style = {'description_width': 'initial'}
        this_dict = {}

        extract_single_channel = widgets.Checkbox(
                    value=False,
                    description='extract_single_channel',
                    disabled=False,
                    indent=False)
        this_dict.update({"extract_single_channel": extract_single_channel})

        use_dinf_for_single_channel = widgets.Checkbox(
                    value=False,
                    description='use_dinf_for_single_channel',
                    disabled=False,
                    indent=False)
        this_dict.update({"use_dinf_for_single_channel": use_dinf_for_single_channel})

        channel_source_fname= widgets.Text(
                    value="single_channel_source",
                    description='channel_source_fname',
                    disabled=False,
                    indent=False,
                    style=wide_style)
        this_dict.update({"channel_source_fname": channel_source_fname})

        return this_dict

    def make_basic_channel_network(self):
        '''
        This creates all the widgets for calculating slope, curvature, etc

        Author: SMM

        Date: 14/07/2020
        '''

        wide_style = {'description_width': 'initial'}
        this_dict = {}

        threshold_contributing_pixels = widgets.BoundedIntText(
                    value=1000,
                    min=1,
                    max=100000000,
                    step=1,
                    description='threshold_contributing_pixels:',
                    disabled=False,
                    style=wide_style)
        this_dict.update({"threshold_contributing_pixels": threshold_contributing_pixels})

        print_stream_order_raster = widgets.Checkbox(
                    value=False,
                    description='print_stream_order_raster',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_stream_order_raster": print_stream_order_raster})

        print_channels_to_csv = widgets.Checkbox(
                    value=False,
                    description='print_channels_to_csv',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_channels_to_csv": print_channels_to_csv})

        print_junction_index_raster = widgets.Checkbox(
                    value=False,
                    description='print_junction_index_raster',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_junction_index_raster": print_junction_index_raster})

        print_junctions_to_csv = widgets.Checkbox(
                    value=False,
                    description='print_junctions_to_csv',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_junctions_to_csv": print_junctions_to_csv})

        return this_dict


    def make_junction_angles(self):
        '''
        This creates all the widgets for calculating slope, curvature, etc

        Author: SMM

        Date: 14/07/2020
        '''

        wide_style = {'description_width': 'initial'}
        this_dict = {}

        SA_vertical_interval = widgets.BoundedFloatText(
                    value=10,
                    min=1,
                    max=200,
                    step=0.1,
                    description='SA_vertical_interval',
                    disabled=False,
                    style=wide_style)
        this_dict.update({"SA_vertical_interval": SA_vertical_interval})

        print_junction_angles_to_csv = widgets.Checkbox(
                    value=False,
                    description='print_junction_angles_to_csv',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_junction_angles_to_csv": print_junction_angles_to_csv})

        return this_dict


    def make_basin_extraction(self):
        '''
        This creates all the widgets for calculating slope, curvature, etc

        Author: SMM

        Date: 14/07/2020
        '''

        wide_style = {'description_width': 'initial'}
        this_dict = {}

        find_basins = widgets.Checkbox(
                    value=False,
                    description='find_basins',
                    disabled=False,
                    indent=False)
        this_dict.update({"find_basins": find_basins})

        minimum_basin_size_pixels = widgets.BoundedIntText(
                    value=50000,
                    min=1,
                    max=100000000000,
                    step=1,
                    description='minimum_basin_size_pixels',
                    disabled=False,
                    style=wide_style)
        this_dict.update({"minimum_basin_size_pixels": minimum_basin_size_pixels})

        maximum_basin_size_pixels = widgets.BoundedIntText(
                    value=1000000,
                    min=1,
                    max=100000000000,
                    step=1,
                    description='maximum_basin_size_pixels',
                    disabled=False,
                    style=wide_style)
        this_dict.update({"maximum_basin_size_pixels": maximum_basin_size_pixels})

        only_take_largest_basin = widgets.Checkbox(
                    value=False,
                    description='only_take_largest_basin',
                    disabled=False,
                    indent=False)
        this_dict.update({"only_take_largest_basin": only_take_largest_basin})

        BaselevelJunctions_file= widgets.Text(
                    value="NULL",
                    description='BaselevelJunctions_file',
                    disabled=False,
                    indent=False,
                    style=wide_style)
        this_dict.update({"BaselevelJunctions_file": BaselevelJunctions_file})

        get_basins_from_outlets = widgets.Checkbox(
                    value=False,
                    description='get_basins_from_outlets',
                    disabled=False,
                    indent=False)
        this_dict.update({"get_basins_from_outlets": get_basins_from_outlets})

        search_radius_nodes = widgets.BoundedIntText(
                    value=8,
                    min=1,
                    max=200,
                    step=1,
                    description='search_radius_nodes',
                    disabled=False,
                    style=wide_style)
        this_dict.update({"search_radius_nodes": search_radius_nodes})

        basin_outlet_csv= widgets.Text(
                    value="NULL",
                    description='basin_outlet_csv',
                    disabled=False,
                    indent=False,
                    style=wide_style)
        this_dict.update({"basin_outlet_csv": basin_outlet_csv})

        extend_channel_to_node_before_receiver_junction = widgets.Checkbox(
                    value=True,
                    description='extend_channel_to_node_before_receiver_junction',
                    disabled=False,
                    indent=False)
        this_dict.update({"extend_channel_to_node_before_receiver_junction": extend_channel_to_node_before_receiver_junction})

        print_basin_raster = widgets.Checkbox(
                    value=False,
                    description='print_basin_raster',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_basin_raster": print_basin_raster})

        return this_dict


    def make_simple_chi(self):
        '''
        This creates all the widgets for calculating slope, curvature, etc

        Author: SMM

        Date: 14/07/2020
        '''

        wide_style = {'description_width': 'initial'}
        this_dict = {}

        A_0 = widgets.BoundedFloatText(
                    value=1,
                    min=1,
                    max=1000000,
                    step=0.1,
                    description='A_0',
                    disabled=False,
                    style=wide_style)
        this_dict.update({"A_0": A_0})

        m_over_n = widgets.BoundedFloatText(
                    value=0.5,
                    min=0.025,
                    max=5,
                    step=0.025,
                    description='m_over_n (concavity)',
                    disabled=False,
                    style=wide_style)
        this_dict.update({"m_over_n": m_over_n})

        print_chi_data_maps = widgets.Checkbox(
                    value=False,
                    description='print_chi_data_maps',
                    disabled=False,
                    indent=False)
        this_dict.update({"print_chi_data_maps": print_chi_data_maps})

        return this_dict


