# Python Desktop Application Project

## Overview

This project consists of creating a desktop application using Python's Tkinter module. It is divided into two main parts that can be worked on independently. The application's goal is to interact with the internet to download data, perform operations on the data, and display the results in various forms.

## Part 1: Data Management Application

Build a desktop application that fetches data from the internet in JSON format, stores it in a SQLite database, and displays summaries and graphical representations of the data.

### NB: we use Spotify's API to set up a music album download system

### Features:
* Data Download and Storage: Download data from spotify in JSON format and store it in a SQLite database.
* Database Management: Clear database content and manage data downloads.
* UI Customization: Customize application appearance, including colors and fonts.
* Data Aggregation and Visualization: Implement functionality to display aggregated data and visualize data through graphs within the main application window.

## Part 2: Document and Graphics Management


Enhance the application's capabilities to export Word documents, create custom graphics, and manage images.

### Features:
* Content Download and Extraction: Download text from a book and extract specific details like title, author, and the first chapter.
* Text Analysis: Analyze and visualize the word count distribution in the first chapter's paragraphs.
* Image Processing: Download, crop, resize, and manipulate images to integrate them into the application.
* Word Document Creation: Generate a Word document containing the book's title, images, author details, and custom header styles. 
* Include a graphical representation of the text analysis and a detailed description.


## General Notes

Exception handling is crucial to prevent the application from crashing.
Implement unit testing for essential functions.
Include a status bar in the main window to display information about the last operation.
Bonus: Improve the application's performance using threading and multiprocessing.

## Getting Started
 * created your work environment
 * install dependencies from requirements.txt
### part1:
    get an spotify key: https://developer.spotify.com/documentation/web-api

    replace client_id and client_secret in src/ui/main_window.py with your information

    run src/ui/main_window.py

### part2:
    run Data_Exploration/main.py

## contribution

To contribute to this project, please create a branch and submit a pull request for review.

## License

This project is under the MIT license.

Don't forget to add information specific to your project if necessary, such as instructions for using MongoDB Compass or details about the structure of the application. After updating the 'README.md', commit the changes and push them to your Git repository.