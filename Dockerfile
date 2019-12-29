FROM python:3
ADD getData.py / createCMR.py
RUN pip install pipedrive-python-lib
CMD [ "python", "./my_script.py"]
