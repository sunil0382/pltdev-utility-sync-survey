FROM python:3.11-alpine
LABEL org.opencontainers.image.source="https://github.com/eand-iot/pltdev-utility-sync-survey"
# Install necessary packages
RUN apk update && \
    apk add --no-cache git tzdata postgresql-dev gcc build-base libpq bash

# Set timezone
ENV TZ=Asia/Dubai

# Set environment variables for version and commit hash
ARG COMMIT_HASH="dev-hash"
ARG VERSION="dev"
ENV POSTGRESQL_CONNECTION_STRING=postgresql+psycopg2://admin:usync2025Dxb@20.233.222.33:5432/utility_sync
ENV ADDC_SCHEMA=addc
ENV AADC_SCHEMA=aadc
ENV ENV=ADDC

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . ./

# Copy the start script and make it executable
COPY start.sh ./
RUN chmod +x start.sh

# Expose the necessary ports
EXPOSE 80 50051

# Run the server script
CMD ["./start.sh"]
#CMD ["sh", "-c", "ls -l /app && ./start.sh"]