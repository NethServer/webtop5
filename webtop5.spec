Summary: WebTop5
Name: webtop5
Version: 1.5.20
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
* Mon Sep 23 2024 Matteo Valentini <matteo.valentini@nethesis.it> - 1.5.20-1
- WebTop 5.25.1 - NethServer/dev#7012

* Tue Jul 23 2024 Matteo Valentini <matteo.valentini@nethesis.it> - 1.5.19-1
- WebTop 5.24.1 - NethServer/dev#6973

* Thu May 23 2024 Matteo Valentini <matteo.valentini@nethesis.it> - 1.5.18-1
- WebTop 5.24.0 - NethServer/dev#6921

* Fri May 03 2024 Matteo Valentini <matteo.valentini@nethesis.it> - 1.5.17-1
- WebTop 5.22.1 - NethServer/dev#6904

* Tue Nov 28 2023 Matteo Valentini <matteo.valentini@nethesis.it> - 1.5.16-1
- WebTop 5.21.3 - NethServer/dev#6775

* Wed Nov 22 2023 Matteo Valentini <matteo.valentini@nethesis.it> - 1.5.15-1
- WebTop 5.21.2 - NethServer/dev#6775

* Thu Oct 19 2023 Matteo Valentini <matteo.valentini@nethesis.it> - 1.5.14-1
- WebTop 5.21.1 - NethServer/dev#6764

* Wed Jul 26 2023 Matteo Valentini <matteo.valentini@nethesis.it> - 1.5.13-1
- WebTop 5.20.3 - NethServer/dev#6756

* Wed Jul 05 2023 Matteo Valentini <matteo.valentini@nethesis.it> - 1.5.12-1
- WebTop 5.20.1 - NethServer/dev#6753

* Thu Apr 27 2023 Matteo Valentini <matteo.valentini@nethesis.it> - 1.5.11-1
- WebTop 5.19.6 - NethServer/dev#6736

* Mon Mar 13 2023 Matteo Valentini <matteo.valentini@nethesis.it> - 1.5.10-1
- WebTop 5.18.5 - NethServer/dev#6734

* Mon Dec 12 2022 Matteo Valentini <matteo.valentini@nethesis.it> - 1.5.9-1
- WebTop 5.18.4 - NethServer/dev#6724

* Fri Nov 04 2022 Matteo Valentini <matteo.valentini@nethesis.it> - 1.5.8-1
- WebTop 5.18.3 - NethServer/dev#6714

* Fri Oct 14 2022 Matteo Valentini <matteo.valentini@nethesis.it> - 1.5.7-1
- WebTop 5.18.2 - NethServer/dev#6701

* Tue Jul 12 2022 Matteo Valentini <matteo.valentini@nethesis.it> - 1.5.6-1
- WebTop 5.17.5 - NethServer/dev#6684

* Wed Jul 06 2022 Matteo Valentini <matteo.valentini@nethesis.it> - 1.5.5-1
- WebTop 5.17.4 - NethServer/dev#6683

* Fri Jul 01 2022 Matteo Valentini <matteo.valentini@nethesis.it> - 1.5.4-1
- WebTop 5.17.3 - NethServer/dev#6674

* Wed May 18 2022 Matteo Valentini <matteo.valentini@nethesis.it> - 1.5.3-1
- WebTop 5.16.5 - NethServer/dev#6662

* Fri Apr 22 2022 Matteo Valentini <matteo.valentini@nethesis.it> - 1.5.2-1
- WebTop 5.16.3 - NethServer/dev#6656

* Tue Apr 12 2022 Matteo Valentini <matteo.valentini@nethesis.it> - 1.5.1-1
  - Update to upstream release wt-5.16.2

* Mon Mar 21 2022 Matteo Valentini <matteo.valentini@nethesis.it> - 1.5.0-1
- WebTop 5.16.1 - NethServer/dev#6640
  - Update to upstream release wt-5.16.1
  - prep-sources: use new Sonicle's build system

* Thu Nov 25 2021 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.4.26-1
- WebTop 5.14.2 - NethServer/dev#6604

* Thu Nov 11 2021 Matteo Valentini <matteo.valentini@nethesis.it> - 1.4.25-1
- WebTop 5.14.1 - NethServer/dev#6585

* Thu Sep 16 2021 Matteo Valentini <matteo.valentini@nethesis.it> - 1.4.24-1
- WebTop 5.13.2 - NethServer/dev#6570

* Mon Jul 26 2021 Matteo Valentini <matteo.valentini@nethesis.it> - 1.4.23-1
- WebTop 5.13.1 - NethServer/dev#6549

* Wed Jul 21 2021 Matteo Valentini <matteo.valentini@nethesis.it> - 1.4.22-1
-  WebTop 5.13.0 - NethServer/dev#6544

* Thu Jul 01 2021 Matteo Valentini <matteo.valentini@nethesis.it> - 1.4.21-1
- WebTop 5.12.4 - NethServer/dev#6536

* Thu Jun 10 2021 Matteo Valentini <matteo.valentini@nethesis.it> - 1.4.20-1
- WebTop 5.12.3 - NethServer/dev#6521

* Mon May 31 2021 Matteo Valentini <matteo.valentini@nethesis.it> - 1.4.19-1
- WebTop 5.12.2 - NethServer/dev#6515

* Fri May 14 2021 Matteo Valentini <matteo.valentini@nethesis.it> - 1.4.18-1
- WebTop 5.12.1 - NethServer/dev#6503

* Fri Apr 16 2021 Matteo Valentini <matteo.valentini@nethesis.it> - 1.4.17-1
- WebTop 5.11.3 - NethServer/dev#6463

* Thu Mar 11 2021 Matteo Valentini <matteo.valentini@nethesis.it> - 1.4.16-1
- WebTop 5.10.5 - NethServer/dev#6453
  - Update to upstream release wt-5.10.5

* Thu Feb 25 2021 Matteo Valentini <matteo.valentini@nethesis.it> - 1.4.15-1
- WebTop 5.10.4 - NethServer/dev#6440

* Mon Feb 22 2021 Matteo Valentini <matteo.valentini@nethesis.it> - 1.4.14-1
- WebTop 5.10.3 - NethServer/dev#6431

* Thu Feb 11 2021 Matteo Valentini <matteo.valentini@nethesis.it> - 1.4.13-1
- WebTop 5.10.2 - NethServer/dev#6418

* Fri Jan 29 2021 Matteo Valentini <matteo.valentini@nethesis.it> - 1.4.12-1
- Webtop 5.10.1 - NethServer/dev#6402
  - Update to upstream release wt-5.10.1

* Thu Jan 14 2021 Matteo Valentini <matteo.valentini@nethesis.it> - 1.4.11-1
- Webtop 5.10.0 - NethServer/dev#6368
  - Update to upstream release wt-5.10.0

* Mon Dec 07 2020 Matteo Valentini <matteo.valentini@nethesis.it> - 1.4.10-1
- Webtop 5.9.5 - NethServer/dev#6338

* Fri Oct 09 2020 Matteo Valentini <matteo.valentini@nethesis.it> - 1.4.9-1
- Webtop 5.9.4 - NethServer/dev#6300

* Fri Sep 18 2020 Matteo Valentini <matteo.valentini@nethesis.it> - 1.4.8-1
- WebTop 5.9.3 - NethServer/dev#6246

* Fri May 29 2020 Matteo Valentini <matteo.valentini@nethesis.it> - 1.4.7-1
- WebTop 5.8.5 - NethServer/dev#6181

* Tue May 19 2020 Matteo Valentini <matteo.valentini@nethesis.it> - 1.4.6-1
- WebTop 5.8.4 - NethServer/dev#6159

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

