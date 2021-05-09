import cv2


cap = cv2.VideoCapture(0)
main_char = 0
final_text = ''
void = []
def create_list() :
	for i in range(0,100) :
		for j in range(0,100) :
			void.append(frame[i,j,2])

while (True) :
	# Capture frame-by-frame
	ret, frame = cap.read()
	frame = cv2.resize(frame, (100, 100), interpolation=cv2.INTER_LANCZOS4)
	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	create_list()

	if len(void) > 10000 :
			final_text = ''
			void = []
			create_list()
				#void = []
	#i could make a dictionnary for each char i'll make it in the next version .
	for i in range(len(void)) :
		if void[i] < 25 :
			main_char = '+'
		if void[i] < 45 and void[i] > 25 :
			main_char = 'X'
		if void[i] < 90 and void[i] > 45 :
			main_char = 'x'
		if void[i] < 120 and void[i] > 90:
			main_char = '$'
		if void[i] < 150 and void[i] > 120 :
			main_char = '&'

		if i % 100 == 0 :
			final_text += '\n'
		final_text += str(caca)
	print(final_text)
	




cap.release()
