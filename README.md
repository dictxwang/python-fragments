# python-fragments

python相关的代码片段
大部分可在python3.6运行，少数代码需要在python3.7+运行。

## python之禅

执行命令： python -c 'import this'
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## 代码导航

#### 一、基础模块相关

[1、解析命令行参数（argparse和optparse）](https://github.com/dictxwang/python-fragments/blob/main/basis/about_argparser.py)

[2、异步IO的应用（asyncio）python3.7+](https://github.com/dictxwang/python-fragments/blob/main/basis/about_asyncio.py)

[3、asyncio与threading结合的使用](https://github.com/dictxwang/python-fragments/blob/main/basis/about_asyncio_threading.py)

[4、字节处理（bytes）](https://github.com/dictxwang/python-fragments/blob/main/basis/about_bytes.py)

[5、class类定义与应用](https://github.com/dictxwang/python-fragments/blob/main/basis/about_class.py)

[6、列表排序及collections的使用](https://github.com/dictxwang/python-fragments/blob/main/basis/about_collection.py)

[7、读取静态配置（configparser）](https://github.com/dictxwang/python-fragments/blob/main/basis/about_config.py)

[8、查看代码执行效率（cProfile）](https://github.com/dictxwang/python-fragments/blob/main/basis/about_cprofile.py)

[9、字符的编码解码，编码类型检测（encoding、chardet）](https://github.com/dictxwang/python-fragments/blob/main/basis/about_encoding.py)

[10、异常处理与堆栈信息](https://github.com/dictxwang/python-fragments/blob/main/basis/about_exception.py)

[11、格式化输出（format）](https://github.com/dictxwang/python-fragments/blob/main/basis/about_format.py)

[12、函数与装饰器](https://github.com/dictxwang/python-fragments/blob/main/basis/about_function.py)

[13、函数耗时统计](https://github.com/dictxwang/python-fragments/blob/main/basis/about_function_cost.py)

[14、yield关键字与生成器](https://github.com/dictxwang/python-fragments/blob/main/basis/about_generator.py)

[15、python的自省（inspect）](https://github.com/dictxwang/python-fragments/blob/main/basis/about_inspect.py)

[16、日志工具的编写（logging）](https://github.com/dictxwang/python-fragments/blob/main/basis/about_logging.py)

[17、python的序列化（pickle）](https://github.com/dictxwang/python-fragments/blob/main/basis/about_pickle.py)

[18、图像处理（pil）](https://github.com/dictxwang/python-fragments/blob/main/basis/about_pil.py)

[19、RSA加密算法的实现与应用](https://github.com/dictxwang/python-fragments/blob/main/basis/about_rsa.py)

[20、python执行shell命令的几种方法](https://github.com/dictxwang/python-fragments/blob/main/basis/about_runshell.py)

[21、字符串处理及内置方法的使用](https://github.com/dictxwang/python-fragments/blob/main/basis/about_string.py)

[22、多线程实现生产者消费者模型（threading）](https://github.com/dictxwang/python-fragments/blob/main/basis/producer_consumer.py)

[23、asyncio实现生产者消费者模型](https://github.com/dictxwang/python-fragments/blob/main/basis/producer_consumer_asyncio.py)

[24、比较两种生产者与消费者模型（threading与asyncio）](https://github.com/dictxwang/python-fragments/blob/main/basis/producer_consumer_compare.py)

[25、多进程实现生产者消费者模型（multiprocessing）](https://github.com/dictxwang/python-fragments/blob/main/basis/producer_consumer_process.py)

[26、多进程共享内存的应用（Process和Manager）](https://github.com/dictxwang/python-fragments/blob/main/basis/producer_consumer_process_memery.py)

#### 二、常用算法实现

[1、排序算法：冒泡排序](https://github.com/dictxwang/python-fragments/blob/main/algorithm/about_bubble.py)

[2、排序算法：快速排序](https://github.com/dictxwang/python-fragments/blob/main/algorithm/about_quick_sort.py)

[3、查找算法：BruteForce暴力查找](https://github.com/dictxwang/python-fragments/blob/main/algorithm/about_search_bf.py)

[4、查找算法：KMP查找](https://github.com/dictxwang/python-fragments/blob/main/algorithm/about_search_kmp.py)

[5、搜索算法：Dijkstra最短路径算法](https://github.com/dictxwang/python-fragments/blob/main/algorithm/about_dijkstra.py)

[6、排序算法：堆排序](https://github.com/dictxwang/python-fragments/blob/main/algorithm/about_heap_sort.py)

[7、数据结构：堆的构建过程](https://github.com/dictxwang/python-fragments/blob/main/algorithm/about_make_heap.py)

[8、排序算法：插入排序](https://github.com/dictxwang/python-fragments/blob/main/algorithm/about_insertion_sort.py)

[9、排序算法：希尔排序](https://github.com/dictxwang/python-fragments/blob/main/algorithm/about_shell_sort.py)

[10、排序算法：归并排序](https://github.com/dictxwang/python-fragments/blob/main/algorithm/about_merge_sort.py)

[11、图的遍历：BFS广度优先遍历](https://github.com/dictxwang/python-fragments/blob/main/algorithm/about_bfs.py)

[12、图的遍历：DFS深度优先遍历](https://github.com/dictxwang/python-fragments/blob/main/algorithm/about_dfs.py)

[13、查找算法：二分查找](https://github.com/dictxwang/python-fragments/blob/main/algorithm/about_search_binary.py)

#### 三、扩展模块相关

[1、folium包的地图应用](https://github.com/dictxwang/python-fragments/blob/main/open_modules/about_folium.py)

[2、lxml处理html和xml](https://github.com/dictxwang/python-fragments/blob/main/open_modules/about_lxml.py)

[3、matplotlib绘制2D坐标图](https://github.com/dictxwang/python-fragments/blob/main/open_modules/about_matplotlib.py)

[4、matplotlib的更多应用（曲线图、直方图、散点图、3D图）](https://github.com/dictxwang/python-fragments/blob/main/open_modules/about_matplotlib_2.py)

[5、numpy进行科学计算（精度、排序、矩阵、线性代数）](https://github.com/dictxwang/python-fragments/blob/main/open_modules/about_numpy.py)

[6、opencv的基本应用（通道处理）](https://github.com/dictxwang/python-fragments/blob/main/open_modules/about_opencv.py)

[7、opencv的更多应用（图像特性处理：怀旧、素描、光照、滤镜）](https://github.com/dictxwang/python-fragments/blob/main/open_modules/about_opencv_02.py)

[8、openpyxl处理excel文档（读取、修改、创建）](https://github.com/dictxwang/python-fragments/blob/main/open_modules/about_openpyxl.py)

[9、reportlab制作pdf文件](https://github.com/dictxwang/python-fragments/blob/main/open_modules/about_reportlab.py)

[10、websockets的应用（配合asyncio实现）](https://github.com/dictxwang/python-fragments/blob/main/open_modules/about_websocket.py)

[11、webscokets的多线程应用](https://github.com/dictxwang/python-fragments/blob/main/open_modules/about_websocket_threading.py)

#### 四、工具脚本

[1、贷款本息计算](https://github.com/dictxwang/python-fragments/blob/main/short_tools/calculate_land.py)

[2、个税计算](https://github.com/dictxwang/python-fragments/blob/main/short_tools/calculate_tax_rate.py)

[3、投资年化收益计算](https://github.com/dictxwang/python-fragments/blob/main/short_tools/calculate_yearly_investment_return.py)