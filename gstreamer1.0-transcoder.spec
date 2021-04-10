%define oname	gst-transcoder

%define api	1.0
%define major	0
%define libname	%mklibname gsttranscoder %{api} %{major}
%define devname	%mklibname gsttranscoder -d
%define girname	%mklibname gsttranscoder-gir %{api}

Name:           gstreamer%{api}-transcoder
Version:        1.16.0
Release:        2
Summary:        GStreamer Transcoding API
Group:          Video/Utilities
License:        LGPLv2+
URL:            https://github.com/pitivi/gst-transcoder
Source0:        https://github.com/pitivi/%{oname}/archive/%{version}/%{oname}-%{version}.tar.gz
BuildRequires:  locales
BuildRequires:  meson
BuildRequires:  python
BuildRequires:  gobject-introspection-devel
BuildRequires:  gstreamer1.0-devel
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
Provides:	%{oname} = %{version}-%{release}
Conflicts:	%{_lib}gsttranscoder1.0_0 < 1.12.1

%description
GStreamer Transcoding API.

%package -n %{libname}
Summary:	Shared libraries for %{oname}
Group:		System/Libraries

%description -n %{libname}
This package contains the shared libraries for %{oname}.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{oname}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	GStreamer Transcoding API development files
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{oname}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files for %{oname}.

%prep
%setup -qn %{oname}-%{version}

%build
export LC_ALL=UTF-8
%meson
%meson_build

%install
export LC_ALL=UTF-8
%meson_install

%files
%license LICENSE
%{_bindir}/%{oname}-%{api}
%{_datadir}/gstreamer-%{api}/encoding-profiles/
#plugin
%{_libdir}/gstreamer-%{api}/libgsttranscode.so

%files -n %{libname}
%{_libdir}/libgsttranscoder-%{api}.so.%{major}

%files -n %{girname}
%{_libdir}/girepository-1.0/GstTranscoder-%{api}.typelib

%files -n %{devname}
%{_includedir}/gstreamer-%{api}/gst/transcoder/
%{_libdir}/libgsttranscoder-%{api}.so
%{_libdir}/pkgconfig/%{oname}-%{api}.pc
%{_datadir}/gir-1.0/GstTranscoder-%{api}.gir
