%define upstream_name    SVN-Notify-Mirror
%define upstream_version 0.040

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Keep a mirrored working copy of a repository path
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/SVN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(SVN::Notify)
BuildRequires:	subversion-tools
BuildRequires:	sendmail-command
BuildArch:	noarch

%description
Keep a local directory in sync with a portion of a Subversion repository.
Typically used to keep a development web server in sync with the changes made
to the repository.

NOTE: because 'svn export' is not able to be consistently updated, the sync'd
directory must be a full working copy.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor << EOF
y
EOF
./Build

%check
export SVNLOOK=%{_bindir}/svnlook
export LC_ALL=C
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes README
%{perl_vendorlib}/SVN
%{_mandir}/*/*

%changelog
* Fri Jul 24 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.38.0-1mdv2010.0
+ Revision: 399449
- updated to 0.038 (for real this time)
- using %%perl_convert_version
- fixed license field

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.038-2mdv2009.0
+ Revision: 268721
- rebuild early 2009.0 package (before pixel changes)

* Tue May 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.038-1mdv2009.0
+ Revision: 209334
- update to new version 0.038

* Mon Mar 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.037-1mdv2008.1
+ Revision: 177948
- update to new version 0.037

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.035-1mdv2008.1
+ Revision: 140717
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Feb 28 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.035-1mdv2007.0
+ Revision: 127190
- new version

* Thu Nov 23 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.034.03-1mdv2007.1
+ Revision: 86628
- new version

* Wed Nov 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.034.02-2mdv2007.1
+ Revision: 84385
- new version

* Tue Aug 08 2006 Olivier Thauvin <nanardon@mandriva.org> 0.034-2mdv2007.0
+ Revision: 54105
- rebuild
- Import perl-SVN-Notify-Mirror

* Tue Jul 11 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.034-1mdv2007.0
- New version 0.034

* Sat Jul 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.033-2mdv2007.0
- buildrequires sendmail-command

* Wed Mar 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.033-1mdk
- New release 0.033

* Thu Jan 05 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdk
- new version
- rediff test patch

* Wed Dec 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-3mdk
- fix buildrequires

* Fri Dec 23 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.02-2mdk
- Fix BuildRequires : perl-SVN-Notify

* Wed Dec 14 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-1mdk
- New release 0.02
- fix direct test, disable config test (Notify::Mirror::Config is broken)

* Tue Nov 29 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-1mdk
- first mdk release

