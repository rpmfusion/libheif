Name:           libheif
Version:        1.3.2
Release:        1%{?dist}
Summary:        HEIF file format decoder and encoder

License:        LGPLv3+ and MIT
URL:            https://github.com/strukturag/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig(libde265)
BuildRequires:  pkgconfig(libjpeg)
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
%{_datadir}/mime/packages/heif.xml
%{_datadir}/thumbnailers/

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/libheif.pc
%{_libdir}/*.so


%changelog
* Thu Nov 29 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.3.2-1
- First build

