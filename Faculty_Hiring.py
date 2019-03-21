#######################################################################
# ------------------------------ NOTES ------------------------------ #
#######################################################################
#
# This was built to condense the output of the Google Sheets used for
# the faculty hiring process into something that reads easier.
#
# NOTE: FILES MUST BE EXPORTED AS .CSV FILES FOR THIS PROGRAM TO WORK
#
# Input: python Faculty_Hiring.py input_file_name faculty candidate name
#  ex.   python Faculty_Hiring.py Mark_Babin Mark Babin
#	 where this reads the file Mark_Babin.csv
#
# Output: a text file (.txt) formatted as follows:
#
# For updates to this code, check posts to the associated GitHub repo:
# https://github.com/MarkCBabin/Faculty_Hiring
#
#######################################################################
# ------------------------------ START ------------------------------ #
#######################################################################

import sys
import pandas as pd
import math

# This section takes the input data, reads the requested file, creates
# the new file and creates a header
inFile = str(sys.argv[1])+'.csv'
f = open(inFile,'r')
# takes input from the user to select file from terminal and opens file
outFile = str(sys.argv[1]) +'.txt'
f1 = open(outFile,'w')
# designates the file to write all new information to (based on user input)

f1.write('Graduate Student Evaluation of ' + str(sys.argv[2])+' ' + str(sys.argv[3]) +'\n\n')

# this section inports all the data from the requested file & makes everything
# into the sections that it will print out 
cols = pd.read_csv(inFile,header=0,usecols=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])

for i in range (5):
	for j in range (16):
		test = isinstance(cols.iloc[i,j], basestring)
		if test is False:
			test1 = math.isnan(cols.iloc[i,j])
			if test1 is True:
				cols.iloc[i,j] = str()
# this set of for/if loops cleans up the data - as pandas reads things
# a blank space becomes a NaN, so this converts all NaNs back into blank spaces
			
# gathers responses to the first 9 questions, rated at Good Fair Poor
# this assumes the order is unchanged and that there are 6 evaluators!
research = str(cols.iloc[0,0]) + ' ' + str(cols.iloc[1,0]) +  ' ' + str(cols.iloc[2,0]) +  ' ' + str(cols.iloc[3,0]) + ' ' + str(cols.iloc[4,0]) + ' ' + str(cols.iloc[5,0])

teaching = str(cols.iloc[0,1]) + ' ' + str(cols.iloc[1,1]) +  ' ' + str(cols.iloc[2,1]) +  ' ' + str(cols.iloc[3,1]) + ' ' + str(cols.iloc[4,1]) + ' ' + str(cols.iloc[5,1])

mentoring = str(cols.iloc[0,2]) + ' ' + str(cols.iloc[1,2]) +  ' ' + str(cols.iloc[2,2]) +  ' ' + str(cols.iloc[3,2]) + ' ' + str(cols.iloc[4,2]) + ' ' + str(cols.iloc[5,2])

DEI = str(cols.iloc[0,3]) + ' ' + str(cols.iloc[1,3]) +  ' ' + str(cols.iloc[2,3]) +  ' ' + str(cols.iloc[3,3]) + ' ' + str(cols.iloc[4,3]) + ' ' + str(cols.iloc[5,3])

respect = str(cols.iloc[0,4]) + ' ' + str(cols.iloc[1,4]) +  ' ' + str(cols.iloc[2,4]) +  ' ' + str(cols.iloc[3,4]) + ' ' + str(cols.iloc[4,4]) + ' ' + str(cols.iloc[5,4])

environment = str(cols.iloc[0,5]) + ' ' + str(cols.iloc[1,5]) +  ' ' + str(cols.iloc[2,5]) +  ' ' + str(cols.iloc[3,5]) + ' ' + str(cols.iloc[4,5]) + ' ' + str(cols.iloc[5,5])

conflict = str(cols.iloc[0,6]) + ' ' + str(cols.iloc[1,6]) +  ' ' + str(cols.iloc[2,6]) +  ' ' + str(cols.iloc[3,6]) + ' ' + str(cols.iloc[4,6]) + ' ' + str(cols.iloc[5,6])

feedback = str(cols.iloc[0,7]) + ' ' + str(cols.iloc[1,7]) +  ' ' + str(cols.iloc[2,7]) +  ' ' + str(cols.iloc[3,7]) + ' ' + str(cols.iloc[4,7]) + ' ' + str(cols.iloc[5,7])

expectations = str(cols.iloc[0,8]) + ' ' + str(cols.iloc[1,8]) +  ' ' + str(cols.iloc[2,8]) +  ' ' + str(cols.iloc[3,8]) + ' ' + str(cols.iloc[4,8]) + ' ' + str(cols.iloc[5,8])

########################################################################################################################

f1.write(str(cols.iloc[1,9]))


f1.write('-')

