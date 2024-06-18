# a tkinter gui to start the django app and run the import_csv command

import os
import subprocess
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import time

# make the user select the APP_PATH through a open folder instead of hardcoding it
APP_PATH = ''
UPLOAD_DB_PATH = 'upload_database.py'
DOWNLOAD_DB_PATH = 'download_database.py'
RENEW_DB_PATH = 'renew_database.py'
GET_ATTENDANCE_PATH = ''
GET_EXCUSES_PATH = '.py'
MERGE_ATTENDANCE_PATH = '.py'
GENERATE_PASSWORDS_PATH = '.py'

def start_app():
    # Change to the app directory
    global APP_PATH
    if APP_PATH == '':
        APP_PATH = filedialog.askdirectory(title='Select App Directory')
    
    os.chdir(APP_PATH)
    subprocess.Popen([r'venv\Scripts\activate.bat'])

def upload_database():
    os.chdir(APP_PATH)
    CSV_FILE_PATH = filedialog.askopenfilename(title='Select CSV File', filetypes=[('CSV Files', '*.csv')])
    if CSV_FILE_PATH:
        subprocess.Popen(['python', UPLOAD_DB_PATH, '--file', CSV_FILE_PATH])
        time.sleep(2)


def download_database():
    os.chdir(APP_PATH)
    subprocess.Popen(['python', DOWNLOAD_DB_PATH])
    time.sleep(2)

def renew_database():
    os.chdir(APP_PATH)
    subprocess.Popen(['python', RENEW_DB_PATH])
    time.sleep(2)

def get_attendance():
    os.chdir(APP_PATH)
    #get attendance start date
    start_date = ''
    subprocess.Popen(['python', GET_ATTENDANCE_PATH, '--start_date', start_date])
    time.sleep(2)

def get_excuses():
    os.chdir(APP_PATH)
    #get excuses start date
    start_date = ''
    subprocess.Popen(['python', GET_EXCUSES_PATH, '--start_date', start_date])
    time.sleep(2)

def merge_attendances():
    os.chdir(APP_PATH)
    CSV_FILES_PATH = filedialog.askopenfilenames(title='Select CSV Files', filetypes=[('CSV Files', '*.csv')])
    if CSV_FILES_PATH:
        subprocess.Popen(['python', MERGE_ATTENDANCE_PATH, '--files', str(CSV_FILES_PATH)])
        time.sleep(2)

def generate_passwords():
    os.chdir(APP_PATH)
    CSV_FILE_PATH = filedialog.askopenfilename(title='Select CSV File', filetypes=[('CSV Files', '*.csv')])
    if CSV_FILE_PATH:
        subprocess.Popen(['python', GENERATE_PASSWORDS_PATH, '--file', CSV_FILE_PATH])
        time.sleep(2)

    
    

def on_start_button_click():
    start_app()
    messagebox.showinfo('Choir App', 'app started successfully!')

def on_upload_button_click():
    upload_database()
    messagebox.showinfo('Upload DB', 'CSV data imported successfully!')

def on_download_button_click():
    download_database()
    messagebox.showinfo('Download DB', 'CSV data exported successfully!')

def on_renew_button_click():
    renew_database()
    messagebox.showinfo('Renew DB', 'Current DB renewed and CSV data exported successfully!')

def on_get_attendance_button_click():
    get_attendance()
    messagebox.showinfo('Get Attendance', 'Requested Attendance downloaded successfully!')

def on_get_excuses_button_click():
    get_excuses()
    messagebox.showinfo('Get Excuses', 'Requested Excuses downloaded successfully!')

def on_merge_attendances_button_click():
    merge_attendances()
    messagebox.showinfo('Merge Attendances', 'Full report exported successfully!')

def on_generate_passwords_button_click():
    generate_passwords()
    messagebox.showinfo('Generate Password', 'Passwords file generated successfully!')


# Create the main window
root = tk.Tk()
root.title('Choir Admin App Starter')
# TODO: size

# Create and place the Start button
start_button = tk.Button(root, text='Start App', command=on_start_button_click)
start_button.pack(pady=10)

# Create and place the upload button
upload_button = tk.Button(root, text='Upload Database', command=on_upload_button_click)
upload_button.pack(pady=10)

# Create and place the download button
download_button = tk.Button(root, text='Download Database', command=on_download_button_click)
download_button.pack(pady=10)

# Create and place the renew button
renew_button = tk.Button(root, text='Renew Database', command=on_renew_button_click)
renew_button.pack(pady=10)

# Create and place the get attendance button
get_attendance_button = tk.Button(root, text='Get Attendance', command=on_get_attendance_button_click)
get_attendance_button.pack(pady=10)

# Create and place the get excuses button
get_excuses_button = tk.Button(root, text='Get Excuses', command=on_get_excuses_button_click)
get_excuses_button.pack(pady=10)

# Create and place the merge attendance button
merge_attendance_button = tk.Button(root, text='Merge Attendance', command=on_merge_attendances_button_click)
merge_attendance_button.pack(pady=10)

# Create and place the generate passwords button
generate_passwords_button = tk.Button(root, text='Generate Passwords file', command=on_generate_passwords_button_click)
generate_passwords_button.pack(pady=10)


# Run the main event loop
root.mainloop()