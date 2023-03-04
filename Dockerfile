FROM python:3.10-slim

# set the working directory
WORKDIR /app

# install dependencies (as requirements don't change much we cache it)
# hence why we have two copy commands  
COPY ./requirements.txt .
#as docker has its own cache 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the src to the folder 
COPY ./app ./app

# start the server (note:we reload server in dev environment)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]