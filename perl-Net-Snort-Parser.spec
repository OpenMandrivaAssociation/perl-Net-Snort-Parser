%define module Net-Snort-Parser

Summary:	A simple yet complicated rules maintance system for Snort
Name:		perl-%{module}
Version:	1.36
Release:	%mkrel 5
License:	BSD
Group:		Development/Perl
URL:		http://www.shmoo.com/~bmc/software/snortconfig/
Source0:	http://www.shmoo.com/~bmc/software/snortconfig/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
Provides:	snortconfig
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
snortconfig is a rules modification system for snort that is generated from a
configuration file. This allows a user to keep their ruleset updated without
too much of a headache. Configuration is done using a basic INI style
configuration. 

snortconfig supports three methods of configuration of rules. The methods are
specifing what rules to apply changes to. These methods are files, sids, and
classifications. This allows make broad changes to snort rules very quickly.

%prep

%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%makeinstall_std

%clean 
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc README examples
%attr(0755,root,root) %{_bindir}/snortconfig
%{perl_vendorlib}/Net/Snort/Parser/*.pm
%{_mandir}/*/*




%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.36-5mdv2010.0
+ Revision: 430515
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.36-4mdv2009.0
+ Revision: 258126
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.36-3mdv2009.0
+ Revision: 246173
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.36-1mdv2008.1
+ Revision: 140694
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Jan 26 2007 Oden Eriksson <oeriksson@mandriva.com> 1.36-1mdv2007.0
+ Revision: 113844
- Import perl-Net-Snort-Parser

* Fri Jan 26 2007 Oden Eriksson <oeriksson@mandriva.com> 1.36-1mdv2007.1
- 1.36

* Sun Dec 25 2005 Oden Eriksson <oeriksson@mandriva.com> 1.21-2mdk
- rebuild

* Mon Nov 01 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.21-1mdk
- initial mandrake package

