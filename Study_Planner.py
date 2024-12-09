import tkinter as tk
from tkinter import Menu, messagebox

class StudyPlannerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Study Planner")
        self.geometry("800x600")

        # Menu Bar
        self.create_menu_bar()

        # Navigation Pane
        self.create_navigation_pane()

        # Main Content Frame
        self.main_frame = tk.Frame(self, bg="white")
        self.main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def create_menu_bar(self):
        menu_bar = Menu(self)
        self.config(menu=menu_bar)

        # File Menu
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Help Menu
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        help_menu.add_command(label="User Guide", command=self.show_user_guide)
        menu_bar.add_cascade(label="Help", menu=help_menu)

    def create_navigation_pane(self):
        nav_frame = tk.Frame(self, bg="lightgray", width=200)
        nav_frame.pack(side=tk.LEFT, fill=tk.Y)

        buttons = ["Dashboard", "Schedule", "Goals", "Progress"]
        for btn_text in buttons:
            btn = tk.Button(nav_frame, text=btn_text, command=lambda txt=btn_text: self.show_frame(txt))
            btn.pack(fill=tk.X, padx=5, pady=5)

    def show_frame(self, frame_name):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        if frame_name == "Dashboard":
            self.show_dashboard()
        elif frame_name == "Schedule":
            self.show_schedule()
        elif frame_name == "Goals":
            self.show_goals()
        elif frame_name == "Progress":
            self.show_progress()

    def show_dashboard(self):
        tk.Label(self.main_frame, text="Dashboard", font=("Helvetica", 16)).pack(pady=10)

    def show_schedule(self):
        tk.Label(self.main_frame, text="Schedule", font=("Helvetica", 16)).pack(pady=10)

    def show_goals(self):
        tk.Label(self.main_frame, text="Goals", font=("Helvetica", 16)).pack(pady=10)

    def show_progress(self):
        tk.Label(self.main_frame, text="Progress", font=("Helvetica", 16)).pack(pady=10)

    def show_about(self):
        messagebox.showinfo("About", "Study Planner Application\nDeveloper: Your Name")

    def show_user_guide(self):
        messagebox.showinfo("User Guide", "Instructions on how to use the Study Planner Application")

if __name__ == "__main__":
    app = StudyPlannerApp()
    app.mainloop()
