# Created by Ivan Legorreta
# Date: 14/07/2023
# Kavak Sr. Data Engineer Code Assessment

# Using python:slim as default base. This provides a good balance between size and functionality (i.e. alpine build is too slim).
# Also not setting a version - the implication of this is that the Python version auto-updates.

FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy files into Container working directory
COPY requirements.txt /app
COPY src/ /app/src
COPY data/ /app/data

# Install needed packages
RUN pip install -r /app/requirements.txt

# We switch to a non-root users to increase security
RUN groupadd -r appuser && \
    useradd -r -g appuser -d /app appuser && \
    chown -R appuser /app 

USER appuser
