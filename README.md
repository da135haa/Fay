[`English`](https://github.com/TheRamU/Fay/blob/main/README_EN.md)

<div align="center">
    <br>
    <img src="images/icon.png" alt="Fay">
    <h1>FAY</h1>
	<h3>Fay数字人框架 带货版</h3>
</div>

Fay 数字人框架 带货版用于构建：虚拟主播、现场推销货、商品导购，等数字人应用场景。该项目各模块之间耦合度非常低，包括声音來源、语音识别、情绪分析、NLP 处理、情绪语音合成、语音输出和表情动作输出等模块。每个模块都可以轻松地更换。

如果你需要的是一个人机交互的数字人助理，请移步 [`助理完整版`](https://github.com/xszyou/Fay/tree/fay-assistant-edition)

如果你需要是一个可以自主决策、主动联系主人的 agent，请移步[`agent版`](https://github.com/xszyou/Fay/tree/fay-agent-edition)

## **应用逻辑**

Remote Android 　　　　　　 Local PC 　　　　　 Remote PC

└─────────────┼─────────────┘

Aliyun API ─┐ 　　　 │

├── ASR

[FunASR](https://www.bilibili.com/video/BV1qs4y1g74e) ─┘ 　　 │ 　　 　 ┌─ Yuan 1.0

│ 　　 　 ├─ [LingJu](https://www.bilibili.com/video/BV1NW4y1D76a/)

NLP ────┼─ [GPT/ChatGPT](https://www.bilibili.com/video/BV1Dg4y1V7pn)

│ 　　 　 ├─ [Rasa+ChatGLM-6B](https://www.bilibili.com/video/BV1D14y1f7pr)

Azure ─┐ 　 　 │ 　　 　 ├─ [VisualGLM](https://www.bilibili.com/video/BV1mP411Q7mj)

Edge TTS ─┼── TTS 　 　 └─ [RWKV](https://www.bilibili.com/video/BV1yu41157zB)

[开源 TTS](https://www.bilibili.com/read/cv25192534) ─┘ 　 　 │

│

│

┌──────────┬────┼───────┬─────────┐

Remote Android 　　[Live2D](https://www.bilibili.com/video/BV1sx4y1d775/?vd_source=564eede213b9ddfa9a10f12e5350fd64)　　 [UE](https://www.bilibili.com/read/cv25133736)　　　 [xuniren](https://www.bilibili.com/read/cv24997550)　　　 Remote PC

## **一、Fay 控制器用途**

![](images/kzq.jpg)

### **远程语音助理** [`PC demo`](https://github.com/TheRamU/Fay/tree/main/python_connector_demo)

### **远程语音助理** [`android demo`](https://github.com/TheRamU/Fay/tree/main/android_connector_demo)

抖音监听 https://github.com/wwengg/douyin
b 站监听 https://github.com/wangzai23333/blivedm
微信视频号监听 https://github.com/fire4nt/wxlivespy

### **与数字形象通讯**（非必须,控制器需要关闭“面板播放”）

控制器与采用 WebSocket 方式与 UE 通讯

![](images/cs.png)

下载工程: [https://pan.baidu.com/s/1RBo2Pie6A5yTrCf1cn_Tuw?pwd=ck99](https://pan.baidu.com/s/1RBo2Pie6A5yTrCf1cn_Tuw?pwd=ck99)

下载 windows 运行包: [https://pan.baidu.com/s/1CsJ647uV5rS2NjQH3QT0Iw?pwd=s9s8](https://pan.baidu.com/s/1CsJ647uV5rS2NjQH3QT0Iw?pwd=s9s8)

![](images/UElucky.png)

工程包：https://github.com/xszyou/fay-ue5

通讯地址: [`ws://127.0.0.1:10002`](ws://127.0.0.1:10002)（已接通）

消息格式: 查看 [WebSocket.md](https://github.com/TheRamU/Fay/blob/main/WebSocket.md)

### **与远程音频输入输出设备连接**（非必须,外网需要配置http://ngrok.cc tcp 通道的 clientid）

控制器与采用 socket(非 websocket) 方式与 音频输出设备通讯

内网通讯地址: [`ws://127.0.0.1:10001`](ws://127.0.0.1:10001)

外网通讯地址: 通过http://ngrok.cc获取（有伙伴愿意赞助服务器给社区免费使用吗？）

![](images/Dingtalk_20230131122109.jpg)
消息格式: 参考 [remote_audio.py](https://github.com/TheRamU/Fay/blob/main/python_connector_demo/remote_audio.py)

## **二、Fay 控制器核心逻辑**

![](images/luoji.png)

**注：**

1、去 API 及会话管理功能将在下一版本发布；

2、以上每个模块可轻易替换成自家核心产品。

3、本地 nlp（rasa+chatglm）的替换方法（https://m.bilibili.com/video/BV1D14y1f7pr?wxfid=o7omF0Vs6RIQFUGAzB6LXOBHa6Yg）：
1、安装启动 chatglm(github)
2、安装 rasa 包：rasa、rasa-sdk
3、进入 test/rasa 目录启动 actions：rasa run actions
4、启动 rasa api server：rasa run --enable-api -p 5006
5、fay_core.py 引入 nlp_rasa.py

### **目录结构**

```
.
├── main.py					# 程序主入口
├── fay_booter.py			# 核心启动模块
├── config.json				# 控制器配置文件
├── system.conf				# 系统配置文件
├── ai_module
│   ├── ali_nls.py			# 阿里云 实时语音
│   ├── ms_tts_sdk.py       # 微软 文本转语音
│   ├── nlp_xfaiui.py          # 讯飞 人机交互-自然语言处理
│   ├── nlp_lingju.py          # 灵聚 人机交互-自然语言处理
│   ├── nlp_gpt.py          # gpt3.5对接
│   ├── nlp_yuan.py          # 浪潮.源大模型对接
│   └── xf_ltp.py           # 讯飞 情感分析
├── bin                     # 可执行文件目录
├── core                    # 数字人核心
│   ├── fay_core.py         # 数字人核心模块
│   ├── recorder.py         # 录音器
│   ├── qa_service.py         # qa回答管理
│   ├── tts_voice.py        # 语音生源枚举
│   ├── authorize_tb.py     # fay.db认证表管理
│   ├── viewer.py           # 抖音直播间接入模块
│   └── wsa_server.py       # WebSocket 服务端
├── gui                     # 图形界面
│   ├── flask_server.py     # Flask 服务端
│   ├── static
│   ├── templates
│   └── window.py           # 窗口模块
├── scheduler
│   └── thread_manager.py   # 调度管理器
└── utils                   # 工具模块
    ├── config_util.py
    ├── storer.py
    └── util.py
```

## **四、安装说明**

### **环境**

- Python 3.8.0 +
- Chrome 浏览器 (若不開啟直播功能，可跳过)

### **安装依赖**

```shell
pip install -r requirements.txt
```

### **配置应用密钥**

- 查看 [AI 模块](#ai-模块)
- 浏览链接，注册并创建应用，将应用密钥填入 `./system.conf` 中

### **启动**

启动 Fay 控制器

```shell
python main.py
```

### **AI 模块**

启动前需填入应用密钥

| 代码模块                  | 描述                                             | 链接                                                                          |
| ------------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------- |
| ./ai_module/ali_nls.py    | 阿里云 实时语音识别                              | https://ai.aliyun.com/nls/trans                                               |
| ./ai_module/ms_tts_sdk.py | 微软 文本转情绪语音（可选）                      | https://azure.microsoft.com/zh-cn/services/cognitive-services/text-to-speech/ |
| ./ai_module/nlp_lingju.py | 灵聚 NLP api(支持 GPT3.5 及多应用)（NLP 多选 1） | https://open.lingju.ai 需联系客服务开通 gpt3.5 权限                           |
| ./ai_module/xf_ltp.py     | 讯飞 情感分析                                    | https://www.xfyun.cn/service/emotion-analysis                                 |
| ./utils/ngrok_util.py     | ngrok.cc 外网穿透（可选）                        | http://ngrok.cc                                                               |
| ./ai_module/yuan_1_0.py   | 浪潮源大模型（NLP 3 选 1）                       | https://air.inspur.com/                                                       |
| ./ai_module/chatgpt.py    | ChatGPT（NLP 3 选 1）                            | **\*\*\***                                                                    |
| ./ai_module/xf_aiui.py    | 讯飞自然语言处理（NLP 3 选 1）                   | https://aiui.xfyun.cn/solution/webapi                                         |

## **五、使用说明**

### **使用说明**

- 抖音虚拟主播：启动 bin/Release_2.85/2.85.exe + fay 控制器（抖音输入源開啟）+ 数字人 + 抖音伴侣（测试时直接通过浏览器打开别人的直播间）；

- 现场推销货：fay 控制器（填写商品信息）+ 数字人；

- 商品导购：fay 控制器（麦克风输入源開啟、填写商品信息、填写商品 Q&A）+ 数字人；

  b 站字幕监测源码：https://github.com/wangzai23333/blivedm

  抖音源码：https://github.com/wwengg/douyi

  微信视频号监测源码：https://github.com/fire4nt/wxlivespy

  操作教程：[接入教程](https://qqk9ntwbcit.feishu.cn/wiki/QX0QwBAbfiMtPBkaVuPci8WMnwS)

### **语音指令**

- **关闭核心**
  关闭
  再见
  你走吧
- **静音**
  静音
  闭嘴
  我想静静
- **取消静音**
  取消静音
  你在哪呢？
  你可以说话了
- **播放歌曲**（网易音乐库不可用，寻找替代中）
  播放歌曲
  播放音乐
  唱首歌
  放首歌
  听音乐
  你会唱歌吗？
- **暂停播放**
  暂停播放
  别唱了
  我不想听了

### **图形界面**

![](images/controller.png)

### **人设**

数字人属性，与用户交互中能做出相应的响应。

#### 交互灵敏度

在交互中，数字人能感受用户的情感，并作出反应。最直的体现，就是语气的变化，如 开心/伤心/生气 等。
设置灵敏度，可改变用户情感对于数字人的影响程度。

### **接收來源**

#### 抖音

填入直播间地址，实现与直播间粉丝交互

#### 麦克风

选择麦克风设备，实现面对面交互，成为你的伙伴

#### socket 远程音频输入

可以接入远程音频输入，远程音频输出

#### 商品栏

填入商品介绍，数字人将自动讲解商品。

当用户对商品有疑问时，数字人可自动跳转至对应商品并解答问题。

配合抖音接收來源，实现直播间自动带货。

### 相关文章：

1、[(34 条消息) 非常全面的数字人解决方案*郭泽斌之心的博客-CSDN 博客*数字人算法](https://blog.csdn.net/aa84758481/article/details/124758727)

2、[(34 条消息) Fay 数字人开源项目在 mac 上的安装办法\_郭泽斌之心的博客-CSDN 博客](https://blog.csdn.net/aa84758481/article/details/127551258)

3、【开源项目：数字人 FAY——Fay 新架构使用讲解】 https://www.bilibili.com/video/BV1NM411B7Ab/?share_source=copy_web&vd_source=64cd9062f5046acba398177b62bea9ad

4、【开源项目 FAY——UE 工程讲解】https://www.bilibili.com/video/BV1C8411P7Ac?vd_source=64cd9062f5046acba398177b62bea9ad

5、m1 机器安装办法（Gason 提供）：https://www.zhihu.com/question/437075754

二次开发指导联系 QQ 467665317

关注公众号获取最新微信技术交流群二维码（请先 star 本仓库）

![](images/gzh.jpg)
