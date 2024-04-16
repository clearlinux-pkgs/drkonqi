#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v10
# autospec commit: 5905be9
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : drkonqi
Version  : 6.0.4
Release  : 96
URL      : https://download.kde.org/stable/plasma/6.0.4/drkonqi-6.0.4.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.0.4/drkonqi-6.0.4.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.0.4/drkonqi-6.0.4.tar.xz.sig
Source2  : D7574483BB57B18D.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0
Requires: drkonqi-bin = %{version}-%{release}
Requires: drkonqi-data = %{version}-%{release}
Requires: drkonqi-lib = %{version}-%{release}
Requires: drkonqi-license = %{version}-%{release}
Requires: drkonqi-locales = %{version}-%{release}
Requires: drkonqi-services = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kidletime-dev
BuildRequires : kstatusnotifieritem-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pypi-chai
BuildRequires : pypi-psutil
BuildRequires : pypi-pygdbmi
BuildRequires : pypi-sentry_sdk
BuildRequires : python3-dev
BuildRequires : qt6base-dev
BuildRequires : syntax-highlighting-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
Requires: systemd

%description services
services components for the drkonqi package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) D7574483BB57B18D' gpg.status
%setup -q -n drkonqi-6.0.4
cd %{_builddir}/drkonqi-6.0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713295614
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DWITH_PYTHON_VENDORING=FALSE
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DWITH_PYTHON_VENDORING=FALSE
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1713295614
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/drkonqi
cp %{_builddir}/drkonqi-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/drkonqi/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e || :
cp %{_builddir}/drkonqi-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/drkonqi/3630f1ffcec0e075bf446b88c7b507b1287b571d || :
cp %{_builddir}/drkonqi-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/drkonqi/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/drkonqi-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/drkonqi/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/drkonqi-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/drkonqi/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/drkonqi-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/drkonqi/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/drkonqi-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/drkonqi/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/drkonqi-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/drkonqi/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/drkonqi-%{version}/LICENSES/LGPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/drkonqi/0b71159e19bef95069e18d17296291916e89b5cd || :
cp %{_builddir}/drkonqi-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/drkonqi/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/drkonqi-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/drkonqi/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/drkonqi-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/drkonqi/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/drkonqi-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/drkonqi/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/drkonqi-%{version}/logo.png.license %{buildroot}/usr/share/package-licenses/drkonqi/0185dcaed81bd3d62abe10263cfa6fe72f69a719 || :
cp %{_builddir}/drkonqi-%{version}/src/tests/data/linux-procfs-maps-with-deleted-exe.license %{buildroot}/usr/share/package-licenses/drkonqi/864bc0eb28c73bd997ac19ff91935ab771846615 || :
cp %{_builddir}/drkonqi-%{version}/src/tests/data/linux-procfs-maps-with-missing-files.license %{buildroot}/usr/share/package-licenses/drkonqi/864bc0eb28c73bd997ac19ff91935ab771846615 || :
cp %{_builddir}/drkonqi-%{version}/src/tests/data/linux-procfs-maps.so.license %{buildroot}/usr/share/package-licenses/drkonqi/864bc0eb28c73bd997ac19ff91935ab771846615 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang drkonqi
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/libexec/drkonqi
/V3/usr/lib64/libexec/drkonqi-coredump-cleanup
/V3/usr/lib64/libexec/drkonqi-coredump-launcher
/V3/usr/lib64/libexec/drkonqi-coredump-processor
/V3/usr/lib64/libexec/drkonqi-sentry-postman
/V3/usr/lib64/libexec/kf6/drkonqi-polkit-helper
/usr/lib64/libexec/drkonqi
/usr/lib64/libexec/drkonqi-coredump-cleanup
/usr/lib64/libexec/drkonqi-coredump-launcher
/usr/lib64/libexec/drkonqi-coredump-processor
/usr/lib64/libexec/drkonqi-sentry-postman
/usr/lib64/libexec/kf6/drkonqi-polkit-helper

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/drkonqi-coredump-gui
/V3/usr/bin/drkonqi-sentry-data
/usr/bin/drkonqi-coredump-gui
/usr/bin/drkonqi-sentry-data

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.drkonqi.coredump.gui.desktop
/usr/share/applications/org.kde.drkonqi.desktop
/usr/share/dbus-1/system-services/org.kde.drkonqi.service
/usr/share/dbus-1/system.d/org.kde.drkonqi.conf
/usr/share/drkonqi/debuggers/external.mac/lldbrc
/usr/share/drkonqi/debuggers/external/gdbrc
/usr/share/drkonqi/debuggers/external/lldbrc
/usr/share/drkonqi/debuggers/internal/gdbrc
/usr/share/drkonqi/debuggers/internal/lldbrc
/usr/share/drkonqi/gdb/python/gdb_preamble/__init__.py
/usr/share/drkonqi/gdb/python/gdb_preamble/preamble.py
/usr/share/drkonqi/mappings
/usr/share/polkit-1/actions/org.kde.drkonqi.policy
/usr/share/qlogging-categories6/drkonqi.categories

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt6/plugins/drkonqi/KDECoredumpNotifierTruck.so
/usr/lib64/qt6/plugins/drkonqi/KDECoredumpNotifierTruck.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/drkonqi/0185dcaed81bd3d62abe10263cfa6fe72f69a719
/usr/share/package-licenses/drkonqi/0b71159e19bef95069e18d17296291916e89b5cd
/usr/share/package-licenses/drkonqi/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/drkonqi/3630f1ffcec0e075bf446b88c7b507b1287b571d
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
/usr/lib/systemd/system/systemd-coredump@.service.wants/drkonqi-coredump-processor@.service
/usr/lib/systemd/user/default.target.wants/drkonqi-coredump-cleanup.service
/usr/lib/systemd/user/default.target.wants/drkonqi-sentry-postman.path
/usr/lib/systemd/user/drkonqi-coredump-cleanup.service
/usr/lib/systemd/user/drkonqi-coredump-cleanup.timer
/usr/lib/systemd/user/drkonqi-coredump-launcher.socket
/usr/lib/systemd/user/drkonqi-coredump-launcher@.service
/usr/lib/systemd/user/drkonqi-coredump-pickup.service
/usr/lib/systemd/user/drkonqi-sentry-postman.path
/usr/lib/systemd/user/drkonqi-sentry-postman.service
/usr/lib/systemd/user/drkonqi-sentry-postman.timer
/usr/lib/systemd/user/plasma-core.target.wants/drkonqi-coredump-pickup.service
/usr/lib/systemd/user/plasma-core.target.wants/drkonqi-sentry-postman.path
/usr/lib/systemd/user/plasma-core.target.wants/drkonqi-sentry-postman.timer
/usr/lib/systemd/user/sockets.target.wants/drkonqi-coredump-launcher.socket
/usr/lib/systemd/user/timers.target.wants/drkonqi-coredump-cleanup.timer
/usr/lib/systemd/user/timers.target.wants/drkonqi-sentry-postman.timer

%files locales -f drkonqi.lang
%defattr(-,root,root,-)

