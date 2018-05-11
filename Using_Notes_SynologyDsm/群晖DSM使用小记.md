## 群晖DSM使用小记

## 流水账：

- 20180508 

	- | 操作 | 品牌   | 型号      | 规模       | 平台 | 价格    |
		| ---- | ------ | --------- | ---------- | ---- | ------- |
		| 购买 | 群晖   | ds218+    | 支持docker | 京东 | 2780    |
		| 购买 | 希捷   | 酷狼      | 2T         | 淘宝 | 549     |
		| 观望 | 金士顿 | DDR3 4    | 4G         | 京东 | 300-800 |
		| 观望 | 施耐德 | ups-bk500 | 小巧，重   | 京东 | 510-600 |
		| 观望 | 路由器 | 千兆      |            |      |         |
		| 观望 | 宽带   | 千兆      |            |      |         |

- 20180510

	- 东西到齐
	- 安装硬盘（3.5寸硬盘不用螺丝，多余的），
	- 注册群晖id
	- 备份lastpass
	- 转移资料
	- 同步备份



## 操作总结

- **Refenrence：**[原文1](https://post.smzdm.com/p/545304) [备份1](群晖DSM6.1应用详解 篇二.md)  [原文2](https://post.smzdm.com/p/552010/) [备份1](群晖DSM6.1应用详解 篇二.md)  

- **目录：**

  - Cloud Station 
  - Hyper Backup 
  - Snapshot Replication 
  - USB Copy2.0

- Cloud Station 同步

  > Cloud Station套件其实是一个套件组，包含5个功能模块，其中Cloud Station Server是Cloud Station在NAS上的服务器端；云同步（Cloud Station Drive）和云备份（Cloud Station Backup）是电脑端软件，Drive是电脑端和NAS端的双向同步，Backup是电脑端向NAS端的单向备份；Cloud Station ShareSync是群晖NAS和NAS之间的同步；DS Cloud是移动端APP。 

  - cloud station drive  云同步     
  	- drive是双向同步使用起来感觉方便，最好设置好备份的文档

  - cloud station backup 云备份
  	-  back up 是实时备份，单项同步的 从PC->NAS时 ，第一次操作文件太大（40G），首次同步超级慢，因为bacakup 事无巨细全部备份，网络问题，性能问题一起导致用了 5+小时还有十六万个文件，心态崩了 ，取消了。用了小文件夹发现还是不错的，个人问题。版本资源管理器类似git。
  - cloud station sharesync
  	-  sharesync和backup类似，两台nas直接操作，工作量大，操作不起大致流程了解了一下，没有操作，贫穷让我省下了时间。
  - ds cloud
  	- ds cloud 很好用 在安卓机操作也不错，不过用于路由器和带宽限制，还是相对有点慢，10m/s以下，比上不足比下有余，凑合用呗。
  	- 安卓端 
  		- ds file    
  		- ds cloud
  		- ds photo  
  		- ds audio
  		- ds video
  		- drive    
  		- ds note  需要和evernote  onenote做一下对比
  		- ds get   

- hyper back up 备份

  - 和cloud station backup 相比是定时定点备份 不是实时备份。增量备份，所以首次备份依旧速度很慢，无解。
  - 感觉是给文档更改频繁的小企业用的，不适合个人用户。有空再搞。

- Snapshot Replication  快照

  - 快照还是很方便的，相当于多上了一层保险，推荐用。

- USB Copy2.0

  - 数据转移或者有数据冷备份要求的人高清下载多的人笔记合适，只用了一次将移动硬盘数据转移到nas，还是不错的。

- Photo Station

  -  照片管理，因为nas网络映射到pc所以不常在nas进行照片管理，不过按照地点和时间线进行管理功能很强。 停用这个功能，有需要再用。

- Video Station 

  - 同上，试用了一下简洁易用，只是没需要。停用这个功能，有需要再用。

- Audio Station

  - 同上，试用了一下还不错。停用这个功能，有需要再用。 

- Download Station 

  - 批量添加种子，但是不能过滤文件的内容剔除不必要的文件，下载速度和软件无关，和种子有关。
  - 计划管理，可以设置限速。还是可以的，只是没有下片这个需要，下下美剧还是可以的。

  

  ​		

