#!/usr/bin/python

'''*************************************************************************************************
Program: ensembler.py

Synopsis:
A simple python script that calculates the ensemble average of CMIP5 derivative data

Usage: ./ensembler.py [args]

Arguments:
filedir 		-	The location of the source files
outfolder		-	The destination folder for output

*************************************************************************************************'''

import subprocess, os, glob, argparse

if __name__ == '__main__':
    
	parser = argparse.ArgumentParser()
	parser.add_argument('filedir', type=str)
	parser.add_argument('outfolder', type=str)
	args = parser.parse_args()
	
	#Define the source folder for the input files
	filedir = args.filedir
	
	#Define the destination folder for the output
	outfolder = args.outfolder
	
	vars = ['days_tmax_abv','days_tmin_blw','days_prcp_abv','longest_run_tmax_abv',
	'longest_run_prcp_blw','growing_degree_day','heating_degree_day','cooling_degree_day',
	'growing_season_lngth']
	
	
	#Create the historical ensemble
	for i in range(len(vars)):
		files = glob.glob(filedir+"/*hist*"+vars[i]+"*.nc")
		for j in range(5):
			cmd = "ncea -h -d time,"+str(j)+","+str(j)+",1 -v "+vars[i]+" "+" ".join(files)+" tmp"+str(j)+".nc"
			process = subprocess.call(cmd,shell=True)
			#cmd = "ncecat -h -O -u time "+"tmp"+str(j)+".nc "+"tmp"+str(j)+".nc"		
			#process = subprocess.call(cmd,shell=True)		
			#cmd = "ncks -h -O --mk_rec_dmn time "+"tmp"+str(j)+".nc "+"tmp"+str(j)+".nc"		
			#process = subprocess.call(cmd,shell=True)	
		tmpfiles = glob.glob("./tmp*.nc")
		tmpfiles.sort()	
		cmd = "ncrcat -h "+" ".join(tmpfiles)+" ensemble_historical_"+vars[i]+"_decadal.nc"		
		process = subprocess.call(cmd,shell=True)	
		cmd = "rm tmp*.nc"	
		process = subprocess.call(cmd,shell=True)
		cmd = "mv *.nc "+outfolder+"/"
		process = subprocess.call(cmd,shell=True)
		
	#Create the rcp45 ensemble
	for i in range(len(vars)):
		files = glob.glob(filedir+"/*rcp45*"+vars[i]+"*.nc")
		for j in range(9):
			cmd = "ncea -h -d time,"+str(j)+","+str(j)+",1 -v "+vars[i]+" "+" ".join(files)+" tmp"+str(j)+".nc"
			process = subprocess.call(cmd,shell=True)
			#cmd = "ncecat -h -O -u time "+"tmp"+str(j)+".nc "+"tmp"+str(j)+".nc"		
			#process = subprocess.call(cmd,shell=True)		
			#cmd = "ncks -h -O --mk_rec_dmn time "+"tmp"+str(j)+".nc "+"tmp"+str(j)+".nc"		
			#process = subprocess.call(cmd,shell=True)	
		tmpfiles = glob.glob("./tmp*.nc")
		tmpfiles.sort()	
		cmd = "ncrcat -h "+" ".join(tmpfiles)+" ensemble_rcp45_"+vars[i]+"_decadal.nc"		
		process = subprocess.call(cmd,shell=True)	
		cmd = "rm tmp*.nc"	
		process = subprocess.call(cmd,shell=True)
		cmd = "mv *.nc "+outfolder+"/"
		process = subprocess.call(cmd,shell=True)
		
	#Create the rcp85 ensemble
	for i in range(len(vars)):
		files = glob.glob(filedir+"/*rcp85*"+vars[i]+"*.nc")
		for j in range(9):
			cmd = "ncea -h -d time,"+str(j)+","+str(j)+",1 -v "+vars[i]+" "+" ".join(files)+" tmp"+str(j)+".nc"
			process = subprocess.call(cmd,shell=True)
			#cmd = "ncecat -h -O -u time "+"tmp"+str(j)+".nc "+"tmp"+str(j)+".nc"		
			#process = subprocess.call(cmd,shell=True)		
			#cmd = "ncks -h -O --mk_rec_dmn time "+"tmp"+str(j)+".nc "+"tmp"+str(j)+".nc"		
			#process = subprocess.call(cmd,shell=True)	
		tmpfiles = glob.glob("./tmp*.nc")
		tmpfiles.sort()	
		cmd = "ncrcat -h "+" ".join(tmpfiles)+" ensemble_rcp85_"+vars[i]+"_decadal.nc"		
		process = subprocess.call(cmd,shell=True)	
		cmd = "rm tmp*.nc"	
		process = subprocess.call(cmd,shell=True)
		cmd = "mv *.nc "+outfolder+"/"
		process = subprocess.call(cmd,shell=True)