%define webtop_version rc6

Summary: WebTop5 core
Name: webtop5-core
Version: 1.0.1
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
Source1: http://www.sonicle.com/nethesis/webtop5/nethesis-webtop5-%{webtop_version}.zip 
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
mkdir -p root/usr/share/webtop/
unzip %{SOURCE1}
mv sql root/usr/share/webtop/
unzip webtop5.war \
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
echo %{webtop_version} > root/usr/share/webtop/doc/VERSION

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})

%post

%preun

%files
%defattr(-,root,root)
/var/lib/tomcats/webtop/webapps/webtop/*
/usr/share/webtop/sql/*
%doc /usr/share/webtop/doc/VERSION
%doc COPYING

%changelog
* Thu Mar 09 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- WebTop 5: contacts don't work at all - Bug NethServer/dev#5237

* Wed Mar 08 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- First WebTop5 release - NethServer/dev#5225

