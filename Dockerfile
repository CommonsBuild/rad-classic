FROM python:3.9

# Create app directory
RUN mkdir -p /opt/rad
WORKDIR /opt/rad

# Copy workspace config
ADD ./analysis_tools ./analysis_tools
ADD ./distribution_tools ./distribution_tools
ADD ./original_data ./original_data
ADD ./rad_main.py .
ADD ./requirements.txt .
ADD ./run.sh .

RUN chmod +x run.sh
#RUN pip install -r requirements.txt

ENTRYPOINT ["/opt/rad/run.sh"]
