ubuntu 16.04

## 端口映射
```bash
iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
```

操作表名nat，添加规则名PREROUTING,协议名tcp，转发端口80，动作REDIRECT,到目标端口8080


此时，访问http://ip 和http://ip:8080是一样的。

## 安装库
```bash
apt install zlib1g-dev
apt install libbz2-dev
```


## 安装SJM
Installing SJM requires the following prerequisites:

1. GCC to compile the program.
2. The Boost regex library ([http://www.boost.org](http://www.boost.org/)). If you don't already have it on your system you must install boost before installing SJM. The easiest way is to install a prebuilt package, but you can download the source release from the boost web site and build it yourself. See the instructions here: http://www.boost.org/doc/libs/1_49_0/more/getting_started/index.html Be sure to follow the build instructions in the section called "Prepare to Use a Boost Library Binary".
3. The TCLAP library (http://tclap.sourceforge.net/). Download and install it before installing SJM.
4. A job scheduler: either Sun Grid Engine or Platform LSF. SJM doesn't currently support other schedulers but it is relatively easy to add a new one (see Other Job Schedulers below).
5. For Sun Grid Engine: a parallel environment for running multi-core (threaded) jobs on a single node of the cluster. Common names for this PE are "smp" or "shm". Here is a sample SGE configuration:



```bash
apt install libtclap-dev

apt install libboost-dev

apt install openjdk-8-jdk

apt install libboost-regex-dev

apt install gridengine-drmaa-dev

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/gridengine-drmaa/lib
export SGE_ROOT=/var/lib/gridengine

./sjm

跑任务时要先创建log文件夹

```

