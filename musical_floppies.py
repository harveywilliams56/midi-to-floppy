
from __future__ import division
import sys
import wiringpi2 as wiringpi
wiringpi.wiringPiSetup()
wiringpi.pinMode(6,1)
wiringpi.pinMode(7,1)
wiringpi.pinMode(4,1)
wiringpi.pinMode(5,1)
from time import sleep
bar = 2
#space = 0.05
space = 0.1
bars_one = 32
bars_two = 16
divde = 0.15

cv = 1/523.25
csv = 1/554.37
dv = 1/587.33
dsv = 1/622.25
ev = 1/659.25
fv = 1/698.46
fsv = 1/739.99
gv = 1/783.99
gsv = 1/830.61
av = 1/880.00
asv = 1/932.33
bv = 1/987.77

civ = cv*2
csiv = csv*2
div = dv*2
dsiv = dsv*2
eiv = ev*2
fiv = fv*2
fsiv = fsv*2
giv = fv*2
gsiv = gsv*2
aiv = av*2
asiv = asv*2
biv = bv*2

ciii = cv*4
csiii = csv*4
diii = dv*4
dsiii = dsv*4
eiii = ev*4
fiii = fv*4
fsiii = fsv*4
giii = fv*4
gsiii = gsv*4
aiii = av*4
asiii = asv*4
biii = bv*4

cii = cv*8
csii = csv*8
dii = dv*8
dsii = dsv*8
eii = ev*8
fii = fv*8
fsii = fsv*8
gii = fv*8
gsii = gsv*8
aii = av*8
asii = asv*8
bii = bv*8

ci = cv*16
csi = csv*16
di = dv*16
dsi = dsv*16
ei = ev*16
fi = fv*16
fsi = fsv*16
gi = fv*16
gsi = gsv*16
ai = av*16
asi = asv*16
bi = bv*16

cz = cv*32
csz = csv*32
dz = dv*32
dsz = dsv*32
ez = ev*32
fz = fv*32
fsz = fsv*32
gz = fv*32
gsz = gsv*32
az = av*32
asz = asv*32
bz = bv*32
one = 0
two = 0

blank = [[bar*17, 1, space, 0], [bar*17, 1, space, 0]]

tetris = [[eiii, int(bar/4/eiii/(0.5*2)), space, 0],
	[bii, int(bar/8/bii/(0.5*2)), space, 0],
	[ciii, int(bar/8/ciii/(0.5*2)), space, 0],
	[diii, int(bar/4/diii/(0.5*2)), space, 0],
	[ciii, int(bar/8/ciii/(0.5*2)), space, 0],
	[bii, int(bar/8/bii/(0.5*2)), space, 0],
	[aii, int(bar/4/aii/(0.5*2)), space, 0],
	[aii, int(bar/8/aii/(0.5*2)), space, 0],
	[ciii, int(bar/8/ciii/(0.5*2)), space, 0],
	[eiii, int(bar/4/eiii/(0.5*2)), space, 0],
	[diii, int(bar/8/diii/(0.5*2)), space, 0],
	[ciii, int(bar/8/ciii/(0.5*2)), space, 0],
	[bii, int(bar/8*3/bii/(0.5*2)), space, 0],
	[ciii, int(bar/8/ciii/(0.5*2)), space, 0],
	[diii, int(bar/4/diii/(0.5*2)), space, 0],
	[eiii, int(bar/4/eiii/(0.5*2)), space, 0],
	[ciii, int(bar/4/ciii/(0.5*2)), space, 0],
	[aii, int(bar/4/aii/(0.5*2)), space, 0],
	[aii, int(bar/8/aii/(0.5*2)), space, 0],
	[aii, int(bar/8/aii/(0.5*2)), space, 0],
	[bii, int(bar/8/bii/(0.5*2)), space, 0],
	[ciii, int(bar/8/ciii/(0.5*2)), space, 0],
	[diii, int(bar/8*3/diii/(0.5*2)), space, 0],
	[fiii, int(bar/8/fiii/(0.5*2)), space, 0],
	[aiii, int(bar/4/aiii/(0.5*2)), space, 0],
	[giii, int(bar/8/giii/(0.5*2)), space, 0],
	[fiii, int(bar/8/fiii/(0.5*2)), space, 0],
	[eiii, int(bar/8*3/eiii/(0.5*2)), space, 0],
	[ciii, int(bar/8/ciii/(0.5*2)), space, 0],
	[eiii, int(bar/4/eiii/(0.5*2)), space, 0],
	[diii, int(bar/8/diii/(0.5*2)), space, 0],
	[ciii, int(bar/8/ciii/(0.5*2)), space, 0],
	[bii, int(bar/4/bii/(0.5*2)), space, 0],
	[bii, int(bar/8/bii/(0.5*2)), space, 0],
	[ciii, int(bar/8/ciii/(0.5*2)), space, 0],
	[diii, int(bar/4/diii/(0.5*2)), space, 0],
	[eiii, int(bar/4/eiii/(0.5*2)), space, 0],
	[ciii, int(bar/4/ciii/(0.5*2)), space, 0],
	[aii, int(bar/4/aii/(0.5*2)), space, 0],
	[aii, int(bar/4/aii/(0.5*2)), space, (bar/4)],
	[eiii, int(bar/4/eiii/(0.5*2)), space, 0],
	[bii, int(bar/8/bii/(0.5*2)), space, 0],
	[ciii, int(bar/8/ciii/(0.5*2)), space, 0],
	[diii, int(bar/4/diii/(0.5*2)), space, 0],
	[ciii, int(bar/8/ciii/(0.5*2)), space, 0],
	[bii, int(bar/8/bii/(0.5*2)), space, 0],
	[aii, int(bar/4/aii/(0.5*2)), space, 0],
	[aii, int(bar/8/aii/(0.5*2)), space, 0],
	[ciii, int(bar/8/ciii/(0.5*2)), space, 0],
	[eiii, int(bar/4/eiii/(0.5*2)), space, 0],
	[diii, int(bar/8/diii/(0.5*2)), space, 0],
	[ciii, int(bar/8/ciii/(0.5*2)), space, 0],
	[bii, int(bar/8*3/bii/(0.5*2)), space, 0],
	[ciii, int(bar/8/ciii/(0.5*2)), space, 0],
	[diii, int(bar/4/diii/(0.5*2)), space, 0],
	[eiii, int(bar/4/eiii/(0.5*2)), space, 0],
	[ciii, int(bar/4/ciii/(0.5*2)), space, 0],
	[aii, int(bar/4/aii/(0.5*2)), space, 0],
	[aii, int(bar/8/aii/(0.5*2)), space, 0],
	[aii, int(bar/8/aii/(0.5*2)), space, 0],
	[bii, int(bar/8/bii/(0.5*2)), space, 0],
	[ciii, int(bar/8/ciii/(0.5*2)), space, 0],
	[diii, int(bar/8*3/diii/(0.5*2)), space, 0],
	[fiii, int(bar/8/fiii/(0.5*2)), space, 0],
	[aiii, int(bar/4/aiii/(0.5*2)), space, 0],
	[giii, int(bar/8/giii/(0.5*2)), space, 0],
	[fiii, int(bar/8/fiii/(0.5*2)), space, 0],
	[eiii, int(bar/8*3/eiii/(0.5*2)), space, 0],
	[ciii, int(bar/8/ciii/(0.5*2)), space, 0],
	[eiii, int(bar/4/eiii/(0.5*2)), space, 0],
	[diii, int(bar/8/diii/(0.5*2)), space, 0],
	[ciii, int(bar/8/ciii/(0.5*2)), space, 0],
	[bii, int(bar/4/bii/(0.5*2)), space, 0],
	[bii, int(bar/8/bii/(0.5*2)), space, 0],
	[ciii, int(bar/8/ciii/(0.5*2)), space, 0],
	[diii, int(bar/4/diii/(0.5*2)), space, 0],
	[eiii, int(bar/4/eiii/(0.5*2)), space, 0],
	[ciii, int(bar/4/ciii/(0.5*2)), space, 0],
	[aii, int(bar/4/aii/(0.5*2)), space, 0],
	[aii, int(bar/4/aii/(0.5*3)), space,    0],
	[eiii, int(bar/2/eiii/(0.5*2)), space, 0],
	[ciii, int(bar/2/ciii/(0.5*2)), space, 0],
	[diii, int(bar/2/diii/(0.5*2)), space, 0],
	[bii, int(bar/2/bii/(0.5*2)), space, 0],
	[ciii, int(bar/2/ciii/(0.5*2)), space, 0],
	[aii, int(bar/2/aii/(0.5*2)), space, 0]]

tetris_two = [[cii, int(bar/8/cii), space, 0],
	[ciii, int(bar/8/ciii), space, 0],
	[cii, int(bar/8/cii), space, 0],
	[ciii, int(bar/8/ciii), space, 0],
	[cii, int(bar/8/cii), space, 0],
	[ciii, int(bar/8/ciii), space, 0],
	[cii, int(bar/8/cii), space, 0],
	[ciii, int(bar/8/ciii), space, 0],
	[fii, int(bar/8/fii), space, 0],
	[fiii, int(bar/8/fiii), space, 0],
	[fii, int(bar/8/fii), space, 0],
	[fiii, int(bar/8/fiii), space, 0],
	[fii, int(bar/8/fii), space, 0],
	[fiii, int(bar/8/fiii), space, 0],
	[fii, int(bar/8/fii), space, 0],
	[fiii, int(bar/8/fiii), space, 0],
	[eii, int(bar/8/eii), space, 0],
	[eiii, int(bar/8/eiii), space, 0],
	[eii, int(bar/8/eii), space, 0],
	[eiii, int(bar/8/eiii), space, 0],
	[cii, int(bar/8/cii), space, 0],
	[ciii, int(bar/8/ciii), space, 0],
	[cii, int(bar/8/cii), space, 0],
	[ciii, int(bar/8/ciii), space, 0],
	[fii, int(bar/8/fii), space, 0],
	[fiii, int(bar/8/fiii), space, 0],
	[fii, int(bar/8/fii), space, 0],
	[fiii, int(bar/8/fiii), space, 0],
	[fii, int(bar/8/fii), space, 0],
	[fiii, int(bar/8/fiii), space, 0],
	[gii, int(bar/8/gii), space, 0],
	[aii, int(bar/8/aii), space, 0],
	[bii, int(bar/8/bii), space, 0],
	[ei, int(bar/8/ei), space, ((bar/8)*1.1)],
	[ei, int(bar/8/ei), space, ((bar/8)*1.1)],
	[ei, int(bar/8/ei), space, 0],
	[fii, int(bar/8/fii), space, 0],
	[ei, int(bar/8/ei), space, 0],
	[di, int(bar/8/di), space, 0],
	[aii, int(bar/8/aii), space, ((bar/8)*1.1)],
	[aii, int(bar/8/aii), space, 0],
	[di, int(bar/8/di), space, 0],
	[eii, int(bar/8/eii), space, 0],
	[eii, int(bar/8/eii), space, ((bar/8)*1.1)],
	[gii, int(bar/8/gii), space, 0],
	[giii, int(bar/8/giii), space, ((bar/8)*1.1)],
	[giii, int(bar/8/giii), space, ((bar/8)*1.1)],
	[eiii, int(bar/8/eiii), space, ((bar/8)*1.1)],
	[giii, int(bar/8/giii), space, 0],
	[fii, int(bar/8/fii), space, 0],
	[fiii, int(bar/8/fiii), space, 0],
	[fii, int(bar/8/fii), space, 0],
	[fiii, int(bar/8/fiii), space, 0],
	[fii, int(bar/2/fii), space, 0],
	[cii, int(bar/8/cii), space, 0],
	[ciii, int(bar/8/ciii), space, 0],
	[cii, int(bar/8/cii), space, 0],
	[ciii, int(bar/8/ciii), space, 0],
	[cii, int(bar/8/cii), space, 0],
	[ciii, int(bar/8/ciii), space, 0],
	[cii, int(bar/8/cii), space, 0],
	[ciii, int(bar/8/ciii), space, 0],
	[fii, int(bar/8/fii), space, 0],
	[fiii, int(bar/8/fiii), space, 0],
	[fii, int(bar/8/fii), space, 0],
	[fiii, int(bar/8/fiii), space, 0],
	[fii, int(bar/8/fii), space, 0],
	[fiii, int(bar/8/fiii), space, 0],
	[fii, int(bar/8/fii), space, 0],
	[fiii, int(bar/8/fiii), space, 0],
	[eii, int(bar/8/eii), space, 0],
	[eiii, int(bar/8/eiii), space, 0],
	[eii, int(bar/8/eii), space, 0],
	[eiii, int(bar/8/eiii), space, 0],
	[cii, int(bar/8/cii), space, 0],
	[ciii, int(bar/8/ciii), space, 0],
	[cii, int(bar/8/cii), space, 0],
	[ciii, int(bar/8/ciii), space, 0],
	[fii, int(bar/8/fii), space, 0],
	[fiii, int(bar/8/fiii), space, 0],
	[fii, int(bar/8/fii), space, 0],
	[fiii, int(bar/8/fiii), space, 0],
	[fii, int(bar/8/fii), space, 0],
	[fiii, int(bar/8/fiii), space, 0],
	[gii, int(bar/8/gii), space, 0],
	[aii, int(bar/8/aii), space, 0],
	[bii, int(bar/8/bii), space, 0],
	[ei, int(bar/8/ei), space, ((bar/8)*1.1)],
	[ei, int(bar/8/ei), space, ((bar/8)*1.1)],
	[ei, int(bar/8/ei), space, 0],
	[fii, int(bar/8/fii), space, 0],
	[ei, int(bar/8/ei), space, 0],
	[di, int(bar/8/di), space, 0],
	[aii, int(bar/8/aii), space, ((bar/8)*1.1)],
	[aii, int(bar/8/aii), space, 0],
	[di, int(bar/8/di), space, 0],
	[eii, int(bar/8/eii), space, 0],
	[eii, int(bar/8/eii), space, ((bar/8)*1.1)],
	[gii, int(bar/8/gii), space, 0],
	[giii, int(bar/8/giii), space, ((bar/8)*1.1)],
	[giii, int(bar/8/giii), space, ((bar/8)*1.1)],
	[eiii, int(bar/8/eiii), space, ((bar/8)*1.1)],
	[giii, int(bar/8/giii), space, 0],
	[fii, int(bar/8/fii), space, 0],
	[fiii, int(bar/8/fiii), space, 0],
	[fii, int(bar/8/fii), space, 0],
	[fiii, int(bar/8/fiii), space, 0],
	[fii, int(bar/2/fii), space, 0]]

layer_one = tetris
layer_two = tetris_two
boolean_one = 0
boolean_two = 0
note_one = layer_one[one]
note_two = layer_two[two]
wait_one = note_one[0]
wait_two = note_two[0]
repeat_one = note_one[1]
repeat_two = note_two[1]

while True:
	if wait_one > wait_two:
		wiringpi.digitalWrite(4, boolean_two)
		boolean_two = 1 - boolean_two
		wiringpi.digitalWrite(7,0)
		wiringpi.digitalWrite(5, 0)
		sleep(wait_two)
		wiringpi.digitalWrite(5, 1)
		wait_one -= wait_two
		wait_two = note_two[1]
		repeat_two -= 1
	if wait_one < wait_two:
		wiringpi.digitalWrite(6, boolean_one)
		boolean_one = 1 - boolean_one
		wiringpi.digitalWrite(7,0)
		wiringpi.digitalWrite(5, 0)
		sleep(wait_one)
		wiringpi.digitalWrite(7, 1)
		wait_two -= wait_one
		wait_one = note_one[1]
		repeat_one -= 1
	if repeat_one == 0:
		one += 1
		gap = ((note_one[2]*note_one[1])*0.1)
		note_one = layer_one[one]
		wait_one = note_one[1] + gap + note_one[0]
		repeat_one = note_one[2]
	if repeat_two == 0:
		two += 1
		gap = ((note_two[2]*note_two[1])*0.1)
		note_two = layer_two[two]
		wait_two = note_two[1] + gap + note_two[0]
		repeat_two = note_two[1]
