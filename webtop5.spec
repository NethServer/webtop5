Summary: WebTop5
Name: webtop5
Version: 1.4.5
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
# Source1 and Source2 can be created executing the 'prep-sources' script
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
patch -d root/usr/share/webtop/sql/schema -p0 < %{PATCH0}
unzip %{SOURCE1} -d root/var/lib/tomcats/webtop/webapps/webtop
mv root/var/lib/tomcats/webtop/webapps/webtop/META-INF/data-sources.xml root/var/lib/tomcats/webtop/webapps/webtop/META-INF/data-sources.xml.example

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})


%files
%defattr(-,root,root)
/var/lib/tomcats/webtop/webapps/webtop/*
/usr/share/webtop/sql/*
%doc COPYING
%doc VERSION

%changelog
* Mon Mar 23 2020 Matteo Valentini <matteo.valentini@nethesis.it> - 1.4.5-1
- WebTop 5.8.3 - NethServer/dev#6079

* Wed Mar 04 2020 Matteo Valentini <matteo.valentini@nethesis.it> - 1.4.4-1
- WebTop 5.8.1 - NethServer/dev#6060

* Tue Jan 07 2020 Matteo Valentini <matteo.valentini@nethesis.it> - 1.4.3-1
- WebTop 5.7.7 - NethServer/dev#5985
  - Update to upstream release 5.7.7

* Tue Dec 03 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.4.2-1
- WebTop 5.7.5 - NethServer/dev#5928

* Thu Nov 07 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.4.1-1
- WebTop 5.7.4 - NethServer/dev#5903

* Tue Oct 01 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.4.0-1
- WebTop 5.7.3 - NethServer/dev#5770

* Tue Jun 25 2019 Matteo Valentini <matteo.valentini@nethesis.it> - 1.3.0-1
- WebTop 5.7.1 - NethServer/dev#5770
  - Update to upstream release 5.7.1
  - Revert "rpm spec: restart tomcat after upgrade"

* Tue May 28 2019 Matteo Valentini <matteo.valentini@nethesis.it> - 1.2.15-1
- WebTop 5.6.5 - NethServer/dev#5768

* Tue Apr 30 2019 Matteo Valentini <matteo.valentini@nethesis.it> - 1.2.14-1
- WebTop 5.6.4 - NethServer/dev#5750

* Tue Mar 26 2019 Matteo Valentini <matteo.valentini@nethesis.it> - 1.2.13-1
- WebTop: no icon on mail attachments - Bug NethServer/dev#5731
- WebTop 5.6.3 - NethServer/dev#5729

* Wed Feb 20 2019 Matteo Valentini <matteo.valentini@nethesis.it> - 1.2.12-1
- WebTop 5.5.3 - NethServer/dev#5712
  - Update to upstream release 5.5.3

* Tue Feb 12 2019 Matteo Valentini <matteo.valentini@nethesis.it> - 1.2.11-1
- WebTop 5.5.2 - NethServer/dev#5706
  - Update to upstream release 5.5.2

* Thu Dec 13 2018 Matteo Valentini <matteo.valentini@nethesis.it> - 1.2.10-1
-  WebTop 5.5.0 - NethServer/dev#5666
  - Update to upstream release 5.5.0

* Thu Nov 22 2018 Matteo Valentini <matteo.valentini@nethesis.it> - 1.2.9-1
- Webtop 5.4.5 - NethServer/dev#5651

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

