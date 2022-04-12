FROM python:3.10-bullseye
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY ./app /app
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "__init__.py" ]
