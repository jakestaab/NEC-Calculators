
#This library contains all non-standard library data imported into the
#following calculators: conduit_fill, wire_derate, voltage_drop, inverter_select.

#For each calculator, there is a dedicated Class with methods, lists,
#and dictionaries specific to that program, located in this library.
#For example, conduit_fill.py imports the class NECTablesConduitFill.




"""CONDUIT FILL"""
class NECTablesConduitFill():

	thhn_awg_to_area = {
	"12": .0133,
	"10": .0211,
	"8": .0366,
	"6": .0507,
	"4": .0824,
	"3": .0973,
	"2": .1158,
	"1": .1562,
	"1/0": .1855,
	"2/0": .2223,
	"3/0": .2679,
	"4/0": .3237,
	"250 kcmil": .3970,
	"300 kcmil": .4608,
	"350 kcmil": .5242,
	"400 kcmil": .5863,
	"500 kcmil": .7073,
	"600 kcmil": .8676,
	"700 kcmil": .9887,
	"750 kcmil": 1.0496,
	"800 kcmil": 1.1085,
	"900 kcmil": 1.2311,
	"1000 kcmil": 1.3478
	}
	
	pv_awg_to_area = {
	"10": .0531,
	"8": .0769,
	"6": .0957,
	"4": .1232,
	"3": .1412,
	"2": .1633,
	"1": .2215,
	"1/0": .2552,
	"2/0": .2961,
	"3/0": .3463,
	"4/0": .4072,
	"250 kcmil": .4803,
	"300 kcmil": .5463,
	"350 kcmil": .6096,
	"400 kcmil": .6720,
	"500 kcmil": .7949
	}

	rhw_awg_to_area = {
	"10": .0437,
	"8": .0835,
	"6": .1041,
	"4": .1333,
	"3": .1521,
	"2": .1750,
	"1": .2660,
	"1/0": .3039,
	"2/0": .3505,
	"3/0": .4072,
	"4/0": 4757,
	"250 kcmil": .6291,
	"300 kcmil": .7088,
	"350 kcmil": .7870,
	"400 kcmil": .8626,
	"500 kcmil": 1.0082,
	"600 kcmil": 1.2135,
	"700 kcmil": 1.3561,
	"750 kcmil": 1.4272,
	"800 kcmil": 1.4957,
	"900 kcmil": 1.6377,
	"1000 kcmil": 1.7719
	}

	emt_dict = {
	.304: '1/2"',
	.533: '3/4"',
	.864: '1"',
	1.496: '1-1/4"',
	2.036: '1-1/2"',
	3.356: '2"',
	5.858: '2-1/2"',
	8.846: '3"',
	11.545: '3-1/2"',
	14.753: '4"'
	}

	emt_lst = [.0, .304, .533, .864, 1.496, 2.036, 3.356,
	5.858, 8.846, 11.545, 14.753]
	
	pvc_dict = {
	.285: '1/2',
	.508: '3/4"',
	.832: '1"',
	1.453: '1-1/4"',
	1.986: '1-1/2"',
	3.291: '2"',
	4.695: '2-1/2"',
	7.268: '3"',
	9.737: '3-1/2"',
	12.554: '4"',
	19.761: '5"',
	28.567: '6"'
	}
	
	pvc_lst = [.0, .285, .508, .832, 1.453, 1.986, 3.291, 4.695,
	7.268, 9.737, 12.554, 19.761, 28.567]
"""CONDUIT FILL"""











"""WIRE DERATE"""
class NECTablesWireDerate():
	
	#---------------#
	
	fill_dict = {
	4: 1,
	7: .8,
	10: .7,
	21: .5,
	31: .45,
	41: .4
	}
	
	fill_lst = [4, 7, 10, 21, 31, 41]

	#---------------#

	temp_dict_90 = {
	78: 1.04,
	87: 1,
	96: .96,
	105: .91,
	114: .87,
	123: .82
	}
	
	temp_dict_75 = {
	78: 1.05,
	87: 1,
	96: .94,
	105: .88,
	114: .82,
	123: .75
	}

	temp_lst = [78, 87, 96, 105, 114, 123]
	
	#---------------#

	#--90--#
	cu_ampacity_90 = [25,30,40,55,75,95,115,130,145,170,195,225,260,290,320,350,380,430,475,520,535,555,585,615]

	cu_ampacity_to_awg_90 = {
	25: 14,
	30: 12,
	40: 10,
	55: 8,
	75: 6,
	95: 4,
	115: 3,
	130: 2,
	145: 1,
	170: '1/0',
	195: '2/0',
	225: '3/0',
	260: '4/0',
	290: '250 kcmil',
	320: '300 kcmil',
	350: '350 kcmil',
	380: '400 kcmil',
	430: '500 kcmil',
	475: '600 kcmil',
	520: '700 kcmil',
	535: '750 kcmil',
	555: '800 kcmil',
	585: '900 kcmil',
	615: '1000 kcmil'
	}
	
	al_ampacity_90 = [25,35,45,55,75,85,100,115,135,150,175,205,230,260,280,305,350,385,425,435,445,480,500,545,585]
	
	al_ampacity_to_awg_90 = {
	25: 12,
	35: 10,
	45: 8,
	55: 6,
	75: 4,
	85: 3,
	100: 2,
	115: 1,
	135: '1/0',
	150: '2/0',
	175: '3/0',
	205: '4/0',
	230: '250 kcmil',
	260: '300 kcmil',
	280: '350 kcmil',
	305: '400 kcmil',
	350: '500 kcmil',
	385: '600 kcmil',
	425: '700 kcmil',
	435: '750 kcmil',
	445: '800 kcmil',
	480: '900 kcmil',
	500: '1000 kcmil',
	545: '1250 kcmil',
	585: '1500 kcmil'
	}

	#--75--#
	cu_ampacity_75 = [20,25,35,50,65,85,100,115,130,150,175,200,230,255,285,310,335,380,420,460,475,490,520,545,590,625]
	
	cu_ampacity_to_awg_75 = {
	20: 14,
	25: 12,
	35: 10,
	50: 8,
	65: 6,
	85: 4,
	100: 3,
	115: 2,
	130: 1,
	150: '1/0',
	175: '2/0',
	200: '3/0',
	230: '4/0',
	255: '250 kcmil',
	285: '300 kcmil',
	310: '350 kcmil',
	335: '400 kcmil',
	380: '500 kcmil',
	420: '600 kcmil',
	460: '700 kcmil',
	475: '750 kcmil',
	490: '800 kcmil',
	520: '900 kcmil',
	545: '1000 kcmil',
	590: '1250 kcmil',
	625: '1500 kcmil'
	}
	
	al_ampacity_75 = [20,30,40,50,65,75,90,100,120,135,155,180,205,230,250,270,310,340,375,385,395,425,445,485,520,545,560]
	
	al_ampacity_to_awg_75 = {
	20: 12,
	30: 10,
	40: 8,
	50: 6,
	65: 4,
	75: 3,
	90: 2,
	100: 1,
	120: '1/0',
	135: '2/0',
	155: '3/0',
	180: '4/0',
	205: '250 kcmil',
	230: '300 kcmil',
	250: '350 kcmil',
	270: '400 kcmil',
	310: '500 kcmil',
	340: '600 kcmil',
	375: '700 kcmil',
	385: '750 kcmil',
	395: '800 kcmil',
	425: '900 kcmil',
	445: '1000 kcmil',
	485: '1250 kcmil',
	520: '1500 kcmil',
	545: '1750 kcmil',
	560: '2000 kcmil'
	}

	#---------------#
"""WIRE DERATE"""











"""VOLTAGE DROP"""
class NECTables():
	
	# keys are trade size convention AWG (American Wire Gauge)
	# corresponding values are circular mils taken from NEC
	awg_to_circmils = {
	'18': 1620,
	'16': 2580,
	'14': 4110,
	'12': 6530,
	'10': 10380,
	'8': 16510,
	'6': 26240,
	'4': 41740,
	'3': 52620,
	'2': 66360,
	'1': 83690,
	'1/0': 105600,
	'2/0': 133100,
	'3/0': 167800,
	'4/0': 211600,
	'250 kcmil': 250000,
	'300 kcmil': 300000,
	'350 kcmil': 350000,
	'400 kcmil': 400000,
	'450 kcmil': 450000,
	'500 kcmil': 500000,
	'600 kcmil': 600000,
	'700 kcmil': 700000,
	'750 kcmil': 750000,
	'800 kcmil': 800000,
	'900 kcmil': 900000,
	'1000 kcmil': 1000000,
	'1250 kcmil': 1250000,
	'1500 kcmil': 1500000,
	'1750 kcmil': 1750000,
	'2000 kcmil': 2000000
	}

	# phase factors correspond to normal 'single phase' 3-wire systems
	# and Delta or WYE 'three-phase' 4-wire transformer configurations
	# commonly used in North America
	def phase_modifier(phase):
		if phase == 1:
			return 2
		if phase == 3:
			return (3 ** .5)

	# assumes modern uncoated Copper or Aluminum wire as described in NEC
	def wire_modifier(c):
		if c == "CU":
			return 12.9
		if c == "AL":
			return 21.2


class FinalCalc(object):
	# this is the actual formula for voltage drop (one method of calculation)
	# the formula is used once for each individual circuit segment
	def final(base_current, voltage, phase, c, length, awg):
		 current = base_current * NECTables.phase_modifier(phase) * NECTables.wire_modifier(c) * length

		 numerator = current
		 denominator = NECTables.awg_to_circmils[awg]
		 
		 vd = numerator / denominator
		 percentage_1 = (voltage - vd) / voltage
		 percentage_2 = 1 - percentage_1
		 final_calc = percentage_2 * 100
		 return final_calc
"""VOLTAGE DROP"""
