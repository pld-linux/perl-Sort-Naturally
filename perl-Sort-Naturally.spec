#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Sort
%define		pnam	Naturally
Summary:	Sort::Naturally Perl module - sort lexically, but sort numeral parts numerically
Summary(pl.UTF-8):	Moduł Perla Sort::Naturally - sortujący leksykalnie, ale liczby numerycznie
Name:		perl-Sort-Naturally
Version:	1.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Sort/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fef2e36d1b1ea23ee79ec68b5872453f
URL:		http://search.cpan.org/dist/Sort-Naturally/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sort::Naturally module exports two functions, nsort and ncmp; they are
used in implementing my idea of a "natural sorting" algorithm. Under
natural sorting, numeric substrings are compared numerically, and
other word-characters are compared lexically.

%description -l pl.UTF-8
Moduł Sort::Naturally ma wyeksportowane dwie funkcje: nsort i ncmp. Są
one implementacją algorytmu "naturalnego sortowania". W algorytmie tym
podciągi numeryczne są sortowane numerycznie, a pozostałe znaki -
leksykalnie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests: %{__make} test}

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
%{_mandir}/man3/Sort::Naturally.3pm*
