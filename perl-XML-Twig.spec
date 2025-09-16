#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	XML
%define		pnam	Twig
Summary:	XML::Twig - a perl module for processing huge XML documents in tree mode
Summary(pl.UTF-8):	XML::Twig - przetwarzanie dużych dokumentów XML w trybie drzewa
Name:		perl-XML-Twig
Version:	3.54
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	02f83a3e78644d9d0c3378422b6394d9
URL:		https://metacpan.org/dist/XML-Twig
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Encode >= 2.42_01
BuildRequires:	perl-IO-CaptureOutput >= 1.1102
# IO::Scalar
BuildRequires:	perl-IO-stringy >= 2.110
BuildRequires:	perl-Scalar-List-Utils >= 1.23
BuildRequires:	perl-Test >= 1.25_02
BuildRequires:	perl-Test-Pod >= 1.45
BuildRequires:	perl-Tie-IxHash >= 1.22
BuildRequires:	perl-Unicode-Map8
BuildRequires:	perl-Unicode-String
BuildRequires:	perl-XML-Filter-BufferText >= 1.01
BuildRequires:	perl-XML-Handler-YAWriter >= 0.23
BuildRequires:	perl-XML-Parser >= 2.23
BuildRequires:	perl-XML-SAX-Writer >= 0.53
BuildRequires:	perl-XML-Simple >= 2.18
BuildRequires:	perl-XML-XPathEngine >= 0.13
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
Requires:	perl-XML-Parser >= 2.23
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_perl	XML::Twig::Elt

%description
This module provides a way to process XML documents. It is build on
top of XML::Parser.

The module offers a tree interface to the document, while allowing you
to output the parts of it that have been completely processed.

%description -l pl.UTF-8
Ten moduł udostępnia sposób na przetwarzanie dokumentów XML. Jest
zbudowany w oparciu o XML::Parser.

Moduł oferuje drzewiasty interfejs do dokumentu, pozwalając
przekazywać na wyjście części, które zostały już całkowicie
przetworzone.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL -y \
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
%doc Changes
%attr(755,root,root) %{_bindir}/xml_*
%{perl_vendorlib}/XML/Twig.pm
%dir %{perl_vendorlib}/XML/Twig
%{perl_vendorlib}/XML/Twig/*.pm
%{_mandir}/man1/xml_*.1p*
%{_mandir}/man3/XML::Twig*.3pm*
