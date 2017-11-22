#!/usr/bin/python3
# -*- coding: utf-8 -*-

import threading
import psutil
from psutil import process_iter, virtual_memory, disk_usage
from time import sleep

# PROCNAME = 'mjpg_streamer'
NAME = ('mjpg_streamer', 'raspistill')

def getCamProc(i):
	"""
	i est l'indice du tuple NAME.
	"""
	cam = []
	for proc in process_iter():
		if proc.name() == NAME[int(i)]:
			cam.append(proc)
	return cam

def timoutCam(s, i, j=0):
	"""
	Fonction destinée a être utilisée dans un thread afin de couper la webcam au bout d'un certain temps."
	param@s : la duree de fontionnememnt de la camera
	param@i : est l'indice du tuple NAME.
	"""
	sleep(s)
	getCamProc(i)[j].suspend()

def StatusCam(i,j=0):
	"""
	Connaitre le status du processus de la webcam (soit 'sleeping' ou soit 'stopped')
	i est l'indice du tuple NAME.
	@return: le status sous forme de chaine.
	"""

	status = getCamProc(i)[j].status()
	
	return status

def cam(state, i, j=0):
	"""
	Allume ou éteint la cam en question.
	state off ou on
	i est en fonction du nom du proc voulut (l'indice du tuple NAME).
	j est l'indice du proc voulut
	@param:state, On ou off pour allumer ou éteindre.
	"""

	if state == 'off':
		# Suspendre, met en pause le processus :
		getCamProc(i)[j].suspend()
	elif state == 'on':
		# Reprends :
		getCamProc(i)[j].resume()
		threading.Thread(target=timoutCam, args=(300,i,j,)).start()
	else:
		exit()
	
# test de la fonction
if __name__ == "__main__":
	if StatusCam(NAME[1]) == 'sleeping':
		print("La cam fonctionne.")
	else:
		print("La cam est éteinte.")
		print()
		cam("on" ,NAME[1])
