# Creating a Django fixture file from a CSV
This Python script was intended to help me to solve a problem with a task at my job. I had a CSV file with some initial data for a particular model and I needed to seed that data into the database.
I decided to follow this approach based on the Django docs (https://docs.djangoproject.com/en/4.1/howto/initial-data/#initial-data-via-fixtures).
## How to run the script
1. Create a virtual environment
2. Activate the virtual environment
3. Install the packages from `requirements.txt`
	```pip install -r requirements.txt```
4. Paste the source CSV file into the `resources` folder
5. Edit the path and filename for your source
6. Edit the string `result` assignments accordingly to your model
7. Edit the path and filename for the result_file
8. Run the script
	```python script.py```
9. That's it! The JSON file was created in the root directory

## *Base packages versions*
Python 3.9.13
Pip: 22.2.2