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

3.一个新的app的设计思路，主要看架构方面的想法

4.多个登录方式，比如qq， 微信，微博，手机号，邮箱等的登录，如果真对变化进行封装。这里考虑的更多的是设计模式上的问题

5.事件响应链（比如点击事件）

http://www.cocoachina.com/ios/20170720/19964.html
http://www.cocoachina.com/ios/20160113/14896.html
https://www.jianshu.com/p/6f2cc4b1f5a1

6.GCD中group的优点，及串行，并行队列

7.framework时动态链接库还是静态链接库，和.a的区别是什么

8.将对象加入字典，array时的引用计数是多少

9.weak的实现原理 strong的实现原理

10.关于引用计数的知识点

11.block中的弱引用强引用，什么情况会导致循环引用，什么时候需要__strong保持强引用

12.app的性能优化，都有哪些

13.对于image加载的优化方案有哪些

14.Runloop, runtime的理解


//阿里一面



1.Category支持添加属性与成员变量吗

2.是否了解设计模式, 用过哪些

3.iOS7之后, 蓝牙的围栏功能

4.MVC是否了解?介绍下使用情况。

5.MVC里面, View怎么通知到Model

6.了解delegate吗?并介绍



7.说说Cell重用原理

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

28.

29.

30.

31.

32.

33.

34.

35.

36.


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




