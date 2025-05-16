# Budget Book Web Edition

This is my sister project of my Budget Book application.

## Overview

The purpose is the same as the main Budget Book, create something I need while learning as much as I can about [Python](https://www.python.org) and related
components at the same time.  In this case also adapting the application as a web based app using [Django](https://www.djangoproject.com/).

> This currently is just a separation of the two repos and so the README and its contents wont likely be updated for a while.  For more
up to date details I suggest the main [Budget Book](https://github.com/Gergzilla/budgetbook) repository.

## Goals

I expect the end state to be able to:

- Import transactions from common file formats (CSV for now)
- Compile this data into a single file for simplicity
- Allow custom labelling or tagging for budget and expense categories
- User friendly interface for validating and correcting import issues
- Provide a nice UI for viewing transactions, reports, summaries and charts
- System can be run on a private hosted web system with minimal footprint

Future roadmap:

- secure login capabilities for data protection
- extend support for other file formats such as PDF
- A possible desktop client alternative with GUI
- ~Use a database like SQLite to store all transaction data for more robust options~ Implemented

## Current Features

- Functional GUI using TKinter
- Able to import CSV expense files
- Dynamically update GUI with imported data
- Able to import transactions from capital one pdf files as pandas dataFrames
- PDF parsing converted to a class for better page and document handling

## TODO List

Tracking for what I need to change, fix or implement

- ~Setup base landing page templates~
- Improve UI layout and widget alignment
- Setup multiple UI pages for different actions ie, importing, editing, reports, charts, etc
- Update the SQL functions to support the TKinter version
- ~Modify original POC scripts to interact with Django's SQLite DB~
- ~Import test data~
- ~Correct formatting of import data <sup>The date format is causing issues</sup>~ Resolved 5-7-2025
- ~Create budget summary page template~
- Update links, filters and buttons for summary browsing <sup> on hold until Django development resumes</sup>
- Create a page to edit the budget data to add tags and make corrections <sup> on hold until Django development resumes</sup>
- Add ability to upload CSV/TSV files for easier import <sup>CSV file import added 5-7-2025</sup>
- Setup tagging in a more friendly way, inline editing of a table perhaps
- Add a reliable storage method for tags to be used to to correlate common names with a tag to 'learn' how things get tagged

## Rlease Notes

- Moving future commits to dev branch for better sanity checks and logic control - 5/15/2025

## Bugs or Issues

- ~Despite the table having a date field the SQL query object doesnt have it so no date is displayed~ Resolved 4-17-2025
- ~App crashes if you cancel the import file dialogue box without selecting a file~ Resolved 5-8-2025
- The dynamic entry boxes do not always properly reset when importing different data or changing sources

## Footnote
