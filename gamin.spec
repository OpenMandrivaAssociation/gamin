%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api 1
%define major 0
%define libname %mklibname %{name} %{api} %{major}
%define libfam %mklibname fam %{major}
%define devname %mklibname %{name} -d

Summary:	Library providing the FAM File Alteration Monitor API
Name:		gamin
Version:	0.1.10
Release:	20
License:	LGPLv2+
Group:		Monitoring
Url:		http://www.gnome.org/~veillard/gamin/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gamin/%{url_ver}/gamin-%{version}.tar.bz2
Patch0:		gamin-0.1.10_G_CONST_RETURN.patch
# See http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=542361
Patch1:		gamin-fix-deadlock.patch
Patch2:		gamin-0.1.10-no-abstract-sockets.patch
Patch3:		clang_FTBFS_Wreturn-type.patch
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(python)
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libfam} = %{version}-%{release}

%description
This C library provides an API and ABI compatible file alteration
monitor mechanism compatible with FAM but not dependent on a system wide
daemon.

%package -n python-%{name}
Summary:	Python bindings for the gamin library
Group:		Development/Python

%description -n python-%{name}
This package contains a module that allow monitoring of
files and directories from the Python language based on the support
of the gamin package.

%package -n %{libname}
Summary:	Dynamic library for Gamin
Group:		System/Libraries
Obsoletes:	%{_lib}gamin-1_0 < 0.1.10-9

%description -n %{libname}
This C library provides an API and ABI compatible file alteration
monitor mechanism compatible with FAM but not dependent on a system wide
daemon.

%package -n %{libfam}
Summary:	Dynamic library for Gamin
Group:		System/Libraries
Conflicts:	%{_lib}gamin-1_0 < 0.1.10-9

%description -n %{libfam}
This package contains a shared library for %{name}.

%package -n %{devname}
Summary:	Libraries, includes, etc. to embed the Gamin library
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	%{libfam} = %{version}
Provides:	%{name}-devel = %{version}
Provides:	fam-devel
Obsoletes:	%{_lib}gamin-1-devel < 0.1.10-9

%description -n %{devname}
This C library provides an API and ABI compatible file alteration
monitor mechanism compatible with FAM but not dependent on a system wide
daemon.

%prep
%setup -q
%apply_patches

%build
sed -i 's/AM_CONFIG_HEADER/AC_CONFIG_HEADER/g' configure.in
sed -i 's/AM_PROG_CC_STDC/AC_PROG_CC/g' configure.in
autoreconf -fi
export PYTHON=%{_bindir}/python2
%configure \
	--disable-static \
	--enable-inotify

%make

%install
%makeinstall_std
rm -f %{buildroot}%{_libdir}/python%{pyver}/site-packages/_gamin.a

%files
%doc AUTHORS ChangeLog README Copyright TODO
%{_libexecdir}/gam_server

%files -n %{libname}
%{_libdir}/libgamin-%{api}.so.%{major}*

%files -n %{libfam}
%{_libdir}/libfam.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog README Copyright TODO
%{_libdir}/lib*.so
%{_libdir}/libgamin_shared.a
%{_includedir}/fam.h
%{_libdir}/pkgconfig/gamin.pc

%files -n python-%{name}
%doc python/tests/*.py
%doc doc/python.html
%{py2_platsitedir}/*gamin*
