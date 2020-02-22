# New_project
做一个pdf提取文中图片的算法



现在想到的算法是..

先在pdf中提取段落文字,这些文字的特征是可以学到的.ocr识别文本然后再拼接成块,然后做一些判断


然后得到段落的首尾坐标.那么余下的部分就可以进行裁剪了.

最后用opencv等,进行裁剪之后的一圈进行像素比较.裁剪出最后的图片. 基本就是提出多余的空白部分.






下面进行实践..


因为没有服务器了,就自己弄docker整centos系统.

2020-02-21,14点30

docker 搞出来了

https://qq52o.me/2475.html
用的是Docker Quickstart Terminal

注意修改配置后要重启电脑才行.

然后以后这个窗口就跟使用centos一样.

比如复制东西就再开一个这个terminal 然后 docker cp 即可.

内存不够:
docker run -d -m 6G --memory-swap 7G -p 9999:80  --restart=always --name gitlab twang2218/gitlab-ce-zh
a3254078a79a084f3f3bed5f4ade3e26c7d86951cd822d95b113227d75b00097

docker run -ti -m 6G --memory-swap 7G  a6bef5378b95

上面这条命令没有用的.
需要打开virtual box ,然后设置default里面的内存大小.然后启动default 虚拟机.
这时候再在docker 中输入上面的命令才可以修改虚拟机中的内存!!!!!!!!!!!















然后ocr 用的还是自己的ocr_byzhang这个镜像.










