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
			parameter_dict = self.read_widgets_lsdtt_basic_metrics(self.tab_nest)
			
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
	
		self.pp_widget = self.make_vertical_widgets(widget_dict = self.preprocessing)
		self.print_widget = self.make_vertical_widgets(widget_dict = self.basic_raster_printing)

		basic_accordion = widgets.Accordion(children=[self.pp_widget, self.print_widget])
		basic_accordion.set_title(0, 'Preprocessing')
		basic_accordion.set_title(1, 'Basic raster printing')


		tab_nest = widgets.Tab()
		tab_nest.children = [basic_accordion, basic_accordion]
		tab_nest.set_title(0, 'Prep and basic print')
		tab_nest.set_title(1, 'Slope, etc')
		#tab_nest.set_title(2, 'Channels and basins')
		#tab_nest.set_title(3, 'Chi ananlysis')

		return tab_nest
	
	def read_widgets_lsdtt_basic_metrics(self,tab_nest):
		'''
		This reads the values from the widget into a dictionary. It is wrapped by the runction read_widgets

		Returns:  A dictionary with parameter values

		Author: SMM

		Date: 13/07/2020
		'''		
		
		value_dict = {}
		
		for key,widge in self.preprocessing.items():
			# We need some logic here because the value dict needs to be in strings
			if isinstance(widge.value,bool):
				if widge.value:
					this_value = "true"
				else:
					this_value = "false"
			else:
				this_value = str(widge.value)

			value_dict.update({key: this_value})
			
		for key,widge in self.basic_raster_printing.items():
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
		
		this_dict = {}
		
		minimum_elevation = widgets.BoundedFloatText(
					value=0,
					min=-10000.0,
					max=10000.0,
					step=0.1,
					description='minimum_elevation:',
					disabled=False)
		this_dict.update({"minimum_elevation": minimum_elevation})
		
		maximum_elevation = widgets.BoundedFloatText(
					value=30000,
					min=-10000.0,
					max=30000.0,
					step=0.1,
					description='maximum_elevation:',
					disabled=False)
		this_dict.update({"maximum_elevation": maximum_elevation})
		
		min_slope_for_fill = widgets.FloatLogSlider(
					value=0.0001,
					base=10,
					min=-5, # max exponent of base
					max=-1, # min exponent of base
					step=0.2, # exponent step
					description='min_slope_for_fill:')
		this_dict.update({"min_slope_for_fill": min_slope_for_fill})
		
		raster_is_filled = widgets.Checkbox(
					value=False,
					description='raster_is_filled:',
					disabled=False,
					indent=False)
		this_dict.update({"raster_is_filled": raster_is_filled})	  
		
		remove_seas = widgets.Checkbox(
					value=True,
					description='remove_seas:',
					disabled=False,
					indent=False)
		this_dict.update({"remove_seas": remove_seas}) 
		
		carve_before_fill = widgets.Checkbox(
					value=False,
					description='carve_before_fill:',
					disabled=False,
					indent=False)
		this_dict.update({"carve_before_fill": carve_before_fill})  
		
		only_check_parameters = widgets.Checkbox(
					value=False,
					description='only_check_parameters:',
					disabled=False,
					indent=False)
		this_dict.update({"only_check_parameters": only_check_parameters})  
		
		print("The dictionary contains")
		return this_dict
   
	def make_basic_raster_printing(self):
		'''
		This creates all the widgets for basic raster printing
		
		Author: SMM
		
		Date: 13/07/2020
		'''	   
		
		this_dict = {}
		write_hillshade = widgets.Checkbox(
					value=False,
					description='write_hillshade:',
					disabled=False,
					indent=False)
		this_dict.update({"write_hillshade": write_hillshade})	  
		
		print_raster_without_seas= widgets.Checkbox(
					value=False,
					description='print_raster_without_seas:',
					disabled=False,
					indent=False)
		this_dict.update({"print_raster_without_seas": print_raster_without_seas})  
		
		print_distance_from_outlet = widgets.Checkbox(
					value=False,
					description='print_distance_from_outlet:',
					disabled=False,
					indent=False)
		this_dict.update({"print_distance_from_outlet": print_distance_from_outlet})
		
		print_fill_raster = widgets.Checkbox(
					value=False,
					description='print_fill_raster:',
					disabled=False,
					indent=False)
		this_dict.update({"print_fill_raster": print_fill_raster})
		
		return this_dict

	