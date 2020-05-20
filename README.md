## 针对一日一报表格的自动填写脚本

### 1.windows下环境配置
python 3.7 + selenium + chrome + chrome driver

安装selenium: ```pip install selenium ```

在chrome输入网址 chrome://version/，查看可知版本，我的是`81.0.4044`。 在http://npm.taobao.org/mirrors/chromedriver/ 中找到81.0.4044里面的chromedriver_win32.zip下载，解压得到`chrome_driver.exe`。记下位置，后续用到。

### 2.创建填写personal.json
在项目目录下创建personal.json,并填下格式如下：
```
{
    "executable_path" : "C:\\Users\\chromedriver.exe",  # 刚解压的位置
    "web_url"  :  "https://baidu.com",                  # 自动表格的网址
    "username" :  "", # 登录的用户名
    "password" :  "", # 登录的密码
    "address"  :  ""  # 个人住址
}
```

### 3.扩展其他表格
当前项目仅解决，疫情期间地区或目前公司要求的一日一报填写，根据表格的前端代码进行针对性极强的预填，`仅供参考`。

如拓展填写其他预填项或拓展其他表格，请`自行修改代码`。
