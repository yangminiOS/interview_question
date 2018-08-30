'''

一、mrc和arc相关知识
1. mrc和arc
http://www.cocoachina.com/ios/20151210/14636.html


2.Autorelease的原理 ?
http://www.cocoachina.com/ios/20150610/12093.html
http://blog.csdn.net/allangold/article/details/51673199
http://www.cocoachina.com/ios/20150601/11970.html

3.weak弱引用的代码逻辑实现?
http://www.cocoachina.com/ios/20171213/21520.html
http://www.cocoachina.com/ios/20170904/20460.html
http://www.cocoachina.com/ios/20170328/18962.html
http://www.cocoachina.com/ios/20150605/11990.html
http://www.cocoachina.com/ios/20170328/18962.html
4.atomic 和 nonatomic 的区别?

http://blog.csdn.net/xueshangzhiying_ios/article/details/62039168
http://blog.csdn.net/qian521kun521/article/details/53397090

二、runtime 和 runloop相关知识

14.Runloop, runtime的理解
https://www.ianisme.com/ios/2019.html
http://www.cocoachina.com/ios/20150601/11970.html


1.Category支持添加属性与成员变量吗
https://www.jianshu.com/p/535d1574cb86

9.SEL和Method和IMP分别说下再谈下对IMP的理解?
https://www.jianshu.com/p/aff083ec3203


5.事件响应链（比如点击事件）

http://www.cocoachina.com/ios/20170720/19964.html
http://www.cocoachina.com/ios/20160113/14896.html
https://www.jianshu.com/p/6f2cc4b1f5a1

三、网络相关知识

1.Socket建立网络连接的步骤;
http://blog.csdn.net/chenlycly/article/details/51657179
http://blog.csdn.net/u013782203/article/details/51767763

3.七层协议
http://blog.csdn.net/li_ning_/article/details/52117463
http://blog.csdn.net/superjunjin/article/details/7841099


3.http的post和get啥区别
http://blog.csdn.net/wangzhilife/article/details/12440089


四、多线程相关知识

1.谈下iOS开发中知道的哪些锁? 哪个性能最差?SD和AFN使用的哪个? 一般开发中你最常用哪个? 哪个锁apple存在问题又是什么问题?
https://juejin.im/entry/5a00f59ff265da4314401967
http://blog.csdn.net/qq_30513483/article/details/52349968


6.GCD中group的优点，及串行，并行队列
http://www.cocoachina.com/ios/20150731/12819.html
https://www.jianshu.com/p/35702778d9dc
https://www.jianshu.com/p/f536f9a17d90

8.异步下载如何实现



五、block
11.block中的弱引用强引用，什么情况会导致循环引用，什么时候需要__strong保持强引用
《Objective-C高级编程：iOS与OS X多线程和内存管理》


六、APP性能优化
https://mp.weixin.qq.com/s/oUOKKEuaoVW4nNISMD-CHg
https://mp.weixin.qq.com/s/ijooFqdxQPy_75TRrSfJ0g

7.说说Cell重用原理
底层原理是两个可变数组，一个装在界面显示的cell（地址） ，一个装被标记且划出界面的cell.说到这里大家应该懂了，面试的时候千万不要说什么identifir这么简单的回答。

可以在UITableView.h文件中去搜索visible  关键字。其实底层就有有个visibleArray里面的cell就是visibleCells

七、设计模式

1. MVC /  MVVM  /MVP

2. 组件化

3. 函数编程

4. 响应式编程

八、bug 处理相关知识

8.crash的收集和定位bug的方式谈下?

https://www.jianshu.com/p/746184ea5662
https://www.jianshu.com/p/f5c4eee3a043
https://www.jianshu.com/p/799dcb0cb5ba
http://dev.umeng.com/analytics/reports/errors#2
http://bughd.com


十、其他
7.framework时动态链接库还是静态链接库，和.a的区别是什么
https://www.cnblogs.com/bboymars/p/4980754.html
https://www.jianshu.com/p/5eea9a56d249

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

32.哈希表如何处理冲突


iOS App间常用的五种通信方式
http://www.cocoachina.com/ios/20171229/21709.html

深入了解哈希表
http://ios.jobbole.com/87716/

'''




