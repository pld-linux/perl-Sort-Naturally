%include	/usr/lib/rpm/macros.perl
%define		pdir	Sort
%define		pnam	Naturally
Summary:	Sort::Naturally Perl module - sort lexically, but sort numeral parts numerically
Summary(pl):	Modu³ Perla Sort::Naturally - sortuj±cy leksykalnie, ale liczby numerycznie
Name:		perl-Sort-Naturally
Version:	1.01
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2a32b8d1c1760dd828046805cba23af7
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sort::Naturally module exports two functions, nsort and ncmp; they are
used in implementing my idea of a "natural sorting" algorithm. Under
natural sorting, numeric substrings are compared numerically, and
other word-characters are compared lexically.

%description -l pl
Modu³ Sort::Naturally ma wyeksportowane dwie funkcje: nsort i ncmp. S±
one implementacj± algorytmu "naturalnego sortowania". W algorytmie tym
podci±gi numeryczne s± sortowane numerycznie, a pozosta³e znaki -
leksykalnie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc ChangeLog README
%{perl_vendorlib}/Sort/Naturally.pm
%{_mandir}/man3/*
