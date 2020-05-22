## 针对一日一报表格的自动填写脚本
### 0.效果
![image](https://github.com/tanrunj/Table_AutoFill_Tools/blob/master/gif.gif)

### 1.windows下环境配置
**python 3.7 + selenium + chrome + chrome driver**

安装selenium: ```pip install selenium ```

在chrome输入网址chrome://version/，查看浏览器版本，我的是`81.0.4044`。 
在http://npm.taobao.org/mirrors/chromedriver/ 中找到81.0.4044里面的chromedriver_win32.zip下载，解压得到`chrome_driver.exe`。记下位置，后续personal.json填写用。

### 2.创建填写personal.json
在项目目录下创建personal.json,填写个人隐私信息，格式如下：
```
{
    "executable_path" : "C:\\Users\\chromedriver.exe", 
    "web_url"  :  "表格的网址",                  
    "username" :  "登录的用户名",  
    "password" :  "登录的密码", 
    "address"  :  "个人住址"   
}
其中表格的网址需要每天更新，温度也需校准。
```
### 3.执行自动填写
```python autoFill.py```
可见进入登录页面，自动登录并填写**一日一报**，则成功执行。

最后，确保问卷信息正确无误才提交。因为疫情相关，**不能谎报**。

### 4.扩展其他表格
当前项目针对疫情期间或目前公司要求的一日一报填写，根据特定表格的前端代码进行针对性极强的预填，`只可仅供参考`。

如扩展填写其他预填项或延伸其他表格用途，请`自行修改代码`。
