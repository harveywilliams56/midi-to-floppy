import sys
#import wiringpi2 as wiringpi
#wiringpi.wiringPiSetup()
#wiringpi.pinMode(6,1)
#wiringpi.pinMode(7,1)
#wiringpi.pinMode(4,1)
#wiringpi.pinMode(5,1)
from time import sleep
import binascii as tool #importing module containing hex conversion
class midi_decoder:
	def __init__(self):
		file = 'test.mid'
		piece = open(file)
		data = piece.read()
		self.hexi = tool.hexlify(data)
		self.deltatoreal = 0
		self.notes = [16.35, 17.32, 18.35, 19.45, 20.60, 21.83, 23.12, 24.50, 25.96, 27.50, 29.14, 30.87]


	def search(self,item): ##class for finding 'item' in text and returning cursor position
		skip = 0
		positions = []
		while self.hexi.find(item, skip) != -1:
			skip = self.hexi.find(item, skip) + len(item)
			positions += [skip]
		return positions

	def time_division(self):
		header = self.search('4d546864')
		time_type = int(self.return_data(header[0]+17,header[0]+17), 16)
		if time_type < 8:
			tempo = self.search('ff5103')
			print tempo
			if len(tempo) == 1:
				tempo = tempo[0]
				bpms = self.return_data(tempo+1, tempo+6)
				print 'bpms', bpms
				bpms = int(bpms, 16)
			else:
				bpms = 500000
			debug = self.return_data(header[0]+17, header[0]+20)
			print 'debug', debug, 'bpms', bpms
			self.deltatoreal = int(debug, 16) * 1000000 / bpms
		else:
			frames = int(self.return_data(header[0]+17, header[0]+18,16)) - 128 
			if frames == 29:
				frames = 29.97
			ticks_per_frame = int(self.return_data(header[0]+19, header[0]+20), 16)
			self.deltatoreal = frames * ticks_per_frame
			
		print time_type
		print 'time div. ',self.deltatoreal
			
	def run(self):
		playable = []
		self.time_division()
		events = []
		tracks = self.search('4d54726b')
		end_tracks = self.search('ff2f00')
		if len(tracks) != len(end_tracks):
			print 'whatsup'
			#end_tracks = end_tracks + [len(self.hexi)-1]
		for track in range(0,len(tracks)):
			print "track", track
			event =  self.find_events(tracks[track],end_tracks[0]) 
			events += [event]
			tracks = self.search('4d54726b')
			end_tracks = self.search('ff2f00')
		for track in events:
			deltas = self.find_delta(track)
			notes =  self.find_notes(deltas)
			final = self.calculate_loops(notes)
			playable += [final]
		print playable
		
	def return_data(self,start,end):
		if start != 0:
			return self.hexi[start-1:end]
		else:
			return self.hexi[start:end]
			

	def find_continuation(self,cp):
			continuation = True
			vlv = 0
			while continuation:
				data = self.return_data(cp, cp + 1)
				value = int(data, 16)
				if value >= 128:
					vlv += 1
					cp += 2 
				else:
					return vlv


	def meta(self,cp, extra):
		cont = self.find_continuation(cp+4)
		value_str = self.return_data(cp+4,cp +(2*cont)+5)
		length = int(value_str, 16)*2
		return self.return_data(cp, cp + len(value_str) + length + 3)


	def sys(self,cp, extra):
		cont = self.find_continuation(cp+2)
		value_str = self.return_data(cp+2,cp +(2*cont)+3)
		length = int(value_str, 16)*2
		return self.return_data(cp, cp + len(value_str) + length + 1)
			

	def find_events(self,TrackStart,TrackEnd):
		events = []
		while True:
			event = ''
			cp = TrackStart + 9
			if cp >= TrackEnd:
				#events.pop() ##removes last event, which is an end track
				return events
			vlv = self.find_continuation(cp)
			length = (2*(vlv+1))
			cp = cp + length 
			check = self.return_data(cp, cp+1)
			if check == 'ff':
				event = self.meta(cp,2)
			elif check == 'f7':
				event = self.sys(cp,0)
			elif check == 'f0':
				event = self.sys(cp,0)
			else:
				check = self.return_data(cp, cp)
				if check == 'c':
					event = self.return_data(cp, cp + 3)
				elif check == 'd':
					event = self.return_data(cp, cp + 3)
				else:
					event = self.return_data(cp, cp + 5)
			event_whole = [self.return_data(TrackStart+9, cp -1), event]
			events += [event_whole]
			before = len(self.hexi)
			self.hexi = self.return_data(0, TrackStart+8)+self.return_data(cp + len(event), len(self.hexi))
			after = len(self.hexi)
			TrackEnd -= (before-after)
			

	def find_delta(self, track):
		notes = []
		pause = 0
		length = 0
		search = False
		for event in track:
			delta = int(event[0], 16)
			note = event[1]
			for extra in range(0,(len(event[0])-2)/2+1):
				if extra != 0:
					delta = delta - 2**(extra*8+7)
			if search == True:
				length += delta
				if (note[0] == '9' and note[4:6] == '00') or note[0] == '8':
					if note[2:4] == pitch:
						pause = float(pause)/float(self.deltatoreal)
						notes += [[pause, pitch, length]]
						length = 0
						pause = 0
						search = False
			if search != True:
				if note[0] == '9'and note[4:6] != '00':
					pitch = note[2:4]
					search = True
					pause = delta
				
		return notes
				
				
	def find_notes(self, track):
		new_track = []
		for event in track:
			multiple = 0
			number = int(event[1], 16)-12
			while number > 11:
				number -= 12
				multiple += 2
			note = 1/(self.notes[number] * multiple)
			event[1] = note
			new_track += [event]
		return new_track

	def calculate_loops(self, track):		
		new_track = []
		for event in track:
			repetitions = event[2]/event[1]
			event[2] = repetitions
			new_track += [event]
		return new_track
	def play(self, tracks):
		layer_one = tracks[0]
		layer_two = tracks[1]
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
		
if __name__ == '__main__':
	midi_decoder().run()
