%define webtop_version beta3

Summary: WebTop5 core
Name: webtop5-core
Version: 0.0.1
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
mkdir -p root/var/lib/tomcat/webapps/webtop
mkdir -p root/usr/share/webtop/
unzip %{SOURCE1}
mv sql root/usr/share/webtop/
unzip webtop5.war \
 WEB-INF/*sonicle*.jar \
 WEB-INF/*webtop*.jar \
 META-INF/MANIFEST.MF \
 META-INF/context.xml \
 WEB-INF/classes/logback.xml \
 WEB-INF/shiro.ini \
 WEB-INF/web.xml \
 -d root/var/lib/tomcat/webapps/webtop
mkdir -p root/usr/share/webtop/doc/
echo %{webtop_version} > root/usr/share/webtop/doc/VERSION

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})

%post

%preun

%files
%defattr(-,root,root)
/var/lib/tomcat/webapps/webtop/*
/usr/share/webtop/sql/*
%doc /usr/share/webtop/doc/VERSION
%doc COPYING

%changelog
