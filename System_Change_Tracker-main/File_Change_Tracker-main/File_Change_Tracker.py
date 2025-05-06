import os
import time

def is_windows_system_file(file_path):
    # Add more conditions based on your needs to identify Windows system files
    return "\\Windows\\" in file_path

def list_changed_files(base_path, duration_hours):
    print("Scanning for changed files. This may take a while...")

    current_time = time.time()
    duration_seconds = duration_hours * 3600

    changed_files = []

    for drive in os.listdir(base_path):
        drive_path = os.path.join(base_path, drive)

        for foldername, subfolders, filenames in os.walk(drive_path):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)

                # Filter out changes to Windows system files
                if is_windows_system_file(file_path):
                    continue

                try:
                    last_access_time = os.path.getatime(file_path)
                    last_modification_time = os.path.getmtime(file_path)
                    creation_time = os.path.getctime(file_path)
                except OSError:
                    continue

                # Check if the file was created, modified, or accessed within the specified duration
                if (
                    current_time - last_access_time <= duration_seconds or
                    current_time - last_modification_time <= duration_seconds or
                    current_time - creation_time <= duration_seconds
                ):
                    changed_files.append((file_path, creation_time, last_modification_time, last_access_time))

    print("Scanning complete.")
    return changed_files

if __name__ == "__main__":
    base_path = os.path.abspath(os.sep)  # Get the root directory
    duration_hours = int(input("Enter the duration to go back in hours: "))

    changed_files = list_changed_files(base_path, duration_hours)

    if changed_files:
        print("Changed files in the last {} hours:".format(duration_hours))
        for file_info in changed_files:
            file_path, creation_time, last_modification_time, last_access_time = file_info
            print(f"- File: {file_path}")
            print(f"  - Creation Time: {time.ctime(creation_time)}")
            print(f"  - Last Modification Time: {time.ctime(last_modification_time)}")
            print(f"  - Last Access Time: {time.ctime(last_access_time)}")
    else:
        print("No changed files found in the specified duration.")

    input("Press Enter to exit.")
