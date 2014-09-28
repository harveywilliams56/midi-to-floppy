import binascii as tool #importing module containing hex conversion
class midi_decoder:
	def __init__(self):
		piece = open('Pirates.mid')
		data = piece.read()
		self.hexi = tool.hexlify(data)
		#self.hexi = '4d54726b000000148000ff0202000000f70203f700f001f700ff2f004d54726b000000148000ff0202121100f70205f700f001f700ff2f00'


	def search(self,item): ##class for finding 'item' in text and returning cursor position
		positions = []
		found = 0
		cursor_position = 0
		item.split ##turns str 'item' into a list of its seperate characters
		for letter in self.hexi:
			cursor_position += 1
			if letter != item[found]:
				found = 0
			if letter == item[found]:
				found += 1
			if found == len(item):
				positions += [cursor_position]
				found = 0
		return positions


			

	def define_tracks():
		tracks = self.search('4d54726b')
		end_tracks = self.search('ff2f00')
		for cp in end_tracks:
			vlv = find_continuation(cp)
		if len(end_tracks) != len(tracks):
			end_tracks = end_tracks + [len(self.hexi)-1]
		
	def run(self):
		if True:
			print self.hexi
			#self.remove_meta()
			events = []
			tracks = self.search('4d54726b')
			end_tracks = self.search('ff2f00')
			if len(tracks) != len(end_tracks):
				end_tracks = end_tracks + [len(self.hexi)-1]
			for track in range(0,len(tracks)):
				print "track", track
				event =  [self.find_events(tracks[track],end_tracks[0])] 
				print event
				events += event
				tracks = self.search('4d54726b')
				#print "tracks",tracks
				end_tracks = self.search('ff2f00')
				#print "end_tracks",end_tracks, len(end_tracks)
			print events

	def return_data(self,start,end):
		letters = []
		for letter in self.hexi:
			start -= 1
			end -= 1
			if start <= 0 and end >= 0:
				letters += letter
			if end == 0:
				return "".join(letters)
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
			event_whole = [[self.return_data(TrackStart+9, cp -1)], [event]]
			events += [event_whole]
			before = len(self.hexi)
			self.hexi = self.return_data(0, TrackStart+8)+self.return_data(cp + len(event), len(self.hexi))
			after = len(self.hexi)
			TrackEnd -= (before-after)
			print event_whole
			
	def find_notes(self,TrackStart,TrackEnd):
		notes = []
		cp = TrackStart+9
		while True:
			value = self.return_data(cp,cp+1)
			if cp >= TrackEnd or cp == 'null':
				return notes
			if value == '9':
				note = self.return_data(cp+2, cp+4)
				notes += [note]
			cp += 6	
		
		
		
		
		
if __name__ == '__main__':
	midi_decoder().run()
