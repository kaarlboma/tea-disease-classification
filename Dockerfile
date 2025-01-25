# start from base image
FROM python:3.12.8

# change working directory
WORKDIR /code

# add requirements file to image
COPY ./requirements.txt /code/requirements.txt

# install python libraries
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Check if fastapi was installed successfully
RUN python -c "import fastapi; print(fastapi.__version__)"

# add python code
COPY ./app/ /code/app/

# copy the model file into the container
COPY ./models/xgb_reg.pkl /code/models/xgb_reg.pkl

# specify default commands
CMD ["fastapi", "run", "app/main.py", "--port", "80"]