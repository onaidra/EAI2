import sys
from modim_interaction import *
from pddl2txt import *
from scripts_ import *



vocab = ['banca', 'fisiologia', 'botanica', 'genetica', 'medicina', 'obitorio', 'scienze statistiche', 'scienze politiche', 'ciao',
         'lettere e filosofia', 'scienze umanistiche', 'laboratori chimica', 'fisica', 'chimica', 'chimica farmaceutica', 'geologia',
         'giurisprudenza', 'matematica', 'igiene', 'zoologia', 'neurologia', 'scienze dello spettacolo', 'ortopedia']

dialogue = Dialogue()

def main_run():
    
    interaction = start_interaction(dialogue)
    if (interaction):
        dialogue.say("Do you need indications or do you want to play?")
        rightanswer=False
        while(not rightanswer):
            answer = dialogue.listen()
            if answer == "Indications":
                rightanswer = True
                dialogue.say("Perfect! Where do you have to go?")
                goal = dialogue.listen(vocabulary=vocab)
                if (goal not in vocab):
                    find = False
                    while(not find):
                        dialogue.say("Sorry I didn't understand, can you repeat please?")
                        goal = dialogue.listen(vocabulary=vocab)
                        if (str(goal) in vocab):
                            find=True
                """f = open("../utils/goal.txt","w")
                f.write(answer)
                f.close()"""
                dialogue.say("Ok, now using the tablet press on the cells in which are obstacles, if None press the Ok button")
                #APRI INTERAZIONE CON MAPPA SUL TABLET
                TabletInteraction("i1")
                dialogue.say("please wait, i'm computing the best path for you")
                with open("../utils/obs.out","r") as f:
                    obs = f.readline()
                    f.close()
                    obs = obs.strip("\n")
                
                img_p = create_problem(obs,goal)
                with open("../actions/quit","r") as f:
                    lines = f.readlines()
                    f.close()
                    lines[1] = "<*,*,*,*>: img/"+img_p+"\n"
                with open("../actions/quit","w") as f:
                    for line in lines:
                        f.write(line)
                    f.close()
                dialogue.say("I'm ready! Look at my tablet to see your path")
                TabletInteraction("i3")
                dialogue.say("I hope it helped, see you next time bye!")
                Gestures.sayhi()
            elif answer=="Play":
                rightanswer = True
                dialogue.say("Perfect! Let's play a memory game on the tablet")
                #APRI INTERAZIONE CON GIOCO SU TABLET
                TabletInteraction("i2")
            else:
                dialogue.say("Sorry, I didn't understand")
    return
    
if __name__ == "__main__":

	print("Starting monitor, to stop robot send KeyboardInterrupt signal.")
	while True:
		try:
			sonar = Sonar()
			check = sonar.listen(personHere=False)
			if check == 'front':
				main_run()
		except KeyboardInterrupt:
			print("Interrupted")
			Reset()
			sys.exit(0)
