# Automatically Delete History Files

#### Introduce

  Attachments are always generated or uploaded in daily work,these files will still exist on the server after be used,it will also take up a huge amount of storage space with time goes by. This mini program can automatically delete files which was created before a specified time and generate logs. All you have to do is configure a directory, specify the historical duration, and set the scheduled task.

#### Struct of Directory 

1. `/code `is the directory of program code
2. `/exe` is the directory of executable file
3. `delHisFileConfig.vcfg`is the configuration file

#### Instructions

1. Open the configuration file`delHisFileConfig.vcfg` with using text editing software such as **Notepad** or **Visual Studio Code**.

   > PS: Garbled code may appear after opening the configuration file, just like this:
   >
   > ![image-20220516174901058](https://version-pic-bed.oss-cn-hangzhou.aliyuncs.com/images/image-20220516174818700.png)
   >
   > At this time, just change the coding rule to **GB2312**.
   >
   > ![image-20220516175001553](https://version-pic-bed.oss-cn-hangzhou.aliyuncs.com/images/image-20220516175001553.png)
   >
   > ![image-20220516175317952](https://version-pic-bed.oss-cn-hangzhou.aliyuncs.com/images/image-20220516175317952.png)
   
2. Multiple configurations are supported. Multiple configurations are distinguished by line feed, that is, one line is one configuration.

   The configuration line is divided into two configuration items by the combination symbol `(*#*) `

   ![image-20220516175856308](https://version-pic-bed.oss-cn-hangzhou.aliyuncs.com/images/image-20220516175856308.png)

   the value after ` $folderlocation$= ` is the directory to be deleted, and the value after`$deleteDays$=` is the days count for delete.The first line example in the figure above,running the program will delete all files of the local directory  ***D:\\_TempFiles\删除文件测试***  which were last modified more than 10 days ago. Remember to save and close the configuration file after modification.
   
   > The configuration file must be placed in the same directory as the main program file
   
3. Then run`deleteHistoryFiles.exe` with double click.

4. If necessary, you can set scheduled tasks to achieve the effect of regular cleaning, the setting method of scheduled tasks will not be clarified here.
