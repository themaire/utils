#!/usr/bin/python3
# -*- coding: utf-8 -*-

##### Description #####
# blinkt_pulse : show a LEDs pulse

##### Modules #####

from time import sleep

# Hardware
from blinkt import set_pixel, set_brightness, show, clear

if __name__ != "__main__":
	# Colors dictionary
	from utils.m_color_list import colors

##### Variables #####

# ---->

##### Classes #####

class myblinkt():
	def __init__(self):
		self.brightness = 0.6

	def on(self,col):
		set_brightness(self.brightness)
		for i in range(8):
			set_pixel(i, colors(col)[0], colors(col)[1], colors(col)[2])
		show()

	def off(self):
		clear()
		show()

##### Fonctions #####

def blinkt_pulse(col):
	#### Turning on each LED by LED in a for loop
		for i in range(8):
			clear()
			set_pixel(i, colors(col)[0], colors(col)[1], colors(col)[2])
			show()
			sleep(0.1)
		
		#### Turn off LED #7 (the 8th)
		clear()
		set_pixel(7, 0, 0, 0)
		show()

def chenillard(col, col2):
	for i in range(8):
		clear()
		if i > 0:
			set_pixel(i, colors(col)[0], colors(col)[1], colors(col)[2])
		if i >= 1 and i < 8:
			set_pixel(i-1, colors(col2)[0], colors(col2)[1], colors(col2)[2])
		show()
		sleep(0.4)

	for i in reversed(range(8)):
		clear()
		if i > 0:
			set_pixel(i, colors(col)[0], colors(col)[1], colors(col)[2])
		if i < 8 and i >= 1:
			set_pixel(i-1, colors(col2)[0], colors(col2)[1], colors(col2)[2])
		show()
		sleep(0.4)

# test des deux fonctions
if __name__ == "__main__":

	from m_color_list import colors
	
	set_brightness(0.1)

	for i in range(7):
		blinkt_pulse('pink')

	chenillard('red', 'yellow')
	
	b = myblinkt()
	b.on('blue light')
	sleep(10)
	b.off()