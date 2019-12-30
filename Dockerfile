FROM python:3
WORKDIR Dekstop/docker_tutorial/create_cmr
COPY . .
RUN pip install pipedrive-python-lib
CMD [ "python", "./createCMR.py"]

FROM python:3
WORKDIR Desktop/docker_tutorial/get_data
COPY . .
CMD [ "python", "./getData.py"]
