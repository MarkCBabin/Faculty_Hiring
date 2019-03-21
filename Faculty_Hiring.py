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

for i in range (6):
	for j in range (17):
		test = isinstance(cols.iloc[i,j], basestring)
		if test is False:
			test1 = math.isnan(cols.iloc[i,j])
			if test1 is True:
				cols.iloc[i,j] = 'N/A'
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

f1.write('Potential contributions to research\n' + research + '\n')
f1.write('Potential contributions as a teacher or lecturer\n' + teaching + '\n')
f1.write('Potential contributions to mentoring\n' + mentoring + '\n')
f1.write('Potential contributions to diversity, equity, and inclusion\n' + DEI + '\n')
f1.write('Treated student evaluators with dignity and respect\n' + respect + '\n')
f1.write('Has a clear plan to foster a positive work environment in their lab\n' + environment + '\n')
f1.write('Can articulate strategy for handling conflicts (esp. relating to assigning authorship)\n' + conflict + '\n')
f1.write('Has a concrete plan for gathering feedback from students about lab management and graduate student mentorship\n' + feedback + '\n')
f1.write('Has a clear plan for articulating expectations to graduate students\n' + expectations + '\n')

f1.write('Irrespective of your field, how exciting do you find their research to be?\n')
for i in range (6):
	f1.write('- ' + str(cols.iloc[i,9])+'\n')

f1.write('Would they be a good recruiter for bringing new students to the department?\n')
for i in range (6):
	f1.write('- ' + str(cols.iloc[i,10])+'\n')

f1.write('For statements where you selected a fair or poor, does the faculty candidate have specific plans to improve these areas? If so, please describe them.\n')
for i in range (6):
	f1.write('- ' + str(cols.iloc[i,11])+'\n')

f1.write('Please describe any concrete examples that the faculty candidate gave to demonstrate that he/she has prepared himself/herself to mentor graduate students and/or manage a research group.\n')
for i in range (6):
	f1.write('- ' + str(cols.iloc[i,12])+'\n')

f1.write('What impresses you the most about this candidate?\n')
for i in range (6):
	f1.write('- ' + str(cols.iloc[i,13])+'\n')

f1.write('What concerns you the most about this candidate?\n')
for i in range (6):
	f1.write('- ' + str(cols.iloc[i,14])+'\n')

f1.write('Is this a candidate that you think would be a good addition to our faculty? Why?\n')
for i in range (6):
	f1.write('- ' + str(cols.iloc[i,15])+'\n')

f1.write('Is there any other information that you would like to provide to the hiring committee concerning this faculty candidate?\n')
for i in range (6):
	f1.write('- ' + str(cols.iloc[i,16])+'\n')

