Summary: WebTop z-push
Name: webtop5-zpush
Version: 1.0.0
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name}
Source0: https://github.com/sonicle-webtop/z-push-webtop/archive/master-sonicle.tar.gz
BuildArch: noarch

Requires: webtop5-core
Conflicts: webtop4-zpush

BuildRequires: unzip

%description
NethServer z-push for WebTop 5

%prep
#%setup

%build
mkdir -p root/var/log/z-push/state
mkdir -p root/usr/share/webtop/z-push/
tar xvzf %{SOURCE0} --exclude='.gitignore' -C root/usr/share/webtop/z-push --strip-components=2 z-push-webtop-master-sonicle/src
rm -rf  root/usr/share/webtop/z-push/backend/{caldav,carddav,kopano,ldap,maildir,searchldap,sqlstatemachine,vcarddir}

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})


%files
%defattr(-,root,root)
%attr(755, apache, apache) /var/log/z-push
%attr(755, apache, apache) /var/log/z-push/state
%attr(755, root, root) /usr/share/webtop/z-push/z-push-admin.php
/usr/share/webtop/z-push/*

%changelog
* Wed Mar 08 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- First WebTop5 release - NethServer/dev#5225
