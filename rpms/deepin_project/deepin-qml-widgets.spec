Name:           deepin-qml-widgets
Version:        2.3.5
Release:        1%{?dist}
Summary:        Deepin QML widgets
Group:          Development/Libraries
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-qml-widgets
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig
BuildRequires:  desktop-file-utils
BuildRequires:  deepin-gettext-tools
BuildRequires:  deepin-tool-kit-devel
BuildRequires:  gtk2-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libxcb-devel
Requires:       qt5-qtgraphicaleffects(?%_isa)
Requires:       qt5-qtquickcontrols(?%_isa)

%description
Extends QML by providing widgets that is used by Deepin applications.

%prep
%setup -q

%build
deepin-generate-mo locale/locale_config.ini
%qmake_qt5
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

install -d %{buildroot}%{_datadir}/locale/
cp -r locale/mo/* %{buildroot}%{_datadir}/locale/

%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/deepin-dialog
%{_qt5_qmldir}/Deepin/Locale/
%{_qt5_qmldir}/Deepin/StyleResources/
%{_qt5_qmldir}/Deepin/Widgets/
%{_datadir}/dbus-1/services/com.deepin.dialog.service

%changelog
* Sat Aug  5 2017 mosquito <sensor.wen@gmail.com> - 2.3.5-1
- Add Req qt5-qtgraphicaleffects, qt5-qtquickcontrols
- Remove BReq qt5-qtquick1

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 2.3.5-1.git3813576
- Update to 2.3.5

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 2.3.4-1.gitef84331
- Update to 2.3.4

* Wed Jul 01 2015 mosquito <sensor.wen@gmail.com> - 2.3.0-1.gita864d6f
- Update version to 2.3.0-1.gita864d6f

* Wed Dec 31 2014 mosquito <sensor.wen@gmail.com> - 0.0.2git20141231-1
- Update version to 0.0.2git20141231

* Tue Dec 23 2014 mosquito <sensor.wen@gmail.com> - 0.0.2git20141216-1
- Update version to 0.0.2git20141216

* Mon Dec 15 2014 mosquito <sensor.wen@gmail.com> - 0.0.2git20141214-1
- Update version to 0.0.2git20141214

* Mon Dec 08 2014 mosquito <sensor.wen@gmail.com> - 0.0.2git20141205-1
- Update version to 0.0.2git20141205

* Thu Dec 04 2014 mosquito <sensor.wen@gmail.com> - 0.0.2git20141204-1
- Update version to 0.0.2git20141204

* Wed Dec 03 2014 mosquito <sensor.wen@gmail.com> - 0.0.2git20141202-1
- Update version to 0.0.2git20141202

* Tue Dec 02 2014 mosquito <sensor.wen@gmail.com> - 0.0.2git20141201-1
- Update version to 0.0.2git20141201

* Tue Nov 18 2014 mosquito <sensor.wen@gmail.com> - 0.0.2git20141117-1
- Update version to 0.0.2git20141117

* Wed Nov 12 2014 mosquito <sensor.wen@gmail.com> - 0.0.2git20141112-1
- Update version to 0.0.2git20141112

* Tue Nov 4 2014 mosquito <sensor.wen@gmail.com> - 0.0.2git20141104-1
- Update version to 0.0.2git20141104

* Mon Sep 29 2014 mosquito <sensor.wen@gmail.com> - 0.0.2git20140925-1
- Initial build
