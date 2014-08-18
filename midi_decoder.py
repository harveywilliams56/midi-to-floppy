import binascii as tool #importing module containing hex conversion
class midi_decoder:
	def __init__(self):
		piece = open('minimal.mid')
		data = piece.read()
		self.hexi = tool.hexlify(data)
		self.MTrck = '4d54726b'
		self.notes = []
	def search(self,data,item,cp): ##class for finding 'item' in text and returning cursor position
		found = 0
		item.split ##turns str 'item' into a list of its seperate characters
		cursor_position = cp
		for letter in data:
			if found == len(item)-1:
				return cursor_position
			if letter != item[found]:
				found = 0
			if letter == item[found]:
				found += 1
			cursor_position += 1
	def run(self):
		result = self.search(self.hexi,self.MTrck,0)
		print result
		##print self.hexi
		
if __name__ == '__main__':
	midi_decoder().run()
