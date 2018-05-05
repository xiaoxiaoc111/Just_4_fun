# TAG_Heartbleed(16)

### [tombkeeper](https://weibo.com/101174?refer_flag=1005055015_)  

[2014-4-12 12:19](https://weibo.com/1401527553/AFkD2mf9r?from=page_1005051401527553_profile&wvr=6&mod=weibotime) 来自 [微博 weibo.com](http://weibo.com/)

[@ZoomEye](https://weibo.com/n/ZoomEye?from=feed&loc=at) 可以试试把存在 Hearebleed 的 IP 和 Banner 为常见嵌入式 HTTP Server 的 IP 做个交叉对比，再和有 OpenSSH 的 IP 做个交叉对比，最后找出开了 OpenSSH 和 HTTP 又受漏洞影响的嵌入式设备。然后对 Web 首页用些简单的关键字匹配把设备的用途和归属分分类。然后就可以……献给国家了。 

标签： [Heartbleed](https://weibo.com/1401527553/profile?is_tag=1&tag_name=Heartbleed)

--------------------

### [tombkeeper](https://weibo.com/101174?refer_flag=1005055015_)  

[2014-4-12 00:13](https://weibo.com/1401527553/AFfSAxU9I?from=page_1005051401527553_profile&wvr=6&mod=weibotime) 来自 [微博 weibo.com](http://weibo.com/)

各家做终端安全软件的，赶紧增加个全盘查 OpenSSL 库版本的功能啊，这么大好的机会，我前天就提示你们了。比如对 Windows，就搜一下 SSLeay32.dll 和 Libeay32.dll，查查版本号，搞个一键升级。想再高级点，可以根据代码特征把静态链接的和改了文件名的也查查，不过对静态链接的只能提示，没法升级。 

标签： [Heartbleed](https://weibo.com/1401527553/profile?is_tag=1&tag_name=Heartbleed)

--------------------


### [tombkeeper](https://weibo.com/101174?refer_flag=1005055015_)  

[2014-4-11 19:02](https://weibo.com/1401527553/AFdQko9PC?from=page_1005051401527553_profile&wvr=6&mod=weibotime) 来自 [iPhone 5s](http://app.weibo.com/t/feed/3G5oUM)

类似Heartbleed漏洞，你们觉得ZDI或厂商，出多少钱收购比较合理？如果有人打算购买后用于攻击牟利，你认为最多出多少钱仍是有利可图的？ 

标签： [Heartbleed](https://weibo.com/1401527553/profile?is_tag=1&tag_name=Heartbleed)

--------------------

### [tombkeeper](https://weibo.com/101174?refer_flag=1005055015_)  

[2014-4-11 18:30](https://weibo.com/1401527553/AFdDcAe8d?from=page_1005051401527553_profile&wvr=6&mod=weibotime) 来自 [iPhone 5s](http://app.weibo.com/t/feed/3G5oUM)

那位同志应该不是水军。另外，根据我一直在学习的正能量看事物法，他这次功劳不小——你们什么时候见过甲方、乙方、防的、攻的、360、360的对手……大家这么同仇敌忾？今天看到国内信息安全技术届多年未见的团结局面，即使可能就这么短暂的一瞬，我依然感动得眼泪水都要流出来…… 

标签： [Heartbleed](https://weibo.com/1401527553/profile?is_tag=1&tag_name=Heartbleed)

--------------------

### [tombkeeper](https://weibo.com/101174?refer_flag=1005055015_)  

[2014-4-10 19:51](https://weibo.com/1401527553/AF4JAl4MK?from=page_1005051401527553_profile&wvr=6&mod=weibotime) 来自 [微博 weibo.com](http://weibo.com/)

很多安全问题刚暴露时，都会有人说威胁被高估了，尤其是一些懂计算机但不懂安全的人特别容易做出这样的判断。不过多数情况下，其实没有被高估。有时候，还被低估了。比如说，堆栈溢出曾被认为无法利用，后来堆溢出也被认为无法利用，再后来虚表指针覆盖又被认为无法利用……这次 Heartbleed 也是一例。 

标签： [Heartbleed](https://weibo.com/1401527553/profile?is_tag=1&tag_name=Heartbleed)

--------------------

### [tombkeeper](https://weibo.com/101174?refer_flag=1005055015_)  

[2014-4-10 14:18](https://weibo.com/1401527553/AF2yp2Myn?from=page_1005051401527553_profile&wvr=6&mod=weibotime) 来自 [微博 weibo.com](http://weibo.com/)

Windows 上用 OpenSSL 的软件也不少，且多数使用自己安装目录下的 SSLeay32.dll 和 Libeay32.dll，没有统一的升级管理机制，漏洞可能会长期存在。某些因 ASLR/DEP 而难以攻击的新老漏洞，现在（甚至很长一段时间内）就很容易了。好在 Windows 软件用的库版本普遍偏老，目前看到受影响的并不很多。 

标签： [Heartbleed](https://weibo.com/1401527553/profile?is_tag=1&tag_name=Heartbleed)

--------------------

### [tombkeeper](https://weibo.com/101174?refer_flag=1005055015_)  

[2014-4-10 11:07](https://weibo.com/1401527553/AF1iKgYmC?from=page_1005051401527553_profile&wvr=6&mod=weibotime) 来自 [微博 weibo.com](http://weibo.com/)

友情提醒：这两天四处找人要各种 Heartbleed 工具的，注意检查一下代码，别被人反搞。如果代码是 Python 版，更得格外留意。今年 Python 刚出了一个 recvfrom_into() 函数的缓冲区溢出（CVE-2014-1912）。利用这个漏洞，完全可以设计出非常隐蔽的 Exploit 反噬后门。 

标签： [Heartbleed](https://weibo.com/1401527553/profile?is_tag=1&tag_name=Heartbleed)

--------------------

### [tombkeeper](https://weibo.com/101174?refer_flag=1005055015_)  

[2014-4-9 15:36](https://weibo.com/1401527553/AETDK3T0H?from=page_1005051401527553_profile&wvr=6&mod=weibotime) 来自 [微博 weibo.com](http://weibo.com/)

Heartbleed 事件也可很好体现 Netflow 类技术的价值。因为来回通信包的长度特征都很明显，通过 Netflow 记录就可以追溯攻击流量和攻击历史。比如可以查查类似通信特征在过去几年内是否早就出现过。 [@宫一鸣cn](https://weibo.com/n/%E5%AE%AB%E4%B8%80%E9%B8%A3cn?from=feed&loc=at) 

标签： [Heartbleed](https://weibo.com/1401527553/profile?is_tag=1&tag_name=Heartbleed)

--------------------

### [tombkeeper](https://weibo.com/101174?refer_flag=1005055015_)  

[2014-4-9 14:53](https://weibo.com/1401527553/AETmcDHkz?from=page_1005051401527553_profile&wvr=6&mod=weibotime) 来自 [微博 weibo.com](http://weibo.com/)

Heartbleed 这事儿还没完，说夸张点，可能刚刚开始。1、昨天各家的安全工程师都很辛苦。但搞入侵的可能比你们更辛苦，很多人估计昨晚一宿没睡。他们赶在各家修复前所抓到的数据会在未来几天里被分析、提取、利用。2、据一个向来比较靠谱的同志说：OpenSSL不是唯一存在类似问题的库。 

标签： [Heartbleed](https://weibo.com/1401527553/profile?is_tag=1&tag_name=Heartbleed)

--------------------

### [tombkeeper](https://weibo.com/101174?refer_flag=1005055015_)  

[2014-4-9 13:57](https://weibo.com/1401527553/AESZgahSM?from=page_1005051401527553_profile&wvr=6&mod=weibotime) 来自 [微博 weibo.com](http://weibo.com/)

要改密码的现在可以去改了。昨天有些同志当时就吓得说要去改密码——要是昨天没登陆，其实啥事没有，跑去改密码，反倒让密码进内存了。最近安全事件的影响力有赶超80年代副食品涨价的趋势，大家辛苦点，不过对行业是好事。

[@阿里安全响应中心](https://weibo.com/alisec?refer_flag=1005055015_)

关于OpenSSL某些版本存在基于基础协议的通用漏洞，阿里各网站已经在第一时间进行了修复处理，目前已经处理完毕，包括淘宝、天猫、支付宝等各大网站都确认可以放心使用。 

[2014-4-9 13:01](https://weibo.com/3754312562/AESCQ8Op7) 来自 [微博 weibo.com](http://weibo.com/)

标签： [Heartbleed](https://weibo.com/1401527553/profile?is_tag=1&tag_name=Heartbleed)

--------------------

### [tombkeeper](https://weibo.com/101174?refer_flag=1005055015_)  

[2014-4-9 09:23](https://weibo.com/1401527553/AERc6FRr2?from=page_1005051401527553_profile&wvr=6&mod=weibotime) 来自 [新浪长微博](http://app.weibo.com/t/feed/2Y8gAH)

我发表了文章《“Heartbleed”漏洞之后》：……对密码可能被盗取的用户进行额外风控措施……一旦发现异常，再通知修改密码——用另外的信道发这个通知，比如用户的注册邮箱。当然，如果监控到注册邮箱被修改了，往修改前的邮箱发。 [*°*“Heartbleed”漏洞之后](http://t.cn/8souK9c) 

#### [“Heartbleed”漏洞之后](http://t.cn/8souK9c?m=3697376029976856&u=1401527553)

除非有特别的审计措施，绝大多数网站可能无法统计有多少敏感信息因昨天的OpenSSL Heartbleed漏洞而被窃取。这些信息可能包括证书、Cookie、用户名密码等。证书好办，可以重新申请颁发，花点

标签： [Heartbleed](https://weibo.com/1401527553/profile?is_tag=1&tag_name=Heartbleed)

--------------------

### [tombkeeper](https://weibo.com/101174?refer_flag=1005055015_)  

[2014-4-8 16:53](https://weibo.com/1401527553/AEKI8BMiU?from=page_1005051401527553_profile&wvr=6&mod=weibotime) 来自 [微博 weibo.com](http://weibo.com/)

统计了一下，平均每个请求可以得到2组明文用户名密码。另外，作为普通用户，能做的大概就是今天别登陆。

[@tombkeeper](https://weibo.com/101174?refer_flag=1005055015_)

这个OpenSSL“心血”漏洞，各大互联网企业的运维今天可能得辛苦点，抓紧升级，或在边界上采取点措施扛一下。刚才写了个脚本简单跑了跑，一分钟就从某巨型购物网站的登陆服务器上抓到若干组明文用户名/密码。实测可成功登陆。其中一组还是某旗舰店的，幸好有手机验证这一关挡着。 

[2014-4-8 16:32](https://weibo.com/1401527553/AEKzXv6Q2) 来自 [微博 weibo.com](http://weibo.com/)

标签： [Heartbleed](https://weibo.com/1401527553/profile?is_tag=1&tag_name=Heartbleed)

--------------------

### [tombkeeper](https://weibo.com/101174?refer_flag=1005055015_)  

[2014-4-8 16:32](https://weibo.com/1401527553/AEKzXv6Q2?from=page_1005051401527553_profile&wvr=6&mod=weibotime) 来自 [微博 weibo.com](http://weibo.com/)

这个OpenSSL“心血”漏洞，各大互联网企业的运维今天可能得辛苦点，抓紧升级，或在边界上采取点措施扛一下。刚才写了个脚本简单跑了跑，一分钟就从某巨型购物网站的登陆服务器上抓到若干组明文用户名/密码。实测可成功登陆。其中一组还是某旗舰店的，幸好有手机验证这一关挡着。 

标签： [Heartbleed](https://weibo.com/1401527553/profile?is_tag=1&tag_name=Heartbleed)

--------------------

### [tombkeeper](https://weibo.com/101174?refer_flag=1005055015_)  

[2014-4-8 16:26](https://weibo.com/1401527553/AEKxu9Ujw?from=page_1005051401527553_profile&wvr=6&mod=weibotime) 来自 [微博 weibo.com](http://weibo.com/)

大致看了OpenSSL那个“心血”漏洞。1、漏洞可以无限制反复利用，所以即使不使用精巧的堆操控手段来控制读取的地址，也可以通过反复暴力尝试获取大量内存片段，然后从中寻找有价值的数据。2、利用泄露的信息所能干的事完全取决于你的想象力：对抗ASLR、窃取私钥、窃取用户Cookie、窃取用户名密码…… 

标签： [Heartbleed](https://weibo.com/1401527553/profile?is_tag=1&tag_name=Heartbleed)

--------------------

### [tombkeeper](https://weibo.com/101174?refer_flag=1005055015_)  

[2014-4-8 15:16](https://weibo.com/1401527553/AEK4Z81zp?from=page_1005051401527553_profile&wvr=6&mod=weibotime) 来自 [微博 weibo.com](http://weibo.com/)

推荐阅读[@乌云知识库](https://weibo.com/n/%E4%B9%8C%E4%BA%91%E7%9F%A5%E8%AF%86%E5%BA%93?from=feed&loc=at) 中这篇OpenSSL“心血”漏洞分析：[*O*网页链接](http://t.cn/8so46dR)。作者提到应对OpenSSL这样的关键安全基础设施进行安全审计。我和朋友讨论“自主可控”时，也说了类似观点：除非斥巨资组织对核心代码的安全审计，否则，拿个开源OS无论怎么汉化，怎么定制界面，最多只是实现了“自主编译”。 

标签： [Heartbleed](https://weibo.com/1401527553/profile?is_tag=1&tag_name=Heartbleed)

--------------------

### [tombkeeper](https://weibo.com/101174?refer_flag=1005055015_)  

[2011-8-17 21:08](https://weibo.com/1401527553/xjVlvEssC?from=page_1005051401527553_profile&wvr=6&mod=weibotime) 来自 [微博 weibo.com](http://weibo.com/)

虽然大多数人都觉得自己能做到“对事不对人”，也能做到“充满人文关怀”。不过我认为人不太可能既“情感丰富”、“充满人文关怀”，又“客观理性”、“对事不对人”。我觉得后者是人类进化的方向，虽然具有前者特质的人在情感可能上无法接受这一点。 

标签： [Heartbleed](https://weibo.com/1401527553/profile?is_tag=1&tag_name=Heartbleed)
