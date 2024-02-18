import sys
#尽量先判断path是否存在
path=sys.argv[1]#获取用户执行脚本时传入的参数
# 如 G:\Anaconda3\envs\sharkfin\python.exe "G:\pycharm\PyCharm Community Edition 2022.3.3\defunction\Module deletion.py" D:\test
# 该语句位命令行cmd 中的语句  在cmd中输入上面的地址后 即执行 该脚本 删除path ,相当于这一大长串是输入给cmd的参数 回车就执行函数。
# sys.argv=["G:\pycharm\PyCharm Community Edition 2022.3.3\defunction\Module deletion.py","D:\test"]

import shutil #删除模块

shutil.rmtree(path)