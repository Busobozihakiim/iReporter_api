[![Build Status](https://travis-ci.com/Busobozihakiim/iReporter_api.svg?branch=develop)](https://travis-ci.com/Busobozihakiim/iReporter_api)
[![Coverage Status](https://coveralls.io/repos/github/Busobozihakiim/iReporter_api/badge.svg?branch=develop)](https://coveralls.io/github/Busobozihakiim/iReporter_api?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/df1e6df22422268f450d/maintainability)](https://codeclimate.com/github/Busobozihakiim/iReporter_api/maintainability)
# iReporter
iReporter, an online backed solution that is meant to reduce on the corruption level on the continent. With this method any citizen with an internet access can present any form of corruption to the right authorities.
iReporter also enables users to report any other discovery or situation that needs government intervention.

## Features
- `create a record.` User should be able to make a red flag record
- `Get all records.` User should be able to return all red flag  records
- `Get a single record.` User should be able to fetch a single red flag report
- `edit the location of a record.` User should be able to update the location of a red flag record
- `edit comments of a record.`  User should be able to to update the comment of a red flag record
- `delete a record.` User should be able to delete a red flag record
- `change the status of a record` Admin should be able to update the status of a red fag record

## Installing
First clone this repository

```
git clone -b develop https://github.com/Busobozihakiim/iReporter_api.git 
cd iReporter_api
```

Then create a virtual environment
```
virtualenv venv
```
and start it
```
On Windows
venv/Scripts/activate
On linux
source/venv/bin/activate
```

Then install all the necessary dependencies
```
pip install -r requirements.txt
```

## Running
At the terminal type in
```
python run.py
```

To run tests run this command at the console/terminal
```
pytest
```

Use the api endpoints with an app like [Postman](https://www.getpostman.com/apps) 

## Hosted on Heroku
The online api can be found here

https://ireporter007.herokuapp.com/api/v1/red_flags

Acceptable post format
- When making a report
```
{
    'type': 'red-flag',
    'location':"5555,555",
    'images':'images',
    'videos':'videos',
    'comment':'lorem ipsum doe'
}
```
- When editing the location
```
{
    'location':'32.565, 26.356'
}
```
- When editing a comment
```
{
    'comment':'the new comment'
}
```
- When editing the status
```
{
    'status':'STATUS'
}
where STATUS = resolved, rejected, under-investigation
```

## Available API Endpoints
|  EndPoint  |  Functionality  |
| ------------- | ------------- |
| POST /red-flags | Create a red flag record |
| GET /red-flags | Fetch all red flag records |
| GET /red-flags/<red-flag-id>| Fetch a single red flag record given its id |
| PATCH /red-flags/<red-flag-id>/location| Edit the location of a redflag record |
| PATCH /red-flags/<red-flag-id>/location| Edit the location of a redflag record |
| DELETE /red-flags/<red-flag-id>| Delete a red fag record given an id |
| PATCH /red-flags/<red-flag-id>| Change the status of a record given an id |