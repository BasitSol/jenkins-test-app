# app.py (Simplified for Jenkins "Run Script" demo)
import sys         #Updated For SCM Polling demo
import os
from flask import Flask # Still import Flask, but won't run web server

    app = Flask(__name__)
    # Updated for Webhook demo
    @app.route('/')
    def home():
        return "This should not be hit by Jenkins build job."

    if __name__ == '__main__':
        # This code runs when 'python app.py' is executed by Jenkins
        print("--- Flask app script is running inside Jenkins! ---")
        print(f"Python version: {sys.version}")
        print(f"Current working directory in Jenkins: {os.getcwd()}")

        # You can add simple build/test steps here for demonstration
        # For example, checking if a file exists:
        if os.path.exists('requirements.txt'):
            print("requirements.txt found!")
        else:
            print("WARNING: requirements.txt NOT found!")

        print("--- Script finished successfully within Jenkins build ---")
    
# Scroll down and click "Commit new file."
