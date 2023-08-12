# text-summarization

# Text Summarization Project

This project focuses on text summarization using various techniques. It allows users to generate concise summaries of longer texts.

## Installation

Follow these steps to set up the project environment:

1. Open the command prompt (cmd).
2. Install or update required packages:

   ```bash
   pip install -U pip setuptools wheel
   pip install -U spacy

 3. Download the English language model for spaCy:
  
  python -m spacy download en_core_web_sm


  
If you're encountering a "module not found" error when trying to import modules like Flask, render_template, and request in Visual Studio Code (VS Code), follow these steps:


Step 1: Create a Virtual Environment (Recommended)
It's a good practice to work within a virtual environment to manage package dependencies. Open your terminal and navigate to your project directory. Then create a virtual environment:

python -m venv venv
Step 2: Activate the Virtual Environment
Activate the virtual environment using the appropriate command based on your operating system:

On Windows:

venv\Scripts\activate


On macOS and Linux:
source venv/bin/activate


Step 3: Install Required Packages
With the virtual environment active, install the required packages using pip:

pip install Flask
pip install Jinja2  # If you plan to use render_template


Step 4: Restart VS Code
After installing the necessary packages, close and reopen VS Code. Make sure to set your virtual environment as the Python interpreter for your project.

To select the interpreter in VS Code, you can click on the bottom bar where the Python version is displayed and choose the interpreter from the list. If it doesn't appear in the list, you might need to reload the window.

Step 5: Try Importing Again
With the virtual environment active and the packages installed, try importing the modules in your Python code again:

from flask import Flask, render_template, request



By following these steps, you should be able to resolve the "module not found" error and work with the Flask framework and related modules in VS Code.




TO RUN THIS PROJECT:
go to cmd and navigate to project folder 
and 
         python app.py
