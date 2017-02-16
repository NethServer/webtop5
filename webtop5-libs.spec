%define webtop_version beta3

Summary: WebTop5 libs
Name: webtop5-libs
Version: 0.0.1
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
Source1: http://www.sonicle.com/nethesis/webtop5/nethesis-webtop5-%{webtop_version}.zip 
BuildArch: noarch
Conflicts: webtop4-libs

BuildRequires: unzip

%description
NethServer WebTop 5 libraries

%prep
%setup

%build
mkdir -p root/var/lib/tomcat/webapps/webtop
unzip %{SOURCE1}
unzip webtop5.war \
 *jar \
 -x *sonicle*.jar \
 -x *webtop*.jar \
 -d root/var/lib/tomcat/webapps/webtop

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})

%post

%preun

%files
%defattr(-,root,root)
/var/lib/tomcat/webapps/webtop/*

%changelog
