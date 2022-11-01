# Green3B Assessment 

## How to run the REST API
Get this project from Github
``` 
git clone https://github.com/khunshan97/green3b_assessment
 
```

### Create a virtual environment

```
python -m venv env
```

### Activate the virtual environment

For Windows:
```
env\Scripts\activate
```
For Linux:
```
source env/bin/activate
```


### Install the requirements 

``` 
pip install -r requirements.txt
```

### Create the database
``` python create_db.py ```

## Run the API
``` uvicorn main:app --reload ```

## Run the tests
``` pytest ```
