Name:           deepin-notifications
Version:        3.0.6
Release:        1%{?dist}
Summary:        System notifications for linuxdeepin desktop environment
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-notifications
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  deepin-tool-kit-devel
BuildRequires:  gtk2-devel

%description
System notifications for linuxdeepin desktop environment.

%prep
%setup -q
sed -i 's|lib|libexec|' deepin-notifications.pro \
    files/com.deepin.Notifications.service.in

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%license LICENSE
%{_libexecdir}/%{name}/%{name}
%{_datadir}/dbus-1/services/com.deepin.Notifications.service

%changelog
* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 3.0.6-1.git0033758
- Update to 3.0.6

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 3.0.4-1.git07c0163
- Update to 3.0.4

* Sun Feb 26 2017 mosquito <sensor.wen@gmail.com> - 3.0.0-1.git9c70ddf
- Update to 3.0.0

* Sat Jan 21 2017 mosquito <sensor.wen@gmail.com> - 2.3.10-1.git1c35b5e
- Update to 2.3.10

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 2.3.9-1.git0ab9bd2
- Update to 2.3.9

* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.9-1
- Updated to 2.3.9

* Thu Jan 05 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.8-4
- Fixed build dependecies

* Thu Dec 15 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.8-3
- Fixed path in dbus services

* Sun Dec 04 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.8-2
- Rebuild with newer deepin-tool-kit

* Sun Sep 25 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.8-1
- Initial package build
