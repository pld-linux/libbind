# NOTE: will be superseded by http://wiki.netbsd.org/individual-software-releases/netresolv/
Summary:	libbind provides the standard resolver library
Summary(pl.UTF-8):	Standardowa biblioteka rozwiązywania nazw
Name:		libbind
Version:	6.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://ftp.isc.org/isc/libbind/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	3e4e36fa39d0275ef97f74b737f30f0b
URL:		http://www.isc.org/software/libbind/
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

%description -l pl.UTF-8
ISC libbind to biblioteka standardowego resolvera (rozwiązywania nazw)
wraz z plikami nagłówkowymi i dokumentacją do komunikacji z serwerami
nazw, pobierania wpisów hostów sieciowych z pliku /etc/hosts lub
poprzez DNS, przekształcania adresów sieci CIDR, wyszukiwania
informacji Hesiod, pobierania wpisów sieci z /etc/networks,
implementacji bezpieczeństwa transakcji/żądań TSIG komunikatów DNS,
tłumaczenia nazw na adresy i adresów na nazwy oraz wykorzystywania
pliku /etc/resolv.conf do konfiguracji.

%package devel
Summary:	Header files for libbind library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libbind
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libbind library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libbind.

%package static
Summary:	Static libbind library
Summary(pl.UTF-8):	Statyczna biblioteka libbind
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libbind library.

%description static -l pl.UTF-8
Statyczna biblioteka libbind.

%prep
%setup -q

%build
%configure \
	--includedir=%{_includedir}/%{name} \
	--enable-shared \
	--enable-static \
	--enable-threads \
	--with-libtool

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# preprocessed man pages
%{__rm} -r $RPM_BUILD_ROOT%{_mandir}/cat{3,5,7}
# provided by glibc-devel-doc
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man3/{getaddrinfo,gethostbyname,getipnodebyname,getnameinfo,getnetent,resolver}.3
# provided by man-pages
%{__rm} $RPM_BUILD_ROOT%{_mandir}/{man5/resolver.5,man7/hostname.7}

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
%{_mandir}/man3/hesiod.3*
%{_mandir}/man3/inet_cidr.3*
%{_mandir}/man3/tsig.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libbind.a
