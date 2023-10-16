from python:3.11.6-alpine


# Настройка FastAPI

COPY ./ $HOME/app/

WORKDIR $HOME/app/

RUN pip install -r requirements.txt

RUN pip install uvicorn

RUN pip install dependencies/UniversalCache-0.0.1.tar.gz
RUN pip install sqlalchemy

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] # Запуск FastAPI
