#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : simple-scan
Version  : 3.32.1
Release  : 14
URL      : https://download.gnome.org/sources/simple-scan/3.32/simple-scan-3.32.1.tar.xz
Source0  : https://download.gnome.org/sources/simple-scan/3.32/simple-scan-3.32.1.tar.xz
Summary  : Simple scanning utility
Group    : Development/Tools
License  : GPL-3.0
Requires: simple-scan-bin = %{version}-%{release}
Requires: simple-scan-data = %{version}-%{release}
Requires: simple-scan-license = %{version}-%{release}
Requires: simple-scan-locales = %{version}-%{release}
Requires: simple-scan-man = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : colord
BuildRequires : colord-dev
BuildRequires : itstool
BuildRequires : libwebp-dev
BuildRequires : pkgconfig(colord)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gusb)
BuildRequires : pkgconfig(libwebp)
BuildRequires : pkgconfig(libwebpmux)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(packagekit-glib2)
BuildRequires : pkgconfig(sane-backends)
BuildRequires : vala-dev

%description
[![Build Status](https://gitlab.gnome.org/GNOME/simple-scan/badges/master/build.svg)](https://gitlab.gnome.org/GNOME/simple-scan/pipelines)
[![License](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://gitlab.gnome.org/GNOME/simple-scan/blob/master/COPYING)

%package bin
Summary: bin components for the simple-scan package.
Group: Binaries
Requires: simple-scan-data = %{version}-%{release}
Requires: simple-scan-license = %{version}-%{release}

%description bin
bin components for the simple-scan package.


%package data
Summary: data components for the simple-scan package.
Group: Data

%description data
data components for the simple-scan package.


%package doc
Summary: doc components for the simple-scan package.
Group: Documentation
Requires: simple-scan-man = %{version}-%{release}

%description doc
doc components for the simple-scan package.


%package license
Summary: license components for the simple-scan package.
Group: Default

%description license
license components for the simple-scan package.


%package locales
Summary: locales components for the simple-scan package.
Group: Default

%description locales
locales components for the simple-scan package.


%package man
Summary: man components for the simple-scan package.
Group: Default

%description man
man components for the simple-scan package.


%prep
%setup -q -n simple-scan-3.32.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554792828
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/simple-scan
cp COPYING %{buildroot}/usr/share/package-licenses/simple-scan/COPYING
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang simple-scan

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/simple-scan

%files data
%defattr(-,root,root,-)
/usr/share/applications/simple-scan.desktop
/usr/share/glib-2.0/schemas/org.gnome.SimpleScan.gschema.xml
/usr/share/metainfo/simple-scan.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/simple-scan/adf.page
/usr/share/help/C/simple-scan/brightness-contrast.page
/usr/share/help/C/simple-scan/crop.page
/usr/share/help/C/simple-scan/dpi.page
/usr/share/help/C/simple-scan/email.page
/usr/share/help/C/simple-scan/figures/icon.png
/usr/share/help/C/simple-scan/figures/preferences.png
/usr/share/help/C/simple-scan/figures/scan_toolbar.png
/usr/share/help/C/simple-scan/index.page
/usr/share/help/C/simple-scan/legal.xml
/usr/share/help/C/simple-scan/print.page
/usr/share/help/C/simple-scan/quality.page
/usr/share/help/C/simple-scan/reorder.page
/usr/share/help/C/simple-scan/rotate.page
/usr/share/help/C/simple-scan/save.page
/usr/share/help/C/simple-scan/scanner.page
/usr/share/help/C/simple-scan/scanning.page
/usr/share/help/ar/simple-scan/adf.page
/usr/share/help/ar/simple-scan/brightness-contrast.page
/usr/share/help/ar/simple-scan/crop.page
/usr/share/help/ar/simple-scan/dpi.page
/usr/share/help/ar/simple-scan/email.page
/usr/share/help/ar/simple-scan/figures/icon.png
/usr/share/help/ar/simple-scan/figures/preferences.png
/usr/share/help/ar/simple-scan/figures/scan_toolbar.png
/usr/share/help/ar/simple-scan/index.page
/usr/share/help/ar/simple-scan/legal.xml
/usr/share/help/ar/simple-scan/print.page
/usr/share/help/ar/simple-scan/quality.page
/usr/share/help/ar/simple-scan/reorder.page
/usr/share/help/ar/simple-scan/rotate.page
/usr/share/help/ar/simple-scan/save.page
/usr/share/help/ar/simple-scan/scanner.page
/usr/share/help/ar/simple-scan/scanning.page
/usr/share/help/bg/simple-scan/adf.page
/usr/share/help/bg/simple-scan/brightness-contrast.page
/usr/share/help/bg/simple-scan/crop.page
/usr/share/help/bg/simple-scan/dpi.page
/usr/share/help/bg/simple-scan/email.page
/usr/share/help/bg/simple-scan/figures/icon.png
/usr/share/help/bg/simple-scan/figures/preferences.png
/usr/share/help/bg/simple-scan/figures/scan_toolbar.png
/usr/share/help/bg/simple-scan/index.page
/usr/share/help/bg/simple-scan/legal.xml
/usr/share/help/bg/simple-scan/print.page
/usr/share/help/bg/simple-scan/quality.page
/usr/share/help/bg/simple-scan/reorder.page
/usr/share/help/bg/simple-scan/rotate.page
/usr/share/help/bg/simple-scan/save.page
/usr/share/help/bg/simple-scan/scanner.page
/usr/share/help/bg/simple-scan/scanning.page
/usr/share/help/ca/simple-scan/adf.page
/usr/share/help/ca/simple-scan/brightness-contrast.page
/usr/share/help/ca/simple-scan/crop.page
/usr/share/help/ca/simple-scan/dpi.page
/usr/share/help/ca/simple-scan/email.page
/usr/share/help/ca/simple-scan/figures/icon.png
/usr/share/help/ca/simple-scan/figures/preferences.png
/usr/share/help/ca/simple-scan/figures/scan_toolbar.png
/usr/share/help/ca/simple-scan/index.page
/usr/share/help/ca/simple-scan/legal.xml
/usr/share/help/ca/simple-scan/print.page
/usr/share/help/ca/simple-scan/quality.page
/usr/share/help/ca/simple-scan/reorder.page
/usr/share/help/ca/simple-scan/rotate.page
/usr/share/help/ca/simple-scan/save.page
/usr/share/help/ca/simple-scan/scanner.page
/usr/share/help/ca/simple-scan/scanning.page
/usr/share/help/cs/simple-scan/adf.page
/usr/share/help/cs/simple-scan/brightness-contrast.page
/usr/share/help/cs/simple-scan/crop.page
/usr/share/help/cs/simple-scan/dpi.page
/usr/share/help/cs/simple-scan/email.page
/usr/share/help/cs/simple-scan/figures/icon.png
/usr/share/help/cs/simple-scan/figures/preferences.png
/usr/share/help/cs/simple-scan/figures/scan_toolbar.png
/usr/share/help/cs/simple-scan/index.page
/usr/share/help/cs/simple-scan/legal.xml
/usr/share/help/cs/simple-scan/print.page
/usr/share/help/cs/simple-scan/quality.page
/usr/share/help/cs/simple-scan/reorder.page
/usr/share/help/cs/simple-scan/rotate.page
/usr/share/help/cs/simple-scan/save.page
/usr/share/help/cs/simple-scan/scanner.page
/usr/share/help/cs/simple-scan/scanning.page
/usr/share/help/da/simple-scan/adf.page
/usr/share/help/da/simple-scan/brightness-contrast.page
/usr/share/help/da/simple-scan/crop.page
/usr/share/help/da/simple-scan/dpi.page
/usr/share/help/da/simple-scan/email.page
/usr/share/help/da/simple-scan/figures/icon.png
/usr/share/help/da/simple-scan/figures/preferences.png
/usr/share/help/da/simple-scan/figures/scan_toolbar.png
/usr/share/help/da/simple-scan/index.page
/usr/share/help/da/simple-scan/legal.xml
/usr/share/help/da/simple-scan/print.page
/usr/share/help/da/simple-scan/quality.page
/usr/share/help/da/simple-scan/reorder.page
/usr/share/help/da/simple-scan/rotate.page
/usr/share/help/da/simple-scan/save.page
/usr/share/help/da/simple-scan/scanner.page
/usr/share/help/da/simple-scan/scanning.page
/usr/share/help/de/simple-scan/adf.page
/usr/share/help/de/simple-scan/brightness-contrast.page
/usr/share/help/de/simple-scan/crop.page
/usr/share/help/de/simple-scan/dpi.page
/usr/share/help/de/simple-scan/email.page
/usr/share/help/de/simple-scan/figures/icon.png
/usr/share/help/de/simple-scan/figures/preferences.png
/usr/share/help/de/simple-scan/figures/scan_toolbar.png
/usr/share/help/de/simple-scan/index.page
/usr/share/help/de/simple-scan/legal.xml
/usr/share/help/de/simple-scan/print.page
/usr/share/help/de/simple-scan/quality.page
/usr/share/help/de/simple-scan/reorder.page
/usr/share/help/de/simple-scan/rotate.page
/usr/share/help/de/simple-scan/save.page
/usr/share/help/de/simple-scan/scanner.page
/usr/share/help/de/simple-scan/scanning.page
/usr/share/help/en_GB/simple-scan/adf.page
/usr/share/help/en_GB/simple-scan/brightness-contrast.page
/usr/share/help/en_GB/simple-scan/crop.page
/usr/share/help/en_GB/simple-scan/dpi.page
/usr/share/help/en_GB/simple-scan/email.page
/usr/share/help/en_GB/simple-scan/figures/icon.png
/usr/share/help/en_GB/simple-scan/figures/preferences.png
/usr/share/help/en_GB/simple-scan/figures/scan_toolbar.png
/usr/share/help/en_GB/simple-scan/index.page
/usr/share/help/en_GB/simple-scan/legal.xml
/usr/share/help/en_GB/simple-scan/print.page
/usr/share/help/en_GB/simple-scan/quality.page
/usr/share/help/en_GB/simple-scan/reorder.page
/usr/share/help/en_GB/simple-scan/rotate.page
/usr/share/help/en_GB/simple-scan/save.page
/usr/share/help/en_GB/simple-scan/scanner.page
/usr/share/help/en_GB/simple-scan/scanning.page
/usr/share/help/es/simple-scan/adf.page
/usr/share/help/es/simple-scan/brightness-contrast.page
/usr/share/help/es/simple-scan/crop.page
/usr/share/help/es/simple-scan/dpi.page
/usr/share/help/es/simple-scan/email.page
/usr/share/help/es/simple-scan/figures/icon.png
/usr/share/help/es/simple-scan/figures/preferences.png
/usr/share/help/es/simple-scan/figures/scan_toolbar.png
/usr/share/help/es/simple-scan/index.page
/usr/share/help/es/simple-scan/legal.xml
/usr/share/help/es/simple-scan/print.page
/usr/share/help/es/simple-scan/quality.page
/usr/share/help/es/simple-scan/reorder.page
/usr/share/help/es/simple-scan/rotate.page
/usr/share/help/es/simple-scan/save.page
/usr/share/help/es/simple-scan/scanner.page
/usr/share/help/es/simple-scan/scanning.page
/usr/share/help/eu/simple-scan/adf.page
/usr/share/help/eu/simple-scan/brightness-contrast.page
/usr/share/help/eu/simple-scan/crop.page
/usr/share/help/eu/simple-scan/dpi.page
/usr/share/help/eu/simple-scan/email.page
/usr/share/help/eu/simple-scan/figures/icon.png
/usr/share/help/eu/simple-scan/figures/preferences.png
/usr/share/help/eu/simple-scan/figures/scan_toolbar.png
/usr/share/help/eu/simple-scan/index.page
/usr/share/help/eu/simple-scan/legal.xml
/usr/share/help/eu/simple-scan/print.page
/usr/share/help/eu/simple-scan/quality.page
/usr/share/help/eu/simple-scan/reorder.page
/usr/share/help/eu/simple-scan/rotate.page
/usr/share/help/eu/simple-scan/save.page
/usr/share/help/eu/simple-scan/scanner.page
/usr/share/help/eu/simple-scan/scanning.page
/usr/share/help/fi/simple-scan/adf.page
/usr/share/help/fi/simple-scan/brightness-contrast.page
/usr/share/help/fi/simple-scan/crop.page
/usr/share/help/fi/simple-scan/dpi.page
/usr/share/help/fi/simple-scan/email.page
/usr/share/help/fi/simple-scan/figures/icon.png
/usr/share/help/fi/simple-scan/figures/preferences.png
/usr/share/help/fi/simple-scan/figures/scan_toolbar.png
/usr/share/help/fi/simple-scan/index.page
/usr/share/help/fi/simple-scan/legal.xml
/usr/share/help/fi/simple-scan/print.page
/usr/share/help/fi/simple-scan/quality.page
/usr/share/help/fi/simple-scan/reorder.page
/usr/share/help/fi/simple-scan/rotate.page
/usr/share/help/fi/simple-scan/save.page
/usr/share/help/fi/simple-scan/scanner.page
/usr/share/help/fi/simple-scan/scanning.page
/usr/share/help/fr/simple-scan/adf.page
/usr/share/help/fr/simple-scan/brightness-contrast.page
/usr/share/help/fr/simple-scan/crop.page
/usr/share/help/fr/simple-scan/dpi.page
/usr/share/help/fr/simple-scan/email.page
/usr/share/help/fr/simple-scan/figures/icon.png
/usr/share/help/fr/simple-scan/figures/preferences.png
/usr/share/help/fr/simple-scan/figures/scan_toolbar.png
/usr/share/help/fr/simple-scan/index.page
/usr/share/help/fr/simple-scan/legal.xml
/usr/share/help/fr/simple-scan/print.page
/usr/share/help/fr/simple-scan/quality.page
/usr/share/help/fr/simple-scan/reorder.page
/usr/share/help/fr/simple-scan/rotate.page
/usr/share/help/fr/simple-scan/save.page
/usr/share/help/fr/simple-scan/scanner.page
/usr/share/help/fr/simple-scan/scanning.page
/usr/share/help/gl/simple-scan/adf.page
/usr/share/help/gl/simple-scan/brightness-contrast.page
/usr/share/help/gl/simple-scan/crop.page
/usr/share/help/gl/simple-scan/dpi.page
/usr/share/help/gl/simple-scan/email.page
/usr/share/help/gl/simple-scan/figures/icon.png
/usr/share/help/gl/simple-scan/figures/preferences.png
/usr/share/help/gl/simple-scan/figures/scan_toolbar.png
/usr/share/help/gl/simple-scan/index.page
/usr/share/help/gl/simple-scan/legal.xml
/usr/share/help/gl/simple-scan/print.page
/usr/share/help/gl/simple-scan/quality.page
/usr/share/help/gl/simple-scan/reorder.page
/usr/share/help/gl/simple-scan/rotate.page
/usr/share/help/gl/simple-scan/save.page
/usr/share/help/gl/simple-scan/scanner.page
/usr/share/help/gl/simple-scan/scanning.page
/usr/share/help/hr/simple-scan/adf.page
/usr/share/help/hr/simple-scan/brightness-contrast.page
/usr/share/help/hr/simple-scan/crop.page
/usr/share/help/hr/simple-scan/dpi.page
/usr/share/help/hr/simple-scan/email.page
/usr/share/help/hr/simple-scan/figures/icon.png
/usr/share/help/hr/simple-scan/figures/preferences.png
/usr/share/help/hr/simple-scan/figures/scan_toolbar.png
/usr/share/help/hr/simple-scan/index.page
/usr/share/help/hr/simple-scan/legal.xml
/usr/share/help/hr/simple-scan/print.page
/usr/share/help/hr/simple-scan/quality.page
/usr/share/help/hr/simple-scan/reorder.page
/usr/share/help/hr/simple-scan/rotate.page
/usr/share/help/hr/simple-scan/save.page
/usr/share/help/hr/simple-scan/scanner.page
/usr/share/help/hr/simple-scan/scanning.page
/usr/share/help/hu/simple-scan/adf.page
/usr/share/help/hu/simple-scan/brightness-contrast.page
/usr/share/help/hu/simple-scan/crop.page
/usr/share/help/hu/simple-scan/dpi.page
/usr/share/help/hu/simple-scan/email.page
/usr/share/help/hu/simple-scan/figures/icon.png
/usr/share/help/hu/simple-scan/figures/preferences.png
/usr/share/help/hu/simple-scan/figures/scan_toolbar.png
/usr/share/help/hu/simple-scan/index.page
/usr/share/help/hu/simple-scan/legal.xml
/usr/share/help/hu/simple-scan/print.page
/usr/share/help/hu/simple-scan/quality.page
/usr/share/help/hu/simple-scan/reorder.page
/usr/share/help/hu/simple-scan/rotate.page
/usr/share/help/hu/simple-scan/save.page
/usr/share/help/hu/simple-scan/scanner.page
/usr/share/help/hu/simple-scan/scanning.page
/usr/share/help/ia/simple-scan/adf.page
/usr/share/help/ia/simple-scan/brightness-contrast.page
/usr/share/help/ia/simple-scan/crop.page
/usr/share/help/ia/simple-scan/dpi.page
/usr/share/help/ia/simple-scan/email.page
/usr/share/help/ia/simple-scan/figures/icon.png
/usr/share/help/ia/simple-scan/figures/preferences.png
/usr/share/help/ia/simple-scan/figures/scan_toolbar.png
/usr/share/help/ia/simple-scan/index.page
/usr/share/help/ia/simple-scan/legal.xml
/usr/share/help/ia/simple-scan/print.page
/usr/share/help/ia/simple-scan/quality.page
/usr/share/help/ia/simple-scan/reorder.page
/usr/share/help/ia/simple-scan/rotate.page
/usr/share/help/ia/simple-scan/save.page
/usr/share/help/ia/simple-scan/scanner.page
/usr/share/help/ia/simple-scan/scanning.page
/usr/share/help/it/simple-scan/adf.page
/usr/share/help/it/simple-scan/brightness-contrast.page
/usr/share/help/it/simple-scan/crop.page
/usr/share/help/it/simple-scan/dpi.page
/usr/share/help/it/simple-scan/email.page
/usr/share/help/it/simple-scan/figures/icon.png
/usr/share/help/it/simple-scan/figures/preferences.png
/usr/share/help/it/simple-scan/figures/scan_toolbar.png
/usr/share/help/it/simple-scan/index.page
/usr/share/help/it/simple-scan/legal.xml
/usr/share/help/it/simple-scan/print.page
/usr/share/help/it/simple-scan/quality.page
/usr/share/help/it/simple-scan/reorder.page
/usr/share/help/it/simple-scan/rotate.page
/usr/share/help/it/simple-scan/save.page
/usr/share/help/it/simple-scan/scanner.page
/usr/share/help/it/simple-scan/scanning.page
/usr/share/help/ja/simple-scan/adf.page
/usr/share/help/ja/simple-scan/brightness-contrast.page
/usr/share/help/ja/simple-scan/crop.page
/usr/share/help/ja/simple-scan/dpi.page
/usr/share/help/ja/simple-scan/email.page
/usr/share/help/ja/simple-scan/figures/icon.png
/usr/share/help/ja/simple-scan/figures/preferences.png
/usr/share/help/ja/simple-scan/figures/scan_toolbar.png
/usr/share/help/ja/simple-scan/index.page
/usr/share/help/ja/simple-scan/legal.xml
/usr/share/help/ja/simple-scan/print.page
/usr/share/help/ja/simple-scan/quality.page
/usr/share/help/ja/simple-scan/reorder.page
/usr/share/help/ja/simple-scan/rotate.page
/usr/share/help/ja/simple-scan/save.page
/usr/share/help/ja/simple-scan/scanner.page
/usr/share/help/ja/simple-scan/scanning.page
/usr/share/help/ku/simple-scan/adf.page
/usr/share/help/ku/simple-scan/brightness-contrast.page
/usr/share/help/ku/simple-scan/crop.page
/usr/share/help/ku/simple-scan/dpi.page
/usr/share/help/ku/simple-scan/email.page
/usr/share/help/ku/simple-scan/figures/icon.png
/usr/share/help/ku/simple-scan/figures/preferences.png
/usr/share/help/ku/simple-scan/figures/scan_toolbar.png
/usr/share/help/ku/simple-scan/index.page
/usr/share/help/ku/simple-scan/legal.xml
/usr/share/help/ku/simple-scan/print.page
/usr/share/help/ku/simple-scan/quality.page
/usr/share/help/ku/simple-scan/reorder.page
/usr/share/help/ku/simple-scan/rotate.page
/usr/share/help/ku/simple-scan/save.page
/usr/share/help/ku/simple-scan/scanner.page
/usr/share/help/ku/simple-scan/scanning.page
/usr/share/help/nb/simple-scan/adf.page
/usr/share/help/nb/simple-scan/brightness-contrast.page
/usr/share/help/nb/simple-scan/crop.page
/usr/share/help/nb/simple-scan/dpi.page
/usr/share/help/nb/simple-scan/email.page
/usr/share/help/nb/simple-scan/figures/icon.png
/usr/share/help/nb/simple-scan/figures/preferences.png
/usr/share/help/nb/simple-scan/figures/scan_toolbar.png
/usr/share/help/nb/simple-scan/index.page
/usr/share/help/nb/simple-scan/legal.xml
/usr/share/help/nb/simple-scan/print.page
/usr/share/help/nb/simple-scan/quality.page
/usr/share/help/nb/simple-scan/reorder.page
/usr/share/help/nb/simple-scan/rotate.page
/usr/share/help/nb/simple-scan/save.page
/usr/share/help/nb/simple-scan/scanner.page
/usr/share/help/nb/simple-scan/scanning.page
/usr/share/help/nl/simple-scan/adf.page
/usr/share/help/nl/simple-scan/brightness-contrast.page
/usr/share/help/nl/simple-scan/crop.page
/usr/share/help/nl/simple-scan/dpi.page
/usr/share/help/nl/simple-scan/email.page
/usr/share/help/nl/simple-scan/figures/icon.png
/usr/share/help/nl/simple-scan/figures/preferences.png
/usr/share/help/nl/simple-scan/figures/scan_toolbar.png
/usr/share/help/nl/simple-scan/index.page
/usr/share/help/nl/simple-scan/legal.xml
/usr/share/help/nl/simple-scan/print.page
/usr/share/help/nl/simple-scan/quality.page
/usr/share/help/nl/simple-scan/reorder.page
/usr/share/help/nl/simple-scan/rotate.page
/usr/share/help/nl/simple-scan/save.page
/usr/share/help/nl/simple-scan/scanner.page
/usr/share/help/nl/simple-scan/scanning.page
/usr/share/help/pl/simple-scan/adf.page
/usr/share/help/pl/simple-scan/brightness-contrast.page
/usr/share/help/pl/simple-scan/crop.page
/usr/share/help/pl/simple-scan/dpi.page
/usr/share/help/pl/simple-scan/email.page
/usr/share/help/pl/simple-scan/figures/icon.png
/usr/share/help/pl/simple-scan/figures/preferences.png
/usr/share/help/pl/simple-scan/figures/scan_toolbar.png
/usr/share/help/pl/simple-scan/index.page
/usr/share/help/pl/simple-scan/legal.xml
/usr/share/help/pl/simple-scan/print.page
/usr/share/help/pl/simple-scan/quality.page
/usr/share/help/pl/simple-scan/reorder.page
/usr/share/help/pl/simple-scan/rotate.page
/usr/share/help/pl/simple-scan/save.page
/usr/share/help/pl/simple-scan/scanner.page
/usr/share/help/pl/simple-scan/scanning.page
/usr/share/help/pt_BR/simple-scan/adf.page
/usr/share/help/pt_BR/simple-scan/brightness-contrast.page
/usr/share/help/pt_BR/simple-scan/crop.page
/usr/share/help/pt_BR/simple-scan/dpi.page
/usr/share/help/pt_BR/simple-scan/email.page
/usr/share/help/pt_BR/simple-scan/figures/icon.png
/usr/share/help/pt_BR/simple-scan/figures/preferences.png
/usr/share/help/pt_BR/simple-scan/figures/scan_toolbar.png
/usr/share/help/pt_BR/simple-scan/index.page
/usr/share/help/pt_BR/simple-scan/legal.xml
/usr/share/help/pt_BR/simple-scan/print.page
/usr/share/help/pt_BR/simple-scan/quality.page
/usr/share/help/pt_BR/simple-scan/reorder.page
/usr/share/help/pt_BR/simple-scan/rotate.page
/usr/share/help/pt_BR/simple-scan/save.page
/usr/share/help/pt_BR/simple-scan/scanner.page
/usr/share/help/pt_BR/simple-scan/scanning.page
/usr/share/help/ro/simple-scan/adf.page
/usr/share/help/ro/simple-scan/brightness-contrast.page
/usr/share/help/ro/simple-scan/crop.page
/usr/share/help/ro/simple-scan/dpi.page
/usr/share/help/ro/simple-scan/email.page
/usr/share/help/ro/simple-scan/figures/icon.png
/usr/share/help/ro/simple-scan/figures/preferences.png
/usr/share/help/ro/simple-scan/figures/scan_toolbar.png
/usr/share/help/ro/simple-scan/index.page
/usr/share/help/ro/simple-scan/legal.xml
/usr/share/help/ro/simple-scan/print.page
/usr/share/help/ro/simple-scan/quality.page
/usr/share/help/ro/simple-scan/reorder.page
/usr/share/help/ro/simple-scan/rotate.page
/usr/share/help/ro/simple-scan/save.page
/usr/share/help/ro/simple-scan/scanner.page
/usr/share/help/ro/simple-scan/scanning.page
/usr/share/help/ru/simple-scan/adf.page
/usr/share/help/ru/simple-scan/brightness-contrast.page
/usr/share/help/ru/simple-scan/crop.page
/usr/share/help/ru/simple-scan/dpi.page
/usr/share/help/ru/simple-scan/email.page
/usr/share/help/ru/simple-scan/figures/icon.png
/usr/share/help/ru/simple-scan/figures/preferences.png
/usr/share/help/ru/simple-scan/figures/scan_toolbar.png
/usr/share/help/ru/simple-scan/index.page
/usr/share/help/ru/simple-scan/legal.xml
/usr/share/help/ru/simple-scan/print.page
/usr/share/help/ru/simple-scan/quality.page
/usr/share/help/ru/simple-scan/reorder.page
/usr/share/help/ru/simple-scan/rotate.page
/usr/share/help/ru/simple-scan/save.page
/usr/share/help/ru/simple-scan/scanner.page
/usr/share/help/ru/simple-scan/scanning.page
/usr/share/help/sk/simple-scan/adf.page
/usr/share/help/sk/simple-scan/brightness-contrast.page
/usr/share/help/sk/simple-scan/crop.page
/usr/share/help/sk/simple-scan/dpi.page
/usr/share/help/sk/simple-scan/email.page
/usr/share/help/sk/simple-scan/figures/icon.png
/usr/share/help/sk/simple-scan/figures/preferences.png
/usr/share/help/sk/simple-scan/figures/scan_toolbar.png
/usr/share/help/sk/simple-scan/index.page
/usr/share/help/sk/simple-scan/legal.xml
/usr/share/help/sk/simple-scan/print.page
/usr/share/help/sk/simple-scan/quality.page
/usr/share/help/sk/simple-scan/reorder.page
/usr/share/help/sk/simple-scan/rotate.page
/usr/share/help/sk/simple-scan/save.page
/usr/share/help/sk/simple-scan/scanner.page
/usr/share/help/sk/simple-scan/scanning.page
/usr/share/help/sl/simple-scan/adf.page
/usr/share/help/sl/simple-scan/brightness-contrast.page
/usr/share/help/sl/simple-scan/crop.page
/usr/share/help/sl/simple-scan/dpi.page
/usr/share/help/sl/simple-scan/email.page
/usr/share/help/sl/simple-scan/figures/icon.png
/usr/share/help/sl/simple-scan/figures/preferences.png
/usr/share/help/sl/simple-scan/figures/scan_toolbar.png
/usr/share/help/sl/simple-scan/index.page
/usr/share/help/sl/simple-scan/legal.xml
/usr/share/help/sl/simple-scan/print.page
/usr/share/help/sl/simple-scan/quality.page
/usr/share/help/sl/simple-scan/reorder.page
/usr/share/help/sl/simple-scan/rotate.page
/usr/share/help/sl/simple-scan/save.page
/usr/share/help/sl/simple-scan/scanner.page
/usr/share/help/sl/simple-scan/scanning.page
/usr/share/help/sr/simple-scan/adf.page
/usr/share/help/sr/simple-scan/brightness-contrast.page
/usr/share/help/sr/simple-scan/crop.page
/usr/share/help/sr/simple-scan/dpi.page
/usr/share/help/sr/simple-scan/email.page
/usr/share/help/sr/simple-scan/figures/icon.png
/usr/share/help/sr/simple-scan/figures/preferences.png
/usr/share/help/sr/simple-scan/figures/scan_toolbar.png
/usr/share/help/sr/simple-scan/index.page
/usr/share/help/sr/simple-scan/legal.xml
/usr/share/help/sr/simple-scan/print.page
/usr/share/help/sr/simple-scan/quality.page
/usr/share/help/sr/simple-scan/reorder.page
/usr/share/help/sr/simple-scan/rotate.page
/usr/share/help/sr/simple-scan/save.page
/usr/share/help/sr/simple-scan/scanner.page
/usr/share/help/sr/simple-scan/scanning.page
/usr/share/help/sv/simple-scan/adf.page
/usr/share/help/sv/simple-scan/brightness-contrast.page
/usr/share/help/sv/simple-scan/crop.page
/usr/share/help/sv/simple-scan/dpi.page
/usr/share/help/sv/simple-scan/email.page
/usr/share/help/sv/simple-scan/figures/icon.png
/usr/share/help/sv/simple-scan/figures/preferences.png
/usr/share/help/sv/simple-scan/figures/scan_toolbar.png
/usr/share/help/sv/simple-scan/index.page
/usr/share/help/sv/simple-scan/legal.xml
/usr/share/help/sv/simple-scan/print.page
/usr/share/help/sv/simple-scan/quality.page
/usr/share/help/sv/simple-scan/reorder.page
/usr/share/help/sv/simple-scan/rotate.page
/usr/share/help/sv/simple-scan/save.page
/usr/share/help/sv/simple-scan/scanner.page
/usr/share/help/sv/simple-scan/scanning.page
/usr/share/help/uk/simple-scan/adf.page
/usr/share/help/uk/simple-scan/brightness-contrast.page
/usr/share/help/uk/simple-scan/crop.page
/usr/share/help/uk/simple-scan/dpi.page
/usr/share/help/uk/simple-scan/email.page
/usr/share/help/uk/simple-scan/figures/icon.png
/usr/share/help/uk/simple-scan/figures/preferences.png
/usr/share/help/uk/simple-scan/figures/scan_toolbar.png
/usr/share/help/uk/simple-scan/index.page
/usr/share/help/uk/simple-scan/legal.xml
/usr/share/help/uk/simple-scan/print.page
/usr/share/help/uk/simple-scan/quality.page
/usr/share/help/uk/simple-scan/reorder.page
/usr/share/help/uk/simple-scan/rotate.page
/usr/share/help/uk/simple-scan/save.page
/usr/share/help/uk/simple-scan/scanner.page
/usr/share/help/uk/simple-scan/scanning.page
/usr/share/help/zh_TW/simple-scan/adf.page
/usr/share/help/zh_TW/simple-scan/brightness-contrast.page
/usr/share/help/zh_TW/simple-scan/crop.page
/usr/share/help/zh_TW/simple-scan/dpi.page
/usr/share/help/zh_TW/simple-scan/email.page
/usr/share/help/zh_TW/simple-scan/figures/icon.png
/usr/share/help/zh_TW/simple-scan/figures/preferences.png
/usr/share/help/zh_TW/simple-scan/figures/scan_toolbar.png
/usr/share/help/zh_TW/simple-scan/index.page
/usr/share/help/zh_TW/simple-scan/legal.xml
/usr/share/help/zh_TW/simple-scan/print.page
/usr/share/help/zh_TW/simple-scan/quality.page
/usr/share/help/zh_TW/simple-scan/reorder.page
/usr/share/help/zh_TW/simple-scan/rotate.page
/usr/share/help/zh_TW/simple-scan/save.page
/usr/share/help/zh_TW/simple-scan/scanner.page
/usr/share/help/zh_TW/simple-scan/scanning.page

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/simple-scan/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/simple-scan.1

%files locales -f simple-scan.lang
%defattr(-,root,root,-)

