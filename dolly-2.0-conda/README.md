# Introduction

How to run Dolly 2.0 locally using Conda.

## Installation

If you want to try this samples on your local machine, we would recommend you to install and use Conda, as it allows for a good Python environment control.

> Python 3.8+ is required to run the samples in this guide.

### Using Conda

Download Miniconda, for detailed information, check the Miniconda download page: <https://docs.conda.io/en/latest/miniconda.html>

- For Linux and [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/about)

```bash
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

- MacOS Intel

```bash
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o Miniconda3-latest-MacOSX-x86_64.sh
bash Miniconda3-latest-MacOSX-x86_64.sh
```

- MacOS Apple Silicon

```bash
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o Miniconda3-latest-MacOSX-arm64.sh
bash Miniconda3-latest-MacOSX-x86_64.sh
```

> You may need to restart your terminal or `source ~/.bashrc` or `~/.zshrc` to enable the conda command. Use `conda -V` to test if it is installed successfully.

Create new conda environment with Python 3.8

```bash
conda create -n dolly-2.0
```

Activate it.

```bash
conda activate dolly-2.0
```

Install PyTorch

```bash
conda install pytorch torchvision torchaudio -c pytorch
```

Install Dolly dependancies. *Notice* we had to install `deepspeed==0.9.0` in order for the example to work.

```bash
python -m pip install -r requirements.txt
```

Run the code

```bash
python dolly2-1.py
```
