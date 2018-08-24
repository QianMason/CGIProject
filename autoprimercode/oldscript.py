import os
import subprocess


#ask user for input files
#ask for location output
#subprocess to run primer3 with the input files and target output destination
#parse output file 


#class PrimerScript():
	#part A: take input and set stuff like initial file settings, input, output destination

#def PrimerParser():

# def PrimerParser(filepath):
# 	#takeoutput of primer3 run and parse for primers
# 	#ask user to indicate number of primers they set or you can reuse the number the user set earlier
# 	primernum = int(input('Please specify number of primers asked to be returned: '))
# 	count = 0
# 	left = 0
# 	right = 0
# 	primerpairs = {}
# 	leftprimers = []
# 	rightprimers = []

# 	with open(filepath, 'r') as primer_file:

# 		lines = primer_file.readlines()
# 		while count < primernum:
# 			for line in lines:
# 				if (line.startswith('PRIMER_LEFT_' + str(left) + '_SEQUENCE')):
# 					left+=1
# 					leftprimers.append(line.split('=')[1])
# 				if (line.startswith('PRIMER_RIGHT_' + str(right) + '_SEQUENCE')):
# 					right+=1
# 					rightprimers.append(line.split('=')[1])
# 					count+=1

# 	#right here i may want to add functionality for the user to upload ane existing sheet to append more primers to?
# 	with open(filepath + 'primerlist', 'a+') as primer_output:
# 		for i in range(len(leftprimers)):
# 			primer_output.write('>' + 'left_primer_' + str(i) + '-F' + '\n')
# 			primer_output.write(leftprimers[i])
# 			primer_output.write('>' + 'right_primer_' + str(i) + '-R' + '\n')
# 			primer_output.write(rightprimers[i])
				


def PrimerParser(filepath):
	#takeoutput of primer3 run and parse for primers
	#ask user to indicate number of primers they set or you can reuse the number the user set earlier
	count = 0
	primerpairs = {}
	leftprimers = []
	rightprimers = []

	with open(filepath, 'r') as primer_file:

		lines = primer_file.readlines()
		for line in lines:
			if (line.startswith('PRIMER_LEFT_0_SEQUENCE')):
				leftprimers.append(line.split('=')[1])
			if (line.startswith('PRIMER_RIGHT_0_SEQUENCE')):
				rightprimers.append(line.split('=')[1])
			if (line.startswith('PRIMER_PAIR_NUM_RETURNED=0')):
				print('primer pair not found for some sequence(s), please check output file')

	#right here i may want to add functionality for the user to upload ane existing sheet to append more primers to?
	with open(filepath + 'primerlist.txt', 'w+') as primer_output:
		for i in range(len(leftprimers)):
			primer_output.write('>' + 'primer' + str(i) + '-F' + '\n')
			primer_output.write(leftprimers[i])
			primer_output.write('>' + 'primer' + str(i) + '-R' + '\n')
			primer_output.write(rightprimers[i])






def SettingFileParser(filepath):
    with open(filepath, 'r') as read_file:
        lines = read_file.readlines()
        with open(filepath, 'w') as write_file:
            for line in lines:
                if line.startswith('PRIMER_PRODUCT_SIZE_RANGE='):
                    # keep the line the same except the part needing replacement
                    replace = input('please specify product size range: ')
                    write_file.write(line.replace(line.split('=')[1], replace + '\n'))

                elif line.startswith('PRIMER_NUM_RETURN='):
                	replace = input('please specify number of primer pairs to return: ')
                	write_file.write(line.replace(line.split('=')[1], replace + '\n'))

                elif line.startswith('PRIMER_MIN_SIZE='):
                	replace = input('please specify minumum primer size: ')
                	write_file.write(line.replace(line.split('=')[1], replace + '\n'))

                elif line.startswith('PRIMER_OPT_SIZE='):
                	replace = input('please specify optimal primer size: ')
                	write_file.write(line.replace(line.split('=')[1], replace + '\n'))

                elif line.startswith('PRIMER_MAX_SIZE='):
                	replace = input('please specify max primer size (36 is limit): ')
                	write_file.write(line.replace(line.split('=')[1], replace + '\n'))	

                elif line.startswith('PRIMER_MIN_TM='):
                	replace = input('please specify minumum primer melting temp: ')
                	write_file.write(line.replace(line.split('=')[1], replace + '\n'))

                elif line.startswith('PRIMER_OPT_TM='):
                	replace = input('please specify optimal primer melting temp: ')
                	write_file.write(line.replace(line.split('=')[1], replace + '\n'))

                elif line.startswith('PRIMER_MAX_TM='):
                	replace = input('please specify maximum primer melting temp: ')
                	write_file.write(line.replace(line.split('=')[1], replace + '\n'))

                elif line.startswith('PRIMER_MIN_GC='):
                	replace = input('please specify minimum primer GC% (ie 25.0): ')
                	write_file.write(line.replace(line.split('=')[1], replace + '\n'))

                elif line.startswith('PRIMER_MAX_GC='):
                	replace = input('please specify maximum primer GC% (ie 80.0): ')
                	write_file.write(line.replace(line.split('=')[1], replace + '\n'))

                elif line.startswith('PRIMER_MAX_POLY_X='):
                	replace = input('please specify max # repeated mononucleotides to be accepted: ')
                	write_file.write(line.replace(line.split('=')[1], replace + '\n'))

                elif line.startswith('PRIMER_GC_CLAMP='):
                	replace = input('please specify # of allowable GCs at the 3\' end of primers: ')
                	write_file.write(line.replace(line.split('=')[1], replace + '\n'))

                elif line.startswith('PRIMER_MAX_SELF_END='):
                	replace = input('please specify max 3\' self complementary bases allowed: ')
                	write_file.write(line.replace(line.split('=')[1], replace + '\n'))

                elif line.startswith('PRIMER_MAX_SELF_ANY='):
                	replace = input('please specify max # of binding bases allowed for primer: ')
                	write_file.write(line.replace(line.split('=')[1], replace + '\n'))

                else:
                    # otherwise just write the line as is
                    write_file.write(line)


		





settingsboolean = input('Would you like to add a global parameter file?: y/n ')
if (settingsboolean == 'y'):
	setparametersbool = input('Would you like to set parameters in the command line(1) or provide your own setting file(2)?: 1/2 ')
	if setparametersbool == '1':
		filepa = input('Please provide a filepath for a template setting file: ')
		SettingFileParser(filepa)
		p3filesettings = '-p3_settings_file=' + filepa
	else:
		p3filesettings = '-p3_settings_file=' + input('Please type parameters file path: ')






inputlocation = input('Please type input filepath: ')
output = input('Please type output filepath: ')
outputlocation = '-output=' + output + 'primeroutput.txt'


if (settingsboolean == 'y'):
	cmd = ['primer3_core', p3filesettings, outputlocation, inputlocation]
else:
	cmd = ['primer3_core', outputlocation, inputlocation]

subprocess.call(cmd)

PrimerParser(output + 'primeroutput.txt')

#subprocess.call('./pooler')


