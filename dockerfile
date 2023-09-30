FROM python:3.11


ADD app.py .

# RUN pip install requests beutifylsoup4

CMD [ "python", "./app.py", "daemon of" ]

