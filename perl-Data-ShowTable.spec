%include	/usr/lib/rpm/macros.perl
%define		pdir	Data
%define		pnam	ShowTable
Summary:	Data::ShowTable - Perl module to print arrays of data
Summary(pl.UTF-8):   Data::ShowTable - moduł Perla do wypisywania tablic danych
Name:		perl-Data-ShowTable
Version:	3.3
Release:	11
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e8a3060790803bdf9f0fcb73bb4e71c4
Patch0:		%{name}-paths.patch
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
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

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
