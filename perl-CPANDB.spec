%define upstream_name    CPANDB
%define upstream_version 0.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	CPANDB class for the distribution table
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DateTime)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(LWP::Online)
BuildRequires:	perl(ORLite::Mirror)
BuildRequires:	perl(ORLite::Statistics)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Test::More)

BuildArch:	noarch

%description
CPANDB class for the distribution table.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc LICENSE README Changes
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/cpangraph


%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.140.0-2mdv2011.0
+ Revision: 658520
- rebuild for updated spec-helper

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2011.0
+ Revision: 553062
- update to 0.14

* Tue Apr 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2010.1
+ Revision: 536960
- update to 0.13

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.1
+ Revision: 460936
- adding missing buildrequires
- update to 0.12

* Thu Aug 20 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.0
+ Revision: 418440
- adding missing buildrequires:
- update to 0.10

* Tue Aug 11 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 415000
- update to 0.05

* Thu Jul 09 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 393826
- import perl-CPANDB


* Thu Jul 09 2009 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist
