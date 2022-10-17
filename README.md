# click-number-predictor

The purpose of this take home assignment is to predict the number of clicks for every row.

## Dataset

* **index** - Just for reference. To be ignored
* **city** - city_id
* **district** - district_id
* **min_booking_duration** - minimum duration of booking accepted
* **beds** - number of beds
* **rooms** - number of rooms
* **deposit** - amount of deposit
* **area** - area of the listing
* **price** - price of the listing
* **accomodates** - no. of people it accomodates
* **number_of_pics** - no. of pics
* **Cleaning_fee**
* **first_pic_category**
* **clicks(Target/Label)** - No. of clicks

## Tasks
1. Provide an EDA.
2. Expand on data inconsistencies, data issues and which errors to minimise during
modelling.
3. Provide the reasoning behind feature selection and feature engineering.
4. Show and compare different model performances and pick the most suitable one.

## Quick Start
the project is developped into a REST API to do prediction of clicks based on post Data. 
1. Install Requirements
```python
pip install -r requirements.txt 
```
2. Run the API
```python
uvicorn api.main:app --host 0.0.0.0 --port 5002 --reload 
```
3.Check API Swagger at
```python
localhost:5002/docs
```
