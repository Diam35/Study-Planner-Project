import tkinter as tk
from tkinter import Menu, messagebox, filedialog, ttk
import datetime

class StudyPlannerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Study Planner")
        self.geometry("1000x600")

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
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Help Menu
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        help_menu.add_command(label="User Guide", command=self.show_user_guide)
        menu_bar.add_cascade(label="Help", menu=help_menu)

    def new_file(self):
        messagebox.showinfo("New", "New file created.")

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            messagebox.showinfo("Open", f"File opened: {file_path}")

    def save_file(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            messagebox.showinfo("Save", f"File saved: {file_path}")

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
        
        # Calendar and list view for study sessions
        tk.Label(self.main_frame, text="Calendar View").pack(pady=10)
        tk.Label(self.main_frame, text="Scheduled Study Sessions").pack(pady=10)

        # Buttons for adding, editing, and deleting study sessions
        button_frame = tk.Frame(self.main_frame)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Add Session", command=self.add_session).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Edit Session").pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Delete Session").pack(side=tk.LEFT, padx=5)

    def add_session(self):
        # Popup window for entering study session details
        popup = tk.Toplevel(self)
        popup.title("Add Study Session")
        
        tk.Label(popup, text="Subject:").grid(row=0, column=0, padx=10, pady=10)
        subject_entry = tk.Entry(popup)
        subject_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(popup, text="Date:").grid(row=1, column=0, padx=10, pady=10)
        date_entry = tk.Entry(popup)
        date_entry.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(popup, text="Time:").grid(row=2, column=0, padx=10, pady=10)
        time_entry = tk.Entry(popup)
        time_entry.grid(row=2, column=1, padx=10, pady=10)
        
        tk.Label(popup, text="Duration:").grid(row=3, column=0, padx=10, pady=10)
        duration_entry = tk.Entry(popup)
        duration_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Button(popup, text="Save", command=popup.destroy).grid(row=4, column=0, columnspan=2, pady=10)

    def show_goals(self):
        tk.Label(self.main_frame, text="Goals", font=("Helvetica", 16)).pack(pady=10)

    def show_progress(self):
        tk.Label(self.main_frame, text="Progress", font=("Helvetica", 16)).pack(pady=10)

    def show_about(self):
        messagebox.showinfo("About", "Study Planner Application\nDeveloper:Diamond Reed")

    def show_user_guide(self):
        messagebox.showinfo("User Guide", "Instructions on how to use the Study Planner Application")

if __name__ == "__main__":
    app = StudyPlannerApp()
    app.mainloop()
    def show_goals(self):
        tk.Label(self.main_frame, text="Goals", font=("Helvetica", 16)).pack(pady=10)
        
        # List view for displaying study goals
        self.goals_listbox = tk.Listbox(self.main_frame)
        self.goals_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Buttons for adding, editing, and deleting goals
        button_frame = tk.Frame(self.main_frame)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Add Goal", command=self.add_goal).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Edit Goal").pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Delete Goal").pack(side=tk.LEFT, padx=5)

    def add_goal(self):
        # Popup window for entering goal details
        popup = tk.Toplevel(self)
        popup.title("Add Goal")
        
        tk.Label(popup, text="Description:").grid(row=0, column=0, padx=10, pady=10)
        description_entry = tk.Entry(popup)
        description_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(popup, text="Deadline:").grid(row=1, column=0, padx=10, pady=10)
        deadline_entry = tk.Entry(popup)
        deadline_entry.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(popup, text="Priority:").grid(row=2, column=0, padx=10, pady=10)
        priority_entry = tk.Entry(popup)
        priority_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Button(popup, text="Save", command=popup.destroy).grid(row=3, column=0, columnspan=2, pady=10)
    def show_progress(self):
        tk.Label(self.main_frame, text="Progress", font=("Helvetica", 16)).pack(pady=10)
        
        # Placeholder for graphical representation of study progress
        tk.Label(self.main_frame, text="Graphical representation of study progress (e.g., bar charts, pie charts)").pack(pady=10)

        # Summary of completed study sessions and achieved goals
        tk.Label(self.main_frame, text="Summary of completed study sessions and achieved goals").pack(pady=10)
        
        # Option to export progress report
        button_frame = tk.Frame(self.main_frame)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Export Progress Report", command=self.export_progress_report).pack(side=tk.LEFT, padx=5)

    def export_progress_report(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write("Sample progress report data\n")
            messagebox.showinfo("Export", f"Progress report exported to: {file_path}")
    def show_reminders(self):
        tk.Label(self.main_frame, text="Reminders and Notifications", font=("Helvetica", 16)).pack(pady=10)
        
        # Settings for configuring reminder preferences

      
    
      

  
