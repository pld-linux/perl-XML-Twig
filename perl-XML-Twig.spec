#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Twig
Summary:	XML::Twig - A perl module for processing huge XML documents in tree mode
Summary(pl):	Modu³ Perla XML::Trig - do przetwarzania du¿ych dokumentów XML w trybie drzewa
Name:		perl-XML-Twig
Version:	3.05
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
URL:		http://www.xmltwig.com/
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-XML-Parser
%endif
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
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
