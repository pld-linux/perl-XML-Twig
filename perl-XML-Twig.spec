#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Twig
Summary:	XML::Twig - A perl module for processing huge XML documents in tree mode
Summary(pl):	XML::Trig - przetwarzanie du¿ych dokumentów XML w trybie drzewa
Name:		perl-XML-Twig
Version:	3.14
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	325bddd9f122e6aa09be238c9b08e917
URL:		http://www.xmltwig.com/
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-XML-Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a way to process XML documents. It is build on top
of XML::Parser.

The module offers a tree interface to the document, while allowing you
to output the parts of it that have been completely processed.

%description -l pl
Ten modu³ udostêpnia sposób na przetwarzanie dokumentów XML. Jest
zbudowany w oparciu o XML::Parser.

Modu³ oferuje drzewiasty interfejs do dokumentu, pozwalaj±c przekazywaæ
na wyj¶cie czê¶ci, które zosta³y ju¿ ca³kowicie przetworzone.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL </dev/null\
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xml_*
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
%{_mandir}/man1/*
