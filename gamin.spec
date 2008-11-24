%define lib_major 0
%define lib_name %mklibname %{name}- 1 %{lib_major}  
%define libfam %mklibname fam 0

Summary: Library providing the FAM File Alteration Monitor API
Name: gamin
Version: 0.1.10
Release: %mkrel 1
License: LGPL
Group: Monitoring
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/gamin-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root
URL: http://www.gnome.org/~veillard/gamin/
Obsoletes: fam
Provides: fam
BuildRequires: glib2-devel
BuildRequires: python-devel

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
Requires: %{name} >= %{version}
Obsoletes: %{libfam}
Provides: %{libfam}

%description -n %{lib_name}
This C library provides an API and ABI compatible file alteration
monitor mechanism compatible with FAM but not dependent on a system wide
daemon.



%package -n %{lib_name}-devel
Summary: Libraries, includes, etc. to embed the Gamin library
Group: Development/C
Requires: %{name} = %{version}
Requires: %{lib_name} = %{version}
Provides: lib%{name}-1-devel = %{version}
Provides: lib%{name}-devel = %{version}
Provides: %{name}-devel = %{version}
Obsoletes: %{libfam}-devel
Provides: %{libfam}-devel
Provides: libfam-devel
Provides: fam-devel

%description -n %{lib_name}-devel
This C library provides an API and ABI compatible file alteration
monitor mechanism compatible with FAM but not dependent on a system wide
daemon.

%prep
%setup -q

%build
%configure2_5x --enable-inotify

%make

%install
rm -fr %{buildroot}

%makeinstall_std
rm -f %buildroot%_libdir/python%pyver/site-packages/_gamin.a

%clean
rm -fr %{buildroot}

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog README Copyright TODO
%{_libdir}/gam_server

%files -n %{lib_name}
%defattr(-, root, root)
%{_libdir}/lib*.so.*

%files -n %{lib_name}-devel
%defattr(-, root, root)
%doc AUTHORS ChangeLog README Copyright TODO
%{_libdir}/lib*.so
%{_libdir}/*a
%{_includedir}/fam.h
%{_libdir}/pkgconfig/gamin.pc

%files -n python-%{name}
%defattr(-, root, root)
%doc python/tests/*.py
%doc doc/python.html
%py_platsitedir/*gamin*


