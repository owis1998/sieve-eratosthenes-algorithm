from tkinter import *
from tkinter import ttk
import time

class Window(Tk):
	def __init__(self):
		super().__init__()
		super().title('sieve eartosthenes')

		self.top_frame = Frame(master = self)
		self.top_frame.grid(row = 0, column = 0)
		
		self.__init_plane()
		self.__init_start_button()
		
		super().mainloop()

	def __init_plane(self):
		label_number = 1
		for i in range(0, 12):
			for j in range(0,10):
				ttk.Label(
							self.top_frame, 
							text = label_number, 
							font = (None, 10), 
							background = None
						
						).grid(
								row = i, 
								column = j, 
								padx = 3, 
								pady = 3
							)
				label_number += 1	

	def __init_start_button(self):
		ttk.Button(
					master = self,
					text = 'start',
					command = self.__eartosthenes_algorithm
				
				).grid(row = 1, column = 0)

	def __eartosthenes_algorithm(self):
		ttk.Label(master = self, text = 'Loading').grid(row = 2, column = 0)
		composite = [i for i in range(2,121)]
		prime = []
		for n in composite:
			label_number = 1
			prime.append(n)
			for i in range(0, 12):
				for j in range(0,10):
					time.sleep(0.1/n)
					super().update()
					if label_number % n == 0 and label_number in composite and label_number not in prime:
						ttk.Label(
									self.top_frame, 
									text = label_number, 
									font = (None, 10), 
									background = 'green'
								
								).grid(
										row = i, 
										column = j, 
										padx = 3, 
										pady = 3
									)
						composite.remove(label_number)
					label_number += 1
			if n*n > len(composite):
				break

		ttk.Label(master = self, text = '  Done  ').grid(row = 2, column = 0)
