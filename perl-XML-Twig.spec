#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Twig
Summary:	XML::Twig - a perl module for processing huge XML documents in tree mode
Summary(pl):	XML::Trig - przetwarzanie du�ych dokument�w XML w trybie drzewa
Name:		perl-XML-Twig
Version:	3.17
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	70be541c68247b1394138eb2e1dc109a
URL:		http://www.xmltwig.com/
BuildRequires:	perl-devel >= 1:5.8.0
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
Ten modu� udost�pnia spos�b na przetwarzanie dokument�w XML. Jest
zbudowany w oparciu o XML::Parser.

Modu� oferuje drzewiasty interfejs do dokumentu, pozwalaj�c przekazywa�
na wyj�cie cz�ci, kt�re zosta�y ju� ca�kowicie przetworzone.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL </dev/null\
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
%attr(755,root,root) %{_bindir}/xml_*
%{perl_vendorlib}/%{pdir}/*.pm
%dir %{perl_vendorlib}/%{pdir}/%{pnam}
%{perl_vendorlib}/%{pdir}/%{pnam}/*.pm
%{_mandir}/man3/*
%{_mandir}/man1/*
