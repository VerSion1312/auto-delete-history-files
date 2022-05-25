# 自动删除历史文件

#### 介绍
在日常工作中经常会生成附件或上传附件，这些文件在使用后仍旧会存在服务器上，日积月累也会占用巨额的存储空间。这个小程序能够自动删除指定时间前的文件并生成日志。只需要配置目录、指定历史时长、设置定时任务即可。

#### 结构说明

1. `/code `目录为程序源码
2. `/exe` 目录为可执行文件
3. `delHisFileConfig.vcfg`文件为配置文件

#### 使用说明

1. 使用 **记事本** 或 **Visual Studio Code** 等文本编辑软件打开配置文件`delHisFileConfig.vcfg`

   > 注意：打开配置文件后可能会出现乱码的情况，如下图：
   >
   > ![image-20220516174901058](https://version-pic-bed.oss-cn-hangzhou.aliyuncs.com/images/image-20220516174818700.png)
   >
   > 此时只需将编码规则改为 **GB2312** 即可。
   >
   > ![image-20220516175001553](https://version-pic-bed.oss-cn-hangzhou.aliyuncs.com/images/image-20220516175001553.png)
   >
   > ![image-20220516175317952](https://version-pic-bed.oss-cn-hangzhou.aliyuncs.com/images/image-20220516175317952.png)
   
2. 支持多个配置，多个配置通过换行来区分，即一行便是一个配置。

   配置行通过组合符号`(*#*)`来划分为两个配置项：

   ![image-20220516175856308](https://version-pic-bed.oss-cn-hangzhou.aliyuncs.com/images/image-20220516175856308.png)

   其中，`$folderLocation$=`后的值是需要删除的目录；`$deleteDays$=`后的值是天数。以上图中第一行为例，运行程序则会删除本地目录 ***D:\\_TempFiles\删除文件测试*** 中所有最后修改时间距今超过10天的文件。配置修改完成后保存关闭即可。
   
   > 配置文件请务必保证与主程序文件放在同一个目录下
   
3. 双击运行`deleteHistoryFiles.exe`即可。

4. 如有需要可以设置定时任务从而达到定期清理的效果，定时任务的设置此处不再赘述。
