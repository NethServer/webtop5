## WebTop 5 (beta)

WebTop5 is a modern web groupware solution written in Java and HTML5.

- [Features](#features)
- [Support](#support)
- [Download](#download)
- [Roadmap](#roadmap)
- [RPM install](#rpm-install)
- [Manual install](#manual-install)

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

- Documentation about build process to obtain a working war out of the source code
- Contribution guidelines on how to open a pull request
- CardDav/CalDav support
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


### RPM install

Access the command line, and execute:

```
yum --enablerepo=nethserver-testing install nethserver-webtop5
```

### Manual install

#### Requirements

- Java 1.7 or higher
- Tomcat 7 or higher
- PostgreSQL

#### Download

- Download the latest release from: [http://www.sonicle.com/nethesis/webtop5/](http://www.sonicle.com/nethesis/webtop5/)
- Extract the zip

#### Database

- Create a new database named `webtop5`
- Execute all sql scripts iniside `sql/schema` directory
- Edit sql scripts inside `sql/data` accordingly to your needs
- Execute all sql scripts inside `sql/data` in the following order:

  - init-data-core.sql
  - nethserver-domain-init.sql


##### Default settings

init-data-core.sql:

- set admin password under `local_vault` section
- set Dropbox key, Google drive key and  vmailsecret under  `settings` section

init-data-mail.sql:

- check configuration under `settings` section (eg. spam folder name)

nethserver-domain-init.sql

- set domain configuration with LDAP user and password

#### WAR deployment

Create the following directories:

```
mkdir -p /var/lib/nethserver/webtop/domains/NethServer
mkdir -p /var/lib/nethserver/webtop/domains/NethServer/images
mkdir -p /var/lib/nethserver/webtop/domains/NethServer/temp
mkdir -p /var/lib/nethserver/webtop/domains/NethServer/models
chown -R tomcat:tomcat /var/lib/nethserver/webtop
```

Explode the WAR inside Tomcat webapps directory: `/var/lib/tomcat/webapps`.

#### Tomcat configuration

Recommended Tomcat options inside `/etc/sysconfig/tomcat.conf`:

```
JAVA_OPTS="-server -Xms1024m -Xmx2048m -XX:PermSize=64m -XX:MaxPermSize=256m -Djava.security.egd=file:/dev/./urandom -Dfile.encoding=UTF8 -Dcom.sonicle.webtop.extjsdebug=true -Dcom.sonicle.webtop.scheduler.disable=false -Dcom.sonicle.webtop.devmode=true -Dcom.sonicle.webtop.soextdevmode=false"
```
