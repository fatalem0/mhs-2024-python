FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    texlive-latex-base \
    texlive-latex-extra \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-xetex \
    texlive-pictures \
    texlive-science \
    latexmk \
    make \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY ./2.py /app
COPY ./car_copy.png /app
RUN pip install latex_generator_fatalem0
RUN mkdir /app/generated