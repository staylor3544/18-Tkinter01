import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# DONE: 1. (6 pts)
#
#   1) Create a tkinter window with the title "Form".
#
#   2) Add a label and an entry box for each of the following pieces of
#      information.
#
#       - Name
#       - Address Line 1
#       - Address Line 2
#       - City
#       - State
#       - Zip Code
#       - Phone Number
#       - Email Address
#
#   3) Add a "Submit" button at the bottom of your form.
#
#   4) Give your form a color theme by changing the colors of your widgets.
#      Also, feel free to change the sizes of the widgets as you see fit.
#
#   5) Make sure you call the window's mainloop() method so your window will
#      appear.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
window = tk.Tk()
window.title("Form")
window.configure(background="#F8DED1")

greeting_label = tk.Label(
    window,
    text = "Hello User!\nFill out my questions. Not optional.\nI will find you.",
    font = "Times 15 underline bold",
    background = "#F48F85",
    foreground = "#312773",
    width = 60,
    height = 4
)
greeting_label.configure(relief = 'ridge')
greeting_label.grid(column=1, columnspan=5, row=1, pady=5, padx=5)

frame1 = tk.Frame(window)
frame1.configure(borderwidth = 3, relief = 'sunken')
frame1.grid(column=1, row=2, pady=5, padx=5)

label1 = tk.Label(
    frame1,
    text = "I will first need your name.\nGive it to me.",
    font = "Times 12 italic bold",
    background = "#C2DDFA",
    foreground = "#D54405",
    width = 30,
    height = 2
)
label1.grid(column=1, row=2)

entry_frame1 = tk.Frame(window)
entry_frame1.configure(borderwidth = 4, relief = 'raised')
entry_frame1.grid(column=2, row=2, pady=5, padx=5)

entry1 = tk.Entry(
    entry_frame1,
    font = "Times 10 italic",
    width = 20,
)
entry1.grid(column=2, row=2)

frame2 = tk.Frame(window)
frame2.configure(borderwidth = 3, relief = 'sunken')
frame2.grid(column=1, row=3, pady=5, padx=5)

label2 = tk.Label(
    frame2,
    text = "Now your primary residence",
    font = "Times 12 italic bold",
    background = "#C2DDFA",
    foreground = "#D54405",
    width = 30,
    height = 2
)
label2.grid(column=1, row=3)

entry_frame2 = tk.Frame(window)
entry_frame2.configure(borderwidth = 4, relief = 'raised')
entry_frame2.grid(column=2, row=3, pady=5, padx=5)

entry2 = tk.Entry(
    entry_frame2,
    font = "Times 10 italic",
    width = 20,
)
entry2.grid(column=2, row=3)

frame3 = tk.Frame(window)
frame3.configure(borderwidth = 3, relief = 'sunken')
frame3.grid(column=1, row=4, pady=5, padx=5)

label3 = tk.Label(
    frame3,
    text = "Any other places you live?\nJust in case...",
    font = "Times 12 italic bold",
    background = "#C2DDFA",
    foreground = "#D54405",
    width = 30,
    height = 2
)
label3.grid(column=1, row=4)

entry_frame3 = tk.Frame(window)
entry_frame3.configure(borderwidth = 4, relief = 'raised')
entry_frame3.grid(column=2, row=4, pady=5, padx=5)

entry3 = tk.Entry(
    entry_frame3,
    font = "Times 10 italic",
    width = 20,
)
entry3.grid(column=2, row=4)

frame4 = tk.Frame(window)
frame4.configure(borderwidth = 3, relief = 'sunken')
frame4.grid(column=1, row=5, pady=5, padx=5)

label4 = tk.Label(
    frame4,
    text = "You will need to be specific about\nthe city this address is in.",
    font = "Times 12 italic bold",
    background = "#C2DDFA",
    foreground = "#D54405",
    width = 30,
    height = 2
)
label4.grid(column=1, row=5)

entry_frame4 = tk.Frame(window)
entry_frame4.configure(borderwidth = 4, relief = 'raised')
entry_frame4.grid(column=2, row=5, pady=5, padx=5)

entry4 = tk.Entry(
    entry_frame4,
    font = "Times 10 italic",
    width = 20,
)
entry4.grid(column=2, row=5)

frame5 = tk.Frame(window)
frame5.configure(borderwidth = 3, relief = 'sunken')
frame5.grid(column=4, row=2, pady=5, padx=5)

label5 = tk.Label(
    frame5,
    text = "State identification\nalso might be helpful.",
    font = "Times 12 italic bold",
    background = "#C2DDFA",
    foreground = "#D54405",
    width = 30,
    height = 2
)
label5.grid(column=4, row=2)

entry_frame5 = tk.Frame(window)
entry_frame5.configure(borderwidth = 4, relief = 'raised')
entry_frame5.grid(column=5, row=2, pady=5, padx=5)

entry5 = tk.Entry(
    entry_frame5,
    font = "Times 10 italic",
    width = 20,
)
entry5.grid(column=5, row=2)

frame6 = tk.Frame(window)
frame6.configure(borderwidth = 3, relief = 'sunken')
frame6.grid(column=4, row=3, pady=5, padx=5)

label6 = tk.Label(
    frame6,
    text = "The Zip Code for when\nI need to mail your bills.",
    font = "Times 12 italic bold",
    background = "#C2DDFA",
    foreground = "#D54405",
    width = 30,
    height = 2
)
label6.grid(column=4, row=3)

entry_frame6 = tk.Frame(window)
entry_frame6.configure(borderwidth = 4, relief = 'raised')
entry_frame6.grid(column=5, row=3, pady=5, padx=5)

entry6 = tk.Entry(
    entry_frame6,
    font = "Times 10 italic",
    width = 20,
)
entry6.grid(column=5, row=3)

frame7 = tk.Frame(window)
frame7.configure(borderwidth = 3, relief = 'sunken')
frame7.grid(column=4, row=4, pady=5, padx=5)

label7 = tk.Label(
    frame7,
    text = "For no specfic reason... your number?\n *very important",
    font = "Times 12 italic bold",
    background = "#C2DDFA",
    foreground = "#D54405",
    width = 30,
    height = 2
)
label7.grid(column=4, row=4)

entry_frame7 = tk.Frame(window)
entry_frame7.configure(borderwidth = 4, relief = 'raised')
entry_frame7.grid(column=5, row=4, pady=5, padx=5)

entry7 = tk.Entry(
    entry_frame7,
    font = "Times 10 italic",
    width = 20,
)
entry7.grid(column=5, row=4)

frame8 = tk.Frame(window)
frame8.configure(borderwidth = 3, relief = 'sunken')
frame8.grid(column=4, row=5, pady=5, padx=5)

label8 = tk.Label(
    frame8,
    text = "You will have to provide an email\nso I can send you money schemes.",
    font = "Times 12 italic bold",
    background = "#C2DDFA",
    foreground = "#D54405",
    width = 30,
    height = 2
)
label8.grid(column=4, row=5)

entry_frame8 = tk.Frame(window)
entry_frame8.configure(borderwidth = 4, relief = 'raised')
entry_frame8.grid(column=5, row=5, pady=5, padx=5)

entry8 = tk.Entry(
    entry_frame8,
    font = "Times 10 italic",
    width = 20,
)
entry8.grid(column=5, row=5)

submit_button = tk.Button(
    window,
    text = "SUBMIT",
    font = "Times 15 underline bold",
    fg = "#C00425",
    bg = "#FFCCBB"
)
submit_button.grid(column=3, row=6)


finish_label = tk.Label(
    window,
    text = "To late... \n I know where you live",
    font = "Times 8 italic bold",
    background = "white",
    foreground = "black",
    width = 20,
    height = 2
)
finish_label.grid(column=3, row=7)

window.mainloop()