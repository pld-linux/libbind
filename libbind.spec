Summary:	libbind provides the standard resolver library
Summary(pl.UTF-8):	Standardowa biblioteka rozwiązywania nazw
Name:		libbind
Version:	6.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	ftp://ftp.isc.org/isc/libbind/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	3e4e36fa39d0275ef97f74b737f30f0b
URL:		http://www.isc.org/software/libbind
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ISC's libbind provides the standard resolver library, along with
header files and documentation, for communicating with domain name
servers, retrieving network host entries from /etc/hosts or via DNS,
converting CIDR network addresses, performing Hesiod information
lookups, retrieving network entries from /etc/networks, implementing
TSIG transaction/request security of DNS messages, performing
name-to-address and address-to-name translations, and utilizing
/etc/resolv.conf for resolver configuration.

%package devel
Summary:	Header files and develpment documentation for libbind
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja biblioteki libbind
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and libbind documentation.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libbind.

%package static
Summary:	Static libbind library
Summary(pl.UTF-8):	Statyczna biblioteka libbind
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libbind library.

%description static -l pl.UTF-8
Statyczna biblioteka libbind.

%prep
%setup -q

%build
%configure \
	--with-libtool \
	--enable-threads \
	--enable-shared \
	--enable-static \
	--includedir=%{_includedir}/%{name}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_libdir}/libbind.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libbind.so.4
%{_mandir}/man5/irs.conf.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbind.so
%{_libdir}/libbind.la
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/libbind.a
