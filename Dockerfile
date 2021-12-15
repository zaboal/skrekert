FROM python:bullseye

# Preparing for the general step
COPY app .
RUN pip install --no-cache-dir -r requirements.txt

# Commands realising
CMD ["python", "src/Main.py"]
