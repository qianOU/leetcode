# JS逆向

#### 抓包设置

![image-20210802153040803](D:\桌面\学习记录\markdwon笔记图片保存内容\image-20210802153040803.png)

#### 常见JS库

1. Jquery 主要用于发送异步请求。

#### 杂记

1. `call stack 调用栈`，最上面的是栈顶元素，栈顶函数是依次嵌套被栈底函数调用的。

2. `Initatior 中的函数显示也是符合调用栈的形式`，最上面的是栈顶函数。

3. 查看调用栈，或者搜索出的 JS 结果的时候，==可以忽视掉那些 JS库文件或者函数==。诸如：Jquery，react，vue 等。

    ![image-20210802160628455](C:\Users\28659\AppData\Roaming\Typora\typora-user-images\image-20210802160628455.png)

## JS断点设置方案

1. 搜索关键词（一般其后看调用栈）`Ctrl + shift + F`

2. DOM 事件跟踪 （跟踪的位置一般都在加密位置之前，所以不怎么看栈）

    ![image-20210802153319642](C:\Users\28659\AppData\Roaming\Typora\typora-user-images\image-20210802153319642.png)

3. XHR 断点

![image-20210802153949763](C:\Users\28659\AppData\Roaming\Typora\typora-user-images\image-20210802153949763.png)



## 定位参数

### hook 方法

#### hook 类型

1. 覆盖函数

```javascript
var tmp = window.alert // 暂存 alert 方法
// hook window.alert 方法
window.alert = function(){console.log('has been hook!')}
```



