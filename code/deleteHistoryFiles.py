from distutils.command.config import config
import os
import time
from warnings import catch_warnings
import os
import datetime
import time

folderLocation = ''
deleteDays = 10000000000000
configName = './delHisFileConfig.vcfg'
logPath = './deleteLog.vlog'


# 打开日志文件，如果不存在则创建
logFile = open(logPath, 'a+')
try:
    print('正在读取配置文件...')
    if not os.path.exists(configName):
        print('配置文件读取异常！已将异常信息记录至日志')
        raise Exception(time.strftime("%Y-%m-%d %H:%M:%S",
                        time.localtime()) + ' => 配置文件不存在，请确认后再尝试执行！')
    else:
        with open(configName, 'r') as cfgFile:
            line = cfgFile.readline()
            while line:
                if not (line.find('$folderLocation$') >= 0 and line.find('$deleteDays$') >= 0 and line.find('(*#*)') >= 0):
                    cfgFile.close()
                    raise Exception(time.strftime(
                        "%Y-%m-%d %H:%M:%S", time.localtime()) + ' => 读取配置文件失败！请检查配置文件内容是否合法！')
                folderLocation = line.split(
                    '(*#*)')[0].strip().split('=')[1].strip()
                deleteDays = int(line.split(
                    '(*#*)')[1].strip().split('=')[1].strip())
                if folderLocation == '' or deleteDays < 0:
                    print('配置文件读取异常！已将异常信息记录至日志')
                    cfgFile.close()
                    raise Exception(time.strftime(
                        "%Y-%m-%d %H:%M:%S", time.localtime()) + ' => 读取配置文件失败！请检查配置文件内容是否配置完整！')
                print('读取配置成功！')
                print('正在获取路径 '+folderLocation+' 的文件列表...')
                if not os.path.exists(folderLocation):
                    print('路径 '+folderLocation+' 不存在！')
                    raise Exception(time.strftime("%Y-%m-%d %H:%M:%S",
                                    time.localtime()) + ' => 路径 '+folderLocation+' 不存在！')
                # 获取文件的绝对路径
                for root, dirs, files in os.walk(folderLocation):
                    for file in files:
                        # 使⽤join函数将⽂件名称和⽂件所在根⽬录连接起来
                        filePath = os.path.join(root, file)
                        fileTime = datetime.datetime.utcfromtimestamp(
                            os.path.getmtime(filePath))
                        if fileTime < datetime.datetime.now()+datetime.timedelta(days=-1*deleteDays):
                            os.remove(filePath)
                            print('文件 '+filePath+' 已删除')
                            logFile.writelines(time.strftime(
                                "%Y-%m-%d %H:%M:%S", time.localtime()) + ' => 文件 '+filePath+' 删除成功\n')
                print('对路径 '+folderLocation+' 的清理已完成！')
                line = cfgFile.readline()
            cfgFile.close()
except Exception as msg:
    logFile.writelines(str(msg)+'\n')
    print('error:'+str(msg))
finally:
    logFile.close()
