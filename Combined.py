#Author: Jake Staab
#Date: 8/5/2019
#This program provides a user interface for the calculation of
#Voltage Drop, Conduit Fill, and Wire Derate (Wire Select).
#Interface allows for manipulation of input variables to be
#modified in real time.
#
#Requires companion file "solar_lib.py" which contains NEC 2017
#table information for ampacity, derate factors, wire cross-sectional area
#circular mils, conduit trade size and associated cross-sectional area

import tkinter as tk
import math
from tkinter import *
from tkinter.ttk import *
from solar_lib import NECTables as NEC
from solar_lib import NECTablesConduitFill as NEC_CF
from solar_lib import NECTablesWireDerate as NEC_WD

window = Tk()
window.title("Voltage Drop")
window.geometry("900x635")

#-----------------------------------------------------------------------
#VOLTAGE DROP

#calculates voltage drop for circuit given self-explanatory inputs
#output: the total percentage that voltage will decrease
def finalCalc(phase, material, current, length, voltage, wiresize):
	numerator = (phase * material * current * length)
	denominator = NEC.awg_to_circmils[wiresize]
	operating_voltage = voltage - (numerator / denominator)
	percentage = operating_voltage / voltage
	final = round(((1 - percentage) * 100), 3)
	return final
	
#prints the output of finalCalc to the interface	
def print_vd():
	finalVD = "Voltage Drop:  " + str(finalCalc(vd_phase.get(), material.get(), int(vd_currentvar.get()), int(vd_lengthvar.get()), int(vd_voltagevar.get()), vd_wiresize.get())) + "%"
	voltage_drop.configure(text=finalVD)

def awg_combo(event):
	global awg
	awg = NEC.awg_to_circmils[vd_wiresize.get()]

vd_header = Label(window, text="VOLTAGE DROP", font=("Courier", 18))
vd_header.grid(column=0, row=0)

material = tk.DoubleVar()
vd_phase = tk.DoubleVar()
vd_lengthvar = tk.StringVar()
vd_voltagevar = tk.StringVar()
vd_currentvar = tk.StringVar()

material_lbl = Label(window, text="Conductor Material:")
material_lbl.grid(column=0, row=1)
copper = Radiobutton(window, text="CU", variable=material, value=12.9)
copper.grid(column=0, row=2)
aluminum = Radiobutton(window, text="AL", variable=material, value=21.2)
aluminum.grid(column=0, row=3)

size_lbl = Label(window, text="Conductor Size")
size_lbl.grid(column=1, row=1)
vd_wiresize = Combobox(window)
vd_wiresize.grid(column=1, row=2)
vd_wiresize['values'] = (12, 10, 8, 6, 4, 3, 2, 1, "1/0", "2/0", "3/0", "4/0", "250 kcmil", "300 kcmil", "350 kcmil", "400 kcmil", "450 kcmil", "500 kcmil")
vd_wiresize.bind("<<ComboboxSelected>>", awg_combo)

length_lbl = Label(window, text="Circuit Length (ft.)")
length_lbl.grid(column=2, row=1)
length = Entry(window, width=15, textvariable=vd_lengthvar)
length.grid(column=2, row=2)

current_lbl = Label(window, text="Current")
current_lbl.grid(column=3, row=1)
current = Entry(window, width=10, textvariable=vd_currentvar)
current.grid(column=3, row=2)

voltage_lbl = Label(window, text="Voltage")
voltage_lbl.grid(column=4, row=1)
voltage = Entry(window, width=10, textvariable=vd_voltagevar)
voltage.grid(column=4, row=2)

phase_lbl = Label(window, text="Phase")
phase_lbl.grid(column=5, row=1)
phase_1 = Radiobutton(window, text="1", variable=vd_phase, value=2)
phase_1.grid(column=5, row=2)
phase_3 = Radiobutton(window, text="3", variable=vd_phase, value=1.732)
phase_3.grid(column=5, row=3)

calculate = Button(window, text="Calculate", command=print_vd)
calculate.grid(column=0, row=4)

voltage_drop = Label(window, text="----")
voltage_drop.grid(column=1, row=4)

vd_spacer = Label(window, text=" ", font=("Courier", 18))
vd_spacer.grid(column=0, row=6, pady=30)

#-----------------------------------------------------------------------
#CONDUIT FILL

def conductor_combo(event):
	global conductor_combo

#retrieves the cross-sectional area of conductor
#based on AWG size and insulation type
#assigns these values to insulation_area and ground_area
#assigns insulation type to ground; this program does not
#currently allow for bare ground selection 
def insulation_combo(event):
	global insulation_area, ground_area
	if insulation.get() == "PV":
		insulation_area = NEC_CF.pv_awg_to_area[cf_wiresize.get()]
		ground_area = NEC_CF.pv_awg_to_area[ground.get()]
	elif insulation.get() == "THHN":
		insulation_area = NEC_CF.thhn_awg_to_area[cf_wiresize.get()]
		ground_area = NEC_CF.thhn_awg_to_area[ground.get()]
	
def conduit_combo(event):
	global conduit_type

#calculates total cross-sectional area of all conductors
#utilizes conduit_select function to select appropriate conduit size
#prints conclusion to interface 
def conduit_fill_calc():
	global conductor_area, cf_final
	conductor_area = (insulation_area * int(no_of_conductors.get())) + ground_area
	if conduit.get() == "EMT":
		cf_final = conduit_select(NEC_CF.emt_lst, NEC_CF.emt_dict)
	elif conduit.get() == "PVC":
		cf_final = conduit_select(NEC_CF.pvc_lst, NEC_CF.pvc_dict)
	conduit_fill_string = "Total Fill:  " + str(round(cf_final[0], 1)) + "%  in " + str(cf_final[1]) + conduit.get() + "  conduit"
	conduit_fill_percentage.configure(text=conduit_fill_string)

#function determines minimum size conduit based on max 40% fill
#returns the cross-sectional area of wire bundle as a percent
#returns conduit size 
def conduit_select(cond_list,cond_dic):
	for x in cond_list:
		if (conductor_area / .4) > x:
			continue
		elif (conductor_area / .4) < x:
			cross_sect = (conductor_area / x) * 100
			return cross_sect, cond_dic[x]

#takes cross-sectional area of wire bundle and finds the percent fill
#of user chosen conduit size
#this allows the user to increase conduit size manually and
#determine fill percentage for that conduit size 		
def manual_cf():
	if conduit.get() == 'EMT':
		for key, value in NEC_CF.emt_dict.items():
			if value == conduit_manual.get():
				manual = (conductor_area / key) * 100
		manual_fill_string = "Total Fill: " + str(round(manual, 1)) + "% in "
		manual_fill_percentage.configure(text=manual_fill_string)
	elif conduit.get() == 'PVC':
		for key, value in NEC_CF.pvc_dict.items():
			if value == conduit_manual.get():
				manual = (conductor_area / key) * 100
		manual_fill_string = "Total Fill: " + str(round(manual, 1)) + "% in "
		manual_fill_percentage.configure(text=manual_fill_string)


cf_header = Label(window, text="CONDUIT FILL", font=("Courier", 18))
cf_header.grid(column=0, row=7)

no_of_conductors = tk.StringVar()

cf_size_lbl = Label(window, text="Conductor Size")
cf_size_lbl.grid(column=0, row=8)
cf_wiresize = Combobox(window)
cf_wiresize.grid(column=0, row=9)
cf_wiresize['values'] = (12, 10, 8, 6, 4, 3, 2, 1, "1/0", "2/0", "3/0", "4/0", "250 kcmil", "300 kcmil", "350 kcmil", "400 kcmil", "500 kcmil")
cf_wiresize.bind("<<ComboboxSelected>>", insulation_combo)

conductor_count_lbl = Label(window, text="No. of Conductors")
conductor_count_lbl.grid(column=1, row=8)
conductor_count = Entry(window, width=10, textvariable=no_of_conductors)
conductor_count.grid(column=1, row=9)

insulation_lbl = Label(window, text="Insulation Type")
insulation_lbl.grid(column=2, row=8)
insulation = Combobox(window)
insulation.grid(column=2, row=9)
insulation['values'] = ("PV", "THHN")
insulation.bind("<<ComboboxSelected>>", insulation_combo)

ground_lbl = Label(window, text="Ground Size")
ground_lbl.grid(column=3, row=8)
ground = Combobox(window)
ground.grid(column=3, row=9)
ground['values'] = ("10", "8", "6", "4", "3", "2", "1", "1/0", "2/0", "3/0")
ground.bind("<<ComboboxSelected>>", insulation_combo)

conduit_lbl = Label(window, text="Conduit Type")
conduit_lbl.grid(column=4, row=8)
conduit = Combobox(window)
conduit.grid(column=4, row=9)
conduit['values'] = ("EMT", "PVC")
conduit.bind("<<ComboboxSelected>>", conduit_combo)

cf_calculate = Button(window, text="Calculate", command=conduit_fill_calc)
cf_calculate.grid(column=0, row=10)

conduit_fill_percentage = Label(window, text="----")
conduit_fill_percentage.grid(column=1, row=10)

cf_manual_header = Label(window, text="Preferred size:", font=("Courier", 12))
cf_manual_header.grid(column=0, row=11)

manual_conduit_size = Label(window, text="Manual Conduit Size")
manual_conduit_size.grid(column=0, row=12)
conduit_manual = Combobox(window)
conduit_manual.grid(column=0, row=13)
conduit_manual['values'] = ("1/2\"", "3/4\"", "1\"", "1-1/4\"", "1-1/2\"", "2\"", "2-1/2\"", "3\"", "3-1/2\"", "4\"")
conduit_manual.bind("<<ComboboxSelected>>", insulation_combo)

manual_cf_calculate = Button(window, text="Calculate", command=manual_cf)
manual_cf_calculate.grid(column=1, row=13)

manual_fill_percentage = Label(window, text="----")
manual_fill_percentage.grid(column=2, row=13)

cf_spacer = Label(window, text=" ", font=("Courier", 18))
cf_spacer.grid(column=0, row=14, pady=30)

#-----------------------------------------------------------------------
#WIRE DERATE

#NEC 310.15(B)(3)(a) adjustment factors for more than 3
#current-carrying conductors #assumes 90 degree column wire only
#output: derate factor based on no. of conductors 
def fill_factor(lst,num,dic):
	for i in lst:
		if num > i:
			continue
		elif num < i:
			return dic[i]

#NEC 310.15(B)(2)(a) ambient temperature correction factors
#assumes 90 degree column wire only
#output: derate factor based on ambient temperature 
def temp_factor(lst,temp):
	global dic
	dic = NEC_WD.temp_dict_90

	for i in lst:
		if int(wd_temp.get()) > i:
			continue
		elif int(wd_temp.get()) < i:
			return dic[i]

#determines the current in Amps required by the wire gauge (ampacity)
#to safely carry the load current with factored adjustments
#output: minimum ampacity conductor must possess 
def final_calc():
	global f, factors
	f = fill_factor(NEC_WD.fill_lst, int(wd_cond_countvar.get()), NEC_WD.fill_dict)
	t = temp_factor(NEC_WD.temp_lst,int(wd_temp.get()))
	factors = int(wd_currentvar.get()) / f / t
	if wd_continuousvar.get() == 'Y':
		required_ampacity = factors * 1.25
	else:
		required_ampacity = factors
	return required_ampacity
	

#assumes only wire in NEC 90 deg column is used
#assumes 75 degree terminals
#output: the actual copper wire gauge from NEC 75 deg column 	
def cu_wire_select(ampacity):
	cu_lst = NEC_WD.cu_ampacity_90
	cu_dic = NEC_WD.cu_ampacity_to_awg_90

	for a in cu_lst:
		if ampacity > a:
			continue
		elif ampacity < a:
			return cu_dic[a], a

#assumes only wire in NEC 90 deg column is used
#assumes 75 degree terminals
#output: the actual aluminum wire gauge from NEC 75 deg column 
def al_wire_select(ampacity):
	al_lst = NEC_WD.al_ampacity_90
	al_dic = NEC_WD.al_ampacity_to_awg_90
	
	for a in al_lst:
		if ampacity > a:
			continue
		elif ampacity < a:
			return al_dic[a], a

#used to print wire gauges for copper and aluminum within interface 	
def wd_final():
	wd_string = "Copper: " + str(cu_wire_select(final_calc())[0]) + "\nAluminum: " + str(al_wire_select(final_calc())[0])
	cu_wire_size.configure(text=wd_string)
	
wd_header = Label(window, text="WIRE SIZING", font=("Courier", 18))
wd_header.grid(column=0, row=15)

wd_currentvar = tk.StringVar()
wd_cond_countvar = tk.StringVar()
wd_insulation = tk.StringVar()
wd_temp = tk.StringVar()
wd_continuousvar = tk.StringVar()

wd_base_current = Label(window, text="Current")
wd_base_current.grid(column=0, row=16)
wd_currentvar = Entry(window, width=10, textvariable=wd_currentvar)
wd_currentvar.grid(column=0, row=17)

wd_cond_count = Label(window, text="No. of Curr. Carrying Cond.")
wd_cond_count.grid(column=1, row=16)
wd_cond_countvar = Entry(window, width=10, textvariable=wd_cond_countvar)
wd_cond_countvar.grid(column=1, row=17)

wd_insulation_lbl = Label(window, text="Insulation Type")
wd_insulation_lbl.grid(column=2, row=16)
wd_insulation = Combobox(window)
wd_insulation.grid(column=2, row=17)
wd_insulation['values'] = ("PV", "THHN")

wd_temperature_lbl = Label(window, text="Ambient Temp (F)")
wd_temperature_lbl.grid(column=3, row=16)
wd_temp = Entry(window, width=10, textvariable=wd_temp)
wd_temp.grid(column=3, row=17)

wd_continuous = Label(window, text="Continuous Load?")
wd_continuous.grid(column=4, row=16)
wd_cont_yes = Radiobutton(window, text="Yes", variable=wd_continuousvar, value='Y')
wd_cont_yes.grid(column=4, row=17)
wd_cont_no = Radiobutton(window, text="No", variable=material, value='N')
wd_cont_no.grid(column=4, row=18)

wd_cu_calculate = Button(window, text="Calculate", command=wd_final)
wd_cu_calculate.grid(column=0, row=20)

cu_wire_size = Label(window, text="----")
cu_wire_size.grid(column = 1, row=20)


window.mainloop()
