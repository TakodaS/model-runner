FROM continuumio/miniconda3:latest

WORKDIR /pyross

COPY . .

RUN apt install make && cd /pyross && make env && conda activate pyross && make

SHELL ["conda", "run", "-n", "pyross", "/bin/bash", "-c"]

ENTRYPOINT ["/home"]

# This ensures that the default behavior is to run the tests and then create a release
FROM release
