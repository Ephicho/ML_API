FROM python:3.8


ADD main.py .

RUN pip install requests beutifylsoup4

CMD [ "python", "./main.py" ]

