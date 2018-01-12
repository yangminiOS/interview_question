'''
1.谈下iOS开发中知道的哪些锁? 哪个性能最差?SD和AFN使用的哪个? 一般开发中你最常用哪个? 哪个锁apple存在问题又是什么问题?

https://juejin.im/entry/5a00f59ff265da4314401967

http://blog.csdn.net/qq_30513483/article/details/52349968



2.iOS下如何实现指定线程数目的线程池?

http://www.cocoachina.com/ios/20150731/12819.html

3.如何用HTTP实现长连接?

https://www.cnblogs.com/shoren/p/http-connection.html

https://www.cnblogs.com/cswuyg/p/3653263.html

4.http的post和get啥区别

http://blog.csdn.net/wangzhilife/article/details/12440089

5.使用atomic一定是线程安全的吗？

当使用atomic时，虽然对属性的读和写是原子性的，但是仍然可能出现线程错误：当线程A进行写操作，
这时其他线程的读或者写操作会因为该操作而等待。当A线程的写操作结束后，B线程进行写操作，然后当A线程需要读操作时，
却获得了在B线程中的值，这就破坏了线程安全，如果有线程C在A线程读操作前release了该属性，那么还会导致程序崩溃。
所以仅仅使用atomic并不会使得线程安全，我们还要为线程添加lock来确保线程的安全。
也就是要注意：atomic所说的线程安全只是保证了getter和setter存取方法的线程安全，并不能保证整个对象是线程安全的

6.通过[UIImage imageNamed:]生成的对象什么时候被释放？

使用imageNamed这个方法生成的UIImage对象,会在应用的bundle中寻找图片,如果找到则Cache到系统缓存中,
作为内存的cache,而程序员是无法操作cache的,只能由系统自动处理,如果我们需要重复加载一张图片,那这无疑是一种很好的方式,
因为系统能很快的从内存的cache找到这张图片,但是试想,如果加载很多很大的图片的时候,内存消耗过大的时候,就会会强制释放内存

7.iOS下所有的本地持久化方案。
http://www.cocoachina.com/ios/20150720/12610.html

plist文件  preference偏好设置  归档  SQLite  CoreData

8.crash的收集和定位bug的方式谈下?

https://www.jianshu.com/p/746184ea5662
https://www.jianshu.com/p/f5c4eee3a043
https://www.jianshu.com/p/799dcb0cb5ba
http://dev.umeng.com/analytics/reports/errors#2
http://bughd.com

9.SEL和Method和IMP分别说下再谈下对IMP的理解?
https://www.jianshu.com/p/aff083ec3203


10.Autorelease的原理 ?

http://www.cocoachina.com/ios/20150610/12093.html
http://blog.csdn.net/allangold/article/details/51673199
http://www.cocoachina.com/ios/20150601/11970.html


11.ARC的工作原理
http://www.cocoachina.com/ios/20151210/14636.html

12.weak弱引用的代码逻辑实现?
http://www.cocoachina.com/ios/20171213/21520.html
http://www.cocoachina.com/ios/20170904/20460.html
http://www.cocoachina.com/ios/20170328/18962.html
http://www.cocoachina.com/ios/20150605/11990.html

13.Socket建立网络连接的步骤;
http://blog.csdn.net/chenlycly/article/details/51657179
http://blog.csdn.net/u013782203/article/details/51767763

去哪网面试试题

1.atomic 和 nonatomic 的区别?

http://blog.csdn.net/xueshangzhiying_ios/article/details/62039168
http://blog.csdn.net/qian521kun521/article/details/53397090

2.http socket的区别，http是在网络里面的那一层。这里考的是网络传输的那7层。如何知道消息体的数据已经发送完成了。tcp udp的理解
http://blog.csdn.net/li_ning_/article/details/52117463
http://blog.csdn.net/superjunjin/article/details/7841099


3.一个新的app的设计思路，主要看架构方面的想法

4.多个登录方式，比如qq， 微信，微博，手机号，邮箱等的登录，如果真对变化进行封装。这里考虑的更多的是设计模式上的问题

5.事件响应链（比如点击事件）

http://www.cocoachina.com/ios/20170720/19964.html
http://www.cocoachina.com/ios/20160113/14896.html
https://www.jianshu.com/p/6f2cc4b1f5a1

6.GCD中group的优点，及串行，并行队列
http://www.cocoachina.com/ios/20150731/12819.html
https://www.jianshu.com/p/35702778d9dc
https://www.jianshu.com/p/f536f9a17d90

7.framework时动态链接库还是静态链接库，和.a的区别是什么
https://www.cnblogs.com/bboymars/p/4980754.html
https://www.jianshu.com/p/5eea9a56d249

8.将对象加入字典，array时的引用计数是多少
字典的原理看这里：http://blog.csdn.net/zixiweimi/article/details/56677203

array肯定会+1

9.weak的实现原理 strong的实现原理
http://www.cocoachina.com/ios/20170328/18962.html
《Objective-C高级编程：iOS与OS X多线程和内存管理》


10.关于引用计数的知识点
《Objective-C高级编程：iOS与OS X多线程和内存管理》


11.block中的弱引用强引用，什么情况会导致循环引用，什么时候需要__strong保持强引用
《Objective-C高级编程：iOS与OS X多线程和内存管理》


12.app的性能优化，都有哪些
https://mp.weixin.qq.com/s/oUOKKEuaoVW4nNISMD-CHg
https://mp.weixin.qq.com/s/ijooFqdxQPy_75TRrSfJ0g
这两个回答解决了很多的问题

13.对于image加载的优化方案有哪些

14.Runloop, runtime的理解
https://www.ianisme.com/ios/2019.html





//阿里 分组一面

1.Category支持添加属性与成员变量吗
https://www.jianshu.com/p/535d1574cb86

2.是否了解设计模式, 用过哪些

3.iOS7之后, 蓝牙的围栏功能

4.MVC是否了解?介绍下使用情况。

5.MVC里面, View怎么通知到Model

6.了解delegate吗?并介绍



7.说说Cell重用原理
底层原理是两个可变数组，一个装在界面显示的cell（地址） ，一个装被标记且划出界面的cell.说到这里大家应该懂了，面试的时候千万不要说什么identifir这么简单的回答。

可以在UITableView.h文件中去搜索visible  关键字。其实底层就有有个visibleArray里面的cell就是visibleCells


8.异步下载如何实现

9.做过最大的项目是什么?主要难点在哪里

10.如果现在要实现一个下载功能, 你要如何设计。说说每个类具体做什么

11.学过哪些语言

12.C++里面虚函数作用


13.MVC具有什么样的优势，各个模块之间怎么通信，比如点击 Button 后 怎么通知 Model？

14.两个无限长度链表（也就是可能有环） 判断有没有交点

15.UITableView的相关优化

16.KVO、Notification、delegate各自的优缺点，效率还有使用场景

17.如何手动通知KVO

18.Objective-C 中的copy方法

19.runtime 中，SEL和IMP的区别

20.autoreleasepool的使用场景和原理

21.RunLoop的实现原理和数据结构，什么时候会用到

22.block为什么会有循环引用

23.使用GCD如何实现这个需求：A、B、C 三个任务并发，完成后执行任务 D。

24.NSOperation和GCD的区别

25.CoreData的使用，如何处理多线程问题

26.如何设计图片缓存？

27.有没有自己设计过网络控件？

28.介绍下内存的几大区域？

这个在网易和阿里的面试答案中有，前面已经给了

29.你是如何组件化解耦的？

30.runtime如何通过selector找到对应的IMP地址

31.runloop内部实现逻辑？

32.你理解的多线程？

33.GCD执行原理？

34.怎么防止别人反编译你的app？

35.YYAsyncLayer如何异步绘制？

36.优化你是从哪几方面着手？



//阿里分组二面



1.什么时候接触iOS

2.你的这些项目是外包还是自己开发的

3.OC允许多继承吗

4.要用什么方式实现多继承

5.了解内存管理吗, 吧唧吧唧...

6.了解设计模式吗

7.具体说说MVC

8.了解KVO吗

9.如果让你设计KVO, 要怎么设计

10现在你是如何适配的

11比较下storyboard和全代码

12.印象比较深的项目, 难点在哪

13.Cell重用机制具体怎么实现

14.如果有1w张图片要在屏幕滚动显示(每张图片满屏), 至少要几个cell, 如何实现循环滚动

15.平时是怎么进行测试的, 内存方面怎么测试

16.平时如何实现网络请求, 一般返回的数据是什么格式, 如何解析.

17.平时自己有没有封装过比较复杂的控件

18.在什么情况使用Notification

19.如何实现类似 "Find My iPhone" 这样功能

20.怎么判断某个 cell 是否显示在屏幕上

21.进程和线程的区别

22.TCP 与 UDP 区别

23.TCP 流量控制

24.数组和链表的区别

25.UIView 生命周期

26.如果页面 A 跳转到 页面 B，A 的 viewDidDisappear 方法和 B 的 viewDidAppear 方法哪个先调用？

27.block 循环引用问题

28.ARC 的本质

29.RunLoop 的基本概念，它是怎么休眠的？

30.Autoreleasepool 什么时候释放，在什么场景下使用？

31.如何找到字符串中第一个不重复的字符


32.哈希表如何处理冲突

33.在一个app中间有一个button，在你手触摸屏幕点击后，到这个button收到点击事件，中间发生了什么

34.代码文件编译生成过程，做了哪些事情

35.app启动做了哪些事情；

36.AFN原理



37.说说你项目中常用到的调试技巧？



//阿里三面


1.dSYM你是如何分析的？

2.多线程有哪几种？你更倾向于哪一种？

3.单例弊端？

4.如何把异步线程转换成同步任务进行单元测试？

5.介绍下App启动的完成过程？

6.比如App启动过慢，你可能想到的因素有哪些？

7.0x8badf00d表示是什么？

8.怎么防止反编译？

9.说说你遇到到的技术难点？

10.说说你了解的第三方原理或底层知识？

//蚂蚁金服

11.在KVO中，他是怎么知道监听的对象发生了变化？

12.字典的工作原理 ？怎100w个中是怎么快速去取value？

13.一个上线的项目，知道这个方法可能会出问题，在不破坏改方法前提下，怎么搞？

14.Block和函数指针的区别？

//支付宝

15.iOS多线程有哪些？他们之间各有什么区别，优劣性？

16.UIView和NSObject这两个类，所有里面的方法和原理都需要了解一下。

17.Runloop和线程的关系？

18.Runloop的作用？RunloopMode的原理？



//饿了么面试题

1.automic一定是线程安全的吗

2.iOS中的消息传递是怎么一步一步实现的

3.category和extension有什么区别

4.iOS中的私有属性如何设置

5.串行队列和同步锁两者在保护线程安全上的性能对比

6.并行队列是同时执行的吗

7.iOS中有哪些锁，你了解多少

8.iOS中UIKit框架的架构

9.UIView和CALayer之间的关系

10.UIView、CoreAnimation和CoreGraphics的关系

11.应该知道SegmentFault，这个在iOS中是什么错误，那StackOverFlow呢

12.GCD、NSThread、NSOperation性能上有何区别


//网易一面
13.自我介绍

14.学习iOS动机

15.对iOS的看法

16.谈项目

17.怎么看待审核被拒

18.怎么完成后期检测, 优化

19.id ,NSObject, id<NSObject>区别

20.了解iOS内存管理吗

21.release 和 autorelease 区别

22.autorelease 和 @autorelease区别

23.weak什么时候用

24.unsafe_unretained , weak, assign 区别

25.__block什么时候用

26.在block里面, 对数组执行添加操作, 这个数组需要声明成 __block吗

27.在block里面, 对NSInteger进行修改, 这个NSInteger是否需要声明成__blcok

28.了解循环引用吗

29.NSThread, NSOperation, GCD区别

30.如何在异步下载时候, 取消下载, 保证流量不浪费

31了解runtime吗

32.runtime什么时候用

33.通知和KVO区别

34.有序和无序set实现原理区别

35.深度遍历和广度遍历使用场景


36.常用的设计模式

37.哪些设计模式属于观察者模式

38.总结下刚才面试中哪些不足

39.自己有什么优点


40.有什么想问的


1.你一般学习iOS是如何学习的？

2.app内存你是如何分析的？

3.用过 TableView 吗，平时怎么解决 TableView 滑动卡顿问题的？

4.网络模型了解么？有哪几种？说说你的看法？

5.block本质是什么？

6.KVC机制是如何通过key找到value。

7.说说你最熟悉的第三方，知晓其原理么？

8.如何实现一个数组每个元素依次向右移动k位。(后头的往前面补) 比如: [1, 2, 3, 4, 5] 挪两位变成[4, 5, 1, 2, 3]

9.实现连连看算法

10T9算法如何实现, 全拼算法



11

12.

13.

14.

15.

16.

17.

18.

19.

20.




1.

2.

3.

4.

5.

6.

7.

8.

9.

10

11

12.

13.

14.

15.

16.

17.

18.

19.

20.




1.

2.

3.

4.

5.

6.

7.

8.

9.

10

11

12.

13.

14.

15.

16.

17.

18.

19.

20.




1.

2.

3.

4.

5.

6.

7.

8.

9.

10

11

12.

13.

14.

15.

16.

17.

18.

19.

20.




1.

2.

3.

4.

5.

6.

7.

8.

9.

10

11

12.

13.

14.

15.

16.

17.

18.

19.

20.




1.

2.

3.

4.

5.

6.

7.

8.

9.

10

11

12.

13.

14.

15.

16.

17.

18.

19.

20.






1.

2.

3.

4.

5.

6.

7.

8.

9.

10

11

12.

13.

14.

15.

16.

17.

18.

19.

20.






1.

2.

3.

4.

5.

6.

7.

8.

9.

10

11

12.

13.

14.

15.

16.

17.

18.

19.

20.






1.

2.

3.

4.

5.

6.

7.

8.

9.

10

11

12.

13.

14.

15.

16.

17.

18.

19.

20.







1.

2.

3.

4.

5.

6.

7.

8.

9.

10

11

12.

13.

14.

15.

16.

17.

18.

19.

20.






1.

2.

3.

4.

5.

6.

7.

8.

9.

10

11

12.

13.

14.

15.

16.

17.

18.

19.

20.






1.

2.

3.

4.

5.

6.

7.

8.

9.

10

11

12.

13.

14.

15.

16.

17.

18.

19.

20.







1.

2.

3.

4.

5.

6.

7.

8.

9.

10

11

12.

13.

14.

15.

16.

17.

18.

19.

20.







1.

2.

3.

4.

5.

6.

7.

8.

9.

10

11

12.

13.

14.

15.

16.

17.

18.

19.

20.










1.

2.

3.

4.

5.

6.

7.

8.

9.

10

11

12.

13.

14.

15.

16.

17.

18.

19.

20.








1.

2.

3.

4.

5.

6.

7.

8.

9.

10

11

12.

13.

14.

15.

16.

17.

18.

19.

20.









1.

2.

3.

4.

5.

6.

7.

8.

9.

10

11

12.

13.

14.

15.

16.

17.

18.

19.

20.








1.

2.

3.

4.

5.

6.

7.

8.

9.

10

11

12.

13.

14.

15.

16.

17.

18.

19.

20.









1.

2.

3.

4.

5.

6.

7.

8.

9.

10

11

12.

13.

14.

15.

16.

17.

18.

19.

20.


iOS App间常用的五种通信方式
http://www.cocoachina.com/ios/20171229/21709.html

深入了解哈希表
http://ios.jobbole.com/87716/


1.项目中的多线程的使用

2.runtime的使用

3.gcd中的信号量

4.怎么取消gcd中的耗时操作

5.MVC、MVP、MVVM三者区别

6.数据库读写安全

7.为什么要用AFN网络框架,而不自己封装

8.http和https的区别

9.OC和JS的交互,有几种方式

10.库的API怎么设计

11.SDWebImage的缓存策略

12.断点续传怎么做

13.音视频的编解码

14.tableview优化、性能优化

15.UIResponse 事件传递响应链

16.xml和json的区别

17.get和post请求参数长度

18.工作中遇到的难题,怎么解决

19.iOS动画

20.数据持久化方式,使用场景

21.runloop的输入源

22.model分类

23.AutoreleasePool和runloop的关系

24.如何实现复杂web页面缓存

25.iOS私有函数名

26.图片轮播器,当手滑动时,定时器怎么计时

27.苹果远程推送步骤

28.保持单设备登录状态

29.SDWebImage加载图片的原理,url不变图片变了,怎么处理

30.tableViewCell的布局及行高怎么设置

31.每个cell中有时间,应该怎么做

32.NSURLConnection和NSURLSession的异同

33.子线程刷新UI会怎样,为什么

34.怎么保证下载的资源不被系统清理

35.OC与Swift的区别

36.GCD与NSOperation的区别

37.atomic一定线程安全吗

38.AFN的实现原理

39.drawRect方法什么时候执行

40.分类和继承的优缺点

41.NSString用copy还是strong，为什么

42.http请求方法

43.OC中锁机制

44.面向对象的特性

45.KVO和KVC

46.离屏渲染

47.splite存图片,文件. 性能问题

48.app、控制器的生命周期

49.runtime有什么隐患

50.block内部为什么要强引用 — block延迟执行的时候

51.atomic线程安全吗

52.socket，数据包

53.runloop能处理哪些事

54.instrument的使用

55.SDWebImage内部缓存图片用的是什么

56.沙盒文件夹

57.JS和OC交互

58.为什么block外部弱化就能解除循环引用

59.定时器有哪些方式

60.新旧版本兼容

61.UITextFiled只输入中文,不能输入英文

62.Autolayout 点击按钮改变另一个按钮的坐标

63.收集bug,线上bug解决

64.热更新
'''




