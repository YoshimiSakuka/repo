Name:           deepin-voice-recorder
Version:        1.3.1
Release:        1%{?dist}
Summary:        Deepin Voice Recorder
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-voice-recorder
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  deepin-tool-kit-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  ffmpeg-devel

%description
Deepin Voice Recorder

%prep
%setup -q
sed -i 's|=lupdate|=lupdate-qt5|;s|=lrelease|=lrelease-qt5|' deepin-voice-recorder.pro

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null ||:
/usr/bin/update-desktop-database -q ||:

%postun
if [ $1 -eq 0 ]; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null ||:
    /usr/bin/gtk-update-icon-cache -f -t -q %{_datadir}/icons/hicolor ||:
fi
/usr/bin/update-desktop-database -q ||:

%posttrans
/usr/bin/gtk-update-icon-cache -f -t -q %{_datadir}/icons/hicolor ||:

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/dman/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.svg

%changelog
* Thu Jul 20 2017 mosquito <sensor.wen@gmail.com> - 1.3.1-1.git6cf1cb9
- Update to 1.3.1

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 1.3-1.git6c05bf1
- Update to 1.3

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 1.2-1.git2a95a46
- Initial build
