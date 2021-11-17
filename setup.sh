#do with sudo in docker container
#We need dlib installation manually since cuBLAS is mounted after "docker start"(and can't use CUDA on dlib).
#So, we can't install dlib on the Docker file.
#refer
#https://forums.developer.nvidia.com/t/nvidia-l4t-base-missing-cublas-v2-h/174582/5


cd /dlib-19.22
python3 setup.py install
cd
rm -R /dlib-19.22