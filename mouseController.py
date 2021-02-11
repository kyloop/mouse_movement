import subprocess, sys, time, os

def check_package():
	reqs = subprocess.check_output([sys.executable, '-m', 'pip','freeze'])
	installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

	for package in installed_packages:
		print
		if "pyautogui" in package.lower():
			print("Package: ",package, "is found")
			print("Done Checking Package !!!")
			import pyautogui as mouse
			#return()
		

	os.system('curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py')
	subprocess.check_call([sys.executable, '-m', 'pip', 'install','--upgrade','pip'])		
	subprocess.check_call([sys.executable, '-m', 'pip', 'install','pyautogui'])
	#import pyautogui as mouse
	return()

def mouse_movement(sec):
	while True:
		size = mouse.size()
		mouse.moveTo(size.width/4, size.width/4, duration=1)
		time.sleep(sec)
		mouse.moveTo(size.width/2, size.width/2, duration=1)
		time.sleep(sec)
	



#print(installed_packages)

if __name__ == "__main__":

	check_package()
	import pyautogui as mouse
	mouse_movement(60)
