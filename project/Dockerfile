FROM python:3.12
WORKDIR /code
RUN pip install poetry
COPY . /code/
RUN poetry config virtualenvs.create false
RUN poetry install
EXPOSE 8001
CMD [ "poetry", "run", "uvicorn", "weather_forecast.main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"  ]