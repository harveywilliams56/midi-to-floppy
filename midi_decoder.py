import binascii as tool #importing module containing hex conversion
class midi_decoder:
	def __init__(self):
		piece = open('minimal.mid')
		data = piece.read()
		self.hexi = tool.hexlify(data)
		self.MTrck = '4d54726b'
		self.tracks = []


	def search(self,item,cp): ##class for finding 'item' in text and returning cursor position
		found = 0
		item.split ##turns str 'item' into a list of its seperate characters
		cursor_position = cp
		for letter in self.hexi:
			if cp == 0:
				if found == len(item)-1:
					return cursor_position
				if letter != item[found]:
					found = 0
				if letter == item[found]:
					found += 1
				cursor_position += 1
			else:
				cp -=1
		return 'null'


	def run(self):
		print self.find_tracks()


	def find_tracks(self):
		more = True
		cp = 0
		while more:
			cp = self.search(self.MTrck,cp)
			if cp == 'null':
				return self.tracks
				more = False
			else:
				 self.tracks += [cp]
		
		
		
if __name__ == '__main__':
	midi_decoder().run()
