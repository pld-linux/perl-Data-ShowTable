%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	ShowTable
Summary:	Perl module to print arrays of data
Summary(pl):	Modu³ perla Data::ShowTable
Name:		perl-Data-ShowTable
Version:	3.3
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ShowTable.pm is a Perl module which defines subroutines to print
arrays of data in a nicely formatted listing, using one of four
possible formats: simple table, boxed table, list style, and
HTML-formatting (for World-Wide-Web output).

%description -l pl
Data::ShowTable - wy¶wietla dane z tabeli w ró¿nych formatach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/showtable
%{perl_sitelib}/Data/ShowTable.pm
%{_mandir}/man[13]/*
