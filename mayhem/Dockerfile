FROM fuzzers/atheris:2.0.7-python3.9

COPY . /uncurl

# Build Project
WORKDIR /uncurl
RUN pip install .

# Change Permissions
RUN chmod +x /uncurl/mayhem/test_fuzz.py