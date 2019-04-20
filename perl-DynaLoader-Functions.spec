#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DynaLoader-Functions
Version  : 0.003
Release  : 11
URL      : https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/DynaLoader-Functions-0.003.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/DynaLoader-Functions-0.003.tar.gz
Summary  : Perl DynaLoader::Functions CPAN module
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
NAME
DynaLoader::Functions - deconstructed dynamic C library loading
DESCRIPTION

%package dev
Summary: dev components for the perl-DynaLoader-Functions package.
Group: Development
Provides: perl-DynaLoader-Functions-devel = %{version}-%{release}
Requires: perl-DynaLoader-Functions = %{version}-%{release}

%description dev
dev components for the perl-DynaLoader-Functions package.


%prep
%setup -q -n DynaLoader-Functions-0.003

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/DynaLoader/Functions.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DynaLoader::Functions.3
