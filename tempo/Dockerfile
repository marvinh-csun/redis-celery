FROM python:3.11-bullseye


WORKDIR /code
COPY . /code
# RUN apt-get -y update
# RUN apt-get -y install cmake
# RUN apt-get -y update
# RUN apt-get -y install build-essential libeigen3-dev libyaml-dev libfftw3-dev libavcodec-dev libavformat-dev libavutil-dev libswresample-dev libsamplerate0-dev libtag1-dev libchromaprint-dev
# RUN apt-get -y update
# RUN apt-get -y install python3-dev python3-numpy-dev python3-numpy python3-yaml python3-six
# RUN apt-get -y update
# RUN pip3 install ipython numpy matplotlib pyyaml
# RUN git clone https://github.com/MTG/essentia.git essentia && cd essentia && python3 waf configure --with-python && python3 waf  && python3 waf install && ldconfig
RUN pip3 install -r requirements.txt 

EXPOSE 5011
