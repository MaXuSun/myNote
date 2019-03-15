1. 解决搜狗输入法候选乱码问题:
>cd ~/.config
sudo rm -rf SogouPY* sogou*
然后注销即可(注意，这里必须是注销，不注销直接重启并不管用

2. python2.7和3.5间的互换
sudo cp /usr/bin/python /usr/bin/python_bak
第二步：删除原来默认指向python2.7版本的链接。在ternimal下输入命令：
sudo rm /usr/bin/python
第三步：重新指定新的链接给python3.5版本。输入命令：
sudo ln -s /usr/bin/python3.5 /usr/bin/python

3. python 3.7的安装
    * 官网下载源码
    *.tar -zxvf Python-3.7.0.tgz -C ~
    *.安装依赖库sudo apt-get install zlib1g-dev libbz2-dev libssl-dev libncurses5-dev  libsqlite3-dev libreadline-dev tk-dev libgdbm-dev libdb-dev libpcap-dev xz-utils libexpat1-dev   liblzma-dev libffi-dev  libc6-dev
    *.配置安装位置./configure --prefix=/opt/python3.7  --enable-optimizations
    *.进入python-3.7.0编译:make -j 4
    *.sudo make install
    *.sudo make && make install 
    *.将/opt/python3.7/bin/python3连接到/usr/bin/python中
4. 安装好看的主题
    * sudo apt-get install unity-tweak-tool
    * 扁平主题
        sudo add-apt-repository ppa:noobslab/themes
        sudo apt-get update
        sudo apt-get install flatabulous-theme
        sudo add-apt-repository ppa:noobslab/icons
        sudo apt-get update
        sudo apt-get install ultra-flat-icons
    * arc 主题
        sudo add-apt-repository ppa:noobslab/themes
        sudo apt-get update
        sudo apt-get install arc-theme
        sudo add-apt-repository ppa:noobslab/icons
        sudo apt-get update
        sudo apt-get install arc-icons
    * numix 主题
        * sudo add-apt-repository ppa:numix/ppa
        sudo apt-get update
        sudo apt-get install numix-gtk-theme numix-icon-theme-circle
    * 单个的主题或图标
        * sudo add-apt-repository ppa:noobslab/icons
        sudo apt-get update
        sudo apt-get install square-beam-icons
        * sudo add-apt-repository ppa:snwh/pulp
        sudo apt-get update
        sudo apt-get install paper-icon-theme
    * 折腾更好看的：https://blog.csdn.net/YuYunTan/article/details/85052956
5. 安装QQ
    1. 安装deepin-wine环境：上https://github.com/wszqkzqk/deepin-wine-ubuntu页面下载zip包（或用git方式克隆），解压到本地文件夹，在文件夹中打开终端，输入sudo sh ./install.sh一键安装。
    2. 安装相关应用容器：在http://mirrors.aliyun.com/deepin/pool/non-free/d/中下载想要的容器，点击deb安装即可。以下为推荐容器，下载后使用dpkg安装
        * TIM：http://mirrors.aliyun.com/deepin/pool/non-free/d/deepin.com.qq.office/
        * QQ：http://mirrors.aliyun.com/deepin/pool/non-free/d/deepin.com.qq.im/
        * QQ轻聊版：http://mirrors.aliyun.com/deepin/pool/non-free/d/deepin.com.qq.im.light/
    3. 之后的一些问题:
        * Ubuntu桌面无法显示托盘图标：安装TopIconPlus的gnome-shell扩展，命令：sudo apt-get install gnome-shell-extension-top-icons-plus gnome-tweaks，然后用r命令重启gnome-shell，最后用gnome-tweaks开启这个扩展。
        * Ubuntu系发行版不知道如何卸载包：wszqkzqk同学已提供deepinwine环境的uninstall.sh脚本。至于deepinwine的应用容器，用sudo apt remove 软件包主名命令来删除。比如deepin.com.qq.office_2.0.0deepin4_i386.deb的卸载命令是sudo apt remove deepin.com.qq.office
6. 使用监控工具conky
    * https://www.linuxidc.com/Linux/2012-09/71478.htm
    * https://www.linuxidc.com/Linux/2011-02/32508.htm
7. 安装shadowsocks
    * 此时已经将Ubuntu中原生的python2.7换为了python3.7,所以在安装前需要安装pip3
    * sudo apt-get install python3-pip
    * sudo pip3 install shadowsocks
    * sslocal -p ×× -k ……

8. 安装git最新版
>sudo add-apt-repository ppa:git-core/ppa
sudo apt-get update
sudo apt-get install git

9. 配置git
    * 在~/.ssh文件夹下进行操作
    * ssh-keygen -t rsa -C "邮箱地址"   //生成私钥和公钥
    * 将公钥放到github的ssh中
    * 使用 ssh -T git@github.com进行1尝试连接
    * 配置git
        * git config --global user.name "github用户名"
        * git config --global user.email "github邮箱地址"
10. 在同一台电脑上配置github和gitlab
    1. ssh-keygen -t rsa -C "注册 gitlab 账户的邮箱"
    ssh-keygen -t rsa -C "注册 github 账户的邮箱"
    2. 将两个.pub文件分别配置到GitLab和GitHub的ssh keys中
    3. 编写config文件:vim ~/.ssh/config
    >Host github.com
    HostName github.com
    User 任意名称
    IdentityFile ~/.ssh/github_id_rsa
    Host 公司GitLab的域名
    HostName 公司GitLab的域名
    User 任意名称
    IdentityFile ~/.ssh/gitlab_id_rsa
    4. 创建本地仓库
    >git init
    git config --global user.name "注册GitLab的用户名"
    git config --global user.email "注册GitLab的邮箱"
    git init
    git config --global user.name "注册GitHub的用户名"
    git config --global user.email "注册GitHub的邮箱"

