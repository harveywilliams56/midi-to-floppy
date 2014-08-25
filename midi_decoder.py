import binascii as tool #importing module containing hex conversion
class midi_decoder:
	def __init__(self):
		piece = open('minimal.mid')
		data = piece.read()
		self.hexi = tool.hexlify(data)


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


	def clean_data(self):
		events = self.search('ff')
		remove_event = []
		for event in events:
			check = "".join(self.return_data(event+1,event+2))
			if check == 'f2':
				pass
			else:
				pass
			
	def run(self):
		if True:
			print self.hexi
			#self.clean_data()
			events = []
			tracks = self.search('4d54726b')
			end_tracks = self.search('ff2f00')
			extra = tracks + [len(self.hexi)]
			for track in range(0,len(tracks)):
				print track
				events += [self.find_events(tracks[track],end_tracks[track])]
				print events

	
	def return_data(self,start,end):
		letters = []
		for letter in self.hexi:
			start -= 1
			end -= 1
			if start <= 0 and end >= 0:
				letters += letter
			if end == 0:
				return letters
	def find_continuation(self,cp):
			continuation = True
			vlv = 0
			while continuation:
				raw_data = self.return_data(cp, cp + 1)
				value_str = "".join(raw_data)
				value = int(value_str, 16)
				if value >= 128:
					print raw_data
					vlv += 1
					cp += 2 
				else:
					return vlv

	def find_events(self,TrackStart,TrackEnd):
		events = []
		cp = TrackStart + 9
		while True:
			if cp >= TrackEnd:
				events.pop() ##removes last event, which is an end track
				return events
			vlv = self.find_continuation(cp)
			length = (vlv*2)+7
			events += ["".join(self.return_data(cp, cp + length))]
			cp += length + 1
			vlv = 0
			print events
			
	def find_notes(self,TrackStart,TrackEnd):
		notes = []
		cp = TrackStart+8
		while True:
			value = self.return_data(cp,cp+1)
			if cp >= TrackEnd or cp == 'null':
				return notes
			if value == '9':
				print cp
				note = self.return_data(cp+2, cp+4)
				notes += [note]
			cp += 6	
		
		
		
		
		
if __name__ == '__main__':
	midi_decoder().run()
