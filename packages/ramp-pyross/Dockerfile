FROM docker.pkg.github.com/rajeshrinet/pyross/pyross-latest:latest as build

WORKDIR .
COPY scripts/ ./scripts/

# Input specified inside the folder at /data/input
# any addidional data goes into /data/input
ENV MODEL_DATA_DIR /model/input
ENV MODEL_INPUT_DIR /data/input
ENV MODEL_OUTPUT_DIR /data/output

# Input and output files must conform to the schema defined in /api/schema
FROM build as release
ENTRYPOINT ["/scripts/run-pyross", "/data/input/inputFile.json", "/data/output/data.json"]]

# This ensures that the default behavior is to run the tests and then create a release
FROM release
