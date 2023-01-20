# start by pulling the python image
FROM python:3.8-slim

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
# RUN apk update
# RUN apk add make automake gcc g++ subversion python3-dev
# RUN pip install -r requirements.txt
RUN pip3 install -U pip
RUN pip3 install -U wheel
RUN pip3 install -U setuptools
RUN apt update \
    && apt install -y libmariadb-dev \
        gcc\
        python3-dev \
        libcogl-pango-dev \
        libcairo2-dev \
        libtool \
        linux-headers-amd64 \
        musl-dev \
        libffi-dev \
        libssl-dev \
        libjpeg-dev \
        zlib1g-dev
RUN pip install -r requirements.txt


# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py", "--host", "0.0.0.0"]