# get python official image
FROM python:3.10-alpine

# set working directory
WORKDIR /main

# copy requirements.txt 
COPY requirements.txt requirements.txt

# run pip install requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# copy all
COPY . .

# set command
CMD [ "python", "./main.py" ]
# RUN python ./main.py
