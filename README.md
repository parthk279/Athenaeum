# Athenaeum
[![DOI](https://zenodo.org/badge/544187336.svg)](https://zenodo.org/badge/latestdoi/544187336)
<a href="https://github.com/Nikhil1912/Athenaeum/main/LICENSE.md"><img src="https://img.shields.io/github/license/Nikhil1912/CSC510-HW_37?style=plastic" /></a>
![GitHub issues](https://img.shields.io/github/issues/Nikhil1912/Athenaeum)
![Repo Size](https://img.shields.io/github/repo-size/Nikhil1912/Athenaeum?color=brightgreen)
[![Unit tests](https://github.com/Nikhil1912/Athenaeum/actions/workflows/backend-tests.yml/badge.svg)](https://github.com/Nikhil1912/Athenaeum/actions/workflows/backend-tests.yml)
[![codecov](https://codecov.io/gh/Nikhil1912/Athenaeum/branch/main/graph/badge.svg?token=5UIM8QKSNQ)](https://codecov.io/gh/Nikhil1912/Athenaeum)

## Motivation
Athenaeum is an application dedicated to connecting you with the books you're searching for. Our goal: to search the web and find you the books you seek at a reputable distributor and a good price. Using Athenaeum, you can simplify your journey and minimize your costs as you find the resources you need for class. We specifically aim to target students, but all lovers of books are welcome to partake. We currently have no users.

## Current Scope and Future Work
At present, you can add, edit, or delete a book from your local machine. If the book has a link to purchase, the "Buy" button will direct you to the appropriate page. If you search for a book that exists in our database, it will direct you to the appropriate Wikipedia link for that book. 

Our web scraper is currently in progress (see [`\workInProgress`](https://github.com/Nikhil1912/Athenaeum/tree/main/workInProgress) for what we have so far), but we intend to integrate it with our current page to allow for a more optimized searching experience that also presents pricing. We also intend to create a "Buy/Sell" user forum, as well as a functional login page.

## Running Athenaeum
Currently, to get everything up and running:
# Clone the project
* Install dependencies 
   * The easiest way to do this: navigate to `\Athenaeum` and run `pip install -r requirements.txt`
   * [Node.js](https://nodejs.org/en/download/) includes npm (v. 8.15.0), which is also required
* To run the backend:
   * Navigate to the backend directory, `\Athenaeum\backend`
   * Create a new file `\Athenaeum\backend\.env` and add the secret key in the file:
     * `SECRET_KEY = '<secret key>'`
     
   * If running for the first time, run the migrate commands (if confused, review help [here](https://stackoverflow.com/questions/56166319/oserror-winerror-123-the-filename-directory-name-or-volume-label-syntax-is))
   * Run `python manage.py runserver`
   * Navigate to http://localhost:8000/api/books/
   To stop the server, hit CTRL+C
* To run the frontend:
   * Navigate to the frontend directory, `\Athenaeum\frontend`
   * If running for the first time, run `npm ci`
   * Run `npm start`
   * Navigate to http://localhost:3000
   * To leave, hit CTRL+C and then Y
 * Common issues:
   * NOTE: the environment file should be entitled `.env`, NOT `backend.env`
   * Ensure that you have run the migrate commands
   * If `python` doesn't work, try `python3`

## Common Use Cases
* Searching for a book
  * Visit the search bar and search for a book, which will direct you to the book's Wikipedia page
* Adding a book
  * Press "Add a book"
  * Fill in all requirements listed
* Removing a book
  * Press "Delete"
* Editing a book
  * Press "Edit"
* Buying a book
  * If the book has a "Buy" button, use that
   
## Governance and Contributors
As an open-source project, we declare our governance model to be a "do-ocracy"; for insight into what that means, checkout [this](https://www.redhat.com/en/blog/understanding-open-source-governance-models) link from Red Hat. 

Our current contributors are: 
* M M Abid Naziri
* Nikhil Mehra
* Bella Samuelsson
* Parth Katlana
* Heidi Reichert

## Contributing, Bugs, Feature Requests, Etc.
For more information on contributing, check out CONTRIBUTING.md. To report a bug, request a feature, or communicate with the developers, please contact athenaeum_csc510@outlook.com. If you wish to join our mailing list for updates on our software, please email the aforementioned address and we will add you to our mailing list.

## Dependencies
For a list of all dependencies, check out our [dependencies graph](https://github.com/Nikhil1912/Athenaeum/network/dependencies). All dependencies listed are mandatory.


## Funding
This project is not funded and probably never will be.

<img width="665" alt="Screen Shot 2022-10-09 at 7 03 11 PM" src="https://user-images.githubusercontent.com/112109564/194783687-8d2f9dda-ae5c-45d6-a31e-e2318652b159.png">


![Athenaeum](https://user-images.githubusercontent.com/25509428/194795162-0f9904ef-735f-4875-9d76-84cd3074994a.png)
