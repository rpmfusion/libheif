Name:           libheif
Version:        1.4.0
Release:        2%{?dist}
Summary:        HEIF file format decoder and encoder

License:        LGPLv3+ and MIT
URL:            https://github.com/strukturag/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(libde265)
%if 0%{?fedora}
BuildRequires:  pkgconfig(libjpeg)
%else
BuildRequires:  libjpeg-devel
%endif
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(x265)

Requires:  shared-mime-info

%description
HEIF is a image format using HEVC image coding for the best compression ratios.
libheif uses libde265 for the actual image decoding and x265 for encoding.
Alternative codecs for, e.g., AVC and JPEG can be provided as plugins.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup
NOCONFIGURE=1 ./autogen.sh


%build
%configure
%make_build


%install
%make_install
find %buildroot -name '*.la' -or -name '*.a' | xargs rm -f


%ldconfig_scriptlets


%files
%license COPYING
%doc README.md
%{_bindir}/heif-convert
%{_bindir}/heif-enc
%{_bindir}/heif-info
%{_bindir}/heif-thumbnailer
%{_libdir}/*.so.1*
%{_libdir}/gdk-pixbuf-2.0/*/loaders/libpixbufloader-heif.*
%{_datadir}/mime/packages/heif.xml
%{_datadir}/thumbnailers/

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/libheif.pc
%{_libdir}/*.so


%changelog
* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Feb 28 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.4.0-1
- Update to 1.4.0

* Thu Jan 03 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.3.2-2
- Rebuild for new x265 for el7

* Thu Nov 29 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.3.2-1
- First build

