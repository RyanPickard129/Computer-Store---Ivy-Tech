#imports tkinter
import tkinter as tk

#imports Python Imaging Library for the images
from PIL import Image, ImageTk

#creates the primary window
window = tk.Tk()
window.title("Computer Store")
window.geometry("400x470")

#these variables are just being placed in the global namespace
#avoids a lot of errors later on
#they are updated inside functions later
window2 = None
img = None
back_button = None
comp_label = None
alt_text = None
purchase_button = None
question = None

#replit flips out about these even though they PREVENT errors, not cause them


#defines the clear window function
def clear_window():
  #this removes all the stuff from the main window to make it ready to display an image
  office_comp_button.pack_forget()
  pro_comp_button.pack_forget()
  creator_comp_button.pack_forget()
  super_comp_button.pack_forget()
  select.pack_forget()


#this function gets the requested image ready to be displayed
def prepare_image(image):
  #basically it just finds the file and stores the image in a variable
  #this is one of those "None" variables from earlier
  global img
  #loads the image from the file
  load = Image.open(image)
  #renders the image
  render = ImageTk.PhotoImage(load)
  #now puts it into a tkinter variable
  img = tk.Label(image=render)
  #returns the image ready to be displayed to the world
  img.image = render
  return img.image


#this function makes window 2 appear
def summon_window2(comp_type):
  #"none" variable from earlier
  global window2
  #"attaches" window 2 to window 1, making it a secondary window instead of primary
  window2 = tk.Toplevel(window)
  #sets the window up
  window2.title(comp_type)
  window2.geometry("350x350")


#this function is called when the user clicks the "back" button
def back():
  #gets rid of window 2
  window2.destroy()
  #gets rid of the image from window 1
  img.pack_forget()
  #gets rid of the back button
  back_button.pack_forget()
  #gets rid of the "You selected (computer) label"
  comp_label.pack_forget()
  #gets rid of the image alternate text
  alt_text.pack_forget()
  #brings back "select a computer"
  select.pack()
  #brings back all the buttons for each computer
  office_comp_button.pack()
  pro_comp_button.pack()
  creator_comp_button.pack()
  super_comp_button.pack()


#this function is called when the user clicks the "purchase" button
def purchase():
  #gets rid of the purchase button
  purchase_button.pack_forget()
  #gets rid of the "would you like to purchase this computer?" question"
  question.pack_forget()
  #thanks the user for their purchase
  thank_you = tk.Label(window2, text="Thank you for your purchase!")
  thank_you.pack()
  #assures the impatient user that their order will ship soon
  shipping = tk.Label(window2, text="Your order will be shipped soon!")
  shipping.pack()
  #makes a second back button appear
  back_button = tk.Button(window2, text="Back", command=back)
  back_button.pack()


#this function is only called when the user clicks the "purchase" button on the super computer
def purchase_super_computer():
  #gets rid of the purchase button
  purchase_button.pack_forget()
  #gets rid of the "would you like to purchase this computer?" question"
  question.pack_forget()
  #thanks the user for their purchase
  thank_you = tk.Label(window2, text="Thank you for your purchase!")
  thank_you.pack()
  #tells the impatient user that they actually have to pick this one up
  shipping = tk.Label(window2, text="Your order will be NOT shipped soon!")
  """
  The super computer in this program is the one that was recently sold at auction.
  And no, shipping was NOT included.
  """
  shipping.pack()
  come_get_it = tk.Label(window2,
                         text="Come to Cheyenne to get it, good luck.")
  come_get_it.pack()
  #brings the second back button up
  back_button = tk.Button(window2, text="Back", command=back)
  back_button.pack()


#this function is called when the user clicks the "office computer" button
def office_comp():
  #calls the clear window function
  clear_window()
  #one of the "none" variables from earlier
  global comp_label
  #brings up the label telling the user what they selected
  comp_label = tk.Label(text="You have selected the Standard Office Computer")
  comp_label.pack()
  #brings up the image
  img.image = prepare_image("office_computer.jpg")
  img.pack()
  #one of the "none" variables from earlier
  global alt_text
  #alternate text for the image is brought up
  alt_text = tk.Label(text="This is an image of the standard office computer")
  alt_text.pack()
  #one of the "none" variables from earlier
  global back_button
  #brings up the back button
  back_button = tk.Button(master=window, text="Back", command=back)
  back_button.pack()
  #brings up window 2
  summon_window2("Office Computer")
  #tells the user the price
  price = tk.Label(window2, text="This computer costs $500.")
  price.pack()
  #informs the user on all the specs
  specs_label = tk.Label(window2, text="Primary Specs:")
  specs_label.pack()
  cpu_specs = tk.Label(window2, text="CPU: Intel Core i5-12400")
  cpu_specs.pack()
  ram_specs = tk.Label(window2, text="RAM: 8GB, 2666 MHz")
  ram_specs.pack()
  storage_specs = tk.Label(window2, text="Storage: 500GB HDD")
  storage_specs.pack()
  graphics_specs = tk.Label(window2, text="Graphics: Intel UHD Graphics 630")
  graphics_specs.pack()
  #tells the user what is included with the computer
  includes_label = tk.Label(window2, text="Includes:")
  includes_label.pack()
  monitor = tk.Label(window2, text="1080p, 60Hz Monitor")
  monitor.pack()
  keyboard = tk.Label(window2, text="Wireless Keyboard")
  keyboard.pack()
  mouse = tk.Label(window2, text="Wired Mouse")
  mouse.pack()
  #one of the "none" variables from earlier
  global question
  #brings up the question
  question = tk.Label(window2,
                      text="Would you like to purchase this computer?")
  question.pack()
  #one of the "none" variables from earlier
  global purchase_button
  #brings up the purchase button
  purchase_button = tk.Button(window2, text="Purchase", command=purchase)
  purchase_button.pack()


#this code is essentially all the same as the office computer code, except for the specs and the image
#please refer to the comments in the previous function
def pro_comp():
  clear_window()
  global comp_label
  comp_label = tk.Label(text="You have selected the Professional Computer")
  comp_label.pack()
  img.image = prepare_image("pro_computer.jpg")
  img.pack()
  global alt_text
  alt_text = tk.Label(text="This is an image of the professional computer")
  alt_text.pack()
  global back_button
  back_button = tk.Button(master=window, text="Back", command=back)
  back_button.pack()
  summon_window2("Professional Computer")
  price = tk.Label(window2, text="This computer costs $800.")
  price.pack()
  specs_label = tk.Label(window2, text="Primary Specs:")
  specs_label.pack()
  cpu_specs = tk.Label(window2, text="CPU: Intel Core i7-13700K")
  cpu_specs.pack()
  ram_specs = tk.Label(window2, text="RAM: 8GB, 2300 MHz")
  ram_specs.pack()
  storage_specs = tk.Label(window2, text="Storage: 1TB HDD")
  storage_specs.pack()
  graphics_specs = tk.Label(window2, text="Graphics: GeForce GTX 1650")
  graphics_specs.pack()
  includes_label = tk.Label(window2, text="Includes:")
  includes_label.pack()
  monitor = tk.Label(window2, text="1080p, 60Hz Monitor")
  monitor.pack()
  keyboard = tk.Label(window2, text="Wireless Keyboard")
  keyboard.pack()
  mouse = tk.Label(window2, text="Wireless Mouse")
  mouse.pack()
  global question
  question = tk.Label(window2,
                      text="Would you like to purchase this computer?")
  question.pack()
  global purchase_button
  purchase_button = tk.Button(window2, text="Purchase", command=purchase)
  purchase_button.pack()


  #this code is essentially all the same as the office computer code, except for the specs and the image
  #please refer to the comments in the that function
def creator_comp():
  clear_window()
  global comp_label
  comp_label = tk.Label(text="You have selected the Creator Computer")
  comp_label.pack()
  img.image = prepare_image("creator_computer.jpg")
  img.pack()
  global alt_text
  alt_text = tk.Label(text="This is an image of the creator computer")
  alt_text.pack()
  global back_button
  back_button = tk.Button(master=window, text="Back", command=back)
  back_button.pack()
  summon_window2("Creator Computer")
  price = tk.Label(window2, text="This computer costs $1500.")
  price.pack()
  specs_label = tk.Label(window2, text="Primary Specs:")
  specs_label.pack()
  cpu_specs = tk.Label(window2, text="CPU: Intel Core i9-14900K")
  cpu_specs.pack()
  ram_specs = tk.Label(window2, text="RAM: 16GB, 3200 MHz")
  ram_specs.pack()
  storage_specs = tk.Label(window2, text="Storage: 1TB SSD")
  storage_specs.pack()
  graphics_specs = tk.Label(window2, text="Graphics: GeForce RTX 3090")
  graphics_specs.pack()
  includes_label = tk.Label(window2, text="Includes:")
  includes_label.pack()
  monitor = tk.Label(window2, text="1080p, 144Hz Monitor")
  monitor.pack()
  keyboard = tk.Label(window2, text="Wireless Keyboard")
  keyboard.pack()
  mouse = tk.Label(window2, text="Wireless Mouse")
  mouse.pack()
  global question
  question = tk.Label(window2,
                      text="Would you like to purchase this computer?")
  question.pack()
  global purchase_button
  purchase_button = tk.Button(window2, text="Purchase", command=purchase)
  purchase_button.pack()


  #this code is essentially all the same as the office computer code, except for the specs and the image
  #please refer to the comments in the that function
def super_comp():
  clear_window()
  global comp_label
  comp_label = tk.Label(text="You have selected the Super Computer")
  comp_label.pack()
  img.image = prepare_image("super_computer.jpg")
  img.pack()
  global alt_text
  alt_text = tk.Label(text="This is an image of the super computer")
  alt_text.pack()
  global back_button
  back_button = tk.Button(master=window, text="Back", command=back)
  back_button.pack()
  summon_window2("Super Computer")
  price = tk.Label(window2, text="This computer costs $480,000.")
  price.pack()
  specs_label = tk.Label(window2, text="Primary Specs:")
  specs_label.pack()
  cpu_specs = tk.Label(window2, text="CPUs: 8,064 Intel E5-2697v4 CPUs")
  cpu_specs.pack()
  ram_specs = tk.Label(window2, text="RAM: 4096GB")
  ram_specs.pack()
  storage_specs = tk.Label(window2, text="Storage: 32 petabytes")
  storage_specs.pack()
  graphics_specs = tk.Label(window2, text="Graphics: Definitely powerful")
  graphics_specs.pack()
  includes_label = tk.Label(window2, text="Includes:")
  includes_label.pack()
  monitor = tk.Label(window2, text="Literally nothing")
  monitor.pack()
  keyboard = tk.Label(window2, text="Does not include shipping")
  keyboard.pack()
  mouse = tk.Label(window2, text="Good luck!")
  mouse.pack()
  global question
  question = tk.Label(window2,
                      text="Would you like to purchase this computer?")
  question.pack()
  global purchase_button
  #this is slightly different though because it calls a different function
  purchase_button = tk.Button(window2,
                              text="Purchase",
                              command=purchase_super_computer)
  purchase_button.pack()


#this is for the main window. asks the user to select a computer
select = tk.Label(text="Please select a computer")
select.pack()

#creates the office computer button
office_comp_button = tk.Button(text="Standard Office Computer",
                               command=office_comp)
office_comp_button.pack()

#creates the professional computer button
pro_comp_button = tk.Button(text="Professional Computer", command=pro_comp)
pro_comp_button.pack()

#creates the creator computer button
creator_comp_button = tk.Button(text="Creator Computer", command=creator_comp)
creator_comp_button.pack()

#creates the super computer button
super_comp_button = tk.Button(text="SUPER COMPUTER!!!", command=super_comp)
super_comp_button.pack()

#runs the program!git init
tk.mainloop()
