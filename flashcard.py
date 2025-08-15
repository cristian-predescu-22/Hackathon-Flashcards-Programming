import customtkinter as ctk

# ---------- Reusable Button ----------
class FlashcardButton(ctk.CTkButton):
    def __init__(self, master, text, command=None):
        super().__init__(master, text=text, width=120, height=50, command=command)
        self.pack_propagate(False)


# ---------- Main Menu Frame ----------
class MainMenuFrame(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.title_label = ctk.CTkLabel(self, text="Flashcard", font=("Arial", 28))
        self.title_label.grid(row=0, column=0, columnspan=3, pady=(20, 10))

        self.create_button = FlashcardButton(self, text="Create", command=self.controller.show_create_frame)
        self.create_button.grid(row=1, column=0, padx=20, pady=20)

        self.view_button = FlashcardButton(self, text="View", command=lambda: print("View frame later"))
        self.view_button.grid(row=1, column=1, padx=20, pady=20)

        self.placeholder_button = FlashcardButton(self, text="Placeholder", command=lambda: print("Placeholder clicked"))
        self.placeholder_button.grid(row=1, column=2, padx=20, pady=20)


# ---------- Create Flashcard Frame ----------
class CreateFlashcardFrame(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(self, text="Create a Flashcard", font=("Arial", 24))
        self.title_label.grid(row=0, column=0, pady=20)

        # Simple entry fields
        self.q_label = ctk.CTkLabel(self, text="Question:")
        self.q_label.grid(row=1, column=0, sticky="w", padx=20)

        self.q_entry = ctk.CTkEntry(self, width=300)
        self.q_entry.grid(row=2, column=0, pady=5)

        self.a_label = ctk.CTkLabel(self, text="Answer:")
        self.a_label.grid(row=3, column=0, sticky="w", padx=20)

        self.a_entry = ctk.CTkEntry(self, width=300)
        self.a_entry.grid(row=4, column=0, pady=5)

        self.save_button = ctk.CTkButton(self, text="Save Flashcard", command=self.save_flashcard)
        self.save_button.grid(row=5, column=0, pady=15)

        self.back_button = ctk.CTkButton(self, text="← Back", fg_color="gray30", command=self.controller.show_main_menu)
        self.back_button.grid(row=6, column=0, pady=10)

    def save_flashcard(self):
        question = self.q_entry.get()
        answer = self.a_entry.get()
        print(f"Saved Flashcard: {question} -> {answer}")
        # Later: Save to file or DB
        self.q_entry.delete(0, "end")
        self.a_entry.delete(0, "end")


# ---------- App (Controller) ----------
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Flashcard App")
        self.geometry("500x350")

        # current frame placeholder
        self.current_frame = None

        # show the main menu by default
        self.show_main_menu()

    def clear_frame(self):
        """Destroy the current frame before loading another one"""
        if self.current_frame is not None:
            self.current_frame.destroy()

    def show_main_menu(self):
        self.clear_frame()
        self.current_frame = MainMenuFrame(self, controller=self)
        self.current_frame.pack(fill="both", expand=True)

    def show_create_frame(self):
        self.clear_frame()
        self.current_frame = CreateFlashcardFrame(self, controller=self)
        self.current_frame.pack(fill="both", expand=True)


# ---------- Run ----------
if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")
    app = App()
    app.mainloop()
