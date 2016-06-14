# Create a program that parses Logs.txt and allows the user to search inclusivly and exclusivly by the following:

try:
	# Choose the log file to search
	filename = "./input/logs.txt"	
	while True:
		f = open(filename, "r")
		option = raw_input("Enter 1.Search inclusively, 2.Search Exclusively\n and '0' to exit! ")
		if option == '1':
			searchStr = raw_input("Enter a string to be included in the results\n(OS,Browser,IP,Date & Time,File Requested,Referer): ")
			counter = 0
			for line in f:
				if searchStr in line:
					print line
					counter+=1
				elif counter>0:
					print "End of result!"
					break
				else:
					print "NOT FOUND(Beware: Keywords are case sensitive(Example: Windows! not windows))"
					break
		
		elif option == '2':
			searchStr = raw_input("Enter a String to be excluded from the results\n(OS,Browser,IP,Date & Time,File Requested,Referer): ")
			counter = 0
			for line in f:
				if searchStr not in line:
					print line
					counter+=1
				elif counter>0:
					print "End of result!"
					break					
				else:
					print "NOT FOUND(Beware: Keywords are case sensitive(Example: Mozilla! not mozilla))"
					break
		
		elif option == '0':
			break
		
		else: 
		# option != 1 or option != 2:
			print "Enter a valid option!"		
		continue

except IOError:
	print 'cannot open', filename
