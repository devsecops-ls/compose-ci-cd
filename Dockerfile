FROM python:3.8-slim-buster
# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 3001
COPY assistant.py .
# Run the application:
CMD python master.py