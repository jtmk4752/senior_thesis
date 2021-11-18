FROM nvcr.io/nvidia/l4t-ml:r32.6.1-py3

ADD dlib-19.22.tar.bz2 setup.sh /

#dlib-19.22.tar.bz2 was commented out on dlib/cuda/cudnn_dlibapi.cpp "forward_algo = forward_best_algo;"
#refer https://github.com/ageitgey/face_recognition/blob/master/README_Japanese.md
#and I use dlib-19.22 because I don't need special command for CUDA setup.
#refer https://qiita.com/FXsimone/items/4864ff695d7599491ca8


RUN apt update -y && apt upgrade -y && \
    apt install -y \
		python-pip \
		python3-pip \
		
		#for ping command
		iputils-ping \
		net-tools && \

    python3 -m pip install --upgrade pip && \
    python3 -m pip install lmdb bottle && \
    apt install -y \
	wget \
	nano \
	unzip \

	#for changing dlib settings
	cmake \
	libopenblas-dev \
	liblapack-dev \
	libjpeg-dev  &&\
	
	python3 -m pip uninstall -y tensorboard tensorflow tensorflow-estimator torch torchvision torchaudio \
								onnx numba pandas scipy jupyter jupyter-client jupyter-console \
								jupyter-core jupyterlab jupyterlab-pygments jupyterlab-server jupyterlab-widgets && \

	cd / && \
	git config --global init.defaultBranch main && \
	git clone https://github.com/jtmk4752/senior_thesis_jetson_webserver.git && \

	#for https://qiita.com/tosikazu-s/items/7dd6cd6c3f4fc2e21743
	export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libgomp.so.1 >> ~/.bashrc


WORKDIR /senior_thesis_jetson_webserver

CMD ["/bin/bash"]
