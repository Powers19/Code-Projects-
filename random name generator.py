import tkinter #the standard GUI library for python, provides a fast way and easy way to create a GUI
#tkinter can also provide many different controls such as text boxes and buttons that can used in a GUI
import random #this will pick the names below in a random way 

names = ['Feargus', 'Sam', 'Tom', 'Ben', 'Noah', 'Stewart', 'James', 'Andrew', 'Will', 'Dan', 'Callum', 'Joe', 'Anthony', 'Charlie','Nick']
#these show all the names that the 'generator can pick from in a list, these can be edited to add or change the names

def pickName(): #this is the function that will pick and show a name from the list
    nameLabel.configure(text=random.choice(names))
    

root = tkinter.Tk()#this creates a GUI window
root.title("Name Picker") #this sets the title for the GUI window
root.geometry("300x100")#this sets the size of the window

#this adds a label to display a name
nameLabel = tkinter.Label(root, text="", font=('Gothic', 32), fg=('blue'))#the font and size can  change for example the 'Helvetica' can be a size 16 or 32 etc, while you can also have other fonts in python like times at size 24
nameLabel.pack() #'bg' is defined next to the font and this is the background colour displayed behind the label, but this can be changed as i have done to 'fg' which justs sets the colour of the lettering and not of the whole of the shape like 'bg' does

#within in the tkinter button the colour of the text and the button can be displayed through the 'activebackground' and 'activeforeground', the 'activebackground' is the background colour while the 'activeforeground' is the colour of the text. I have gone with red text and a black background as they contrast well but that can all be changed. 
pickButton = tkinter.Button(text="Pick your names!", command=pickName, activebackground = 'black', activeforeground = 'red') #this adds the button to the GUI called 'pick away'
pickButton.pack()


root.mainloop()#this starts the GUI
