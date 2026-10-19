# Base image with Python
FROM python:3.12-slim

LABEL maintainer="Batyr Gazizbek"

# All following commands run inside /app
WORKDIR /app

# Copy application code and student info into the image
COPY app/ /app/
COPY Gazizbek_Batyr_info.txt /app/

# Check the code compiles and create a non-root user
RUN python -m py_compile app.py && useradd --create-home appuser
USER appuser

# Default values (can be overridden with docker run -e ...)
ENV STUDENT_NAME=Batyr \
    STUDENT_SURNAME=Gazizbek \
    STUDENT_GROUP=IT2-2301 \
    STUDENT_ID=38091 \
    PORT=5000

EXPOSE 5000

CMD ["python", "-u", "app.py"]
