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





# 安装SGE（Sun Grid Engine）

**前提条件：**

1. root用户
2. ubuntu 16.04



**1.安装SGE组件**

```bash
apt install --yes \
gridengine-master \
gridengine-client \
gridengine-exec \
gridengine-qmon
```

Configure SGE automatically? **YES**

SGE cell name: **default**

SGE master hostname: **<enter your master hostname>**

**2.在master主机上，设置SGE**

```bash
# 将当前主机设为master节点
qconf -as $HOSTNAME
```



**2.1 主机列表**

```bash
# 增加一个总的主机的列表
qconf -ahgrp @allhosts
```

在打开的文件中，设置主机列表：

hostlist **galaxy**

或者：

```bash
# 将当前主机添加到总的主机列表
qconf -aattr hostgroup hostlist $HOSTNAME @allhosts
```



**2.2 队列**

```bash
# 增加一个队列
qconf -aq all.q
```

在打开的文件中，设置队列：

hostlist              **@allhosts**

slots                 **8,[galaxy=8]**

shell                 **/bin/bash**



或者：

```bash
# 将总的主机列表添加到all.q
qconf -aattr queue hostlist @allhosts all.q

# 设置每个主机的CPU线程数
# master节点的CPU数减1
qconf -aattr queue slots "8, [$HOSTNAME=7]" all.q

# 改变默认的/bin/csh为/bin/bash
qconf -aattr queue shell /bin/bash all.q
```



**2.3 用户列表**

```bash
# 将当前用户加入到用户列表
qconf -au $USER users
```



**2.4 对计算资源的控制**

通常主要是对任务的CPU和内存需求进行控制。

默认是对硬件资源进行控制，也可以自定义控制变量。

全局资源控制： `qconf -sc`，定义资源的类型，以及哪些资源是可以供消耗的：

队列资源控制：`qconf -sq all.q`, 通过complex_values列出队列可供申请的资源，不设置表明资源是无限制的

节点资源控制：`qconf -se galaxy`，通过**complex_values        num_proc=8,virtual_free=16G**列出节点可供申请的资源，不设置表明资源是无限制的

提交任务时，通过`qsub -l vf=*G,p=num`来指定需要的CPU和内存



首先全局设置：

```bash
qconf -mc
```

修改成如下情况：

#name               shortcut   type        relop requestable consumable default  urgency

#----------------------------------------------------------------------------------------

num_proc            p          INT         <=    YES         YES        1        1000

virtual_free        vf         MEMORY      <=    YES         YES        0        0

> name - 资源名称
>
> shortcut - 资源名称缩写
>
> type - 资源类型
>
> relop - 资源可用性的判断，==表示申请的资源必须与提供的相等，<=表示申请的资源小于可提供的就可以
>
> requestable - 资源是否可请求：YES/NO
>
> consumable - 资源是否可消耗，YES/NO，当设置成YES，可申请资源会随着申请逐渐变少
>
> default - 资源消耗的默认值
>
> urgency - 优先级


**设置并环境**

```bash
qconf -ap smp
qconf -ap mpi
```

slots	**999**

投递时，-pe smp 10，相当于-l p=10，指定10个逻辑CPU


**最后**

```bash
# 修改任务监控的时间间隔
qconf -msconf
```

schedule_interval                 **0:0:5**



### **sge 需要掌握的几个基本概念**

| 名字                | 解释                                                         |
| :------------------ | :----------------------------------------------------------- |
| node                | A host computer in the cluster. A node may have multiple processors. Cetus’s nodes are named cetus01, cetus02, etc. |
| core                | A CPU may have multiple cores. A core is often thought of as a separate CPU in its own right, but technically it is not. It does function very much like a separate CPU, but since it shares a CPU with other cores it does not perform quite as well as a separate CPU would. Nonetheless, performance of multiple cores is close to that of the equivalent number of (single core) CPUs, and they are designed to function much like separate CPUs, so it is often practical to think of them as such. |
| queue               | An object which may contain a prioritized list of jobs for which requested resources for the jobs can be satisfied. A queue also has a list of nodes that are available to it, and a limit on the number of jobs that are allowed to run on each node from this queue. |
| queue instance      | A sort of mini-queue that is a branch of the queue on a node. For example, the test.q queue may have instances test.q@cetus01, test.q@cetus02, etc. |
| slots               | For a queue, the number of jobs that may run on a node from this queue. In other words, the number of jobs that may run in each of this queue’s instances. |
| consumable resource | A (usually numeric) resource, such as disk space or memory, for which each job may consume a portion. A resource may be attributable to the cluster as a whole, to a queue, or to a node. When a job is being scheduled, if it requests more than the available amount of a resource, the job is deferred until sufficient resources are available. |



**3.在其他主机上**

待续



**参考：**

https://github.com/GoogleCloudPlatform/solutions-google-compute-engine-cluster-for-grid-engine

https://qinqianshan.com/unix/linux/linux-sge/

https://peteris.rocks/blog/sun-grid-engine-installation-on-ubuntu-server/
https://blog.csdn.net/Xiao_Song_PKU/article/details/86553710





SGE错误：
error: commlib error: access denied (client IP resolved to host name "". This is not identical to cl

解决方法：

```bash
ifconfig
# 查看本机内网IP地址

vi /etc/hosts
# 增加以下一行，类似的其余行删掉
# 172.19.247.XXX  galaxy  galaxy
```