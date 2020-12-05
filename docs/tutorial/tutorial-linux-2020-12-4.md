# 简哥的Linux私房菜：生信篇

## 前言

Linux命令很多，但是对于生物信息学，常用的也就那么几十个。为此，我写了这本相对实用的小册子，以便读者能以最快的时间入门Linux。这本书应该做为生物信息学新人首先要掌握的第一门课程。

## 说明

全书分为三个部分：

* 基础篇
* 进阶篇
* 工具参考篇

## 建议

1. 最好安装一个Linux系统（对于新手Ubuntu容易入门），将教程中的命令敲到bash中看看效果
2. 如果有兴趣，可以在了解之后立即查看相关更完备的内容（比如查阅官方文档）

## 版权声明

> 本书为开源图书，版权归作者所有；欢迎下载及编辑（个人用途），但未经作者同意必须保留此段声明，且不可用于商业用途，否则保留追究法律责任的权利。
>
> * 作者：简佐义
> * 博客：https://jianzuoyi.github.io
> * 知乎：https://www.zhihu.com/people/jianzuoyi
> * 公众号：简说基因

## Linux基础

这一部分主要介绍Linux常用命令工具，比如文件管理、文本处理；为了让读者用最少的时间掌握到常用的知识，对于每个工具的举例，尽量做到小而精。

### 1. 获得帮助

在linux终端，面对命令不知道怎么用，或不记得命令的拼写及参数时，我们需要求助于系统的帮助文档； linux系统内置的帮助文档很详细，通常能解决我们的问题，我+们需要掌握如何正确的去使用它们；

#### 1.1 获得帮助

```bash
man command			# 查看命令command的说明文档
```

* 按`空格`向下翻页，按`b`向上翻页，按`q`退出。

```bash
which command		# 命令在哪儿
```

#### 1.2 你好世界

```bash
echo hello world	# 大家好
whoami				# 我是谁
pwd					# 我在哪儿
last				# 我什么时候登录过
history				# 我用过什么命令
w					# 都有谁和我同时在线
exit				# 我要退出登录
```

### 2. 文件目录

文件管理不外乎文件或目录的创建、删除、查询、移动，有mkdir/rm/mv

文件查询是重点，用find来进行查询；find的参数丰富，也非常强大；

查看文件内容是个大的话题，文本的处理有太多的工具供我们使用，在本章中只是点到即止，后面会有专门的一章来介绍文本的处理工具；

有时候，需要给文件创建一个别名，我们需要用到ln，使用这个别名和使用原文件是相同的效果；

#### 2.1 显示目录 ls

显示当前目录下的文件或目录：

```bash
ls     					# 显示目录内容
ls -l  					# 以列表显示形式显示目录内容
ll -h  					# 以人类可读的方式显示文件大小
ll -t  					# 以文件的修改时间排序，最新修改的在最前面
ll -tr 					# 以文件的修改时间排序，最新修改的在最后面
ls | cat -n				# 给每项文件前面增加一个id编号
ls `pwd`/file  			# 显示文件的绝对路径
```

`ls -l`如此常用，以至于我们需要为它建立一个别名，并放在`~/.bashrc`文件中，以后就可以直接使用别名`ll`了，更方便：

```bash
alias ll='ls -l'
```

显示目录树：

```bash
tree					# 以树状形式显示当前目录的结构
```



#### 2.2 切换目录 cd

```bash
cd dir    # 切换到目录dir
cd	      # 切换到用户的HOME目录
cd ~	  # 同cd，~表示HOME目录
cd ..     # 切换到上一级目录；一个点.表示当前目录，两个点..表示上一级目录
cd -      # 切换到进入当前目录之前所在的目录
```

#### 2.3 查看文件 cat

查看文件内容：cat、head、tail、less

```bash
# 一次性把文件内容输出到屏幕
cat file		# 查看文件内容
cat -n file		# 查看文件内容，同时显示行号
cat -A file		# 显示文件TAB键、换行符等信息

# 分屏显示文件内容
less file       # 分屏显示文件内容，按空格键显示下一页，按下/后可以搜索内容
less -SN file   # 显示文件的行号，并且截断太长的行 

# 查看文件前面多少行
head file	    # 默认显示文件前10行
head -n 20 file # 显示文件前20行

# 查看文件后面多少行
tail file		# 默认显示文件后10行
tail -n 20 file	# 显示文件后20行
tail -n +2 file	# 跳过第1行，显示从第2行开始的所有行，可用于跳过文件的标题行
tail -f file	# 当文件的内容还在增加时，实时显示末尾增加的内容，常用于查看日志文件的更新情况
```

查看两个文件之间的差别：

```bash
diff file1 file2
```

#### 2.3 创建目录 mkdir

创建目录：

```bash
mkdir dir           # 创建dir目录
mkdir -p dir1/dir2  # 递归创建目录，如dir1不存在，会先创建dir1
```

创建空文件：

```bash
touch file					# 创建一个空文件
touch {file1,file2,file3}	# 同时创建3个文件
```

#### 2.4 复制/移动/删除 cp mv rm

```bash
scp file1 file2		    # 将file1复制一份，命名为file2，复制目录要加-r参数：scp -r
scp -r from_dir to_dir  # 复制目录，要加-r参数
mv file1 dir1/			# 将file1移动到dir1/目录下
mv file1 file2			# 重命名：即将file1移动成为file2
rm file					# 删除文件
rm -f file				# 文件若不存在，删除时会报错，加-f参数就不会报错
rm -r dir1				# 删除目录，要加-r参数
rm -rf dir1				# 删除非空目录
```

#### 打包压缩

```bash
# 平时tar基本上就能完成打包、压缩、解压的任务了
tar czvf file.tar.gz files	# 打包并压缩
tar xvf file.tar.gz			# 解包，解压缩

gzip file					# 压缩
gunzip file.gz				# 解压
```

用tar实现文件夹同步，排除部分文件不同步：

```bash
tar --exclude '*.fq.gz' -cvf - /path/to/source | (cd /path/to/target; tar xvf -)
```



#### 2.5 查找文件 find

查找文件或目录：

```bash
find dir -name file			# 在dir/目录下查找名为file的文件，dir可以省略，默认在当前目录下查找
find dir -name '*file*'		# 在dir/目录下查找包含file关键词的文件，-name参数支持正则表达式
```

##### 定制搜索

* 按类型搜索
  * -type参数：f 文件；d 目录；l 符号链接

```bash
find dir -type f -name file			# 在当前目录下查找文件
find dir -type d -name dir			# 在当前目录下查找目录
```

* 按时间搜索
  * -atime 访问时间 (单位是天，分钟单位则是-amin，以下类似）
  * -mtime 修改时间 （内容被修改）
  * -ctime 变化时间 （元数据或权限变化）

```bash
find . -atime 7 -type f		# 最近第7天被访问过的所有文件
find . -atime -7 -type f	# 最近7天内被访问过的所有文件
find . -atime +7 -type f	# 查询7天前被访问过的所有文件
```

* 按大小搜索
  * 大小单位：k M G

```bash
find . -type f -size +2k
```

* 按权限搜索

```bash
find . -type f -perm 644	# 找具有可执行权限的所有文件
```

* 按用户搜索

```bash
find . -type f -user weber  # 找用户weber所拥有的文件
```

##### 找到后执行动作

* 删除

```bash
find dir -name file -delete		# 查找文件并删除
find dir -name file | xargs rm	# 同上
```

* 执行动作

```bash
find -type f -exec rm {} \;		# 查找文件并删除
find -type f -exec cp {} dir \;	# 查找文件并拷贝到某个文件夹
```

{}是一个特殊的字符串，对于每一个匹配的文件，{}会被替换成相应的文件名。

* 结合多个命令

  如果需要后续执行多个命令，可以将多个命令写成一个脚本。然后 -exec 调用时执行脚本即可:

```bash
-exec ./command.sh {} \;
```

##### -print的界定符

默认使用'\n'作为文件的界定符；

-print0使用'\0'作为文件的界定符，这样就可以搜索包含空格的文件；

##### 快速查询

```bash
locate file
```

与`find`不同，`locate`并不是实时查找，而是根据数据库中的文件索引信息。因此需要更新数据库，获得最新的文件索引信息：

```bash
updatedb
```

#### 2.8 创建链接文件 ln

Linux链接文件分两种：

* 软链接：类似于Windows下的快捷方式，源文件删除后，链接文件不可用；

* 硬链接：源文件删除后，链接文件仍然可以用。要删除文件，必须删除源文件及所有链接文件。

```bash
ln -s file fileLink	# 软链接（fileLink为新建的链接文件）
ln -sf file fileLink# 与上述命令的区别是：当fileLink已经存在时，强制创建
ln file fileHard	# 硬链接
```

#### 2.9 管道和重定向

* 命令连接执行，前一条命令的输出，作为后一条命令的输入：使用管道符号`|`

  `command1 | command2`

* 命令串联执行，前一条命令成功与否，都会执行后一条命令：使用分号`;`

  `command1;command2`

* 前面成功，则执行后面一条，否则不执行：使用与符号`&&`

  `command1 && command2`

* 前面失败，则执行后面一条，否则不执行：使用或符号`||`

  `command1 || command2`

Linux中常用重定向操作符有：

1. 标准输入（/dev/stdin）：代码为0， 使用<或<<
2. 标准输出（/dev/stdout）：代码为1，使用>（覆盖）或>>（追加）
3. 标准错误输出（/dev/stderr）：代码为2，使用2>或2>>
4. &>  标准输出和错误输出同时重定向
5. /dev/null  代表垃圾箱，不想要保存的东西都可以重定向到这里

* 输出重定向就是将命令的结果重定向到文件，而不是输出到屏幕，通常用于保存命令的结果

```bash
./run.sh > run.sh.o		# 标准输出到run.sh.o日志文件
./run.sh 2> run.sh.e	# 标准错误输出到run.sh.e错误日志文件
./run.sh &> run.sh.log	# 标准输出和标准错误都输出到定一个文件
./run.sh &> /dev/null	# 丢弃标准输出和标准错误信息
> file					# 清空文件内容
```

* 输入重定向是将文件作为输入的来源，而不是键盘

```bash
command < file			# 将file的内容作为command的输入 
command << END			# 从标准输入（键盘）中读取数据，直到遇到分界符END时停止（分界符用户可以自定义）
command <file1 > file2	# 将file1作为command的输入，并将处理结果输出到file2
```

* 综合运用

```bash
#!/bin/bash

while read line
do
    do something
done < file.txt > result.txt
```

逐行读入file.txt的内容，处理之后，将结果保存到result.txt文件中。

#### 2.11 Bash快捷键

```bash
Ctrl + A	# 光标移动到行首
Ctrl + E	# 光标移动到行尾
Ctrl + K	# 从当前位置删除到行尾
Ctrl + U	# 从当前位置删除到行首
Ctrl + R	# 查找历史命令
Tab键	   # Tab键可以补全命令或文件路径，输入部分命令或路径时，尝试按Tab键补全
Ctrl + C	# 中止当前命令的执行
```



### 3. 文本处理

Linux文本处理的三驾马车：grep，sed，awk，对于生物信息数据分析来说具有非常重要的价值。这三个工具包含了文本处理最常见的几种需求：

* grep：文本搜索。
* sed：文本编辑。
* awk：文本分析。

很多时候，就是靠这三个工具干活，因此必须扎实掌握。

#### 3.1 文本搜索 grep

```bash
grep pattern files			 # 搜索文件中包含pattern的行
grep -v pattern files		 # 搜索文件中不包含pattern的行

grep -f pattern.txt files	 # 搜索的pattern来自于文件中
grep -i pattern files		 # 不区分大小写。默认搜索是区分大小写的
grep -i pattern files		 # 只匹配整个单词，而不是字符串的一部分（如搜索hello，不会匹配到helloworld）
grep -n pattern files		 # 显示行号信息
grep -c pattern files		 # 显示匹配的行数
grep -l pattern files		 # 只显示匹配的文件名
grep -L pattern files		 # 显示不匹配的文件名
grep -C number pattern files # 额外显示匹配行的上下[number]行
grep pattern1 | grep pattern2 files # 显示既匹配pattern1，又匹配pattern2的行
grep -E "pattern1|pattern2" files	# 显示匹配pattern1或者pattern2的行, grep -E相当于egrep

# 用于搜索的特殊字符
^: 表示行前
$: 表示行尾

grep '^#' result.vcf		# 显示VCF文件的表头信息
grep '^hello$' files		# 显示只包含hello的行
grep -v '^\s*$' file		# 删除空白行
```

#### 3.2 文本编辑 sed

sed是stream editor的缩写，中文称之为“流编辑器”。

```bash
sed command file
```

* command部分，针对每行要进行的处理
* file，要处理的文件

**Actions**

- d：删除该行
- p：打印该行
- i：在行的前面插入新行
- a：在行的后面插入新行
- r：读取指定文件的内容。
- w：写入指定文件。

```bash
sed -n '10p' file		# 显示第10行
sed -n '10,20p' file	# 显示第10到20之间的行
sed -n '/pattern/p' file# 显示含有pattern的行
sed -n '/pattern1/,/pattern2/p' file # 显示patter1与pattern2之间的行

sed '10d' file			# 删除第10行
sed '10,20d' file		# 删除第10到20之间的行
sed '/pattern/d'		# 删除匹配pattern的行
sed '/^\s*$/d' file		# 删除空白行
sed 's/^\s*//' file		# 删除行前的空白：空格，制表符
sed 's/\s*$//' file		# 删除行尾的空白：空格，制表符
sed 's/^\s*//;s/\s*$//' file # 删除行首和行尾的空白：空格，制表符

sed 's/AA/BB/' file		# 将文件中的AA替换成BB，只替换一行中第一次出现的AA，替换后的结果输出到屏幕
sed 's/AA/BB/g' file	# 将文件中的所有AA都替换成BB，替换后的结果输出到屏幕
sed -i 's/AA/BB/g' file # 将文件中的所有AA都替换成BB，直接更改文件的内容
sed '/CC/s/AA/BB/g' file# 只替换那些含有CC的行
sed 's/pattern/&XXXX/' file	# 在pattern之后加上XXXX。&表示之前被匹配的内容
sed 's/pattern.*/&XXXX' file# 在匹配pattern的行尾加上XXXX。pattern.*表示包含pattern的整行内容

sed -n '1~4s/^@/>/p;2~4p' file.fq > file.fa	# Fastq文件转Fasta文件
sed -n '2~4p' file.fq		# 提取Fastq文件的序列

sed 'y/ABC/XYZ/' file	# 将ABC逐字替换成XYZ

sed '1i\hello' file		# 在第1行前面插入一行，内容为hello，通常用来为文件增加标题
sed '1a\hello' file		# 在第1行后面插入一行，内容为hello
sed '1r file2' file1	# 在第1行后面读入file2的内容
sed '/pattern/w file2' file1 # 将匹配的行写入file2中
```

#### 3.3 文本处理 awk

Awk是一个强大的文本分析工具，它每次读入一条记录，并把每条记录切分成字段后进行分析。Awk官方文档是非常好的学习材料，通过`man awk`查看。

```bash
awk 'BEGIN { action } pattern { action } END { action }'
```

 **Awk程序通常是一系列 pattern {action}对：**

`pattern`，表示模式匹配，只处理匹配的行。pattern可以省略，表示匹配所有行

`action`，表示对匹配行所做的动作。{actions}可以省略，表示{ print }。`BEGIN`和`END`的{action}不能省略



**pattern可能是：**

`BEGIN`， 执行初始化操作，程序开始时执行一次

`END`，执行收尾工作，程序结束时执行一次

`expression`，一个表达式，既可以是判断语句，也可以是正则表达式

**常用参数**

* `-F value`		    设置域分隔符，相当于给FS内置变量赋值
* `-v var=value`    将变量value的值赋给程序变量var，-v可以多次使用

**记录与字段**

记录是一次读入的内容，通常是文件的一行，保存在字段变量$0中，记录可以被分割成字段，保存在变量$1，$2，...，$NF中。

**表达式与操作符**

Awk表达式的符号与C语言的类似，基本的表达式有数字，字符串，变量，字段，数组以及函数调用。变量无需声明，它们在首次使用时被初始化为`null`。

```bash
assignment          =  +=  -=  *=  /=  %=  ^=
conditional         ?  :
logical and         &&
logical or          ||
logical not         !
array membership    in
matching       		~   !~
relational          <  >   <=  >=  ==  !=
concatenation       (no explicit operator)
add ops             +  -
mul ops             *  /  %
unary               +  -
exponentiation      ^
inc and dec         ++ -- (both post and pre)
field               $
```

**正则表达式**

在Awk中语言中，通常测试一个记录、字段或字符串是否与一个正则表达式匹配，匹配返回1，不匹配返回0。正则表达式用两个反斜杠`/`包围。

```bash
expr ~ /r/							 # 评估expr是否与r匹配。匹配的意思是expr的一个子串是否在正则表达式r定义的字符串集中。

/r/ { action }, $0 ~ /r/ { action }	 # 两者相同， /r/ 等于 $0 ~ /r/
```

任何表达式都可以放到`~`和`!~`右边或者内建的需要正则表达式的地方。在必要的时候，该表达式会被转变成字符串，然后作为一个正则表达式来解释。以下三行awk命令完成同样的功能：输出第5列为10的的行。

```bash
seq 20 | xargs -n5 > file
# cat file
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20

awk '$5 ~ /10/' file
awk '$5 ~ "10"' file
awk '$5 ~ 10' file
```

**数组**

Awk支持一维数组。其表示方法为`array[expr]`，`expr`在内部被统一转换成字符串类型，因此A[1]，与A["1"]相同，事实上索引都是“1”。索引为字符串的数组被称为关联数组。`expr in array`用于判断数组元素array[expr]是否存在。

```bash
for ( var in array ) statement
```

**控制语句**

```bash
if ( expr ) statement
if ( expr ) statement else statement
while ( expr ) statement
do statement while ( expr )
for ( opt_expr ; opt_expr ; opt_expr ) statement
for ( var in array ) statement
continue
break
```

**内置变量**

* `NR` - 当前行数
* `NF` - 当前行的列数
* `RS`，行分隔符，默认是换行符
* `FS`，列分隔符，默认是空格和制表符
* `ORS`，输出行分隔符，默认为换行符
* `OFS`，输出列分隔符，默认为空格
* `FILENAME`，当前文件名

**内置函数**

字符串函数

sub()、substr()、gsub()，sprintf()，index()，length()， match()，split()，tolower(), toupper()

数学函数

sin()，cos(), ...

**输入输出**

有两个输出语句，`print`和`printf`

```python
print							# 打印整条记录到标准输出，相当于print $0
print expr1, expr2, ..., exprn	# 打印指定字段到标准输出
printf format, expr-list		# C语言printf函数的重用
```

输入函数getline有以下几种形式：

```bash
getline							# 读取下一条记录到$0，更新NF，NR和FNR
getline var						# 读取下一条记录到var，更新NR和FNR
getline < file					# 从文件读取记录到$0，更新NF
getline var < file				# 从文件读取记录到var
command | getline				# 通过管道传递command的结果到$0，更新NF
command | getline var			# 通过管道传递command的结果到var
```

```bash
seq 10 | awk '{print $0;getline}'					  # 显示奇数行
seq 10 | awk '{getline; print $0}'					  # 显示偶数行
seq 10 | awk '{getline tmp; print tmp; print $0}'	  # 奇偶行对调

awk 'BEGIN {"date" | getline;close("date");print $0}' # 得到系统当前时间

# fastq转换成fasta
awk '{getline seq; getline comment; getline quality; sub("@", ">", $0); print $0"\n"seq}' file
```

**示例**

```bash
awk '{print $0}' file	# 打印整行
awk '{print $1}' file	# 打印第一列
awk '{print $2}' file	# 打印第二列
awk '{print $NF}' file	# 打印最后一列
awk '{print $(NF-1)}' file#打印倒数第二列
awk -F ';' -v OFS='\t' '{print $1,$2,$NF}' file	# 读入的文件以逗号;分隔列，打印第1列，第2列和最后一列，并且打印时以制表符作为列的分隔符
number=10;awk -v n=$number '{print n}' file	# number的值被传给了程序变量n
awk '$2 > 100' file		# 打印第2列大于100的行
awk 'NR>1 && NR<4' file # 打印第2~3行

awk '/EGFR/' file		# 打印含有EGFR的行，相当于grep EGFR file
awk '$1 ~ /EGFR/' file	# 打印第1列含有EGFR的列

# 按指定列去除重复行
# cat file
1 2 3 4 5
6 2 8 9 10
11 12 13 14 15
16 17 18 19 20
awk '!a[$2]++' file		# 第二列出现两次2，只保留第一次出现的那一行，结果如下：
1 2 3 4 5
11 12 13 14 15
16 17 18 19 20

awk '{sum+=$1} END {print sum}' file	# 累加文件的第一列
awk '{sum+=$1} END {print sum/NR}' file	# 求第一列的平均数

# 从含有多条fasta序列的文件中提取指定序列
 awk -v RS=">" '/chr1/ {print $0}' hg19.fa	# 提取chr1的序列
 awk -v RS=">" '/chr1|chr2/ {print $0}' hg19.fa	# 提取chr1和chr2的序列
```

#### 合并文本（按行） cat

```bash
cat file          	  # 合并一个或多个文件至标准输出，当只有一个文件时，相当于显示所有文件内容
cat file1 file2       # 合并file1和file2的内容，并在屏幕上输出
cat R1.fq.gz R2.fq.gz # 可以合并gzip压缩文件，如测序数据原始reads的合并
```

#### 合并文本（按列） paste

```bash
paste file1 file2			# 按列将两个文本拼接在一起，默认中间加制表符
paste -d ' ' file1 file2	# -d参数可以改变列之间的分隔符
```

#### 合并文本（按列） join

#### 切分文本（按列）cut

```bash
cut -f 1 file					# 剪切文件的第1列
cut -f 1,2						# 剪切文件的第1，2列
cut -f 3-						# 剪切第3列及之后的所有列
cut -f 3 --complement file		# 取除第3列之外的所有列
cut -d ' ' -f 1 file			# 剪切第1列，但以空格作为列与列之间的分隔符。默认以TAB作为分隔符
grep '^>' test.fa | cut -c 2-	# 得到fasta文件中的序列名称（去掉了>符号）
```

* -d 指定分界符
* cut的范围
  * N- 第N个字段到结尾
  * -M 第1个字段到M
  * N-M N到M个字段
* cut的单位
  * -f 以字段为单位（使用分隔符）
  * -c 以字符为单位
  * -b 以字节为单位

#### 分割文件 split

```bash
split -d -l 10000 file chunk_	# 按行数分割文件，每个文件最多10000行，分割成的文件名为chunk_01, chunk_02。。。
split -d -b 100m file chunk_	# 按大小分割文件，每个文件最多100m，分割成的文件名为chunk_01, chunk_02。。。
```

#### 排序  sort

```bash
sort file				# 默认按字典序对文件进行排序
sort -k2,2 -k3,3 file	# 先按第2列排序，第2列相同，再按第3列排序
sort -k2,2n file		# 按第2列排序，且第2列是数字，升序
sort -k2,2nr file		# 按第2列排序，且第2列是数字，降序
sort -u file			# 先排序文件，然后去除相邻的重复行，只保留一条记录
```

#### 去重  uniq

```bash
sort file | uniq		# 去除相信的重复行，只保留一条记录，相当于： sort -u file

# 利用sort, uniq取两个文件的交、并、补集
sort a b | uniq			# 并集
sort a b | uniq -d > c	# 交集
sort a c | uniq -u 		# 补集
```



#### 统计文本  wc

```bash
wc -l file		# 统计行数
wc -w file		# 统计单词数
wc -c file		# 统计字符数
```

#### 格式转换  dos2unix

Linux很多工具都是针对纯文本文件的，并且需要是Unix-like格式的文本文件。但是很多时候文件是从Windows或Mac系统上传到Linux服务器上的，这可能导致文件格式不兼容，原因是不同平台生成的文本文件的换行符不一样。

| 操作系统 | 符号 | 正则表达式 |
| -------- | ---- | ---------- |
| Mac      | ^M   | \r         |
| Linux    | $    | \n         |
| Windows  | ^M$  | \r\n       |

```bash
cat -A file				# 查看文件换行符情况
dos2unix file			# Windows格式转换成Unix-like格式
```

#### 4.3 watch

使用watch 工具监控变化 当需要持续的监控应用的某个数据变化时，watch工具能满足要求； 执行watch命令后，会进入到一个界面，输出当前被监控的数据，一旦数据变化，便会高亮显示变化情况；

示例：有时候，我们运行一个软件或流程，有许多文件需要输出到一个目录中，但时间有点久，我们想实时查看文件的写入情况：

```bash
watch -n 3 -dc ls -l	# 实时高亮显示当前目录内容变化，每3秒刷新一次
```



### 7. 网络工具

#### 7.1 远程登录

```bash
ssh username@host					 # 登录远程服务器，回车后输入密码
```

* username：用户名
* host：服务器IP地址

#### 复制文件

scp复制文件：

```bash
scp username@host:/path/to/file .	 # 将远程服务器上的文件传输到当前目录，文件名保持不变，复制目录加参数-r
scp file username@host:/path/to/dir/ # 将本地文件复制到远程服务器，文件名保持不变，复制目录加参数-r
```



rsync同步文件:

rsync与scp不同，它只是做增量更新且支持断点续传，也就是要复制的文件存在于目标文件夹且内容与当前要复制的相同，则不会复制。

```bash
rsync -azvP dir1 dir2					# 将dir1的内容同步至dir2
rsync -azvP --delete dir1 dir2			# 同步dir2与dir1，dir1中删除的文件，dir2中也要跟着删除
rsync -azvP --exclude 'file' dir1 dir2  # 同步dir2与dir2，且将file排除在外
```

#### 下载文件

```bash
wget URL
```

常用选项：

* -c：断点续传
* -o：指定日志文件；输出都写入日志而不是屏幕
* -O：指定保存到本地的文件名

```bash
wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh	# 下载文件到当前目录，文件名保持不变
```

x

#### 文件校验

md5sum			# 生成，或验证文件的MD5值

### 5. 进程管理

使用进程管理工具，我们可以查询程序当前的运行状态，或终止一个进程；

任何进程都与文件关联；我们会用到lsof工具（list opened files），作用是列举系统中已经被打开的文件。在linux环境中，任何事物都是文件，设备是文件，目录是文件，甚至sockets也是文件。用好lsof命令，对日常的linux管理非常有帮助。

#### 5.1 查询进程

ps

```bash
ps aut		# 查看后台任务运行情况，第2列是任务的PID号
```

#### 5.2 终止进程

```bash
kill PID	# 杀死指定PID的进程 (PID为Process ID)
kill -9 PID # 删除编号为PID的任务
kill %job	# 杀死job工作 (job为job number)
```

#### 5.3 远程任务

nohup，disown - 远程任务管理:

```bash
nohup ./run.sh &> run.sh.o &	# 远程SSH登录服务器，在后台运行任务，断开远程连接后任务仍然在后台跑
```

* 如果运行任务时没有加nohup命令，但任务运行时间长，但又必须断开（比如快下班了），若不想让任务因为断开远程连接而中断，可以用disown命令补救

```bash
./run.sh	# 假如任务是直接这样开始跑的
ctrl + z	# 按ctrl + z，将任务放到后台
jobs		# 输入jobs命令，回车，可以看到任务是暂停的： [1]+  Stopped(SIGTSTP)        bash run.sh
bg			# 让后台暂停的任务开始运行
jobs		# 再次运行jobs，可以看到任务已经跑起来了：   [1]+  Running                 bash run.sh &
disown -r 	# 从当前shell中移除运行中的作业，至此，可以关掉终端回家了
```



### 9. 系统管理

```bash
df -h		# 查看磁盘使用情况，-h: human缩写，以易读的方式显示结果（即带单位：比如M/G，如果不加这个参数，显示的数字以B为单位）
du -sh		# 查看当前目录使用了多少磁盘空间
du -sh *	# 查看当前目录下各文件或文件夹使用的磁盘空间
```



top

```bash
top -c		# 进入top界面，-c显示完整的命令名
```

输入top命令后，进入到交互界面；接着输入字符命令后显示相应的进程状态：

对于进程，平时我们最常想知道的就是哪些进程占用CPU最多，占用内存最多。以下两个命令就可以满足要求:

* P: 根据CPU使用百分比大小进行排序。 
* M: 根据驻留内存大小进行排序。
* i: 使top不显示任何闲置或者僵死进程。

htop

```bash
htop		# top的完美替代品，Linux系统不自带，需要安装， ubuntu系统：apt install htop
```

查看内存使用量：

```bash
free -h		# 查看内存使用情况
```

xx

查询系统版本：

```bash
uname -a
lsb_release -a
```

查询硬件信息：

```bash
cat /proc/cpuinfo | grep processor | wc -l	# 查询CPU信息
cat /proc/meminfo							# 查看内存信息
```

系统时间：

显示时间

格式化时间

设置时间



设置系统日期和时间(格式为2014-09-15 17:05:00):

```bash
date					
date -s 2014-09-15 17:05:00
date -s 2014-09-15
date -s 17:05:00
```

设置时区：

```bash
tzselect		# 根据系统提示，选择相应的时区信息。
```

强制把系统时间写入CMOS（这样，重启后时间也正确了）:

```bash
clock -w
```

格式化输出当前日期时间:

```bash
date +%Y%m%d.%H%M%S
```



### 8. 用户管理

#### 8.1 用户

添加用户：

```bash
useradd -m username	# 创建用户账号和用户目录
```

* -m	创建用户账号时顺便创建用户目录/home/username

删除用户：

```bash
userdel username
```

* -r	删除用户的同时顺便删除其用户目录/home/username，不加该参数只会删除用户

更改密码：

```bash
passwd	    	   # 更改当前用户的密码
passwd username	   # 更改指定用户的密码
```

切换用户：

```bash
su username		   # 登录账号切换为username
```

#### 8.2 组

默认情况下，添加用户操作也会相应的增加一个同名的组，用户属于同名组； 查看当前用户所属的组:

```bash
groups
```

一个用户可以属于多个组，将用户加入到组:

```bash
usermod -G groupName username
```

查看系统所有组：

系统的所有用户及所有组信息分别记录在两个文件中：/etc/passwd , /etc/group 默认情况下这两个文件对所有用户可读：

```bash
less /etc/passwd
less /etc/group
```



#### 8.3 权限

改变文件读、写、执行等属性：

```bash
chmod +x file	# 增加[本人]可执行权限
chmod -x file	# 取消[本人]可执行权限
chmod a+x file	# 增加[所有人]可执行权限
chmod a-x file	# 取消[所有人]可执行权限
```

改变文件的拥有者：

```bash
chown jianzuoyi:jianzuoyi file			# 将文件的所有权给jianzuoyi
chown -R jianzuoyi:jianzuoyi dirname	# 将目录以及目录内的文件的所有权给jianzuoyi
```

#### 8.4 环境变量

我们要把安装软件的路径加入到环境变量`$PATH`中，一般在`~/.bashrc`文件中加入以下内容：

```bash
PATH=/path/to/soft/bin:$PATH
export PATH
```

这样就可以直接输入软件的名字运行软件了，如：

```bash
bwa					# 运行bwa软件
```

如果软件的安装路径没有加入环境变量中，使用软件时必须加上其路径（绝对的或相对的），如：

```bash
/path/to/bin/bwa	# 绝对路径：运行/path/to/bin目录下面的bwa
./bwa				# 相对路径：运行bwa，bwa在当前目录下	
```

注：`.bashrc`在/home/你的用户名/文件夹下，以隐藏文件的方式存储；可使用`ls -a`查看。



bashrc与profile都用于保存用户的环境信息，bashrc用于交互式non-loginshell，而profile用于交互式login shell。

/etc/profile，/etc/bashrc 是系统全局环境变量设定

~/.profile，~/.bashrc用户目录下的私有环境变量设定

当登入系统获得一个shell进程时，其读取环境设置脚本分为三步:

1. 首先读入的是全局环境变量设置文件/etc/profile，然后根据其内容读取额外的文档，如/etc/profile.d和/etc/inputrc
2. 读取当前登录用户Home目录下的文件~/.bash_profile，其次读取~/.bash_login，最后读取~/.profile，这三个文档设定基本上是一样的，读取有优先关系
3. 读取~/.bashrc

~/.profile与~/.bashrc的区别:

- 这两者都具有个性化定制功能
- ~/.profile可以设定本用户专有的路径，环境变量，等，它只能登入的时候执行一次
- ~/.bashrc也是某用户专有设定文档，可以设定路径，命令别名，每次shell script的执行都会使用它一次

例如，我们可以在这些环境变量中设置自己经常进入的文件路径，以及命令的快捷方式：

```bash
.bashrc
alias m='more'
alias cp='cp -i'
alias mv='mv -i'
alias ll='ls -l'
alias lsl='ls -lrt'
alias lm='ls -al|more'

log=/opt/applog/common_dir
unit=/opt/app/unittest/common

.bash_profile
. /opt/app/tuxapp/openav/config/setenv.prod.sh.linux
export PS1='$PWD#'
```

通过上述设置，我们进入log目录就只需要输入cd $log即可；

### 10. Bash编程

```bash
#!/bin/bash

command1

command2

...
```

`chmod +x run.sh` 给run.sh脚本增加可执行权限

执行脚本，以下三种方式都可以：

```bash
# 脚本在前台执行，标准输出和标准错误输出到屏幕
./run.sh
bash run.sh
sh run.sh		# 前提sh链接到了bash，如果没有，需要root权限执行命令：ln -sf /bin/bash /bin/sh

# 脚本在前台执行，标准输出和标准错误保存到文件
./run.sh &> run.sh.o

# 脚本在后台执行，在最后加上一个&符号
./run.sh &> run.sh.o &

# 脚本在后台执行，并且防断线（长时间运行任务时使用）
nohup ./run.sh &> run.sh.o &
```

#### 10.1 迭代文件中的每一行

* while循环法

```bash
while read line
do
    echo $line
done < file.txt

单行shell写法：
cat file.txt | while read line; do echo $line; done
```

#### 10.2 迭代一行中的每一个单词

```bash
for word in $line
do
    echo $word
done
```

#### 10.3 迭代单词中的每一个字符

${string:start_pos:num_of_chars}：从字符串中提取一个字符；(bash文本切片）

${#word}：返回变量word的长度

```bash
for((i=0;i<${#word};i++))
do
    echo ${word:i:1);
done
```



### 其他命令

```bash
time command	# 显示命令执行时间
seq 10			# 产生1到10的整数

```



## Linux进阶

### 环境搭配

x

### 程序安装

下载可执行文件

apt - Ubuntu

conda

源码安装

一般源代码提供的程序安装需要通过配置、编译、安装三个步骤；

1. 配置做的工作主要是检查当前环境是否满足要安装软件的依赖关系，以及设置程序安装所需要的初始化信息，比如安装路径，需要安装哪些组件；配置完成，会生成makefile文件供第二步make使用；
2. 编译是对源文件进行编译链接生成可执行程序；
3. 安装做的工作就简单多了，就是将生成的可执行文件拷贝到配置时设置的初始路径下；

#### 配置

```bash
./configure
```

* -prefix	使用的最常用选项，设置程序安装的路径；

#### 编译

```bash
make
```



#### 安装

安装做的工作就简单多了，就是将生成的可执行文件拷贝到配置时设置的初始路径下:

```bash
make install
```



## 工具参考篇

### 11.并行工具

xargs - 命令组合工具

```bash
cat file | xargs		# 将file的内容显示成一行
cat file | xargs -n3	# 将file的内容每3列一行进行输出
find /ifs/result -name '*.fq.gz' | xargs -n1 -I{} cp {} /ifs/data/	# 查找fq.gz文件并复制到/ifs/data目录下
find /ifs/result -name '*.fq.gz' | xargs tar czvf all.fq.gz			# 查找fq.gz文件并打包在一起
find . -type f -name '*.log' -print0 | xargs -0 rm -f				# 当rm文件过多时，可以这样删除
find . -type f -name '*.py' -print0 | xargs -0 wc -l				# 统计一个目录中所有python文件的行数
```

parallel - 并行工具

parallel是增强版的xargs。假如一个脚本文件中有4条命令：

```bash
# cat run.sh
echo a
echo b
echo c
echo d

# 同时执行4个任务，生信中常通过这种方式并行执行多个任务
cat run.sh | parallel -j 4	
```

```bash
find *.fq | parallel -j 12 "fastqc {} --outdir ."	# 同时执行12个Fastqc任务
find *.bam | parallel --dry-run 'samtools index {}' # 同时执行samtools index任务，--dry-run显示任务命令但不实际执行，用于命令检查
```

x

### vim

Git



如果你对生物信息学感兴趣，可看我在知乎上的文章：从菜鸟到专家。

https://linuxtools-rst.readthedocs.io/zh_CN/latest/base/02_file_manage.html#



自学生信之通过刷Rosalind学Python（一）：



生物信息学算法基础|Rosalind刷题笔记（一）：

生物信息学算法之Python实现|Rosalind刷题笔记（一）：

Rosalind刷题笔记

Rosalind生物信息学算法刷题笔记（一）：



题图

## 问题：



## 解题思路：



## 代码

