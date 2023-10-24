FROM python:3.11

WORKDIR /app

COPY . /app/

 #Install depndencies 
RUN pip install -r requriment.txt

COPY . .

#Expose the port that the application will be running
EXPOSE 8000

#Run the application

CMD [ "uvicorn", "./main:app", "daemon of" ]

