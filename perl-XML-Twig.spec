#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Twig
Summary:	XML::Twig - A perl module for processing huge XML documents in tree mode
Summary(pl):	XML::Trig - przetwarzanie du¿ych dokumentów XML w trybie drzewa
Name:		perl-XML-Twig
Version:	3.09
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
URL:		http://www.xmltwig.com/
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{?_with_tests:1}%{!?_with_tests:0}
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
%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
