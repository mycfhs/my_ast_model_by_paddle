"""
    @Name: models.py
    @Author: Yang Yicheng
    @Time: 2022/5/9
"""


import paddle
from paddlespeech.cli import ASRExecutor

model_list=['deepspeech2online_wenetspeech', 'conformer_wenetspeech']
modelName = 'deepspeech2online_wenetspeech'


print('Loading model...')
asr_executor = ASRExecutor()


def asr_model(filePath):
    return asr_executor(
        model=modelName,
        lang='zh',
        sample_rate=16000,
        config=None,  # Set `config` and `ckpt_path` to None to use pretrained model.
        ckpt_path=None,
        audio_file=filePath,
        force_yes=True,
        device=paddle.get_device())