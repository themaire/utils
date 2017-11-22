#!/usr/bin/python3
# -*- coding: utf-8 -*-

##### Modules #####
import datetime

##### Variables #####


# ---->

##### Fonctions #####

# Fonction for a interval between two days (22pm to 7am)
def childInNight(soir, matin):
	"""
	Saids True if we are in the good time
	"""
	
	now = datetime.datetime.now()
	start = now.replace(hour= soir, minute=0, second=0, microsecond=0) 	# Start
	end = now.replace(hour= matin, minute=0, second=0, microsecond=0)	# End

	difstart = now > start
	difend = now < end

	if difstart or difend:
		return True;
	else:
		return None;

def childInDay(start, startmin, end, endmin):
	now = datetime.datetime.now()
	start = now.replace(hour= start, minute= startmin, second=0, microsecond=0) 	# Start
	end = now.replace(hour= end, minute= endmin, second=0, microsecond=0)	# End

	difstart = now > start
	difend = now < end

	if difstart and difend:
		return True;
	else:
		return None;

# test des deux fonctions
if __name__ == "__main__":

	print ("It's time or not childInNight?")
	print ("Result :" , childInNight(17, 8), sep=' ', end='\n')
	
	print ("It's time or not childInDay?")
	print ("Result :", childInDay(21, 5, 21, 13), sep=' ', end='\n')
