[TOC]
#第一章	初识hadoop


####1.1 数据数据
> A ship in port is safe,but that is not what ships are bulit for. 
停在港口的船很安全，但那不是我们造船的目的 

数据量很多，而且在迅速增长.
####1.2 数据的存储和分析
- 存储 
1.RAID 磁盘阵列
把相同的数据存储在多个硬盘的不同的地方（因此，冗余地）的方法。
2.HDFS 分布式文件系统
- 分析
####1.3 查询所有数据
Mapreduce是一个批量查询处理器。每个查询需要处理整个数据集或者至少一个数据集的大部分。
####1.4 不仅仅是批处理
mapreduce不适合交互式查询，因为查询等待时间一般较长，所以适合离线使用场景.
hadoop现在被用于指代一个更大的，多个项目组成的生态系统。不仅仅是hdfs，mapreduce
####1.5 相较于其他系统的优势
>为什么需要Hadoop？
基于计算机的一个发展趋势:**寻址时间的提升远远跟不上传输速率的提升**

对比|RDBMS |Mapreduce
-|-|-
数据大小|GB|PB 
数据存取|交互式和批处理|批处理 
更新|多次读写|一次写入多次读取 
事务|ACID|无 
结构|写时模式|读时模式 
完整性|高|低 
横向扩展|非线性|线性 

hadoop 对半结构化或者非结构化数据非常有效，因为它是处理数据时才对数据进行解释（即'读时模式'）。








#第二章	关于 Mapreduce
#第三章	Hadoop分布式系统
#第四章	关于YARN
#第五章	Hadoop的I/O操作
#第六章	Mapreduce应用开发
#第七章	Mapreduce的工作机制
#第八章	Mapreduce的类型和格式
#第九章	Maprudece的特性
#第十章	构建hadoop集群
#第十一章	管理hadoop
#第十二章	关于Avro
#第十三章	关于Parquet
#第十四章	关于Flume
#第十五章	关于Sqoop
#第十六章	关于Pig
#第十七章	关于Hive
#第十九章	关于Spark
#第二十章	关于Hbase
#第二十一章	关于Zookeeper
#第二十二章   案例学习