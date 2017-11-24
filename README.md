## WebTop 5

WebTop5 is a modern web groupware solution written in Java and HTML5.

- [Features](#features)
- [Support](#support)
- [Build](#build-from-source)
- [Roadmap](#roadmap)
- [WebTop5 on NethServer](#webtop-5-on-nethserver)
- [Internals and debug](http://docs.nethserver.org/projects/nethserver-devel/en/latest/nethserver-webtop5.html)

### Features

- Web based
- IMAP mail client
- Calendar
- Contacts
- Tasks
- ActiveSync support


### Support

Discussions around WebTop:
[http://community.nethserver.org/c/webtop](http://community.nethserver.org/c/webtop)

Official site:
[https://redmine.sonicle.com/projects/webtop5](https://redmine.sonicle.com/projects/webtop5)

Issue tracker:
[https://redmine.sonicle.com/projects/webtop5/issues](https://redmine.sonicle.com/projects/webtop5/issues)

Internationalization:
[https://www.transifex.com/sonicle/public/](https://www.transifex.com/sonicle/public/)

#### How to report a bug

- Report the issue on community.nethserver.org under the WebTop category
- After the discussion, a developer will take care to open the issue inside the official issue tracker
- The issue number will be posted back to the discussion, so everyone will be able to follow the development

### Roadmap

This is a temporary roadmap and it will likely change in the near feature.
It will be updated as soon as we gather feeback from the community.

February 2017

- Release of a stable release with all basic functions

Q1/2017

- Publish always up to date source code
- Basic developer and user documentation
- Translations opened to external contributors using a public tool
- Better mail client with improved Sieve filters, folder subscriptions
- Migration path from WebTop 4 to WebTop 5

Q2/2017

- Documentation about build process to obtain a working WAR file out of the source code
- Contribution guidelines on how to open a pull request
- ~~CardDav/CalDav support~~
- Mail archive
- Tags for mail messages
- Integrated instant messaging
- Nextcloud integration

Q3/2017

- User dashboard
- Subscription of external calendars
- Global search
- Bulk operations

Q4/2017

- Export of calendar and contacts
- Improved layout for tablets

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
