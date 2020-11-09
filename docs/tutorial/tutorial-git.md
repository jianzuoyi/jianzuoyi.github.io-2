版本控制及代码托管：我的最佳实践



> 版本控制及代码托管，新手往往认为很难，事实上并非如此，本文介绍一下我的最佳实践，其实常用的命令也就那么。



工作或学习过程中会写一些代码，存在本地的话容易丢失，也不方便与他人进行交流。



我一般是把代码托管在Github网站上，这样既解决了代码备份问题，其他人也可以方便地取得。



有人可能会问，如果我只想托管代码，不愿意让别人看到呢？有办法，Github上的代码仓库分为公开和私有两种，公开的所有人都可以访问，私有的只有自己能访问。



之前私有仓库是收费的，需要绑定一张能支付美元的信用卡进行扣费，我记得一年大概是400多接近500元人民币，这不便宜，也难住了一些没信用卡的用户。



不过自从微软收购Github后，私有仓库也免费了，感谢微软。



### 一、基本用法

要利用Github来托管代码，就要先学习一下Git语法。关于Git语法的学习，那真是多了去了，够写几本书。但实际上本人这么多年实践下来，其实最常用的就几个命令。

我的一般工作流程是这样的：

1. 在Github上创建项目仓库：先填写仓库的名字（Repository name*，必须），然后填写项目描述（Description，可选），其次”Add a README file“筛选框沟上，点击“Create repository”
2. 将仓库clone到本地，`git clone git@github.com:jianzuoyi/learngit.git`
3. 代码编写，查看工作区状态，`git status`
4. 将代码添加到暂存区`git add <file>`， <file>是文件名，`git add .`代表添加当前目录的所有修改到暂存区
5. 提交修改，`git commit -m <comment>`，<comment>表示给本次提交添加一个注释，最好认真填写，以便将来知道本次提交到底做了什么修改
6. `git push`，代码推送到远程仓库，至此就完成了代码的远程托管，非常简单

可见，git常用的命令也就是：

```bash
git clone
git status
git add
git commit
git push
```

当要修改本地仓库时，先`git pull`将本地仓库与远程仓库同步，再`git status`, `git add`, `git commit`, `git push`



熟练掌握这几个命令，已经能应付我们80%的工作需求了，这也符合所谓的二八法则，就是掌握20%的命令，完成80%的工作，其他命令需要时再去查。



下面我们再来简单介绍一下Git的核心概念：工作区，暂存区和版本库，Git版本控制就是基于这三个概念进行的。



1. 工作区（Working Directory），即工作目录，就是项目文件所在的目录，如learngit。

2. 暂存区（stage，或者index），故名思义，暂存工作区的文件修改，`git add <file>`就是将文件提交到暂存区

3. 版本库（Repository），工作区中一个隐藏的`.git`目录，即是Git版本库，它记录了项目文件的所有修改记录，通过版本库，你可以随时将文件的内容恢复成之前的某个版本

这里解释一下，为什么要在版本库与工作区之间增加一个暂存区呢，其实是有必要的。比如你一个文件修改了一大段内容，下面又要对这一大段内容进行修改，但是你又怕改错，这时候不妨`git add <file>`暂存一下，然后继续修改，如果要保存最新的修改结果，则再次`git add <file>`覆盖掉暂存区的内容，如果你改错了，则可以把文件恢复到暂存区中的状态。



暂存区的一大好处就是能够多次暂存，最后一次提交到版本库，这样能保证版本库的整洁，不至于那么混乱，试想你每做一点小的修改，就往版本库中提交一次，没有必要。



理解了工作区，暂存区，版本库的概念，那么平时工作，用到的相应命令也就好理解了。

1. 本地还没有代码库，从远程仓库克隆一个到本地```git clone```

2. 本地已经有代码库，修改代码之前先`git pull`与远程代码库同步

3. 当我敲了一会代码，想看下工作区的状态，用`git status`
4. 我想看下某个文件修改了哪些内容，`git diff <file>`，这个命令用于查看工作区的文件与暂存区的（如果有的话）或版本库中的对比

4. 当我觉得需要暂存一下工作内容了，用`git add`
5. 完成了修改，用`git commit`提交到代码库
6. 我想查看现在的版本库情况，`git reflog`，或者`git log --pretty=oneline`



### 二、版本回退

以上介绍的都是工作一帆风顺的情形，但是有些时候，我们发现文件修改错了，想退回到原来的版本，这要分多情况。



**情况1：工作区修改了，还没add到暂存区，需要放弃修改，直接恢复为版本库中的版本**

```bash
git checkout -- <file>
```



**情况2：工作区修改了，已经add到暂存区，又再次修改了，需要恢复成暂存区的版本**

```bash
git checkout -- <file>
```

`git checkout -- <file>`将工作区的内容恢复为最近的版本：暂存区的（如果有的话）或版本库中的



**情况3：工作区修改了，已经add到暂存区，还没commit，需要恢复成版本库中的版本**

```bash
git restore --staged <file>
git checkout -- <file>
# 分两步，先撤销暂存，再回到最新版本。如果不先撤销暂存，只checkout，则只会恢复成用暂存区
```



**情况4：工作区修改了，已经commit到版本库，需要恢复成commit前的版本**

```bash
git reset HEAD^ <file>	# 将上一个版本库中的内容放入暂存区
git checkout -- <file>  # 从暂存区恢复到工作区
```



**情况5：在版本之间切换**

```bash
git reset --hard HEAD^	# HEAD^， HEAD^^， HEAD~3
git reset --hard commit_id	# 在任意版本之间切换
```

HEAD指向的版本就是当前版本，Git允许在任意版本之间切换



### 三、远程仓库

版本管理的最佳实践就是先创建远程仓库，再克隆到本地进行修改，然后push到远程仓库。

但是有些时候代码已经存在本地了，需要将其推送到远程仓库，我通常是这样做的：

1. 在Github上创建项目仓库：先填写仓库的名字（Repository name*，必须），然后填写项目描述（Description，可选），点击“Create repository”，注意”Initialize this repository with:“下面的几个复选框都不要选，直接点“Create repository”

2. 这样会在弹出的页面中显示如下命令

   ```bash
   echo "# learngit" >> README.md
   git init
   git add README.md
   git commit -m "first commit"
   git branch -M main
   git remote add origin git@github.com:jianzuoyi/learngit.git
   git push -u origin main
   ```

3. 切换到本地的代码目录，运行上述命令，就可以在当前目录创建代为仓库，并且与远程仓库进行关联



### 四、分支管理

分支的作用：当一个功能还没开发完成时就提交代码，不完整的代码库会导致程序不能正常工作。如果等完成了再提交，又存在丢失每天进度的风险。



有了分支，就可以等开发完毕后一次性合并到原来的分支上。



查看分支：`git branch`

创建分支：`git branch <name>`

切换分支：`git switch <name>`或者`git checkout <name>`

创建+切换分支：`git switch -c <name>`或者`git checkout -b <name>`

合并某分支到当前分支：`git merge <name>`

删除分支：`git branch -d <name>`

查看分支合并图：`git log --graph --pretty=oneline --abbrev-commit`



与远程库合并：

* 先pull拉下来最新版

* 再push



当pull有冲突时：

```bash
git stash
git pull
git stash pop
git status
git diff
```



**参考**

廖雪峰的官方网站