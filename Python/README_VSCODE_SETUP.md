# VS Code 工作区配置说明

## 问题背景
之前运行Python脚本时，用户可能会意外输入`cd`命令而不是温度值，导致脚本崩溃。现在通过VS Code工作区配置从根本上解决这个问题。

## 配置内容

### 1. 工作区文件 (`python-basicex.code-workspace`)
- **自动设置工作目录**: 终端默认工作目录设置为 `/mnt/e/GitCodes/MyCodes/Python/basicEx/BlockI`
- **预定义任务**: 为常用脚本创建了一键运行任务
- **Python解释器**: 设置为 `/root/miniconda/bin/python`

### 2. 调试配置 (`.vscode/launch.json`)
- **调试设置**: 配置了多个调试配置，自动设置正确的工作目录
- **集成终端**: 调试时使用集成终端，避免目录问题

## 使用方法

### 方法1：使用工作区文件（推荐）
1. 在VS Code中打开 `python-basicex.code-workspace` 文件
2. VS Code会自动加载工作区配置
3. 现在可以直接运行脚本，无需手动切换目录

### 方法2：使用任务运行器
1. 按 `Ctrl+Shift+P` 打开命令面板
2. 输入 `Tasks: Run Task`
3. 选择要运行的脚本任务：
   - `Run centigrade.py` - 运行温度转换脚本
   - `Run circle.py` - 运行圆计算脚本  
   - `Run triangel.py` - 运行三角形计算脚本

### 方法3：使用调试功能
1. 按 `F5` 或点击调试面板
2. 选择相应的调试配置
3. 开始调试，工作目录会自动设置正确

### 方法4：直接运行（已修复输入验证）
即使直接运行脚本，现在也有输入验证保护：
```bash
/root/miniconda/bin/python /mnt/e/GitCodes/MyCodes/Python/basicEx/BlockI/centigrade.py
```
如果意外输入`cd`命令，程序会提示"输入错误！请输入有效的数字温度值。"并继续等待正确输入。

## 优势
- **避免目录切换问题**: 从根本上解决了意外输入`cd`命令的问题
- **提高开发效率**: 一键运行和调试，无需手动设置环境
- **更好的用户体验**: 清晰的错误提示和持续输入验证
- **项目标准化**: 统一的开发环境配置

## 已修复的脚本
- ✅ `centigrade.py` - 华氏温度转摄氏温度
- ✅ `circle.py` - 圆的周长和面积计算
- ✅ `triangel.py` - 三角形判断和面积计算

所有脚本现在都有完善的输入验证，能够优雅处理无效输入。
