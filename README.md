# Cvina

Open source programming language that looks like c but based on python


# Example

''#include ("tkinter")
counter = 0

fn increment():
    global counter
    counter += 1
    label.config(text=f"Clicked {counter} times!")
root = tkinter.Tk()
root.title("Cvina Button Clicker")
root.geometry("300x150")

label = tkinter.Label(root, text="Clicked 0 times", font=("Arial", 12))
label.pack(pady=20)

btn = tkinter.Button(root, text="Click Me!", command=increment)
btn.pack()

root.mainloop()''

# Contributions

Modifying the language
