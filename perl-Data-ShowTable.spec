#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Data
%define		pnam	ShowTable
Summary:	Data::ShowTable - Perl module to print arrays of data
Summary(pl.UTF-8):	Data::ShowTable - moduł Perla do wypisywania tablic danych
Name:		perl-Data-ShowTable
Version:	4.6
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/A/AK/AKSTE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2e1608ad972a60b9dfe44c60f4d8464c
URL:		http://search.cpan.org/dist/Data-ShowTable/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ShowTable.pm is a Perl module which defines subroutines to print
arrays of data in a nicely formatted listing, using one of four
possible formats: simple table, boxed table, list style, and
HTML-formatting (for World-Wide-Web output).

%description -l pl.UTF-8
Data::ShowTable to moduł Perla definiujący funkcje do wypisywania
tablic danych w ładnie sformatowanej postaci przy użyciu jednego
z czterech możliwych formatów: prostej tabeli, tabeli z komórkami,
listy oraz formatowania HTML (do wyjścia WWW).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%{__sed} -i -e '1s,#!/usr/bin/env perl,#!%{__perl},' showtable

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/showtable
%{perl_vendorlib}/Data/ShowTable.pm
%{_mandir}/man[13]/*
