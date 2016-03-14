Name: org.tizen.elm-demo-tizen-wearable
Version:    0.1
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

%define prefix "/usr/apps/org.tizen.elm-demo-tizen-wearable"

%build
rm -rf CMakeFiles CMakeCache.txt && cmake . -DCMAKE_INSTALL_PREFIX=%{prefix}
make %{?jobs:-j%jobs}

%install
%make_install

mkdir -p %{buildroot}/%{_datadir}/packages/
cp %{_builddir}/%{buildsubdir}/org.tizen.elm-demo-tizen-wearable.xml %{buildroot}/%{_datadir}/packages/org.tizen.elm-demo-tizen-wearable.xml

mkdir -p %{buildroot}/%{_datadir}/license
cp %{_builddir}/%{buildsubdir}/LICENSE %{buildroot}/%{_datadir}/license/%{name}

%files
%defattr(-,root,root,-)
/usr/apps/org.tizen.elm-demo-tizen-wearable/bin/*
/usr/apps/org.tizen.elm-demo-tizen-wearable/res/*
%{_datadir}/packages/org.tizen.elm-demo-tizen-wearable.xml
%{_datadir}/icons/default/small/org.tizen.elm-demo-tizen-wearable.png
%{_datadir}/license/%{name}
%manifest %{name}.manifest
