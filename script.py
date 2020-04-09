import tkinter as tk

# variables


root = tk.Tk()
root.title("Subject Database by Donnaven")
# create canvas
canvas = tk.Canvas(root, height=720, width=1280)

# table headings
subjectNumber = tk.Label(root, text="Subject #")
subjectLastName = tk.Label(root, text="Subject Surname")
subjectFirstVisitDate = tk.Label(root, text="First Visit")
subjectVisit2 = tk.Label(root, text="Visit 2")
subjectVisit3 = tk.Label(root, text="Visit 3")
subjectVisit4 = tk.Label(root, text="Visit 4")
subjectVisit5 = tk.Label(root, text="Visit 5")
subjectVisit6 = tk.Label(root, text="Visit 6")
subjectVisit7 = tk.Label(root, text="Visit 7")
subjectVisit8 = tk.Label(root, text="Visit 8")
subjectVisit9 = tk.Label(root, text="Visit 9")
subjectVisit10 = tk.Label(root, text="Visit 10")
subjectNumberHeading = tk.Label(root, text="Subject #")


# subject number boxes
sbox1 = tk.Entry(root, width="5")

# SUBJECT ONE visit boxes
s1v1 = tk.Entry(root, width="5")
s1v2 = tk.Entry(root, width="5")
s1v3 = tk.Entry(root, width="5")
s1v4 = tk.Entry(root, width="5")
s1v5 = tk.Entry(root, width="5")
s1v6 = tk.Entry(root, width="5")
s1v7 = tk.Entry(root, width="5")
s1v8 = tk.Entry(root, width="5")
s1v9 = tk.Entry(root, width="5")
s1v10 = tk.Entry(root, width="5")
# SUBJECT TWO visit boxes
s2v1 = tk.Entry(root, width="5")
s2v2 = tk.Entry(root, width="5")
s2v3 = tk.Entry(root, width="5")
s2v4 = tk.Entry(root, width="5")
s2v5 = tk.Entry(root, width="5")
s2v6 = tk.Entry(root, width="5")
s2v7 = tk.Entry(root, width="5")
s2v8 = tk.Entry(root, width="5")
s2v9 = tk.Entry(root, width="5")
s2v10 = tk.Entry(root, width="5")


# display the gui
canvas.grid()
subjectFirstVisitDate.place(x=0, y=0)
subjectVisit2.place(x=60, y=0)
subjectVisit3.place(x=100, y=0)
subjectVisit4.place(x=140, y=0)
subjectVisit5.place(x=180, y=0)
subjectVisit6.place(x=220, y=0)
subjectVisit7.place(x=260, y=0)
subjectVisit8.place(x=300, y=0)
subjectVisit9.place(x=340, y=0)
subjectVisit10.place(x=380, y=0)
subjectNumberHeading.place(x=420, y=0)
# display subject number boxes
sbox1.place(x=420,y=20)

# display SUBJECT ONE entry boxes
s1v1.place(x=10, y=20)
s1v2.place(x=60, y=20)
s1v3.place(x=100, y=20)
s1v4.place(x=140, y=20)
s1v5.place(x=180, y=20)
s1v6.place(x=220, y=20)
s1v7.place(x=260, y=20)
s1v8.place(x=300, y=20)
s1v9.place(x=340, y=20)
s1v10.place(x=380, y=20)
# display SUBJECT TWO entry boxes
s2v1.place(x=10, y=43)
s2v2.place(x=60, y=43)
s2v3.place(x=100, y=43)
s2v4.place(x=140, y=43)
s2v5.place(x=180, y=43)
s2v6.place(x=220, y=43)
s2v7.place(x=260, y=43)
s2v8.place(x=300, y=43)
s2v9.place(x=340, y=43)
s2v10.place(x=380, y=43)

# create file data

# loop
root.mainloop()

