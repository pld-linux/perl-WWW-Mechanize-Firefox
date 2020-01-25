#
# Conditional build:
%bcond_without	tests		# perform "make test" (require Internet connection)
#
%define	pdir	WWW
%define	pnam	Mechanize-Firefox
Summary:	WWW::Mechanize::Firefox - use Firefox as if it were WWW::Mechanize 
Summary(pl.UTF-8):	WWW::Mechanize::Firefox - wykorzystanie Firefoksa tak jak WWW::Mechanize 
Name:		perl-WWW-Mechanize-Firefox
Version:	0.78
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bc031901d6a196e29e7639a5016090e5
URL:		http://search.cpan.org/dist/WWW-Mechanize-Firefox/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(HTML::Selector::XPath)
BuildRequires:	perl(MozRepl::RemoteObject)
BuildRequires:	perl(Object::Import)
BuildRequires:	perl(Shell::Command)
BuildRequires:	perl(Task::Weaken)
BuildRequires:	perl(WWW::Mechanize::Link)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module will let you automate Firefox through the MozRepl plugin.
You need to have installed that plugin in your Firefox.

%description -l pl.UTF-8
Ten moduł pozwala na używanie Firefoksa w sposób automatyczny za
pomocą pluginu MozRepl. Wymaga zainstalowanego Firefoksa z tym
pluginem.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__cp} -a examples/{*.pl,README} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__rm} -f $RPM_BUILD_ROOT%{perl_vendorlib}/WWW/Mechanize/{Firefox/*.pod,*.pl}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/WWW/Mechanize/Firefox.pm
%{perl_vendorlib}/WWW/Mechanize/Firefox
%{perl_vendorlib}/Firefox/Application.pm
%{perl_vendorlib}/Firefox/Application
%{perl_vendorlib}/HTML/Display/MozRepl.pm
%{perl_vendorlib}/HTTP/Cookies/MozRepl.pm
%{_mandir}/man?/*
%{_examplesdir}/%{name}-%{version}
