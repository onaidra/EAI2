from modim_classes import CleanScreen
import sys
from global_executor import run_executor
from scripts import Sonar, Dialogue,Touch
import math
import pepper_cmd
sys.path.append('tablet/scripts')


if __name__ == "__main__":
	"""
	print("Starting monitor, to stop robot send KeyboardInterrupt signal.")
	while True:
		try:
			sonar = Sonar()
			location = sonar.listen(personHere=False)
			if location == 'front':
				executor_status = run_executor()
				if executor_status == -1:
					print("Interaction with user completed successfully.")
			else:
				dialogue = Dialogue()
				dialogue.say(
					"Who is behind me? If you came to me, come please in front so I could see you.")
				print("Person was detected by rear sonar.")
		except KeyboardInterrupt:
			print("Interrupted")
			CleanScreen()
			sys.exit(0)
	"""
	touch = Touch()
	a=math.pi/180
	touch.change_pose([7, 10, 11],
							[a*50, a*60, -a*90],
							pepper_cmd.robot.getPosture(),
							0.1)