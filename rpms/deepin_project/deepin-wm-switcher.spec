Name:           deepin-wm-switcher
Version:        1.1.2
Release:        1%{?dist}
Summary:        Window manager switcher for Deepin
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-wm-switcher
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  glib2-devel
BuildRequires:  libX11-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  xcb-util-keysyms-devel
Requires:       deepin-daemon
Requires:       deepin-wm
Requires:       deepin-metacity

%description
Deepin Window Manager monitoring and auto-switching service.

It is capable of:

- monitoring health of 3d wm and falling back to 2d if bad things happened.
- detecting platform capability and choose 2d/3d wm accordingly.

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%make_build

%install
%make_install

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Sat Aug  5 2017 mosquito <sensor.wen@gmail.com> - 1.1.2-1
- Update description

* Thu Jul 20 2017 mosquito <sensor.wen@gmail.com> - 1.1.2-1.gita28aecc
- Update to 1.1.2

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 1.1.1-1.git4809e53
- Update to 1.1.1

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 1.1.0-1.git8692ad3
- Update to 1.1.0

* Sat Oct 01 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.7-1
- Initial package build
