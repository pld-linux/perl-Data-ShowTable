%include	/usr/lib/rpm/macros.perl
Summary:	Data-ShowTable perl module
Summary(pl):	Modu³ perla Data-ShowTable
Name:		perl-Data-ShowTable
Version:	3.3
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Data/Data-ShowTable-%{version}.tar.gz
Patch:		perl-Data-ShowTable-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Data-ShowTable - routines to display tabular data in several formats.

%description -l pl
Data-ShowTable - wy¶wietla dane z tabeli w ró¿nych formatach.

%prep
%setup -q -n Data-ShowTable-%{version}
%patch -p1

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Data/ShowTable
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[13]/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz
%attr(755,root,root) %{_bindir}/showtable

%{perl_sitelib}/Data/ShowTable.pm
%{perl_sitearch}/auto/Data/ShowTable

%{_mandir}/man[13]/*
