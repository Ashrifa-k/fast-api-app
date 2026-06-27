# fast-api-app

## create fastapi application


# CRUD operations
-read
-update
-delete

# Rest API
-GET
-POST
-PUT
-DELETE

# STATUS CODES
-200 OK
-201 CREATED
-204 NO CONTENT
-400 BAD REQUEST
-401 UNAUTHORIZED
-403 FORBIDDEN
-404 NOT FOUND
-405 METHOD NOT ALLOWED
-409 CONFLICT
-500 INTERNAL SERVER ERROR

# ARCHITECTURE OF FASTAPI APPLICATION
-MODEL --TABLES CREATION
-ROUTER --ROUTES REQUESTS TO CONTROLLERS
-CONTROLLER --CONTROLLER LOGIC
-SERVICE --BUSINESS LOGIC
-REPOSITORY --DATA ACCESS LAYER
-MIDDLEWARE --REQUEST PROCESSING PIPELINE
# non-relational databse
mongodb
caasandra
redis
dynamodb
# Constraints in DataBase
primary Key-- eg: Student_id,staff_id
foreign key-- eg: department_id in student table
unique -- eg: name
check -- eg: salary>0
default -- eg: timestamp: func.now()

# modules
sqlalchemy -- orm(object relational mapping)
fastapi -- web framework
uvicorn -- server for running fastapi
application --> 'uvicron app.main:app --reload'
psycopg2 -- postgresql driver
pydantic -- 

# concepts
depends
    Sessionmaker
        to create a session with the databse
    sessionlocal
        to create a session with the database for a single request
    declarative_base
        to create a base class for all the models