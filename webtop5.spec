Summary: WebTop5
Name: webtop5
Version: 1.2.8
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
# Source1 and Source2 can be downloaded executing: webtop5-build.sh
Source1: webtop-webapp-5.war
Source2: sql-scripts.tar.gz
Source4: VERSION
BuildArch: noarch
Provides: webtop5-core, webtop5-libs
Obsoletes: webtop5-core, webtop5-libs
Conflicts: webtop4-core
Patch0: password_length.patch

# Do not repack JARs to avoid file date
# Should be safe: https://www.redhat.com/archives/fedora-devel-java-list/2008-September/msg00042.html
%define __jar_repack %{nil}

BuildRequires: unzip

%description
WebTop 5 RPM, see http://sonicle-webtop.sourceforge.net/


%prep
%setup

%build
mkdir -p root/var/lib/tomcats/webtop/webapps/webtop
mkdir -p root/usr/share/webtop/sql
tar xvzf %{SOURCE2} -C root/usr/share/webtop/sql
patch -d root/usr/share/webtop/sql -p1 < %{PATCH0}
unzip %{SOURCE1} -d root/var/lib/tomcats/webtop/webapps/webtop

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})

%pre
if [ $1 -gt 1 ] ; then
    # Stop Tomcat to avoid DB corruption, only if autoDeploy is set to true.
    # Note: nethserver-webtop5 should take care to restart it
    grep -qs 'autoDeploy="true"' /var/lib/tomcats/webtop/conf/server.xml
    if [ $? -eq 0 ]; then
        systemctl stop tomcat@webtop.service > /dev/null 2>&1 || :
    fi
fi

%files
%defattr(-,root,root)
/var/lib/tomcats/webtop/webapps/webtop/*
/usr/share/webtop/sql/*
%doc COPYING
%doc VERSION

%changelog
* Mon Nov 05 2018 Matteo Valentini <matteo.valentini@nethesis.it> - 1.2.8-1
- WebTop 5.4.3 - NethServer/dev#5622

* Wed Oct 24 2018 Matteo Valentini <matteo.valentini@nethesis.it> - 1.2.7-1
  - Update to upstream release 5.4.2

* Wed Oct 17 2018 Matteo Valentini <matteo.valentini@nethesis.it> - 1.2.6-1
- WebTop 5.4.1 - NethServer/dev#5607

* Wed Sep 19 2018 Matteo Valentini <matteo.valentini@nethesis.it> - 1.2.5-1
- WebTop 5.3.3 - NethServer/dev#5571

* Tue Jul 17 2018 Matteo Valentini <matteo.valentini@nethesis.it> - 1.2.4-1
- WebTop 5.2.3 - NethServer/dev#5516

* Thu May 17 2018 Matteo Valentini <matteo.valentini@nethesis.it> - 1.2.3-1
- WebTop 5.1.9 - NethServer/dev#5487

* Thu Apr 26 2018 Matteo Valentini <matteo.valentini@nethesis.it> - 1.2.2-1
- WebTop 5.1.8 - NethServer/dev#5463

* Wed Feb 21 2018 Matteo Valentini <matteo.valentini@nethesis.it> - 1.2.1-1
- WebTop 5.1.7 - NethServer/dev#5423

* Wed Jan 31 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.0-1
- WebTop 5.1.5 - NethServer/dev#5414

* Wed Nov 29 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.6-1
- Update to wt-5.1.4 - NethServer/de#5376

* Fri Sep 08 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.5-1
- WebTop 5.0.13 - Bug NethServer/dev#5338
- Stop Tomcat before WebTop deploy

* Mon Sep 04 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.4-1
- Release WebTop 5.0.13 - NethServer/dev#5338

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

