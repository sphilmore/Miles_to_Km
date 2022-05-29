import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
#Labels
is_equal_label = tkinter.Label(text="equal to", font=("Arial", 12, "bold"))
is_equal_label.config(text="is equal to")
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=10, pady=10)
miles_label=tkinter.Label(text="i am miles", font=("Arial", 12, "bold"))
miles_label.config(text="Miles")
miles_label.grid(column=15, row=0)
miles_label.config(padx=10, pady=10)
km_label= tkinter.Label(text="i am km", font=("Arial", 12, "bold"))
km_label.config(text="Km")
km_label.grid(column=15, row=1)
km_label.config(padx=10, pady=10)
km_results_label = tkinter.Label(text="0")
km_results_label.grid(column=14, row=1)
#entry
miles_entry= tkinter.Entry(width=10)
miles_entry.grid(column=14, row=0)
#The calculations for miles to km
def calculate():
    output = float(miles_entry.get())
    km=output*1.609
    results= km_results_label.config(text=f"{km}")
    return results
#button
button = tkinter.Button(text="calculate", command=calculate)
button.grid(column=14, row=5)
window.mainloop()

