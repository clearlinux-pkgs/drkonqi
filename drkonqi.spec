#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : drkonqi
Version  : 5.20.3
Release  : 46
URL      : https://download.kde.org/stable/plasma/5.20.3/drkonqi-5.20.3.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.20.3/drkonqi-5.20.3.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.20.3/drkonqi-5.20.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: drkonqi-data = %{version}-%{release}
Requires: drkonqi-license = %{version}-%{release}
Requires: drkonqi-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : ki18n-dev
BuildRequires : kidletime-dev
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtx11extras-dev
BuildRequires : syntax-highlighting-dev
BuildRequires : zlib-dev

%description
How to activate the debug button for DrKonqi:
$KDEHOME/share/config/drkonqirc:
[DrKonqi]
ShowDebugButton=true

%package data
Summary: data components for the drkonqi package.
Group: Data

%description data
data components for the drkonqi package.


%package license
Summary: license components for the drkonqi package.
Group: Default

%description license
license components for the drkonqi package.


%package locales
Summary: locales components for the drkonqi package.
Group: Default

%description locales
locales components for the drkonqi package.


%prep
%setup -q -n drkonqi-5.20.3
cd %{_builddir}/drkonqi-5.20.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605050488
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1605050488
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/drkonqi
cp %{_builddir}/drkonqi-5.20.3/COPYING %{buildroot}/usr/share/package-licenses/drkonqi/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/drkonqi-5.20.3/COPYING.LIB %{buildroot}/usr/share/package-licenses/drkonqi/01a6b4bf79aca9b556822601186afab86e8c4fbf
pushd clr-build
%make_install
popd
%find_lang drkonqi5

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/drkonqi

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.drkonqi.desktop
/usr/share/drkonqi/debuggers/external.mac/lldbrc
/usr/share/drkonqi/debuggers/external/cdbrc
/usr/share/drkonqi/debuggers/external/gdbrc
/usr/share/drkonqi/debuggers/external/kdbgrc
/usr/share/drkonqi/debuggers/external/lldbrc
/usr/share/drkonqi/debuggers/internal/cdbrc
/usr/share/drkonqi/debuggers/internal/dbxrc
/usr/share/drkonqi/debuggers/internal/gdbrc
/usr/share/drkonqi/debuggers/internal/kdbgwinrc
/usr/share/drkonqi/debuggers/internal/lldbrc
/usr/share/drkonqi/mappings
/usr/share/qlogging-categories5/drkonqi.categories

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/drkonqi/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/drkonqi/06877624ea5c77efe3b7e39b0f909eda6e25a4ec

%files locales -f drkonqi5.lang
%defattr(-,root,root,-)

