# File_Change_Tracker
The "File Change Tracker" script is a Python tool designed to scan and report changes, creations, and deletions of files on your system within a specified time duration. This script utilizes the os and time modules to traverse through all drives and directories, collecting information about files' creation time, last modification time, and last access time.

Usage:

Clone or download the repository containing the script.
Ensure you have Python installed on your system.
Open a terminal or command prompt and navigate to the script's directory.
Run the script by executing the command python file_change_tracker.py.
Enter the desired duration to go back in hours when prompted.
The script will scan your entire system, excluding Windows system files, and provide a detailed report of changed files, including their creation time, last modification time, and last access time.
Review the generated report to see which files have been created, modified, or accessed within the specified duration.
The script will wait for you to press Enter before exiting, allowing you to review the output.
Note:

For improved accuracy and efficiency, consider running the script with administrative privileges.
Be cautious when running scripts that traverse the entire file system, especially in sensitive environments.
This script is intended for educational purposes and may need modifications based on specific use cases or security requirements. Always adhere to best practices and ethical considerations when scanning and monitoring file changes on a system.
