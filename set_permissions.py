import os

def set_static_file_permissions(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            os.chmod(file_path, 0o644)  # Set read permissions for owner and group, and read-only for others
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            os.chmod(dir_path, 0o755)  # Set read and execute permissions for owner, group, and others

# Call the function before running the collectstatic command
set_static_file_permissions('static')
