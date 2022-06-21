#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : drkonqi
Version  : 5.25.1
Release  : 67
URL      : https://download.kde.org/stable/plasma/5.25.1/drkonqi-5.25.1.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.25.1/drkonqi-5.25.1.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.25.1/drkonqi-5.25.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0
Requires: drkonqi-bin = %{version}-%{release}
Requires: drkonqi-data = %{version}-%{release}
Requires: drkonqi-lib = %{version}-%{release}
Requires: drkonqi-license = %{version}-%{release}
Requires: drkonqi-locales = %{version}-%{release}
Requires: drkonqi-services = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : ki18n-dev
BuildRequires : kidletime-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libsystemd)
BuildRequires : syntax-highlighting-dev
BuildRequires : zlib-dev

%description
<!--
SPDX-License-Identifier: CC0-1.0
-->
# DrKonqi
## Activating the debug button for DrKonqi
Add into `~/.config/drkonqirc`:
```
[DrKonqi]
ShowDebugButton=true
```

%package bin
Summary: bin components for the drkonqi package.
Group: Binaries
Requires: drkonqi-data = %{version}-%{release}
Requires: drkonqi-license = %{version}-%{release}
Requires: drkonqi-services = %{version}-%{release}

%description bin
bin components for the drkonqi package.


%package data
Summary: data components for the drkonqi package.
Group: Data

%description data
data components for the drkonqi package.


%package lib
Summary: lib components for the drkonqi package.
Group: Libraries
Requires: drkonqi-data = %{version}-%{release}
Requires: drkonqi-license = %{version}-%{release}

%description lib
lib components for the drkonqi package.


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


%package services
Summary: services components for the drkonqi package.
Group: Systemd services

%description services
services components for the drkonqi package.


%prep
%setup -q -n drkonqi-5.25.1
cd %{_builddir}/drkonqi-5.25.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1655833180
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1655833180
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/drkonqi
cp %{_builddir}/drkonqi-5.25.1/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/drkonqi/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
cp %{_builddir}/drkonqi-5.25.1/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/drkonqi/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
cp %{_builddir}/drkonqi-5.25.1/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/drkonqi/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/drkonqi-5.25.1/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/drkonqi/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/drkonqi-5.25.1/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/drkonqi/6091db0aead0d90182b93d3c0d09ba93d188f907
cp %{_builddir}/drkonqi-5.25.1/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/drkonqi/3c3d7573e137d48253731c975ecf90d74cfa9efe
cp %{_builddir}/drkonqi-5.25.1/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/drkonqi/757b86330df80f81143d5916b3e92b4bcb1b1890
cp %{_builddir}/drkonqi-5.25.1/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/drkonqi/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/drkonqi-5.25.1/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/drkonqi/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/drkonqi-5.25.1/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/drkonqi/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/drkonqi-5.25.1/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/drkonqi/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/drkonqi-5.25.1/logo.png.license %{buildroot}/usr/share/package-licenses/drkonqi/0185dcaed81bd3d62abe10263cfa6fe72f69a719
cp %{_builddir}/drkonqi-5.25.1/src/tests/data/linux-procfs-maps-with-deleted-exe.license %{buildroot}/usr/share/package-licenses/drkonqi/864bc0eb28c73bd997ac19ff91935ab771846615
cp %{_builddir}/drkonqi-5.25.1/src/tests/data/linux-procfs-maps-with-missing-files.license %{buildroot}/usr/share/package-licenses/drkonqi/864bc0eb28c73bd997ac19ff91935ab771846615
cp %{_builddir}/drkonqi-5.25.1/src/tests/data/linux-procfs-maps.so.license %{buildroot}/usr/share/package-licenses/drkonqi/864bc0eb28c73bd997ac19ff91935ab771846615
pushd clr-build
%make_install
popd
%find_lang drkonqi5

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/drkonqi
/usr/lib64/libexec/drkonqi-coredump-cleanup
/usr/lib64/libexec/drkonqi-coredump-launcher
/usr/lib64/libexec/drkonqi-coredump-processor

%files bin
%defattr(-,root,root,-)
/usr/bin/drkonqi-coredump-gui

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.drkonqi.coredump.gui.desktop
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
/usr/share/drkonqi/gdb/preamble.py
/usr/share/drkonqi/mappings
/usr/share/qlogging-categories5/drkonqi.categories

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/drkonqi/KDECoredumpNotifierTruck.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/drkonqi/0185dcaed81bd3d62abe10263cfa6fe72f69a719
/usr/share/package-licenses/drkonqi/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/drkonqi/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/drkonqi/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/drkonqi/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
/usr/share/package-licenses/drkonqi/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/drkonqi/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/drkonqi/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/drkonqi/864bc0eb28c73bd997ac19ff91935ab771846615
/usr/share/package-licenses/drkonqi/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/drkonqi/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/drkonqi-coredump-processor@.service
/usr/lib/systemd/user/drkonqi-coredump-cleanup.service
/usr/lib/systemd/user/drkonqi-coredump-cleanup.timer
/usr/lib/systemd/user/drkonqi-coredump-launcher.socket
/usr/lib/systemd/user/drkonqi-coredump-launcher@.service

%files locales -f drkonqi5.lang
%defattr(-,root,root,-)

