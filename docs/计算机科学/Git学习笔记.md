# 1 Git简介

Git是目前世界上最先进的分布式版本控制系统，没有之一。Git可以自动记录每次文件的改动，还可以让同事协作编辑。

## 1.1 Git的诞生

Linus在1991年创建了开源的Linux，Linux系统的壮大是靠全世界的志愿者参与。但是在2002年以前，志愿者把源代码文件通过diff方式发给Linus，由Linus本人通过手工方式合并代码。

2002年Linus选择了BitMover公司的商业版本控制系统BitKeeper管理代码。但2005年Linux社区开发Samba的Andrew试图破解BitKeeper的协议，被BitMover公司发行了，BitMover要收回Linux社区的免费试用权。

Linus花了两周时间自己用C写了一个分布式版本控制系统，这就是Git！Git迅速成为了最流行的分布式版本控制系统，2008年GitHub网站上线了，无数开源项目开始迁移至GitHub。

## 1.2 集中式 vs 分布式

**集中式版本控制系统**

+ 版本库集中存放在中央服务器，干活时先从中央服务器取得最新的版本，完成后要把自己的活推送给中央服务器；
+ 必须联网才能工作，性能和安全性是关键点；

![central-repo](https://www.liaoxuefeng.com/files/attachments/918921540355872/0)

**分布式版本控制系统**

+ 无中央服务器，每个人的电脑上都是一套完整的版本库，多人协作只推送修改部分；
+ 安全性大大提升，不需要联网，强大的分支管理能力；

![distributed-repo](https://www.liaoxuefeng.com/files/attachments/918921562236160/0)

主要区别在于历史版本库的存放，集中式系统的历史版本只存在与中央服务器，而分布式控制系统在每个本地库都有历史记录存放。

# 2 创建版本库及版本回退

# 2.1 安装Git

Git可以在Linux、Unix、Mac和Windows平台上运行。

# 2.2 创建版本库

版本库（Repository）可以理解成一个目录，该目录内所有文件都可以被Git管理起来，美国文件的修改和删除，Git都能跟踪、追溯和还原。

创建版本库：

+ 选择一个合适的地方创建目录；
+ 通过*git init* 命令把该目录编程Git可以管理的仓库；
+ 通过*git add* 命令把文件添加到仓库；
+ 通过*git commit* 命令把文件提交到仓库；

Git配置

> $ git config --global user.name "Your Name"
>
> $ git config --global user.email "email@example.com"



# 2.3 版本控制

通过*git status* 命令掌握仓库当前的状态；

```
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   readme.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

通过*git diff* 命令查看修改内容；

```
$ git diff readme.txt 
diff --git a/readme.txt b/readme.txt
index 46d49bf..9247db6 100644
--- a/readme.txt
+++ b/readme.txt
@@ -1,2 +1,2 @@
-Git is a version control system.
+Git is a distributed version control system.
 Git is free software.
```

### 2.3.1 版本回退

- `HEAD`指向的版本就是当前版本，因此，Git允许我们在版本的历史之间穿梭，使用命令`git reset --hard commit_id`；
- 穿梭前，用`git log`可以查看提交历史，以便确定要回退到哪个版本；
- 要重返未来，用`git reflog`查看命令历史，以便确定要回到未来的哪个版本；

### 2.3.2 工作区、暂存区和版本库

**工作区**（Working Directory）：电脑中能看到的目录；

![working-dir](https://www.liaoxuefeng.com/files/attachments/919021113952544/0)

**版本库**（Repository）：包括工作区、暂存区、第一个分支`master`和指向`master`的指针`Head`；

![git-repo](https://www.liaoxuefeng.com/files/attachments/919020037470528/0)

将文件往版本库里添加时是分两步执行的:

- 第一步是用`git add`把文件添加进去，实际上就是把文件修改添加到暂存区；

- 第二步是用`git commit`提交修改，实际上就是把暂存区的所有内容提交到当前分支；

Git管理的是修改，不是文件。每次修改，如果不用*git add* 到暂存区，就不会加入到*commit* 中。

### 2.3.3 撤销修改

**丢弃工作区的修改**：

> $ git checkout -- <file>

两种情况：

+ 一种是file自修改后还没有被放到暂存区，现在，撤销修改就回到和版本库一模一样的状态；

+ 一种是file已经添加到暂存区后，又作了修改，现在，撤销修改就回到添加到暂存区后的状态;

**丢弃暂存区的修改**

改乱了工作区某个文件的内容同时还添加到了暂存区，想丢弃修改时，先使用命令`git reset HEAD <file>`，之后按撤销工作区修改进行操作。

**进行了commit命令提交的修改**

已经提交了不合适的修改到版本库时，想要撤销修改，使用版本回退命令，前提是没有推送到远程库.

###  2.3.4 删除文件

在Git中，删除也是一个修改操作。可以用命令`git rm`删除一个文件。

 如果一个文件已经被提交到版本库，那么你永远不用担心误删，但是要小心，你只能恢复文件到最新版本，你会丢失**最近一次提交后你修改的内容**。

# 3 远程仓库

Git是分布式版本控制系统，同一个Git仓库，可以分布到不同的机器上，通过克隆复制原始版本库。

GitHub网站提供Git仓库托管服务，只要注册GitHub账号，可以免费获得Git远程仓库。由于本地Git仓库和GitHub仓库之间的传输是通过SSH加密的，需要进行设置：

**创建SSH Key**：

在用户主目录下，查看是否有.ssh目录，是否有`id_rsa`和`id_rsa.pub`两个文件；如果没有，

> $ ssh-keygen -t rsa -C "youremail@example.com"

**添加SSH Key：**

登录GitHub，在*Account settings* 中添加SSH Key，

## 3.1 添加远程仓库

