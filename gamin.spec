%define lib_major 0
%define lib_name %mklibname %{name}- 1 %{lib_major}  
%define develname %mklibname %{name}- 1 -d
%define libfam %mklibname fam 0

Summary: Library providing the FAM File Alteration Monitor API
Name: gamin
Version: 0.1.10
Release: 6
License: LGPLv2+
Group: Monitoring
URL: http://www.gnome.org/~veillard/gamin/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/gamin-%{version}.tar.bz2

BuildRequires: glib2-devel
BuildRequires: python-devel
Requires: %{libname} = %{version}-%{release}

%description
This C library provides an API and ABI compatible file alteration
monitor mechanism compatible with FAM but not dependent on a system wide
daemon.

%package -n python-%{name}
Summary: Python bindings for the gamin library
Group: Development/Python

%description -n python-%{name}
This package contains a module that allow monitoring of
files and directories from the Python language based on the support
of the gamin package.

%package -n %{lib_name}
Summary: Dynamic library for Gamin
Group: System/Libraries

%description -n %{lib_name}
This C library provides an API and ABI compatible file alteration
monitor mechanism compatible with FAM but not dependent on a system wide
daemon.

%package -n %{develname}
Summary: Libraries, includes, etc. to embed the Gamin library
Group: Development/C
Requires: %{lib_name} = %{version}
Provides: %{name}-devel = %{version}
Provides: fam-devel
Obsoletes: %mklibname %{name}- 1 0 -d

%description -n %{develname}
This C library provides an API and ABI compatible file alteration
monitor mechanism compatible with FAM but not dependent on a system wide
daemon.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--enable-inotify

%make

%install
rm -fr %{buildroot}
%makeinstall_std
rm -f %buildroot%_libdir/python%pyver/site-packages/_gamin.a

%files
%doc AUTHORS ChangeLog README Copyright TODO
%{_libdir}/gam_server

%files -n %{lib_name}
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%doc AUTHORS ChangeLog README Copyright TODO
%{_libdir}/lib*.so
%{_libdir}/*a
%{_includedir}/fam.h
%{_libdir}/pkgconfig/gamin.pc

%files -n python-%{name}
%doc python/tests/*.py
%doc doc/python.html
%py_platsitedir/*gamin*

