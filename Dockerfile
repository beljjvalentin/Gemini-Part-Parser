# The base image which can be selected from: https://hub.docker.com/search
FROM python:3.9-alpine

# To define the working directory
# 'WORKDIR /'  means root of the base image
WORKDIR /

# To copy the files to the working directory
COPY . .

# To install the dependency
# RUN pip install flask
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# To open the port 5000 in the container
EXPOSE 5000

# To run the app in the container
CMD ["python", "main.py"]