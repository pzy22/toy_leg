

```bash
conda create -n go2gym python=3.8 -y
```

```bash
pip install torch==1.10.0+cu113 torchvision==0.11.1+cu113 torchaudio==0.10.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
```

```bash
cd ~/isaacgym/python && pip install -e . && cd 
```

```bash
pip install numpy==1.21 tensorboard setuptools==59.5.0
```


Tensorboard Checking the Training Curve
```bash
tensorboard --logdir=./ --port=8080
```