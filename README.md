# Manga App Autmation Testing

It's a autmation testing system for three different functionalities of Manga App.

Manga App URL: https://myalice-automation-test.netlify.app/


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Tech](#tech)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)


## Introduction

Manga App has three different features for automated testing. Those features are : Login Functionality, Manga Search and Display, and Manga Details Modal. This project implements automation testing for all of these features

## Features

- `Login Functionality:` By running automated-login.py it will automatically open the Manga App, verify the login page, input valid credentials (testuser,password) and click the login button, and finally go to the search page. If successful it will take a screenshot as login_success.png otherwise it will take a screenshot as login_error.png

- `Manga Search and Display:` By running manga-search.py it will first perform the login step. Then it will verify that it is on the manga search page. After that it will enter four keywords (Naruto, One Piece, Seven Deadly Sins , and No manga found) one by one and click the search button. Later on, it will verify the search results. It will also take screenshots of 4 different results and print necessary messages to the console.

- `Manga Details Modal:` By running manga-details.py it will first perform the login step. Then it will verify that it is on the manga search page. After that it will find the details button of a card and click it. Then, it will verify the modal is open an showing the accurate results and print those results in the console. Later on it will click the close button of the modal and verify that the modal is no longer visible.

## Tech

`Manga App Autmation Testing` uses a number of open source projects to work properly:

- [python] - evented I/O for the testing
- [selenium] - used to carry out automated test cases for browsers or web applications
- [chromedriver.exe] - driver for chrome browser for automated testing

And of course Manga App Autmation Testing itself is open source with a [public repository][QA_TASK] on GitHub.

## Getting Started

Follow these instructions to get the Manga App Autmation Testing up and running on your local machine.

### Prerequisites

Make sure you have the following installed:

- python
- selenium

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Jubair-Ahmed-Khan/QA_TASK

```

## Usage

1. Go to the clone directory:

2. Run 3 different python files to visualize three different functionality
