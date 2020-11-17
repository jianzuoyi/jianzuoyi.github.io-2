Conda是一个包管理器，类似于手机上的AppStore或电脑上的软件管家，可以方便地安装各种软件，并且能够为每一个软件创建自己的运行环境，互不干扰。

Conda有两个版本：Anaconda和Miniconda，通过名字可以看出，前者比较全，但安装文件大。后者比较轻量级，安装文件小。我之前通过Miniconda安装有些软件缺少相关依赖无法运行，用Anaconda就没有问题。因此之后都尽量用Anaconda。

Anaconda主页：https://www.anaconda.com

Linux平台下载命令：

```bash
wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh
```

## 一、安装

```bash
1. bash Anaconda3-2020.07-Linux-x86_64.sh
2. 回车继续
3. 按几次空格，直到出现：
   Do you accept the license terms? [yes|no]
   [no] >>> yes
   输入yes继续
4. 输入anaconda的安装路径，默认安装在用户的HOME目录下：/home/username/anaconda3，回车
5. 最后询问是否将anaconda的程序路径加入环境变量中，输入yes，完成安装
```

## 二、添加镜像源

因为conda默认的镜像源都在国外，安装软件可能比较慢。因此使用conda之前，最好首先添加国内的镜像源，很简单，在HOME目录下创建一个`.condarc`文件，注意前面有一个点`.`开头，表明这是一个隐藏文件。

```bash
show_channel_urls: true
channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
```

这里添加的是清华大学的镜像源，也可以用其他的，如中山大学，豆瓣等。需要说明的是`bioconda`，这是一个专门存储生物信息学软件的频道，是生信软件的AppStore。

## 三、使用

Conda的命令很多，下面列举一些常用的。

安装、卸载：

```bash
conda install bwa
conda remove bwa
```

创建环境：

```bash
# 创建bwa独立的安装环境
conda create -n mybwa
# 激活刚创建的环境
conda activate mybwa
# 安装bwa
conda install bwa
# 验证一下bwa的安装位置
which bwa
# 退出新环境到默认环境base
conda deactivate
```

其他命令：

```bash
# 查看conda安装了哪些软件包
conda list
# 查看conda管理了哪些环境，其中带*号的是当前激活的环境
conda env list
# 搜索是否有可供安装的软件包
conda search bwa
```





