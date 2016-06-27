Name: org.tizen.elm-demo-tizen-wearable
Version:    0.2
Release:    1
Summary: Tizen wearable theme demo
Source: %{name}-%{version}.tar.gz
License: Apache-2.0
Group: tizen/Application
BuildRequires:  pkgconfig(elementary)
BuildRequires:  pkgconfig(efl-extension)
BuildRequires:  pkgconfig(capi-appfw-application)
BuildRequires:  pkgconfig(capi-system-system-settings)
BuildRequires:  pkgconfig(capi-appfw-app-manager)
BuildRequires:  app-core-efl-devel
BuildRequires:  efl-extension-devel
BuildRequires:  cmake
BuildRequires:  edje-bin
BuildRequires:  gettext-tools

%description
Tizen wearable theme demo

%prep
%setup -q

%define _pkg_dir %{TZ_SYS_RO_APP}/%{name}

%build
rm -rf CMakeFiles CMakeCache.txt && cmake . -DCMAKE_INSTALL_PREFIX=%{_pkg_dir} -DPKG_MANIFEST_PATH=%{TZ_SYS_RO_PACKAGES} -DPKG_VERSION=%{version}
make %{?jobs:-j%jobs}

%post
echo -e '\033[1m\033[36m ===== Import to package DB using tpk-backend ===== \033[0m'
echo 'tpk-backend -y %{name} --preload'
tpk-backend -y %{name} --preload
echo -e '\033[1m\033[36m ===== done ===== \033[0m'

%install
%make_install

mkdir -p %{buildroot}/%{_datadir}/license
cp %{_builddir}/%{buildsubdir}/LICENSE %{buildroot}/%{_datadir}/license/%{name}

%files
%defattr(-,root,root,-)
%{_pkg_dir}/bin/*
%{_pkg_dir}/res/*
%{_pkg_dir}/shared/*
%{TZ_SYS_RO_PACKAGES}/%{name}.xml
%{_datadir}/license/%{name}
%manifest %{name}.manifest
