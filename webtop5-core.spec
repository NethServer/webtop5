Summary: WebTop5 core
Name: webtop5-core
Version: 1.1.2
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
# Source1 and Source2 can be downloaded executing: webtop5-build.sh
Source1: webtop-webapp-5.war
Source2: sql-scripts.tar.gz
Source4: VERSION
BuildArch: noarch
Requires: webtop5-libs
Conflicts: webtop4-core

BuildRequires: unzip

%description
NethServer WebTop 5 core libraries

%prep
%setup

%build
mkdir -p root/var/lib/tomcats/webtop/webapps/webtop
mkdir -p root/usr/share/webtop/sql
tar xvzf %{SOURCE2} -C root/usr/share/webtop/sql
unzip %{SOURCE1} \
 WEB-INF/*sonicle*.jar \
 WEB-INF/*webtop*.jar \
 META-INF/MANIFEST.MF \
 META-INF/context.xml \
 META-INF/data-sources.xml \
 WEB-INF/classes/logback.xml \
 WEB-INF/shiro.ini \
 WEB-INF/web.xml \
 -d root/var/lib/tomcats/webtop/webapps/webtop
mkdir -p root/usr/share/webtop/doc/
cp %{SOURCE4} root/usr/share/webtop/doc/

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})

%post

%preun

%files
%defattr(-,root,root)
/var/lib/tomcats/webtop/webapps/webtop/*
/usr/share/webtop/sql/*
%doc COPYING
%doc /usr/share/webtop/doc/VERSION

%changelog
* Tue Jun 13 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.2-1
- Release WebTop 5.0.9 - NethServer/dev#5312

* Fri Jun 09 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.1-1
- Release WebTop 5.0.7 (tag 5.0.8) - NethServer/dev#5312

* Wed May 17 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.0-1
- WebTop 5: enable folder sorting - NethServer/dev#5275
- Build RPM from source

* Mon Mar 27 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1
- Upgrade to RC 6 - NethServer/dev#5250

* Thu Mar 09 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- WebTop 5: contacts don't work at all - Bug NethServer/dev#5237

* Wed Mar 08 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- First WebTop5 release - NethServer/dev#5225

