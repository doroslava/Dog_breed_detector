In order to be sure that everything runs smoothly, first install virtual environment python3 -m venv disasstervenv

Activate virtual environment.

    In Linux system source disasstervenv/bin/activate
    In Windows system disasterenv\Scripts\activate.bat

Install prequistites

    From the requirements file in the project's root directory. pip install requirements.txt
    Install nltk text files python -m nltk.downloader wordnet punkt stopwords



To run the webapp localy, in project's root directory:

    Uncomment designated line in disaster_app.py, depending on if you want to run it on Udacity Workspace or locally on your computer
    Run the following command in the app's directory to run your web app python disaster_app.py

Go to http://localhost:5000/ if running locally