FROM nvcr.io/nvidia/l4t-ml:r32.6.1-py3

ADD dlib-19.17.tar.bz2 /
#dlib-19.17.tar.bz2 was commented out on dlib/cuda/cudnn_dlibapi.cpp "forward_algo = forward_best_algo;"
#refer https://github.com/ageitgey/face_recognition/blob/master/README_Japanese.md


RUN apt update -y && apt upgrade -y && \
    apt install -y \
		python-pip \
		python3-pip && \

    python3 -m pip install --upgrade pip && \
    python3 -m pip install lmdb bottle && \
    apt install -y \
	wget \
	nano \
	unzip \
	libcanberra-gtk* \

	cmake \
	libopenblas-dev \
	liblapack-dev \
	libjpeg-dev  &&\

    cd /dlib-19.17 && \
    python3 setup.py install && \
    cd / && \
    rm -R /dlib-19.17 && \
    pip3 install face_recognition


CMD ["/bin/bash"]
