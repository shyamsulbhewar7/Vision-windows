import vision 
import threading
if __name__ == "__main__":
	x = threading.Thread(target=vision.Key_Controls, args=())
	x.start()
	x.join()