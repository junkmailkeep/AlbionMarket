import customtkinter as ctk
import API



ctk.set_appearance_mode("dark")

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Albion Market")

        self.geometry("800x800")

        self.pulldataButton = ctk.CTkButton(self,text="pull data", command = self.pulldata)
        self.pulldataButton.pack()

        


    def pulldata(self):
        API.pullall()

if __name__ == "__main__":
    app = App()

    app.mainloop()