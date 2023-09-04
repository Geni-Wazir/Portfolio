FROM python:3.9-slim-buster as build

WORKDIR /opt/Portfolio

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

ENV FLASK_APP=./portfolio/app.py


COPY --chown=1001:1001 . /opt/Portfolio

RUN pip install --no-cache-dir -r requirements.txt

# ENTRYPOINT ["/opt/RxonCell/docker-entrypoint.sh"]

ENTRYPOINT [ "flask", "run", "--host=0.0.0.0" ]
