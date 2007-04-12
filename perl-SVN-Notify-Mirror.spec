%define module	SVN-Notify-Mirror
%define name	perl-%{module}
%define version	0.035
%define up_version	0.035
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Keep a mirrored working copy of a repository path
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/SVN/%{module}-%{up_version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl-Module-Build
BuildRequires:  perl-SVN-Notify
BuildRequires:  subversion-tools
BuildRequires:  sendmail-command
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Keep a local directory in sync with a portion of a Subversion repository.
Typically used to keep a development web server in sync with the changes made
to the repository.

NOTE: because 'svn export' is not able to be consistently updated, the sync'd
directory must be a full working copy.

%prep
%setup -q -n %{module}-%{up_version}

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
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/SVN
%{_mandir}/*/*



