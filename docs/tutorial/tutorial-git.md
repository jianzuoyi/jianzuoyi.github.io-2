## 创建版本库

```bash
git init
```



![git-repo](https://www.liaoxuefeng.com/files/attachments/919020037470528/0)



工作区（Working Directory），即工作目录

暂存区（stage，或者index）

版本库（Repository），工作区中的一个隐藏的`.git`目录，即是Git版本库



## 提交修改

Git管理的是修改而不是文件，只有先add到暂存区的修改，才会commit到版本库中。

文件往版本库中添加的时候分两步：

git add 将文件添加到暂存区

remote changes


![git-stage](https://www.liaoxuefeng.com/files/attachments/919020074026336/0)



git commit 将暂存区的所有内容提交到当前分支，暂存区变成空的了

![git-stage-after-commit](https://www.liaoxuefeng.com/files/attachments/919020100829536/0)





```bash
添加文件
git add <file>

提交文件，可多次add，一次commit
git commit -m <comment>

查看是否有文件修改
git status

查看文件修改的内容
工作区的文件与暂存区的（如果有的话）或版本库中的对比
git diff <file>

查看版本库情况
git reflog
git log --pretty=onelie
```





## 撤销修改

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



## 版本回退

```bash
git reset --hard HEAD^	# HEAD^， HEAD^^， HEAD~3
git reset --hard commit_id	# 在任意版本之间切换
```

HEAD指向的版本就是当前版本，Git允许在任意版本之间切换



## 远程仓库

```bash
git remote add origin git@github.com:jianzuoyi/learngit.git	# 关联远程库
git push -u origin master	# 第一次push
git push origin master	# 后续push

```



最佳实践是先创建远程库，再克隆下来：

```bash
git clone git@github.com:jianzuoyi/learngit.git
```



## 分支管理

分支的作用：

当一个功能还没开发完成时就提交代码，不完整的代码库会导致程序不能正常工作。如果等完成了再提交，又存在丢失每天进度的风险。



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



参考：
廖雪峰的官方网站
