# A simple python voice recorder
import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
# Initialize the recognizer
r = sr.Recognizer()
# Exception handling to handle
# exceptions at the runtime
print("Say something....\n\n\n")
try:
		
    # use the microphone as source for input.
	with sr.Microphone() as source2:
			
	# wait for a second to let the recognizer
	# adjust the energy threshold based on
	# the surrounding noise level
		r.adjust_for_ambient_noise(source2, duration=0.2)
			
	#listens for the user's input
		audio2 = r.listen(source2)
			
        # Using google to recognize audio
		MyText = r.recognize_google(audio2)
		MyText = MyText.lower()

		print(MyText)
		engine.say(MyText)
		engine.runAndWait()
			
except sr.RequestError as e:
	print("Could not request results; {0}".format(e))
		
except sr.UnknownValueError:
	print("Unknown error occured")
