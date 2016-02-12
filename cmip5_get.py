#!/usr/bin/python

# Program: cmip5_get.py
# A simple script to write out commands to retrieve cmip5 derivative data from Dave Blodgett's catalog
# Usage (from command line): ./cmip5_get.py > output.txt
# Once complete (1ms), the file output.txt will contain wget directives and also a line to rename each file as it comes in 

import subprocess, os


if __name__ == '__main__':


	vars = ['longest_run_tmax_abv',
	'longest_run_prcp_blw',
	'heating_degree_day',
	'growing_season_lngth',
	'growing_degree_day',
	'days_tmin_blw',
	'days_tmax_abv',
	'days_prcp_abv',
	'cooling_degree_day']

	#scenario = ['historical', 'rcp45', 'rcp85']
	scenario = ['rcp85']
	
	models = ['inmcm4',
	'bcc-csm1-1',
	'NorESM1-M',
	'MRI-CGCM3',
	'MPI-ESM-MR',
	'MPI-ESM-LR',
	'MIROC5',
	'MIROC-ESM',
	'MIROC-ESM-CHEM',
	'IPSL-CM5A-MR',
	'IPSL-CM5A-LR',
	'GFDL-ESM2M',
	'GFDL-ESM2G',
	'GFDL-CM3',
	'CanESM2',
	'CSIRO-Mk3-6-0',
	'CNRM-CM5',
	'CESM1-BGC',
	'CCSM4',
	'BNU-ESM',
	'ACCESS1-0']

	baseurl = 'http://cida.usgs.gov/thredds/fileServer/cmip5_bcca/derivatives/'  #cmip5_hist_der/bcc-csm1-1_historical_r1i1p1/longest_run_tmax_abv.nc
	
	
	for i in range(len(models)):
		for j in range(len(vars)):
			for k in range(len(scenario)):
				if(scenario[k] == 'historical'): subdir = 'cmip5_hist_der/'
				if(scenario[k] != 'historical'): subdir = 'cmip5_der/'
				cmd = 'wget '+baseurl+subdir+models[i]+'_'+scenario[k]+'_r1i1p1/'+vars[j]+'.nc'
				print cmd
				cmd = 'mv '+vars[j]+'.nc '+subdir.split('/')[0]+'_'+models[i]+'_'+scenario[k]+'_r1i1p1_'+vars[j]+'.nc'
				print cmd

	
	
	#process = subprocess.call(cmd,shell=True