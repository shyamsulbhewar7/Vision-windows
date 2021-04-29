from vision import Controls
import threading

if __name__ == "__main__":
	cnt = Controls()
	x = threading.Thread(target=cnt.Key_Controls, args=())
	x.start()
	x.join()