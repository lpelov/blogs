ARG type

FROM python:3.8-slim AS base
RUN apt update
RUN apt-get install -y curl wget gpg git htop vim

FROM base AS pip-install
RUN python -m pip install \
        parse \
        oci

RUN python -m pip install torch
RUN python -m pip install accelerate>=0.12.0
RUN python -m pip install transformers[torch]==4.25.1
RUN python -m pip install ipython ipykernel
RUN python -m pip install ipywidgets


FROM pip-install AS run-type-local
# nothing to see here

FROM pip-install AS run-type-cloud
# COPY hey.py .
# CMD ["python", "hey.py"]

# select type
FROM run-type-${type} AS final