# 基于Web的机器翻译系统
## 程序说明

### 简介
这个课程Demo, 以Web应用的形式，接收前端输入的中文语音，通过百度语音识别库，转化成文字，并且实现了一些额外的功能。


### 实现的功能
* 通过麦克风录制语音，转化成WAV文件。
* 通过调用[百度语音识别](https://ai.baidu.com/tech/speech/asr)，将WAV文件转化为相应的文字。
* 通过[百度翻译API](http://api.fanyi.baidu.com), 根据选择的语言，翻译上述文字。  

*目前支持的语言*  
    语言简写    | 名称 
 ---------- | --- 
 en |  英语 
 jp |  日语 
 ru | 俄语 
* 调用了[有道词典API](http://ai.youdao.com),实现了在翻译为英语的情境下，可以对翻译后文本出现的单词，显示其音标、词性、释义，通过语音合成功能，可以播放该单词的标准发音。
* 基于Web的系统搭建，逻辑端采用了python的Django,前端用到了Bootstrap。
* 可以查看历史的语音识别记录。

### 项目结构
由于设计到了后端设计的知识点，不会过多的介绍

```
.
├── db.sqlite3-----------------------------------数据库文件
├── HttpHandler
│   ├── __init__.py
│   ├── __pycache__
│   ├── settings.py------------------------------项目的配置文件
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── recorder
│   ├── admin.py
│   ├── apps.py
│   ├── dict.py----------------------------------调用有道API的处理
│   ├── __init__.py
│   ├── __pycache__
│   ├── static-----------------------------------服务器的静态资源
│   │   ├── js
│   │   └── mp3
│   ├── templates--------------------------------HTML资源
│   │   └── recorder
│   │       ├── error.html
│   │       ├── index.html
│   │       ├── result.html
│   │       └── table-list.html
│   ├── testReq.py
│   ├── tests.py
│   ├── translation.py---------------------------百度翻译API
│   ├── urls.py----------------------------------路由处理
│   ├── views.py
│   └── yysb.py----------------------------------语音识别
├── server.crt
└── server.key


```

## 环境配置

### 依赖 
* python 3.6.3及以上版本。本项目内置了python虚拟环境，理论上不用安装相关库，这里给出了库安装方法，使用了包管理工具pip.  
```
pip install django
pip intall Baidu-aip
```
* 数据库：由于数据量过小,使用了轻量级数据库sqlite,若果想要使用其他数据库，可参考[Django技术文档](https://docs.djangoproject.com/zh-hans/2.1/)。

### 如何在本地使用
 [项目地址](https://github.com/justin5718/PyProgram.git)

在根目录下打开控制台，输入指令
```
python manage.py runserver
```
然后在浏览器打开[localhost页面](httP://localhost:8000/recorder)，请检查本机的8000端口是否处于开启的状态，或者在配置文件下更改启动的端口h号。

![Aaron Swartz](https://raw.githubusercontent.com/justin5718/pic/master/1.png)
## 操作说明
按下录音键，停顿约一秒后开始说出纯中文，按下停止结束录音，选择目标语言，按下播放键播放先前的录音，以此来调试，最后按提交键，即可看到翻译文本。
![Aaron Swartz](https://raw.githubusercontent.com/justin5718/pic/master/2.png)
如果目标语言选择的是英语，可以通过将鼠标滑动到某一个单词，实现对该词的查询，如发音释义等。
右上角的History Query，可以查看历史的查询记录。然后感兴趣的同学可以看下技术栈。
## 未实现的功能
* 对其他语种实现字典查询功能。(没找到接口?)
* 滑动查词的缓存功能，目前每一次滑动都会发送一次请求，不太理想。
* 对一整句话的语音合成，有点难。
* 实现用户登录功能，或者用持久化，每个人只能看到自己的历史查询，现在实现的比较简单。
* 界面的美化，学不来学不来。
