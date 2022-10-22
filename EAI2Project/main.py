from modim_classes import CleanScreen
import sys
from scripts import Sonar, Dialogue,Gestures
import math
import pepper_cmd
sys.path.append('tablet/scripts')

dialogue = Dialogue()

def main_run():
    interaction = dialogue.start_interaction()
    if (interaction):
        dialogue.say("Do you need indications or do you want to play?")
        answer = dialogue.listen()
        if answer == "Indications":
            dialogue.say("Perfect! Where do you have to go?")
            answer = dialogue.listen() #AGGIUNGERE VOCABOLARIO CON TUTTE LE DESTINAZIONI POSSIBILI 
            dialogue.say("Ok, well now using the tablet press on the cells in which are obstacles, if None press the Ok button")
            #APRI INTERAZIONE CON MAPPA SUL TABLET 
        else:
            dialogue.say("Perfect! Let's play a memory game on the tablet")
            #APRI INTERAZIONE CON GIOCO SU TABLET
    return
    
if __name__ == "__main__":

	print("Starting monitor, to stop robot send KeyboardInterrupt signal.")
	while True:
		try:
			sonar = Sonar()
			check = sonar.listen(personHere=False)
			if check == 'front':
				executor_status = main_run()
				if executor_status == -1:
					print("Interaction with user completed successfully.")
		except KeyboardInterrupt:
			print("Interrupted")
			CleanScreen()
			sys.exit(0)