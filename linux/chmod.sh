# Whenever bulding docker with any user (not root) and mount volume in docker-compose
chmod -R u+rw /path/to/folder_or_file
chmod -R 777 /path/to/folder_or_file