# gladosAutoCheckin
实现glados每日自动签到
自动签到的结果以及签到后账户中剩余使用天数会通过server酱推送到微信中

签到时间为每天的中午十二点


### 使用方法
sendKey为推送用户server酱的sendKey，修改该值即可修改推送的用户

使用时需要修改headers变量中的cookie值，打开Glados官网后进入开发者模式，找到请求中的cookie字段复制过来即可

### 备注
实际上处理请求的返回值可以用json模块，但我还没有学过，就自己写了个简单的函数做了下处理
