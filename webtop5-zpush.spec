Summary: WebTop z-push
Name: webtop5-zpush
Version: 0.0.1
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name}
Source0: http://www.sonicle.com/nethesis/webtop5/z-push-wt5.tgz 
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
tar xvzf %{SOURCE0} -C root/usr/share/webtop/z-push

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
