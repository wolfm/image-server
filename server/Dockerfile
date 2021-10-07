FROM python:3.9

WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install -r ./requirements.txt

# Set environment variables
ENV FLASK_ENV production

# Source
COPY server.py ./

# Initialize server state
RUN mkdir uploads

EXPOSE 5000
CMD ["gunicorn", "-b", ":5000", "server:app"]