import vision as vis
import threading

if __name__ == "__main__":
	x = threading.Thread(target=vis.Key_Controls, args=())
	x.start()
	x.join()