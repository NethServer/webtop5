## WebTop 5

WebTop5 is a modern web groupware solution written in Java and HTML5.

#### How to report a bug

- Report the issue on community.nethserver.org under the WebTop category
- After the discussion, a developer will take care to open the issue inside the official issue tracker
- The issue number will be posted back to the discussion, so everyone will be able to follow the development

### Build from source

You can build WebTop 5 directly from sources, just make sure to have
installed following software inside your machine:

- Maven: [https://maven.apache.org/](https://maven.apache.org/)
- JDK Java compiler [http://openjdk.java.net/](http://openjdk.java.net/)

On Fedora 25:
```
dnf install maven java-1.8.0-openjdk-devel
```

On CentOS 7:
```
yum install maven java-1.8.0-openjdk-devel bzip2
```

Please, see istruction here: https://github.com/sonicle/sonicle-webtop5-gate

#### webtop5-build.sh

You can use also use ``webtop5-build.sh`` automation script.

Before starting the script, make sure to select the correct release by adding it to `VERSION` file:
```
echo wt-5.1.4 > VERSION
```

List of available releases: https://github.com/sonicle-webtop/webtop-webapp/releases

### WebTop 5 on NethServer

Official manual: [http://docs.nethserver.org/en/latest/webtop5.html](http://docs.nethserver.org/en/latest/webtop5.html)


To install, access the Software Center and install the "WebTop 5" module or execute from command line:
```
yum install nethserver-webtop5
```

### Links

- [Discussions around WebTop](http://community.nethserver.org/c/webtop)
- [Official site](https://redmine.sonicle.com/projects/webtop5)
- [Official issue tracker](https://redmine.sonicle.com/projects/webtop5/issues)
- [Internationalization](https://www.transifex.com/sonicle/public/)
- [NethServer internals and debug](http://docs.nethserver.org/projects/nethserver-devel/en/latest/nethserver-webtop5.html)


