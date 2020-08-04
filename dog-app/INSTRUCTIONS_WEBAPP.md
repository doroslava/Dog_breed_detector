# Instructions

## Prequisites
1. In order to be sure that everything runs smoothly, first install virtual environment
    `python3 -m venv dogenv`
    
2. Activate virtual environment.
    - In Linux system 
    `source dogenv/bin/activate`
    - In Windows system 
    `dogenv\Scripts\activate.bat`    
3. Install prequistites 
    - From the requirements file in the project's root directory. 
     `pip install requirements.txt`      
    
## Local deployment

To run the webapp localy, in project's root directory:
    
1. Uncomment designated line in dog_app.py, depending on if you want to run it on Udacity Workspace or locally on your computer

2. Run the following command in the app's directory to run your web app
    `python dog_app.py`

3. Go to http://localhost:5000/ if running locally, or https://view<WORKSPACEID>-3001.udacity-student-workspaces.com/
