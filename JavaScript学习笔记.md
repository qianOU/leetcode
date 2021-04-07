# JavaScript

## 杂记

1. 查看对象具有的属性和方法

```javascript
console.dir(date); // 类似 python dir
```

2. 重复声明变量问题

    * 在控制台中，可以重复声明

    * 在脚本或者某一个作用域中，不允许重复声明

3. 数组==不能使用负数作为索引==, 用负数作为索引 得到的是 `undefined`

## Boolean

1. 

| 数据类型  | true                                                         | false                           |
| --------- | ------------------------------------------------------------ | ------------------------------- |
| String    | 非空字符串                                                   | 空字符串                        |
| Number    | 非0的数值                                                    | 0 、NaN                         |
| Array     | 数组不参与比较时==(空数组转换成Boolean对象时也是 true，但是在做比较时表示 fasle)== | 参与比较的空数组（[] == fasle） |
| Object    | 所有对象                                                     |                                 |
| undefined | 无                                                           | undefined                       |
| null      | 无                                                           | null                            |
| NaN       | 无                                                           | NaN                             |

2. 字符串在与Boolean比较时，两边都为转换为数值类型后再进行比较。

    ```javascript
    console.log("houdunren" == true); //false
    console.log("1" == true); //true
    ```

3. 引用类型的Boolean值为真，如对象和数组

    ```javascript
    if ([]) console.log("true");
    if ({}) console.log("true");
    ```

4. 使用 `!!`/ Boolean 转换布尔类型 

    ```javascript
    !![] // true
    Boolean([])// true
    ```

## Number

1. 指定返回的小数位数可以四舍五入

    ```javascript
    console.log((16.556).toFixed(2)); //四舍五入 16.56
    ```

2. NaN不能使用 `==` 比较使用 Number.isNaN 判断是否是 NaN

    也可以使用 `Object.is` 方法判断两个值是否完全相同

    ```text
    Number.isInteger(1.2)
    Number.isNaN(NaN) 
    Object.is(NaN, NaN)
    ```

3. 数字的二进制输出

```javascript
console.log((0.1).toString(2)) //0.0001100110011001100110011001100110011001100110011001101
```

## 数组 Array

1. 数组可以访问任意位置信息，同时也会将空的位置用空值（undefined）填充

    ```javascript
    let hd = ["后盾人"];
    hd[3] = "hdcms";
    console.log(hd.length); //4
    ```

2. 数组==不能使用负数作为索引==, 用负数作为索引 得到的是 undefined

3. 声明多个空元素的数组

    ```javascript
    let hd = new Array(3);
    console.log(hd.length);
    console.log(hd);
    ```

3. 使用`Array.of` 与 `new Array` 不同是设置一个参数时不会创建空元素数组

    ```javascript
    let hd = Array.of(3);
    Array(3) //  [空 × 3]
    console.log(hd); //[3]
    hd = Array.of(1, 2, 3);
    console.log(hd); //[1, 2, 3]
    ```

4. 类型检测：检测变量是否为数组类型

    ```javascript
    console.log(Array.isArray([1, "后盾人", "hdcms"])); //true
    [1,2,3,4] instanceof Array // true
    console.log(Array.isArray(9)); //fase
    ```

5. 使用`Array.from`可将类数组转换为数组，类数组指包含 `length` 属性或可迭代的对象。

    * 第一个参数为要转换的数据，第二个参数为类似于`map` 函数的回调方法

        ```javascript
        let str = '后盾人';
        console.log(Array.from(str)); //["后", "盾", "人"]
        Array.from('1213213', item=>parseInt(item)) //转换为数组，并且转为整形数据
        ```

    * 为对象设置`length`属性后也可以转换为数组，但要下标为数值或数值字符串

    ```javascript
    let user = {
      0: '后盾人',
      '1': 18,
      length: 2 // length 可以控制 数组中元素的个数
    };
    // 是 对象中的值作为数组元素
    console.log(Array.from(user)); //["后盾人", 18]
    ```

6. 数组 解构 拆包

    ```javascript
    //数组使用
    let [name, ...url] = ['后盾人', 'houdunren.com'];
    console.log(name);
    
    // 只赋值部分变量
    {
    [, url] = ["hdcms.com", "houdunren.com"];
    console.log(web);
    }
    
    // 为变量设置默认值
    let [name, site = 'hdcms'] = ['后盾人'];
    console.log(site); //hdcms
    
    // 函数传参的时候也可以使用 解构
    function hd([a, b]) {
    	console.log(a, b);
    }
    hd(['后盾人', 'hdcms']); //后盾人 hdcms
    ```

7. 追加元素

    `push`可以向数组追加 一个 或者 批量 增加 元素，放回`数组长度`

    ```javascript
    let arr = ["后盾人", "hdcms"];
    let hd = ["houdunren"];
    hd.push(...arr); // 批量增加,返回 3
    console.log(hd); //["houdunren", "后盾人", "hdcms"]
    ```

8. splice 可以实现数组的就地 删除，添加，替换

9. 数组查找： find（主要用于搜索数组中的 `引用类型`） 与 indexOf （`只对值类型有效`）的区别

    * find 方法找到后会把值返回出来，如果找不到的 返回 undefined，惰性查找，find 的参数 是`函数`

        ```javascript
        let arr = ["hdcms", "houdunren", "hdcms"];
        
        let find = arr.find(function(item) {
          return item == "hdcms";
        });
        ```

    * indexOf 方法找到会返回相应的索引，如果找不到返回 -1，惰性查找，参数是数组中切实存在的值

    * 使用`includes`等不能查找引用类型，因为它们的内存地址是不相等的
    * `findIndex` 与 `find` 的区别是返回索引，查找不到时，返回 - 1

    10. 数组排序 sort

    ```javascript
    语法： 
    Array.sort((a,b)=>a-b) // 从小到大排序
    - 返回负数     a 排在 b前面，从小到大
    - 返回正数      b 排在a 前面
    - 返回  0  时     不动
    
    
    Array.sort((a,b)=>b-a) // 从大到小排序
    ```

    默认从小于大排序数组元素

    ```javascript
    let arr = [1, 4, 2, 9];
    console.log(arr.sort()); //[1, 2, 4, 9]
    console.log(arr.sort().reverse()); // 从大到小
    ```

    使用排序函数从大到小排序，参数一与参数二比较，==返回正数为降序负数为升序==

    ```javascript
    let arr = [1, 4, 2, 9];
    
    console.log(arr.sort(function (v1, v2) {
    	return v2 - v1;
    })); //[9, 4, 2, 1]
    ```

    11.  `forEach`使函数作用在每个数组元素上，但是没有返回值。

        作为参数的函数接受三个参数分别是：`数组元素`，`数组索引`，`数组本身`

        ```javascript
        let lessons = [
        	{title: '媒体查询响应式布局',category: 'css'},
          {title: 'FLEX 弹性盒模型',category: 'css'},
        	{title: 'MYSQL多表查询随意操作',category: 'mysql'}
        ];
        // 注意函数参数的意义
        lessons.forEach((item, index, array) => {
            item.title = item.title.substr(0, 5);
            console.log(array[2].title);
        });
        console.log(lessons);
        ```

    12. for / in 取的是数组索引， for / of 取的是数组值 

    13. 使用解构技术，同时获取 数组的索引和值

    ```javascript
    const hd = ["hdcms", "houdunren"];
    // 解构, entries 有点类似 python 中的 enumerate
    for (const [key, value] of hd.entries()) {
      console.log(key, value); //这样就可以遍历了
    }
    ```

    14. 迭代器

    ```javascript
    const hd = ["houdunren", "hdcms"];
    const keys = hd.keys(); // 获取索引的迭代器
    let arr = ["hdcms", "houdunren"];
    while (({ value, done } = values.keys()) && done === false) {
    	console.log(value);
    }
    
    const values = hd.values() // 获取元素的迭代器
    const pairs = hd.entries() // 同时获取 数组的索引和值
    // 解构获取内容
    let {done:done, value:[k, v]} =  hd.entries().next()
    // 在 遍历时 可以 选择忽略 done 参数
    const arr = ["a", "b", "c", "后盾人"];
    for (const [key, value] of arr.entries()) {
      console.log(key, value);
    }
    ```

    15. every 与 some

    `every` 用于递归的检测元素，==要所有元素操作都要返回真结果才为真==。（传递的参数是函数，函数返回的是bool值）使用 `some` 函数可以递归的检测元素，如果有一个返回true，表达式结果就是真。其中：函数位置参数有下列规定，第一个参数为元素，第二个参数为索引，第三个参数为原数组。

    ```javascript
    const user = [
      { name: "李四", js: 89 },
      { name: "马六", js: 55 },
      { name: "张三", js: 78 }
    ];
    const resust = user.every((user, index, arr) => user.js >= 60);
    console.log(resust);
    ```

    16. 使用 `filter` 可以过滤数据中元素，其中传递的参数也是函数。保留那行返回 true 的元素。

    ```javascript
    let lessons = [
      {title: '媒体查询响应式布局',category: 'css'},
      {title: 'FLEX 弹性盒模型',category: 'css'},
      {title: 'MYSQL多表查询随意操作',category: 'mysql'}
    ];
    
    // 函数参数为 ： 元素， 索引， 数组
    let cssLessons = lessons.filter(function (item, index, array) {
      if (item.category.toLowerCase() == 'css') {
        return true;
      }
    });
    
    console.log(cssLessons);
    ```

    17. 使用 `map` 映射可以在数组的所有元素上应用函数，用于映射出新的值。

    18. `reduce `

        `reduce` 第一个参数是执行函数，第二个参数为初始值

        - 传入第二个参数时将所有元素循环一遍
        - 不传第二个参数时从第二个元素开始循环

        | 参数  | 说明                       |
        | ----- | -------------------------- |
        | prev  | 上次调用回调函数返回的结果 |
        | cur   | 当前的元素值               |
        | index | 当前的索引                 |
        | array | 原数组                     |

        ```javascript
        // 数组去重
        let arr = [1, 2, 6, 2, 1];
        let filterArr = arr.reduce((pre, cur, index, array) => {
          if (pre.includes(cur) === false) {
              //pre = [...pre, cur];
              pre.push(cur);
          }
          return pre;
        }, []) // 初始是一个空数组
        console.log(filterArr); // [1,2,6]
        ```

    