import os
import shutil
import datetime
import schedule
import time


source_dir = "C:/Users/shubh/OneDrive/Pictures/Screenshots"
destination_dir = "D:/Codes/projects/file backup"

def copy_folder_to_directory(source,destination):
    today = datetime.date.today()
    dest_dir = os.path.join(destination,str(today))
    
    try:
        shutil.copytree(source,dest_dir)
        print(f"Folder  copied to : {dest_dir}")
    except Exception as e:
        print(e)
        print(f"Folder already exists in : {destination}")

#to check
copy_folder_to_directory(source_dir,destination_dir)
#==============================================================
#to backup automatically at 5 pm
def start_backup():
    copy_folder_to_directory(source_dir,destination_dir)

schedule.every().day.at("17:00").do(start_backup)
#                      24 hr time
while True :
    schedule.run_pending()
    time.sleep(60)
#==============================================================
