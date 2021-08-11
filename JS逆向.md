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

#### hook 时机

1. 控制台注入的hook，刷新页面就失效
2. 在网页加载的第一个JS的位置，第一行下断点，然后控制台手动注入hook（有可能注入的hook还是晚了一些）3
3. 利用 FD 的替换响应，注入 hook ，这种类型的注入时间比较靠前
4. Hook 局部变量的时候，需要在生成局部变量的位置下断点，之后动态注入 hook。

