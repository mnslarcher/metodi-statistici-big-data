find . -name '.DS_Store' -type f -delete
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
