## ASR project install instruction for windows

##### Note: This project is based on paddlespeech.

##### See:https://github.com/PaddlePaddle/PaddleSpeech#quick-start

##### It will take a long time if first use. Don't worry, just for downloading models.

### Requirements

conda

### step

`conda create -n ppasr python=3.7`

`conda activate ppasr`

`conda install -y -c conda-forge sox libsndfile bzip2`

`pip install pytest-runner -i https://pypi.tuna.tsinghua.edu.cn/simple`



------

paddlepaddle:

cpu:

`pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple`

cuda11.2:
 
`python -m pip install paddlepaddle-gpu==2.2.2.post112 -f https://www.paddlepaddle.org.cn/whl/windows/mkl/avx/stable.html`

others

https://www.paddlepaddle.org.cn/ 安装

-------

`pip install paddlespeech -i https://pypi.tuna.tsinghua.edu.cn/simple`

