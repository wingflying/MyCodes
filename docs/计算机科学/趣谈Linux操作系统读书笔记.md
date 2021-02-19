# 1 入门准备
## 01 必要性

打开 Linux 操作系统这扇门，你才是合格的软件工程师
 - 服务器侧类Unix系统比例占70%
 - 移动互联网Android是基于Linux内核
 - 新技术（云计算、虚拟化、容器、大数据和人工智能）基于Linux技术
 - 牛系统（团购、电商、打车和快递）都是部署在Linux服务器上

研究 Linux 内核代码，你能学到数据结构与设计模式的落地，看到数据结构和算法的经典使用案例
 - 文件操作：通过阅读 Linux 代码，你能学到从应用层、系统调用层、进程文件操作抽象层、虚拟文件系统层、、具体文件系统层、缓存层、设备 I/O 层的完美分层机制，尤其是虚拟文件系统对于接入多种类型文件系统的抽象设计，在很多复杂的系统里面，这个思想都能用得上。
 - 数据结构和算法库：大部分情况下可以使用现成的数据结构和算法库，但某些场景对内存的使用需要限制到很小、搜索时间需要限制到很小，要定制数据结构，内核实现机制可以参考。

了解Linux操作系统生态，能让你事半功倍地学习新技术
 - Linux环境下容易找到现成工具，工作事半功倍，还能接触大牛思想，助力个人的技术进步和职业发展
 - 数据库、消息队列、大数据、虚拟化和容器等默认提供Linux下的安装和使用，默认适配
### 两大原则
####  趣谈
![img](https://static001.geekbang.org/resource/image/80/5d/80a4502300dfa51c8520001c013cee5d.jpeg)
#### 图解
![img](https://static001.geekbang.org/resource/image/bf/02/bf0bcbea6a24bc5084bc0d4ffca7c502.jpeg)
## 02 学习路径
### 六个坡
+ 抛弃旧的思维习惯，熟练使用Linux命令行
 >- 基础：--help、man
 >- 进阶：sed、awk、正则、管道、grep、find、shell脚本、vim、git
 >- 推荐：鸟叔的Linux私房菜
+ 通过系统调用或者glibc，学会自己进行程序设计
 >- 进程树 fork
 >- 进程同步 信号量
 >- 应用层与传输层的分界线 socket编程
 >- 推荐：Unix环境高级编程
+ 了解Linux内核机制，反复研习重点突破
 >- 内核机制分析
 >- 推荐：深入理解Linux内核
+ 阅读Linux内核代码，聚焦核心逻辑和场景
 >- 虚拟化 KVM
 >- 网络 内核协议栈
 >- 推荐：Linux内核源码情景分析
+ 实验定制Linux组件，已经没人能阻挡你成为内核开发工程师
![img](https://static001.geekbang.org/resource/image/9e/85/9e970ed142da439f6fbe6d7c06f11785.jpeg)
+ 最后一坡：面向真实场景的开发，实践没有终点
 >- 并发与并行
 >- 锁与保护
 >- 扩展性和兼容性



### 爬坡路线图

![img](https://static001.geekbang.org/resource/image/bc/5b/bcf70b988e59522de732bc1b01b45a5b.jpeg)

# 2 Linux操作系统综述
## 03 你可以把Linux内核当做一家软件外包公司的老板
操作系统就像一个软件外包公司，内核就相当于这家外包公司的老板：
![img](https://static001.geekbang.org/resource/image/e1/4a/e15954f1371a4c782f028202dce1f84a.jpeg)
操作系统内核结构图
![img](https://static001.geekbang.org/resource/image/21/f5/21a9afd64b05cf1ffc87b74515d1d4f5.jpeg)

## 04 快速上手几个Linux命令：每家公司都有自己的黑话

![img](https://static001.geekbang.org/resource/image/88/e5/8855bb645d8ecc35c80aa89cde5d16e5.jpg)
## 05 学会几个系统调用：咱们公司能接纳哪些类型的项目？

### 创建进程
创建进程的总结：
+ Linux中父进程调用fork创建子进程；
+ 父进程调用fork时，子进程拷贝所有父进程的数据接口和代码过来；
+ 当前进程是子进程，fork返回0；当前进程是父进程，fork返回子进程进程号；
+ 如果返回0，说明当前进程是子进程，子进程请求execve系统调用，执行另一个程序；
+ 如果返回子进程号，说明当前进程是父进程，按照原父进程原计划执行；
+ 父进程要对子进程负责，调用waitpid将子进程进程号作为参数，父进程就能知道子进程运行完了没有，成功与否；
+ 操作系统启动的时候先创建了一个所有用户进程的“祖宗进程”，课时1，第3题A选项：0号进程是所有用户态进程的祖先；
>创建进程的系统调用：fork；
>执行另一个程序的系统调用：execve；
>将子进程的进程号作为参数传给它，父进程就能知道子进程运行完了没有，成功与否：waitpid；
### 内存管理
内存管理总结
+  每个进程都有独立的进程内存空间，互相之间不干扰（隔离性）；
+  进程内存空间，存放程序代码的部分，称为代码段（Code Segment）；
+  存放进程运行中产生数据的部分，称为数据段（Data Segment）；
+  进程写入数据的时候，现用现分物理内存给进程使用；
+  分配内存数量比较小时，使用brk调用，会和原来的堆数据连在一起；需要分配的内存数据量比较大的时候，使用mmap，重新划分一块内存区域。
### 文件管理
文件操作六个最重要系统调用：
+ 打开文件：open
+ 关闭文件：close
+ 创建文件：creat
+ 打开文件后跳到文件某个位置：lseek
+ 读文件：read
+ 写文件：write
Linux一切皆文件，统一了操作的入口，提供了极大的便利。
### 信号处理（异常处理）
进程执行过程中一旦有变动，就可以通过信号处理服务及时处理。
### 进程间通信
有两种方式实现进程间通信
+ 消息队列方式:
    + 创建一个新的队列：msgget
    + 发送消息到消息队列：msgsnd
    + 取出队列中的消息：msgrcv
    
+ 共享内存方式：
    + 创建共享内存块：shmget
    
+ 将共享内存映射到自己的内存空间：shmat
  

利用信号量实现隔离性    
+ 占用信号量：sem_wait

+ 释放信号量：sem_post
伪代码：
>假设信号量为1
>signal = 1sem_wait伪代码
>while True {
>if sem_wait == 1；    
>signal -=1;    
>break;
>}
>code.code;
>sem_post伪代码
>signal +=1;

### 网络通信

+ 网络接口：socket
+ 网络通信遵循TCP/IP网络协议栈
### glibc
+ glibc是Linux下开源标准C库
+ glibc把系统调用进一步封
+ sys_open对应glibc的open函数
+ 一个单独的glibcAPI可能调用多个系统调用
+ printf函数调用sys_open、sys_mmap、sys_write、sys_close等等系统调用
### 小结
![img](https://static001.geekbang.org/resource/image/88/e5/8855bb645d8ecc35c80aa89cde5d16e5.jpg)
# 3 系统初始化
## 06 x86架构：有了开放的架构，才能打造开放的阵营
### 计算机逻辑结构
![img](https://static001.geekbang.org/resource/image/fa/9b/fa6c2b6166d02ac37637d7da4e4b579b.jpeg)

![img](https://static001.geekbang.org/resource/image/3a/23/3afda18fc38e7e53604e9ebf9cb42023.jpeg)

### x86逻辑结构

![img](https://static001.geekbang.org/resource/image/2d/1c/2dc8237e996e699a0361a6b5ffd4871c.jpeg)

+ CPU 包括: 运算单元, 数据单元, 控制单元    
  
    - 运算单元 只管算（加法/位移）
    - 数据单元 包括 CPU 内部缓存和寄存器, 暂时存放数据和结果    
    - 控制单元 获取下一条指令, 指导运算单元取数据, 计算, 存放结果- 进程包含代码段, 数据段等, 
    
+ CPU 执行过程:    
    - 控制单元 通过指令指针寄存器(IP), 取下一条指令, 放入指令寄存器中        
    - 指令包括操作和目标数据    
    - 数据单元 根据控制单元的指令, 从数据段读数据到数据寄存器中    
    - 运算单元 开始计算, 结果暂时存放到数据寄存器
    - 两个寄存器, 存当前进程代码段和数据段起始地址, 在进程间切换
    
+ 总线包含两类数据: 地址总线和数据总线

+ x86 开放, 统一, 兼容
    - 数据单元 包含 8个16位通用寄存器, 可分为2个8位使用
    - 控制单元 包含 IP(指令指针寄存器) 以及4个段寄存器 CS DS SS ES    
    - IP 存放指令偏移量    
    - 数据偏移量存放在通用寄存器中    
    - `段地址<<4 + 偏移量` 得到地址
    
+ 32 位处理器
    - 通用寄存器从8个16位拓展为 8个32位, 保留16位和8位使用方式
    
    - IP 从16位扩展为32位, 保持兼容
    
    - 段寄存器仍为 16位, 由段描述符(表格, 缓存到 CPU 中)存储段的起始地址, 由段寄存器选择其中一项    
    
    - 保证段地址灵活性与兼容性：16位为实模式, 32位为保护模式
    
    - 刚开机为实模式, 需要更多内存切换到保护模式
    
      

### 段寻址结构
![img](https://static001.geekbang.org/resource/image/e3/84/e3f4f64e6dfe5591b7d8ef346e8e8884.jpeg)



## 07 从BIOS到bootloader：创业伊始，有活儿老板自己上

+ ROM(read only memory）只读存储器
+ RAM(random access memory)随机存取存储器
+ BIOS(Basic Input and Output System)基本输入输出系统
+ MBR(Master Boot Record)主引导分区/记录

### BIOS初始化流程

+ 实模式只有1MB内存寻址空间（X86）
+ 加电，重置CS为0xFFFF、IP为0x0000，运行BIOS程序
  + 检查系统的硬件是否正常
  + 建立中断向量表和中断服务程序(因为需要用到键盘和鼠标，需要通过中断进行)
  + 在内存空间映射显存的空间![img](https://static001.geekbang.org/resource/image/5f/fc/5f364ef5c9d1a3b1d9bb7153bd166bfc.jpeg)

### BootLoader时期

+ Grub2工具(grand unified bootloader version） 

+ grub2首先会安装boot.img，它由boot.s编译而成。BIOS完成任务后，会将boot.img从硬盘加载到内存中的0x7c00开运行。由于512字节有限，boot.img做不了太多事。能做的最重要的一个事情就是加载Grub2的core.img。core.img由diskboot.img、lz_decompress.img、kernel.img和一系列的模块组成

+ 实时模式只有1M的地址空间，放不了太多，所以在解压缩之前，lzma_compress.img做了一个重要的决定，就是调用real_to_prot，切换到保护模式，这样就能在更大的寻址空间里面，加载更多的东西

  ![img](https://static001.geekbang.org/resource/image/2b/6a/2b8573bbbf31fc0cb0420e32d07b196a.jpeg)

从实时模式到保护模式做了哪些工作：
+ 启用分段，就是在内存中建立段描述表
+ 启用分页，打开第二十一跟地址线
+ 运行kernel.img选择一个操作系统启动内核

## 08  内核初始化：生意做大了就得成立公司

### 职能部门初始化

内核启动从入口函数start_kernel()开始：

![img](https://static001.geekbang.org/resource/image/cd/01/cdfc33db2fe1e07b6acf8faa3959cb01.jpeg)

+ 创建样版进程（0号进程）及各模块初始化
  +  创建0号进程：`set_task_stack_end_magic(&init_task)` and `struct task_struct init_task = INIT_TASK(init_task)`
  + 初始化中断, `trap_init()`. 系统调用也是通过发送中断进行, 由 `set_system_intr_gate()` 完成
  + 初始化内存管理模块, `mm_init()`
  + 初始化进程调度模块, `sched_init()`
  + 初始化基于内存的文件系统 rootfs, `vfs_caches_init()`
  + VFS(虚拟文件系统)将各种文件系统抽象成统一接口
  + 调用 `rest_init()` 完成其他初始化工作
+ 创建管理/创建用户态进程的进程（1号进程）
  + `rest_init()` 通过 `kernel_thread(kernel_init,...)` 创建 1号进程(工作在用户态).
  + 权限管理
      - x86 提供 4个 Ring 分层权限
      - 操作系统利用: Ring0-内核态(访问核心资源); Ring3-用户态(普通程序)
  + 用户态调用系统调用: 用户态-系统调用-保存寄存器-内核态执行系统调用-恢复寄存器-返回用户态
  + 新进程执行 kernel_init 函数, 先运行 ramdisk 的 /init 程序(位于内存中)
      - 首先加载 ELF 文件
      - 设置用于保存用户态寄存器的结构体
      - 返回进入用户态
      - /init 加载存储设备的驱动
   + kernel_init 函数启动存储设备文件系统上的 init
+ 创建管理/创建内核态进程的进程（2号进程）
  + `rest_init()` 通过 `kernel_thread(kthreadd,...)` 创建 2号进程(工作在内核态).
  + `kthreadd` 负责所有内核态线程的调度和管理

### 内核态与用户态

x86提供了分层的权限机制（Ring0到Ring3），操作系统很好利用了这个机制，将能够访问关键资源的代码放在Ring0（**内核态**，Kernel Mode），将普通的程序代码放在Ring3（**用户态**，User Mode）。

![img](https://static001.geekbang.org/resource/image/2b/42/2b53b470673cde8f9d8e2573f7d07242.jpg)

系统处于保护模式，保护模式可以访问更大空间，另一个功能是“保护”，也就是说，用户态代码想要执行更高权限的指令是被禁止的。用户态的代码要访问核心资源，需要暂停当前的运行，通过系统调用进入内核态执行程序。

![img](https://static001.geekbang.org/resource/image/d2/14/d2fce8af88dd278670395ce1ca6d4d14.jpg)

暂停瞬间的CPU寄存器状态保存和恢复

![img](https://static001.geekbang.org/resource/image/71/e6/71b04097edb2d47f01ab5585fd2ea4e6.jpeg)

### 小结



![img](https://static001.geekbang.org/resource/image/75/cd/758c283cf7633465d24ab3ef778328cd.jpeg)

## 09 系统调用：公司成立好了就要开始接项目

站在系统调用的角度，层层深入下去，就能从某个系统调用的场景出发，了解内核中各个模块的实现机制。Linux提供了glibc这个中介，可以封装成更加友好的接口。

### glibc对系统调用的封装

open函数定义：

> 1 int open(const char *pathname, int flags, mode_t mode)

+ glibc的源代码中，有个文件syscalls.list，列举了所有glibc函数对应当系统调用：

> 1 # File name 	Caller 	Syscall name 	Args 	Strong name	Weak name
>
> 2 	open			 -			 open				Ci: siv		_libc_open		_open open

+ glibc有一个脚本make-syscall.sh，可以根据配置文件，对每个封装好的系统调用，生产一个文件，定义了宏，例如#defien SYSCALL_NAME open。

+ gilbc还有一个文件syscall-template.S，定义了系统调用的调用方式。	
	
 > 1 T_PSEUDO（SYSCALL_SYMBOL，SYSCALL_NAME，SYSCALL_NARGS）
 >
 > 2 ret
 >
 > 3 T_PSEUDO_END(SYSCALL_SYMBOL)	
 >
 > 4 #define T_PSEUDO(SYMBOL, NAME, N) 	PSEUDO(SYMBOL, NAME, n)

PSEUDO也是一个宏
 > 1 #define PSEUDO(name, syscall_name, args)
 > 2 .text
 > 3 ENTRY(name)
 > 4 	DO_CALL(syscall_name, args);
 > 5 	cmpl $-4095, %eax;
 > 6 	jae SYSCALL_ERROR_LABEL

对于任何一个系统调用，会调用DO_CALL。

### 系统调用过程

将请求参数放在寄存器里面，根据系统调用的名称，得到系统调用好，放在寄存器eax里面，然后执行ENTER_KERNEL。

> 1 #define ENTER_KERNEL int $0x80

ENTER_KERNEL是一个软中断，通过int $0x80触发一个软中断，陷入(trap)内核：

> 1 ENTRY(entry_INT80_32)
>
> 2		ASM_CLAC
>
> 3		pushl 	%eax
>
> 4 		SAVE_ALL 	pt_regs_ax = $ - ENOSYS
>
> 5 		movl 	%esp, 	%eax
>
> 6		call 		do_syscall_32_irqs_on
>
> 7	.Lsyscall_32_done:
>
> 8	......
>
> 9 	.Lirq_return:
>
> 10		INTERRUPT_RETURN	

在进入内核之前，通过push和SAVE_ALL将当前用户态的寄存器，保持着pt_regs结构里面。然后调用d0_syscall_32_irqs_on，将系统调用号从eax里面取出了，根据系统调用号找到相应的函数进行调用。

系统调用结束后，在entry_INT80_32之后，调用INTERRUPT_RETURN（iret），将原来用户态保存的现场恢复回来，包括代码段、指令指针寄存器等，用户态进程恢复执行。

### 系统调用表

+ 32位系统调用表定义在arch/x86/entry/syscalls/syscall_32.tbl
+ 64位系统调用表定义在arch/x86/entry/syscalls/syscall_64.tbl

### 小结

![img](https://static001.geekbang.org/resource/image/86/a5/868db3f559ad08659ddc74db07a9a0a5.jpg)

## 10 进程：公司接这么多项目，如何管？

### ELF文件的生成

Linux系统下，二进制的可执行程序格式为ELF（Executable and Linkable Format），编译和链接过程如下图：

![img](https://static001.geekbang.org/resource/image/85/de/85320245cd80ce61e69c8391958240de.jpeg)

### ELF文件三种类型

+ 可重定位文件（Relocatable File）
+ 可执行文件（Executable File）
+ 共享对象文件（Shared Object）

**可重定位文件**

在编译的过程中，先做预处理工作，例如将头文件嵌入到正文中，将定义的宏展开，然后就是真正的编译过程，最终编译成为.o文件，这就是ELF文件的第一种类型，可重定位文件，格式如图：

![img](https://static001.geekbang.org/resource/image/e9/d6/e9c2b4c67f8784a8eec7392628ce6cd6.jpg)

+ ELF Header用于描述整个文件，在内核中有定义，分别为struct elf32_hdr和struct elf64_hdr
+ .text：编译好的二进制可执行代码
+ .data：已经初始化的全家变量
+ .rodata：只读数据，例如字符串常量、const的变量
+ .bss：未初始化全局变量，运行时会置0
+ .systab：符号表，记录的是函数和便利
+ .strtab：字符串表、字符串常量和变量名

各节的元数据存放在最后的节头部表（Section Header Table），每个Section都有一项，定义了struct elf32_shdr和struct elf64_shdr等。

**可执行文件**

编译好的代码和变量（.o文件），将来加载到内存的时候，要加载到一定位置。各section，例如.rel.text和.rel.data需要在链接的过程中重新定位，形成二进制可执行文件，格式如下：

![img](https://static001.geekbang.org/resource/image/1d/60/1d8de36a58a98a53352b40efa81e9660.jpg)

这个格式和.o文件大致相似，还是分成一个个的section，并且被节头标描述。这些section是多个.o文件合并过的，但这些section被分成了需要加载到内存里的代码段、数据段和不需要加载到内存里的部分，将小的section合成了大的端segment，并在最前面加了一个段头表（Segment Header Table）。在代码里面的定义为struct elf32_phdr和 struct elf64_phdr，除了有对段的描述外，最重要的是p_vaddr，是这个段加载到内存的虚拟地址。在ELF头里面，有一项e_entry，也是个虚拟地址，是这个程序运行的入口。

**共享对象文件**

静态链接库一旦链接进去，代码和变量的section都合并了，程序运行时就不依赖与这个库是否存在。缺点是相同的代码段如果被多个程序使用的话，在内存里面就有多份，而且一旦静态链接库更新了，如果二进制执行文件不重新编译，也不会自动更新。

因而就出现了**动态链接库**（Shared Libraries），不仅仅是一组对象文件的简单归档，而是多个对象文件的重新组合，可被多个程序共享。当一个动态链接库被链接到一个程序文件中时，最后的程序文件并不包括动态链接库中的代码，而仅仅包括对动态链接库的引用，并不保存动态链接库的全路径。

共享对象文件的差异点：

+ 多了一个.interp的Segment（动态链接器ld-linux.so）

+ 多两个section
  + .plt，过程链接表（Procedure Linkage Table）
  + .got.plt，全局偏移量表（Global Offset Table）

### 加载运行ELF文件

通过load_elf_binary加载ELF文件到内存中运行：

> 1 static struct 	linux_binfmt	elf_format = {
>
> 2			.module				= THIS_MODULE,
>
> 3			.load_binary	 	= load_elf_binary,
>
> 4 		   .load_shlib			= load_elf_library,
>
> 5			.core_dump	  	= elf_core_dump,
>
> 6			.min_coredump   = ELF_EXEC_PAGESIZE,
>
> 7 }	

调用关系： exec->do_execve->do_execveat_common->exec_binprm->search_binary_handler

![img](https://static001.geekbang.org/resource/image/46/f6/465b740b86ccc6ad3f8e38de25336bf6.jpg)

### 进程树

系统启动后，init进程会启动很多的daemon进程，为系统提供服务，然后启动getty，让用户登录，运行shell，用户启动的进程都是通过shell运行的，形成了一棵进程树：

+ 所有的用户态进程，祖先都是1号进程
+ 所有的内核态进程，祖先都是2号进程



![img](https://static001.geekbang.org/resource/image/4d/16/4de740c10670a92bbaa58348e66b7b16.jpeg)

### 小结

+ 通过文件编译过程，生成so文件和可执行文件

+ 用户态进程A执行fork操作，创建进程B，在进程B的处理逻辑中执行exec等系统调用

+ 系统调用通过load_elf_binary方法，将可执行文件加载到进程B的内存中执行

![img](https://static001.geekbang.org/resource/image/db/a9/dbd8785da6c3ce3fe1abb7bb5934b7a9.jpeg)

## 11 线程：如何让复杂的项目并行执行



