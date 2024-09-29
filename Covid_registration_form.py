import tkinter as tk

class Covid_registration_form:
    def __init__(self, root):
        self.root = root
        self.root.title("COVID REGISTRATION FORM")
        self.root.geometry("400x400")
        self.root.configure(bg="lightblue")  # Setting the background color of the window

        # Variables for user input
        self.name = tk.StringVar()
        self.age = tk.StringVar()
        self.gender = tk.StringVar()
        self.vaccine = tk.StringVar()
        self.contact = tk.StringVar()

        # Form title
        tk.Label(root, text="Covid-19 Registration Form", font=("Arial", 16), bg="lightblue").grid(row=0, column=0, columnspan=2, pady=10)

        # Name input
        tk.Label(root, text="Name", bg="lightblue").grid(row=1, column=0, padx=20, pady=5, sticky="w")
        self.name_entry = tk.Entry(root, textvariable=self.name, highlightbackground="black", highlightthickness=1)
        self.name_entry.grid(row=1, column=1, padx=20, pady=5)

        # Age input
        tk.Label(root, text="Age", bg="lightblue").grid(row=2, column=0, padx=20, pady=5, sticky="w")
        self.age_entry = tk.Entry(root, textvariable=self.age, highlightbackground="black", highlightthickness=1)
        self.age_entry.grid(row=2, column=1, padx=20, pady=5)

        # Gender input (Radio buttons)
        tk.Label(root, text="Gender", bg="lightblue").grid(row=3, column=0, padx=20, pady=5, sticky="w")
        tk.Radiobutton(root, text="Male", variable=self.gender, value="Male", bg="lightblue", highlightbackground="black", highlightthickness=1).grid(row=3, column=1, sticky="w")
        tk.Radiobutton(root, text="Female", variable=self.gender, value="Female", bg="lightblue", highlightbackground="black", highlightthickness=1).grid(row=3, column=1, padx=100, sticky="w")

        # Vaccine selection (Option Menu)
        tk.Label(root, text="Vaccine", bg="lightblue").grid(row=4, column=0, padx=20, pady=5, sticky="w")
        vaccine_options = ["Covaxin", "Covishield", "Sputnik V", "Moderna"]
        self.vaccine.set(vaccine_options[0])  # Default value
        tk.OptionMenu(root, self.vaccine, *vaccine_options).grid(row=4, column=1, padx=20, pady=5)

        # Contact number input
        tk.Label(root, text="Contact", bg="lightblue").grid(row=5, column=0, padx=20, pady=5, sticky="w")
        self.contact_entry = tk.Entry(root, textvariable=self.contact, highlightbackground="black", highlightthickness=1)
        self.contact_entry.grid(row=5, column=1, padx=20, pady=5)

        # Submit button
        tk.Button(root, text="Submit", command=self.submit_form, highlightbackground="black", highlightthickness=2).grid(row=6, column=0, columnspan=2, pady=20)

    def submit_form(self):
        # Collecting the user data
        print(f"Name: {self.name.get()}")
        print(f"Age: {self.age.get()}")
        print(f"Gender: {self.gender.get()}")
        print(f"Vaccine: {self.vaccine.get()}")
        print(f"Contact: {self.contact.get()}")

# Running the application
root = tk.Tk()
app = Covid_registration_form(root)
root.mainloop()
