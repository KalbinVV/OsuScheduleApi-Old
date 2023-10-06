from python:3.11.6-alpine

COPY ./ $HOME/app/

WORKDIR $HOME/app/

RUN pip install -r requirements.txt

RUN pip install uvicorn

ENTRYPOINT ["uvicorn", "main:app", "--reload"] 

