## WebTop 5 (rc)

WebTop5 is a modern web groupware solution written in Java and HTML5.

- [Features](#features)
- [Support](#support)
- [Download](#download)
- [Roadmap](#roadmap)
- [RPM install](#rpm-install)
- [ActiveSync](#activesync)
- [Manual install](#manual-install)
- [Internals and debug](http://docs.nethserver.org/projects/nethserver-devel/en/v7/nethserver-webtop5.html)

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

- Documentation about build process to obtain a working WAR file out of the source code
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

This is a **rc** release.

Access the command line, and execute:

```
yum --enablerepo=nethserver-testing install nethserver-webtop5
```
#### Login

Always use the full user name format user@domain.

Example:

- Domain: local.nethserver.org
- User: goofy
- Login: goofy@local.nethserver.org

Default *admin* password is *admin*.

### ActiveSync

ActiveSync is automatically enabled for all users, the default "WebTop" category
for contacts, tasks and calendar is configured in read/write mode for all synched devices.


You can test ActiveSync using this command (please set user, password and server_name):
```
curl -k -u goofy@local.neth.eu:password https://server_name/Microsoft-Server-ActiveSync 
```

You should see an HTML output containing the string:
```
GET not supported
```

### Manual install

You should not need to follow this procedure if you're using WebTop5 on NethServer.

#### Requirements

- Java 1.7
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

- set domain configuration with LDAP user and password (see below)

##### Authentication configuration

The authentication is configured inside the ``core.domains`` table.
Eeach record is a domain with the following fields:

- ``domain_id``: unique id for WebTop domain
- ``internet_name``:  eg. "sonicle.com", is the Internet domain mapped into WebTop domain
- ``enabled``: enabled / disable the domain
- ``description``: description displayed inside the admin section of the web interface
- ``user_auto_creation``: if enabled, each user configured inside the LDAP will be able to login;
  if disabled, the admin must manually enable all users before login
- ``dir_uri``:  (eg "ldapwebtop://www.sonicle.com:389"), identify the directory (LDAP) used for
  authentication and user list. Supported prefixes:
  - webtop: local authentication on db
  - ldap: remote or local LDAP
  - ldapwebtop: LDAP preset fpr xstreamserver
  - ldapneth: LDAP preset for NethServer
  - ad: LDAP preset for Active Directory
- ``dir_admin``: administrative user used for operartions on users. If the autentication
  backend is a LDAP server, it represents the admin DN
- ``dir_password``: set the password for ``dir_admin``
- ``dir_connection_security``: set the security policy for LDAP connection. Supported values: ``<null>``, ``SSL``, ``STARTTLS``
- ``dir_case_sensitive``: if enabled, usernames for login will evaluated in case-sensitive manner
- ``dir_password_policy``: if enabled, WebTop will check for password strenght
- ``dir_parameters``: string in JSON format to configure LDAP parameters. Supported parameters:
   - ``loginDn``: base DN for login (required)
   - ``loginFilter``: filter to allow the login only for selected users (optional)
   - ``userIdField``: fielter to retrieve the user name (optional)
   - ``userDn``: user tree (required)
   - ``userFilter``: filter to restrict the list of users (optional)
   - ``userFirstnameField``: field to retrieve the first name (optional)
   - ``userLastnameField``: field to retrieve the last name (optional)
   - ``userDisplayNameField``: field to retrieve the full name

   Example:
   ```
   {"loginDn":"ou=People,dc=directory,dc=nh","loginFilter":null,"userDn":"ou=People,dc=directory,dc=nh","userFilter":null,"userFirstnameField":null,"userLastnameField":null,"userDisplayNameField":null}
   ```

#### WAR deployment

Create the following directories:

```
mkdir -p /var/lib/nethserver/webtop/domains/NethServer
mkdir -p /var/lib/nethserver/webtop/domains/NethServer/images
mkdir -p /var/lib/nethserver/webtop/domains/NethServer/temp
mkdir -p /var/lib/nethserver/webtop/domains/NethServer/models
chown -R tomcat:tomcat /var/lib/nethserver/webtop
```

Change database credentials inside `META-INF/data-sources.xml` file.

Explode the WAR inside Tomcat webapps directory: `/var/lib/tomcat/webapps`.

#### Tomcat configuration

Recommended Tomcat options inside `/etc/sysconfig/tomcat.conf`:

```
JAVA_OPTS="-server -Xms1024m -Xmx2048m -XX:PermSize=64m -XX:MaxPermSize=256m -Djava.security.egd=file:/dev/./urandom -Dfile.encoding=UTF8 -Dcom.sonicle.webtop.extjsdebug=true -Dcom.sonicle.webtop.scheduler.disable=false -Dcom.sonicle.webtop.devmode=true -Dcom.sonicle.webtop.soextdevmode=false"
```

