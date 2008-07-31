%define module Net-Snort-Parser

Summary:	A simple yet complicated rules maintance system for Snort
Name:		perl-%{module}
Version:	1.36
Release:	%mkrel 4
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


